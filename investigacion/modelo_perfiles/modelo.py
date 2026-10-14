"""Modelo de perfiles socioeconómicos: pensión pública estimada, tasa de sustitución y brecha de ingresos.

Para cada perfil calcula:
  - salario bruto y neto (cotización del trabajador e IRPF aproximado),
  - pensión de jubilación estimada a los 67 con la carrera indicada (tope de pensión máxima),
  - tasa de sustitución bruta y neta,
  - brecha mensual frente al salario neto y frente al gasto de referencia del hogar,
  - capital necesario a los 67 para cubrir la brecha y ahorro mensual necesario desde los 45 o los 55.

Todos los parámetros (y su fuente) están en parametros_2026.json. Uso:
    python3 -I modelo.py
Escribe resultados.csv y resultados.md junto a este archivo.
"""

import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
P = json.loads((HERE / "parametros_2026.json").read_text(encoding="utf-8"))


def v(clave):
    """Valor de un parámetro (los parámetros se guardan como {"valor": ..., "fuente": ...})."""
    nodo = P
    for parte in clave.split("."):
        nodo = nodo[parte]
    return nodo["valor"] if isinstance(nodo, dict) and "valor" in nodo else nodo


# ---------------------------------------------------------------- cotizaciones del trabajador

def cotizacion_trabajador(salario):
    base_max = v("cotizacion.base_max_anual")
    cuota = min(salario, base_max) * v("cotizacion.tipo_trabajador_total")
    exceso = max(0.0, salario - base_max)
    solidaridad = 0.0
    if exceso > 0:
        restante = exceso
        desde = 0.0
        for tramo in v("cotizacion.solidaridad_tramos"):
            hasta = tramo["hasta_pct_sobre_base_max"]
            ancho = (hasta - desde) / 100 * base_max if hasta is not None else restante
            parte = min(restante, ancho)
            solidaridad += parte * tramo["tipo_total"] * v("cotizacion.solidaridad_parte_trabajador")
            restante -= parte
            desde = hasta if hasta is not None else desde
            if restante <= 0:
                break
    return cuota + solidaridad


# ---------------------------------------------------------------- IRPF aproximado (escala general estatal + autonómica supletoria)

def escala(base):
    cuota, desde = 0.0, 0.0
    for tramo in v("irpf.escala"):
        hasta = tramo["hasta"] if tramo["hasta"] is not None else float("inf")
        if base > desde:
            cuota += (min(base, hasta) - desde) * tramo["tipo"]
        desde = hasta
    return cuota


def reduccion_rendimientos_trabajo(rn):
    r = v("irpf.reduccion_trabajo")
    if rn <= r["umbral_1"]:
        return r["importe_max"]
    if rn <= r["umbral_2"]:
        return r["importe_max"] - r["pendiente_1"] * (rn - r["umbral_1"])
    if rn <= r["umbral_3"]:
        return r["importe_tramo_2"] - r["pendiente_2"] * (rn - r["umbral_2"])
    return 0.0


def deduccion_smi(bruto):
    """DA 61.ª LIRPF: deducción en cuota para salarios bajos (no aplica a pensiones)."""
    d = v("irpf.deduccion_smi")
    if bruto <= d["limite_pleno"]:
        return d["importe"]
    if bruto >= d["limite_cero"]:
        return 0.0
    return d["importe"] * (d["limite_cero"] - bruto) / (d["limite_cero"] - d["limite_pleno"])


def irpf(bruto, cotizaciones, mayor_65=False, salario=True):
    rendimiento_neto = max(0.0, bruto - cotizaciones - v("irpf.otros_gastos"))
    base = max(0.0, rendimiento_neto - reduccion_rendimientos_trabajo(rendimiento_neto))
    minimo = v("irpf.minimo_personal_65") if mayor_65 else v("irpf.minimo_personal")
    cuota = max(0.0, escala(base) - escala(min(minimo, base)))
    if salario:
        cuota = max(0.0, cuota - deduccion_smi(bruto))
    return cuota


# ---------------------------------------------------------------- pensión pública

def porcentaje_por_anos(anos):
    """Escala de 2027 en adelante: 15 años = 50 %, +0,19 % por mes hasta el mes 248 y +0,18 % hasta el 264 (37 años = 100 %)."""
    if anos < 15:
        return 0.0
    meses = round((anos - 15) * 12)
    pct = 50 + 0.19 * min(meses, 248) + 0.18 * max(0, min(meses, 264) - 248)
    return min(pct, 100.0) / 100


def base_reguladora_anual(salario_final, crecimiento_real, anos_computo=25):
    """Media de las bases reales de los últimos años, con la base topada en la base máxima.

    Supone un salario que crece en términos reales a `crecimiento_real` al año hasta el final de la carrera
    y que las bases antiguas se actualizan con el IPC (salvo los dos últimos años, efecto menor que se ignora).
    """
    base_max = v("cotizacion.base_max_anual")
    bases = [min(salario_final / (1 + crecimiento_real) ** k, base_max) for k in range(anos_computo)]
    return sum(bases) / len(bases)


def pension_anual(salario_final, anos_cotizados, crecimiento_real):
    bruta = base_reguladora_anual(salario_final, crecimiento_real) * porcentaje_por_anos(anos_cotizados)
    return min(bruta, v("pension.maxima_anual"))


