# La década del relevo: longevidad laboral y talento sénior (2026-2036)

Estudio para la dirección de una aseguradora o entidad de previsión. Analiza la longevidad de las plantillas, las prejubilaciones, la falta de relevo generacional, las pensiones y el coste de un hogar, y el efecto de la IA en el empleo de los próximos diez años. Cada capítulo sigue el orden contexto → problema → solución.

## Entregables

| Entregable | Formato | Enlace |
|---|---|---|
| Documento de investigación | Claude Doc (exportable a Word, PDF o Google Docs), con las pestañas «Soluciones y startups» y «Verificación de Vecdis» | [La década del relevo](https://claude.ai/artifact/WNE1h4gaa4pxMNdoae6JUA) |
| Presentación interna (extensa) | Slides de Claude (descargable a PowerPoint o PDF): 59 diapositivas en 12 bloques de contexto, problema y solución, con lectura y fuente en cada gráfico, y un bloque de socios y pilotos | [La década del relevo · presentación interna](https://claude.ai/artifact/82ET11kZWJTSiG5QkLZ8JM) |
| Presentación ejecutiva (10 min) | Slides de Claude (descargable a PowerPoint o PDF): 14 diapositivas neutrales para la dirección, con notas del orador de unas 1.300 palabras | [La década del relevo · presentación ejecutiva](https://claude.ai/artifact/FFmDh57UcLmpGiWQsveaPt) |

Los enlaces son privados: solo los abre quien tenga acceso o con quien se compartan desde claude.ai.

## Estructura del repositorio

```
investigacion/    copia en Markdown del documento (pestaña principal), fuentes.csv, matriz_verificacion.csv,
                  escenarios_2036.py y modelo_perfiles/ (pensión, brecha y ahorro por perfil)
research_notes/   notas de investigación por bloque, con registro de fuentes y matriz de verificación
datos/procesados/ tablas derivadas de la EPA y de las proyecciones del INE (datos/brutos/ no se versiona)
insumos/          instrucciones para aportar material
privado/          material de terceros (Vecdis, FounderNest): excluido de git porque el repositorio es público
```

## Reproducir los cálculos

```
python3 -I investigacion/modelo_perfiles/modelo.py    # pensión, tasa de sustitución y ahorro por perfil
python3 -I investigacion/escenarios_2036.py            # ocupados de 55+ en 2036 en tres escenarios
python3 -I investigacion/compilar_fuentes.py           # registro de fuentes y recuento de sitios
```
