# Datos

- `procesados/`: tablas derivadas que alimentan los gráficos y cifras del estudio (EPA, proyecciones del INE).
- `brutos/` (no se versiona por tamaño): descargas oficiales de INE (API wstempus y jaxiT3), Eurostat (API de difusión), Seguridad Social, OCDE e Inverco. Cada nota de `research_notes/` indica la tabla o URL de origen para volver a descargarlas.

| Archivo procesado | Origen | Contenido |
|---|---|---|
| epa_matriz_estado_edad_2T.csv | INE, EPA (2T de 2008, 2014, 2019, 2025 y 2026) | Población por situación laboral y grupo de edad, en miles y % |
| epa_series_ocupados_55_y_jovenes.csv | INE, EPA trimestral 2002-2026 | Ocupados 55+ y 16-29, tasas de empleo por edad |
| derivado_personas_65_67_proyeccion_INE_2026_2076.csv | INE, Proyecciones de Población 2026-2076 (tabla 36643) | Personas de 64-67 años por año |
| derivado_piramide_2026_2036_INE.csv | INE, Proyecciones de Población 2026-2076 | Pirámide por grupos de edad y sexo |
| derivado_residentes_por_generacion_ECP_1jul2026.csv | INE, Estadística Continua de Población | Esqueleto por generación (sin cifras) |
