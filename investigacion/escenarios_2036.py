"""Escenarios de ocupados de 55+ en 2036 (capítulo 10 del documento).

Aplica tasas de empleo por edad a la población proyectada por el INE (tabla 36643, escenario central):
  - inercia: tasas de la EPA del 2T-2026,
  - vida laboral extendida: tasas sénior cercanas a las de Alemania y el norte de Europa
    (Eurostat 2025: Alemania 83,1 % a 55-59, 67,6 % a 60-64 y 23,2 % a 65-69; UE-27 77,3 %, 55,0 % y 17,3 %),
  - salida temprana: tasas sénior del 2T-2019.
Las tasas de los menores de 55 son las del 2T-2026 en los tres escenarios.

La tabla del INE no se versiona (datos/brutos/); si falta, se descarga de la API del INE:
    https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/36643?nult=51

Uso: python3 -I investigacion/escenarios_2036.py
"""

import csv
import json
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PROYECCION = RAIZ / "datos" / "brutos" / "demografia" / "ine" / "ine_tabla_36643.json"
URL_PROYECCION = "https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/36643?nult=51"
MATRIZ = RAIZ / "datos" / "procesados" / "epa_matriz_estado_edad_2T.csv"

GRUPOS = [("J16_19", 16, 19), ("J20_24", 20, 24), ("J25_29", 25, 29), ("Adulto30_54", 30, 54),
          ("S55_59", 55, 59), ("S60_64", 60, 64), ("S65_69", 65, 69), ("S70p", 70, 100)]
EXTENDIDA = {"S55_59": 0.78, "S60_64": 0.65, "S65_69": 0.22, "S70p": 0.02}


def poblacion_por_edad():
    if not PROYECCION.exists():
        PROYECCION.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(URL_PROYECCION, timeout=120) as respuesta:
            PROYECCION.write_bytes(respuesta.read())
    series = json.loads(PROYECCION.read_text(encoding="utf-8"))
    edades = {}
    for serie in series:
        if not serie["Nombre"].startswith("Total. "):
            continue
        for edad in range(101):
            if f". {edad} años." in serie["Nombre"] or (edad == 100 and "100 y más" in serie["Nombre"]):
                edades[edad] = {punto["Anyo"]: punto["Valor"] for punto in serie["Data"]}
    return edades


def tasas(periodo):
    filas = list(csv.DictReader(MATRIZ.open(encoding="utf-8")))
    return {g: float(next(f for f in filas if f["Periodo"] == periodo and f["Grupo"] == g)["T_empleo"]) / 100
            for g, _, _ in GRUPOS}


def main():
    edades = poblacion_por_edad()

    def poblacion(desde, hasta, anyo):
        return sum(edades[e][anyo] for e in range(desde, hasta + 1) if e in edades)

    base, t2019 = tasas("2026T2"), tasas("2019T2")
    escenarios = {
        "inercia (tasas de 2026)": base,
        "vida laboral extendida (tasas sénior cercanas a Alemania)": {**base, **EXTENDIDA},
        "salida temprana (tasas sénior de 2019)": {**base, **{g: t for g, t in t2019.items() if g.startswith("S")}},
    }
    print("Tasas de empleo sénior 2019:", {g: round(100 * t, 1) for g, t in t2019.items() if g.startswith("S")})
    print("Tasas de empleo sénior 2026:", {g: round(100 * t, 1) for g, t in base.items() if g.startswith("S")})
    for anyo, nombres in ((2026, ["inercia (tasas de 2026)"]), (2036, list(escenarios))):
        for nombre in nombres:
            ocupados = {g: escenarios[nombre][g] * poblacion(a0, a1, anyo) for g, a0, a1 in GRUPOS}
            total = sum(ocupados.values())
            senior = sum(v for g, v in ocupados.items() if g.startswith("S"))
            print(f"{anyo} · {nombre:58s} ocupados {total / 1e6:5.2f} M · 55+ {senior / 1e6:4.2f} M ({100 * senior / total:.1f} %)")


if __name__ == "__main__":
    main()
