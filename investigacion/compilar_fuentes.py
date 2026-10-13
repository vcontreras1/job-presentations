"""Compila el registro de fuentes y la matriz de verificación de todas las notas de investigación.

Lee las tablas «Registro de fuentes» y «Matriz de verificación» de research_notes/<estudio>/*.md y escribe:
  investigacion/fuentes.csv              una fila por URL única, con su dominio
  investigacion/matriz_verificacion.csv  todas las cifras verificadas, con el archivo de origen
Imprime el número de fuentes y de dominios únicos (objetivo: ≥ 50 sitios distintos).

Uso: python3 -I investigacion/compilar_fuentes.py
"""

import csv
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import urlparse

RAIZ = Path(__file__).resolve().parent.parent
NOTAS = RAIZ / "research_notes" / "Longevidad laboral y talento sénior"
SALIDA = RAIZ / "investigacion"


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", "", texto).strip()


def celdas(linea):
    partes = [c.strip() for c in linea.strip().strip("|").split("|")]
    return partes


def tablas(texto):
    """Devuelve cada tabla Markdown como (cabecera, filas)."""
    lineas = texto.splitlines()
    i = 0
    while i < len(lineas):
        if lineas[i].lstrip().startswith("|") and i + 1 < len(lineas) and re.match(r"^\s*\|?\s*:?-{2,}", lineas[i + 1]):
            cabecera = [normalizar(c) for c in celdas(lineas[i])]
            filas = []
            j = i + 2
            while j < len(lineas) and lineas[j].lstrip().startswith("|"):
                filas.append(celdas(lineas[j]))
                j += 1
            yield cabecera, filas
            i = j
        else:
            i += 1


def columna(cabecera, *claves):
    for k, nombre in enumerate(cabecera):
        if any(clave in nombre for clave in claves):
            return k
    return None


def url_de(celda):
    m = re.search(r"https?://[^\s)\]>|]+", celda)
    return m.group(0).rstrip(".,;") if m else None


def main():
    fuentes, vistas, matriz = [], {}, []
    for archivo in sorted(NOTAS.glob("*.md")):
        texto = archivo.read_text(encoding="utf-8")
        for cabecera, filas in tablas(texto):
            c_url = columna(cabecera, "url", "enlace")
            c_cifra = columna(cabecera, "cifra")
            if c_url is not None:
                c_id = columna(cabecera, "id")
                c_ent = columna(cabecera, "entidad", "fuente", "organismo")
                c_tit = columna(cabecera, "titulo", "documento")
                c_fecha = columna(cabecera, "fecha")
                c_niv = columna(cabecera, "nivel")
                c_abi = columna(cabecera, "abierta")
                c_cif = columna(cabecera, "cifras", "respalda", "datos")
                for fila in filas:
                    url = url_de(fila[c_url]) if c_url < len(fila) else None
                    if not url:
                        continue
                    dato = lambda c: fila[c] if c is not None and c < len(fila) else ""
                    clave = url.lower().rstrip("/")
                    dominio = urlparse(url).netloc.lower().removeprefix("www.")
                    if clave in vistas:
                        vistas[clave]["archivos"].add(archivo.stem)
                        continue
                    registro = {
                        "archivos": {archivo.stem}, "id_local": dato(c_id), "entidad": dato(c_ent),
                        "titulo": dato(c_tit), "url": url, "dominio": dominio, "fecha": dato(c_fecha),
                        "nivel": dato(c_niv), "abierta": dato(c_abi), "cifras": dato(c_cif),
                    }
                    vistas[clave] = registro
                    fuentes.append(registro)
            elif c_cifra is not None and columna(cabecera, "estado") is not None:
                for fila in filas:
                    matriz.append({"archivo": archivo.stem, **{cabecera[k]: (fila[k] if k < len(fila) else "") for k in range(len(cabecera))}})

    with (SALIDA / "fuentes.csv").open("w", newline="", encoding="utf-8") as f:
        campos = ["n", "dominio", "entidad", "titulo", "url", "fecha", "nivel", "abierta", "cifras", "id_local", "archivos"]
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for n, r in enumerate(sorted(fuentes, key=lambda r: (r["dominio"], r["url"])), 1):
            w.writerow({**r, "n": n, "archivos": " ".join(sorted(r["archivos"]))})

    campos_m = ["archivo"] + sorted({k for fila in matriz for k in fila if k != "archivo"})
    with (SALIDA / "matriz_verificacion.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos_m)
        w.writeheader()
        w.writerows(matriz)

    dominios = sorted({r["dominio"] for r in fuentes})
    abiertas = sum(1 for r in fuentes if normalizar(r["abierta"]).startswith("si"))
    print(f"Fuentes únicas: {len(fuentes)} (abiertas: {abiertas})")
    print(f"Dominios únicos: {len(dominios)}")
    print(f"Cifras en la matriz de verificación: {len(matriz)}")
    if "--dominios" in sys.argv:
        print("\n".join(dominios))


if __name__ == "__main__":
    main()