# ---------------------------------------------------------------- finanzas de la brecha

def factor_renta(anos, interes_real):
    """Valor actual de 1 € anual durante `anos` años (pago a principio de año)."""
    if interes_real == 0:
        return anos
    return (1 - (1 + interes_real) ** -anos) / interes_real * (1 + interes_real)


def ahorro_mensual(capital, anos, rentabilidad_real):
    """Aportación mensual constante (en euros de hoy) para reunir `capital` en `anos` años."""
    n = anos * 12
    i = (1 + rentabilidad_real) ** (1 / 12) - 1
    if i == 0:
        return capital / n
    return capital * i / ((1 + i) ** n - 1)


# ---------------------------------------------------------------- cálculo por perfil

def calcular(perfil):
    salario = perfil["salario_bruto_anual"]
    cot = cotizacion_trabajador(salario)
    neto = salario - cot - irpf(salario, cot)

    pension = pension_anual(salario, perfil["anos_cotizados"], v("supuestos.crecimiento_real_salario"))
    pension_neta = pension - irpf(pension, 0.0, mayor_65=True, salario=False)

    gasto_ref = perfil["gasto_hogar_referencia_anual"]
    brecha_salario = max(0.0, neto - pension_neta)
    brecha_gasto = max(0.0, gasto_ref - pension_neta)

    anos_jub = v("supuestos.anos_jubilacion")
    r_jub = v("supuestos.interes_real_jubilacion")
    capital = brecha_salario * factor_renta(anos_jub, r_jub)
    r_acum = v("supuestos.rentabilidad_real_acumulacion")

    return {
        "perfil": perfil["nombre"],
        "salario_bruto_anual": round(salario),
        "salario_neto_anual": round(neto),
        "salario_neto_mensual_12": round(neto / 12),
        "pension_bruta_anual": round(pension),
        "pension_bruta_mensual_14": round(pension / 14),
        "pension_neta_mensual_12": round(pension_neta / 12),
        "tope_pension_maxima": pension >= v("pension.maxima_anual") - 0.5,
        "tasa_sustitucion_bruta": round(pension / salario, 3),
        "tasa_sustitucion_neta": round(pension_neta / neto, 3),
        "brecha_mensual_vs_salario_neto": round(brecha_salario / 12),
        "brecha_mensual_vs_gasto_hogar": round(brecha_gasto / 12),
        "capital_necesario_67": round(capital, -3),
        "ahorro_mensual_desde_45": round(ahorro_mensual(capital, 67 - 45, r_acum)),
        "ahorro_mensual_desde_55": round(ahorro_mensual(capital, 67 - 55, r_acum)),
    }


def curva_sustitucion(desde=15000, hasta=150000, paso=5000):
    """Tasa de sustitución neta para una carrera completa (40 años) a lo largo de la escala salarial."""
    filas = []
    for salario in range(desde, hasta + 1, paso):
        r = calcular({"nombre": "", "salario_bruto_anual": salario, "anos_cotizados": 40,
                      "gasto_hogar_referencia_anual": v("referencias_hogar.gasto_unipersonal_65")})
        filas.append({"salario_bruto_anual": salario, "tasa_sustitucion_neta": r["tasa_sustitucion_neta"],
                      "tasa_sustitucion_bruta": r["tasa_sustitucion_bruta"],
                      "pension_neta_mensual_12": r["pension_neta_mensual_12"]})
    return filas


def salario_umbral(objetivo_neto_anual, anos=40):
    """Salario bruto mínimo cuya pensión neta (carrera completa) alcanza un importe neto anual."""
    lo, hi = 10000.0, 200000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        pension = pension_anual(mid, anos, v("supuestos.crecimiento_real_salario"))
        neta = pension - irpf(pension, 0.0, mayor_65=True, salario=False)
        lo, hi = (mid, hi) if neta < objetivo_neto_anual else (lo, mid)
    return round(hi, -2)


def main():
    filas = [calcular(p) for p in P["perfiles"]]
    curva = curva_sustitucion()
    with (HERE / "curva_sustitucion.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(curva[0].keys()))
        w.writeheader()
        w.writerows(curva)
    umbrales = {
        "umbral_pobreza_1_adulto": salario_umbral(v("referencias_hogar.umbral_pobreza_1_adulto")),
        "gasto_unipersonal_65": salario_umbral(v("referencias_hogar.gasto_unipersonal_65")),
        "gasto_pareja_65_una_pension": salario_umbral(v("referencias_hogar.gasto_pareja_65")),
        "gasto_pareja_65_dos_pensiones_iguales": salario_umbral(v("referencias_hogar.gasto_pareja_65") / 2),
    }
    (HERE / "umbrales_salariales.json").write_text(json.dumps(umbrales, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Salario bruto mínimo (carrera completa) para que la pensión neta cubra:", umbrales)
    with (HERE / "resultados.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    cab = list(filas[0].keys())
    lineas = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    lineas += ["| " + " | ".join(str(f[c]) for c in cab) + " |" for f in filas]
    (HERE / "resultados.md").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    for f in filas:
        print(f)


if __name__ == "__main__":
    main()
