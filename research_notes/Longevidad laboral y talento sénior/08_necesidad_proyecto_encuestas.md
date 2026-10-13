# Necesidad económica frente a proyecto/vocación en el trabajo de los 55+ (España y Europa): inventario crítico de encuestas y fichas de fiabilidad

> Estudio «La década del relevo (2026-2036)». Notas de investigación — creado el 13-oct-2026. ESTADO: BORRADOR INCREMENTAL (se va completando por bloques; lo que figure como «PENDIENTE» aún no está verificado).
> Convención de fiabilidad: Alta / Media / Baja (método, muestra, patrocinador, redacción de la pregunta). Año de cada encuesta indicado siempre.

## Hallazgos clave

(PENDIENTE: se redacta al final con las cifras ya verificadas)

## 1. Módulo ad hoc 2023 (INE/Eurostat): pensionistas que trabajan — motivo económico frente a no económico

### Takeaway
En el módulo EPA/EU-LFS 2023 (50-74 años), el motivo «el trabajo era financieramente necesario» es minoritario como motivo principal para seguir trabajando al empezar a cobrar la pensión de jubilación: 28,6% en la UE-27 y 19,6% en España. El disfrute del trabajo (36,3% UE; 17,9% ES) y mantenerse socialmente integrado (11,3% UE; 11,6% ES) suman 47,6% en la UE y 29,5% en España. Pero en España el 44,9% marca «otra razón» (residual sin identificar) y la base es pequeña (184,9 mil personas ponderadas), de modo que el dato español NO permite afirmar que la mayoría trabaje «por proyecto»; permite afirmar que «necesidad» no es la razón mayoritaria declarada.

### Cited Findings
**Qué mide y a quién (leer antes de citar cifras).**
- El módulo «Pensions and labour market participation» (2023) es un módulo octenal del EU-LFS con 11 variables; la población objetivo son personas de 50-74 años; la pregunta WCONREAS («motivo principal para seguir trabajando con la percepción de la pensión de jubilación») se refiere al período de 6 meses desde que empezó la pensión, no a la situación actual; los porcentajes de Eurobase excluyen la no respuesta — [Eurostat ESMS lfso_23](https://ec.europa.eu/eurostat/cache/metadata/en/lfso_23_esms.htm) (S07).
- En España el módulo se aplicó a un sexto de la muestra trimestral de la EPA durante todo 2023: muestra inicial 40.791 viviendas (sextas entrevistas), 34.405 entrevistadas (84,34%; negativas 5,60%, ausencias/inaccesibles 10,05%); universo analizado: 15.764.500 personas de 50-74 años, de las que 3.806.700 (24,2%) cobraban alguna pensión de jubilación — [INE metodología del módulo 2023](https://www.ine.es/daco/daco42/daco4211/metomodu23.pdf) (S09) y [INE nota de prensa 21-jun-2024](https://www.ine.es/dyngs/Prensa/es/mEPA2023.htm) (S05).
- Solo 184.900 personas de 50-74 años en España «continuaron trabajando» en los seis meses posteriores a recibir la primera pensión de jubilación (68,1 mil sin cambios + 116,7 mil con cambios = 4,9% de los 3,8 millones de pensionistas); el 68,5% dejó de trabajar y el 25,5% no trabajaba — [INE tabla tpx67853](https://www.ine.es/jaxiT3/Tabla.htm?t=67853) (S06; datos en `datos/brutos/epa/ine_modulo2023/ine_modulo2023_tpx67853.csv`).

**Motivo principal para seguir trabajando (WCONREAS), 50-74 años, % sin no respuesta — Eurostat lfso_23pens08 (S01):**

| Motivo | UE-27 | España | IT | NL | DE | FR | PT | SE |
|---|---|---|---|---|---|---|---|---|
| Financieramente necesario | 28,6 | 19,6 | 29,7 | 16,9 | 35,8 | 37,7 | 39,0 | 9,4 |
| Financieramente atractivo | 9,1 | 3,4 (u) | 6,0 | 7,3 | u | u | 7,1 (u) | 15,6 |
| Pareja/cónyuge sigue trabajando | 3,4 | 2,6 (u) | 2,3 | 3,7 | u | u | u | u |
| Disfruta trabajando / ser productivo | 36,3 | 17,9 | 51,7 | 59,6 | 29,2 | 20,6 | 30,4 | 36,4 |
| Mantenerse socialmente integrado | 11,3 | 11,6 | 4,2 | 6,0 | 7,3 (u) | 15,5 | 10,7 | 25,6 |
| Otra razón | 11,3 | 44,9 | 6,1 | 6,6 | 17,1 | 19,5 | 10,3 | 10,9 |
(u = fiabilidad baja según la marca de Eurostat; «u» sin cifra = celda suprimida por baja fiabilidad.)

- Agregando: «económico» (necesario + atractivo) = 37,7% UE y 23,0% ES; «no económico» (disfrute + integración social) = 47,6% UE y 29,5% ES; pareja trabajando + otra = 14,7% UE y 47,5% ES (cálculo propio sobre S01).
- INE publica el mismo dato en bruto sobre 184,9 mil personas: «necesario para obtener ingresos adicionales» 18,8%; «le gustaba trabajar y ser productivo» 17,2%; «le gustaba permanecer socialmente activo» 11,1%; «otras razones» 48,7% (incluye «económicamente atractivo» y «su pareja también seguía trabajando»); NS/NC 4,1% — [INE tabla tpx67855](https://www.ine.es/jaxiT3/Tabla.htm?t=67855) (S06) y [nota de prensa](https://www.ine.es/dyngs/Prensa/es/mEPA2023.htm) (S05). Coincide con Eurostat tras reponderar sin NS/NC (18,8/0,959 = 19,6) → **estado: coincide** entre INE y Eurostat (son la misma fuente, no un contraste independiente).
- **Por sexo, España (INE, % sobre 184,9 mil con NS/NC):** hombres (126,2 mil) 16,7% necesidad / 21,7% disfrute / 12,0% social / 44,4% otras; mujeres (58,7 mil) 23,4% necesidad / 7,5% disfrute / 9,2% social / 58,0% otras (S06, tpx67855). Eurostat (S01, sin NS/NC): ES hombres 17,6 / 22,9 / 12,7 / 39,6; ES mujeres 23,9 / 7,6 (u) / 9,4 (u) / 55,9. UE hombres 27,1 necesario, 38,0 disfrute, 10,3 social; UE mujeres 30,3 / 34,3 / 12,5. → las mujeres declaran más a menudo la necesidad y menos el disfrute, en ES y UE (en ES la diferencia es estadísticamente frágil por tamaño de muestra).
- **Por edad, UE (S01):** 50-64 años: necesario 36,6%, disfrute 28,9%, social 9,6%; 65-74 años: necesario 26,2%, disfrute 38,5%, social 11,8%. España: 50-64 años necesario 33,7% (otra razón 53,4%; disfrute 8,4% u); 65-74 años necesario 15,3%, disfrute 20,9%, social 14,1%, otra 42,2%. → el motivo de necesidad se concentra en quienes se jubilan (o cobran pensión) antes de los 65; el disfrute/vínculo social gana peso con la edad.
- **Asalariado frente a autónomo (S04, Eurostat lfso_23pens11, 50-74 años):** de los pensionistas de jubilación, siguió trabajando o reingresó el 24,4% de quienes eran/son asalariados y el 56,4% de los autónomos en la UE-27; en España el 7,7% de los asalariados y el 18,2% de los autónomos (total ES 7,6%; UE 21,4%). España es el país de la UE con el valor más bajo entre autónomos (Grecia 20,3%; Suecia 98,4%, Finlandia 88,0%, Irlanda 87,7%) — [Eurostat news 6-jun-2025](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250606-1) (S08) y [lfso_23pens11](https://ec.europa.eu/eurostat/databrowser/view/lfso_23pens11/default/table) (S04). Por sexo, en España los autónomos hombres 22,1% frente a autónomas 6,7% (u).
- Composición de quienes siguen en activo (ES, 50-74, miles; S04): total 212,9 mil = asalariados 109,9 (51,6%), autónomos 58,5 (27,5%), sin situación profesional aplicable 41,4 (19,4%), ayuda familiar 3,2 (1,5%). UE-27: 8.466,8 mil = asalariados 51,0%, autónomos 25,9%, NAP 21,0%, ayuda familiar 1,7%. → en España los autónomos no son mayoría numérica entre los que trabajan cobrando pensión, aunque sí tienen mayor propensión relativa.
- Parcialidad: el 10,2% de los pensionistas de jubilación de 50-74 años de la UE está ocupado y el 57,0% de ellos trabaja a tiempo parcial (16,2% entre no pensionistas) — [Eurostat news 6-jun-2025](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20250606-1) (S08).
- **Reingreso tras la jubilación (S03, lfso_23pens10):** motivo de reingreso al mercado laboral en la UE-27 (50-74): necesario 30,6%, disfrute 28,1%, otra razón 41,3%; en España todas las celdas por motivo están marcadas de baja fiabilidad (otra 58,0% u, disfrute 25,8% u, necesario suprimido) y solo 28,1 mil personas (0,78% de los pensionistas que dejaron de trabajar o no trabajaban) reingresaron — [Eurostat lfso_23pens10](https://ec.europa.eu/eurostat/databrowser/view/lfso_23pens10/default/table) (S03) y [INE tpx67856](https://www.ine.es/jaxiT3/Tabla.htm?t=67856) (S06).
- **Otros rasgos del paso a la jubilación en España (INE 2023, S06):** el 24,2% de los pensionistas tuvo reducción por jubilación anticipada, solo el 1,4% bonificación por aplazamiento (52,1 mil), el 64,3% ninguna; edad de primera pensión: 60-64 años el 39,5%, 65-74 el 50,2% (tpx67845, tpx67844).

**Comparación con el módulo 2012 (S10-S12) — misma pregunta, otro universo.**
- En 2012 (50-69 años; ocupados que reciben alguna pensión de jubilación, de otro tipo o prejubilación; 238,8 mil en España) el 69,3% declaraba un motivo principal económico y el 29,9% no económico; por sexo 59,8% hombres y 77,3% mujeres; por edad 82,5% (50-54), 79,2% (55-59), 60,1% (60-64), 29,4% (65-69) — [INE nota de prensa módulo 2012, 18-jun-2013](https://www.ine.es/prensa/np785.pdf) (S10).
- Eurostat 2012 (S11, lfso_12staywork, 50-69, total): España — rentas suficientes 19,6%, derechos de pensión futuros 18,7%, ambos 30,7%, no financiero 30,3%; UE-27 — rentas suficientes 38,9%, derechos futuros 7,7%, ambos 12,4%, no financiero 25,4%, sin respuesta 15,6% — [Eurostat lfso_12staywork](https://ec.europa.eu/eurostat/databrowser/view/lfso_12staywork/default/table). → contraste España 2012 «económico» 69,0% (suma de las tres categorías) frente a 69,3% en INE: **coincide**.
- **Cuidado al comparar 2012 y 2023:** cambian el universo (2012: 50-69 trabajando con cualquier pensión, incluidas invalidez/prejubilación; 2023: 50-74 con pensión de jubilación, motivo en los 6 primeros meses), las categorías (2012: 4 opciones económicas/no financiera; 2023: 6 con «financieramente atractivo», «pareja», «otra razón») y el contexto (2012 = recesión; la tasa de paro no se cita aquí por no haberla verificado en esta sesión). El salto de «no económico» (30% en 2012) a «disfrute + social» (29,5% en 2023 en España; 47,6% UE) no demuestra por sí solo un cambio de comportamiento.
- Además, el 7,2% de los 4,15 millones de activos de 50-69 años que aún no cobraban pensión preveía en 2012 seguir trabajando tras recibirla (4,0% por razones económicas, 3,1% por otras) y el 17,8% no lo había decidido; el 71,0% preveía trabajar solo hasta la pensión — [INE 2012](https://www.ine.es/prensa/np785.pdf) (S10).

### Inferences
- Para el relato «necesidad frente a proyecto»: el dato oficial más sólido (UE-27) apunta a que **la necesidad económica explica menos de un tercio (28,6%) y la suma de disfrute + vínculo social casi la mitad (47,6%)** de quienes siguen en activo al cobrar la pensión. Con «atractivo económico» (9,1%) lo económico llega al 37,7%. No es un colectivo mayoritariamente forzado, aunque tampoco «jubilados por gusto» sin más: son una minoría selecta (21,4% de los pensionistas de 50-74 en la UE; 7,6% en España).
- España no encaja en el patrón europeo y la causa no está documentada: el 44,9% «otra razón» y la baja prevalencia (4,9% de pensionistas siguieron trabajando) sugieren un colectivo reducido y heterogéneo (posiblemente autónomos que mantienen el negocio, jubilación flexible/activa, trabajo por cuenta propia sin relevo), pero esto es hipótesis no contrastada en las tablas públicas.
- Los datos de 2012 (69% económico) y 2023 (19,6% «necesario» en ES; 23% con «atractivo») no son comparables en sentido estricto; cualquier titular «ha caído la necesidad» debe llevar esa advertencia.

### Gaps
- Desglose del motivo (WCONREAS) por **nivel educativo**, por **asalariado/autónomo** o por sector/ocupación: no está en las tablas públicas de Eurostat (lfso_23pens08 solo cruza edad × sexo × país) ni en las tablas INE descargadas (tpx67855 solo por sexo). Requeriría microdatos EU-LFS (acceso por solicitud a Eurostat) o petición ad hoc al INE.
- Tamaño de muestra sin ponderar (n) de los 184,9 mil españoles que siguieron trabajando: no publicado en la nota; Eurostat marca como poco fiables (u) numerosas celdas ES.
- La «otra razón» (44,9% ES) no se desagrega: sin cuestionario completo no se sabe qué opciones recogía; no inferir su contenido.
- Tablas lfso_23pens12 (ocupación) no descargadas aún (posible mejora).

## 2. Módulo 2023: dejar de trabajar antes de lo deseado, motivos y quién habría querido seguir

### Takeaway
El módulo 2023 **no pregunta** si la persona habría querido seguir trabajando (no hay variable equivalente a la WORKLONG de 2012); solo da el motivo principal para dejar de trabajar al empezar la pensión. En España: 70,3% dejó de trabajar por cumplir los requisitos, 6,6% por la edad máxima, 10,5% por enfermedad o incapacidad propia, 6,3% por «otras razones relacionadas con el trabajo» (incluye despido, trabajo estresante, falta de clientes), 1,5% por cuidados (2,8% mujeres frente a 0,6% hombres). La única medida directa de «habría querido seguir» es la de 2012: 43,5% de los pensionistas españoles de 50-69 años fuera del mercado laboral (26,5% en la UE-27).

### Cited Findings
**Motivo principal para dejar de trabajar al empezar la pensión (WSTPREAS), 50-74 años — Eurostat lfso_23pens07 (S02) y INE tpx67854 (S06):**

| Motivo | UE-27 | España (Eurostat) | España (INE, % con NS/NC) | ES hombres | ES mujeres |
|---|---|---|---|---|---|
| Cumplía requisitos de pensión | 76,9 | 70,3 | 69,9 | 69,0 | 72,1 |
| Alcanzó edad máxima de jubilación | 6,3 | 6,6 | 6,5 | 6,4 | 6,8 |
| Condiciones financieras favorables | 2,5 | 1,3 | 1,3 | 1,4 | 1,1 |
| Otras razones relacionadas con el trabajo (despido, estrés…) | 2,8 | 6,3 | 6,3 | 7,2 | 5,0 |
| Enfermedad o incapacidad propia | 6,8 | 10,5 | 10,5 | 10,9 | 10,0 |
| Cuidados u otras razones familiares | 1,8 | 1,5 | 1,5 | 0,6 | 2,8 |
| Otra razón | 2,9 | 3,5 | 3,5 | 4,5 (INE) | 2,1 (INE) |
- Universo ES: 2.607,5 mil personas de 50-74 años que dejaron de trabajar en los seis meses posteriores a percibir la pensión (INE tpx67854). Fuentes: [Eurostat lfso_23pens07](https://ec.europa.eu/eurostat/databrowser/view/lfso_23pens07/default/table), [INE tpx67854](https://www.ine.es/jaxiT3/Tabla.htm?t=67854), [INE nota](https://www.ine.es/dyngs/Prensa/es/mEPA2023.htm).
- Salidas no «normativas» (enfermedad + razones laborales + cuidados): ES 18,3% frente a UE 11,4% (cálculo propio sobre S02). Entre los países comparables, Países Bajos (enfermedad 15,6% + laborales 7,1% + cuidados 4,6% = 27,3%) y Portugal (16,8% + 6,0% + 2,8% = 25,6%) muestran más salidas por problemas que España.
- **Módulo 2012 (S10-S11, pensionistas 50-69 fuera del mercado laboral; incluye pensiones de invalidez y prejubilación):** España — problemas de salud o discapacidad 29,3%, cumplir requisitos 18,7%, edad máxima 15,8%, incentivos económicos 10,5%, pérdida del empleo o imposibilidad de encontrar trabajo 8,3%, otras relacionadas con el trabajo 6,8%, familiares/cuidados 3,2% (mujeres 6,6%, hombres 1,3%) — [INE 2012](https://www.ine.es/prensa/np785.pdf). UE-27 (Eurostat lfso_12reasnot): elegibilidad 39,1%, salud 20,9%, edad máxima 10,1%, pérdida de empleo 7,5%, cuidados 3,4% — [Eurostat lfso_12reasnot](https://ec.europa.eu/eurostat/databrowser/view/lfso_12reasnot/default/table). La categoría «pérdida de empleo / imposibilidad de encontrar trabajo» existía en 2012 y no existe como tal en 2023 (queda en «otras relacionadas con el trabajo»).
- **«Habría querido seguir trabajando» (solo 2012):** 43,5% de los 2,51 millones de personas de 50-69 años fuera del mercado laboral que cobraban pensión (1.093,3 mil), 51,5% no, 5,0% NS; por edad 68,2% (50-54), 61,8% (55-59), 53,7% (60-64), 34,4% (65-69); hombres 43,4%, mujeres 43,8% — [INE 2012](https://www.ine.es/prensa/np785.pdf). Eurostat lfso_12worklong confirma: ES 43,6% (H 43,4; M 44,0); UE-27 26,5% (H 27,9; M 25,1); UE-28 28,0%; Portugal 58,6%; Francia 30,9%; Italia 27,1%; Países Bajos 28,2%; Suecia 29,8%; Alemania 23,8% — [Eurostat lfso_12worklong](https://ec.europa.eu/eurostat/databrowser/view/lfso_12worklong/default/table) (S11). **Estado: coincide.**
- Jubilación anticipada (2012, Eurostat lfso_12earlyret, pensionistas de 50-69): sí 59,3% ES, 44,4% UE-27, 73,5% IT (S11).
- Metadatos: el módulo 2012 («Transition from work to retirement») sí incluía la pregunta «por qué no se quedó más tiempo» y la expectativa de salida; población objetivo 50-69 años, trabajando o que trabajaron después de los 50 — [Eurostat ESMS lfso_12](https://ec.europa.eu/eurostat/cache/metadata/en/lfso_12_esms.htm) (S12).

### Inferences
- La medida más directa de «dejó de trabajar antes de lo que quería» en datos oficiales es la de 2012 (43,5% ES; 26,5% UE-27) y está contaminada por el contexto de crisis de 2012 y por incluir pensionistas por invalidez: no debe usarse como estimación 2026. Sirve como límite superior del deseo de seguir.
- En 2023 los datos oficiales indican que, para el pensionista de jubilación español que dejó de trabajar, la salida «forzada» (enfermedad, despido/estrés, cuidados) afectó a ~1 de cada 5 (18,3%), más que en la UE (11,4%); el resto responde a umbrales normativos (edad/requisitos: 76,9% en ES). «Cumplir requisitos» no distingue voluntad de salida: es un motivo normativo, no una preferencia revelada.
- La brecha de cuidados por sexo (2,8% mujeres frente a 0,6% hombres) es pequeña en términos absolutos entre quienes ya cobran pensión: los cuidados pesan más en las salidas anteriores a la pensión (no cubiertas por este módulo).

### Gaps
- El módulo 2023 no contiene la pregunta «habría querido seguir» ni «qué factores le habrían hecho seguir» (la ESMS lista solo 11 variables: PENSTYP1, AGEPENSO, STATRECE, PENSTYP2, AGEPENSD, PROVTYPE, PENSSITU, WSTPREAS, WCONREAS, LMREENT, LMENTREAS): **hueco estructural**, no de descarga. Alternativas: SHARE y encuestas privadas (secciones 3 y 6).
- Los «factores que habrían hecho seguir trabajando» solo pueden aproximarse con SHARE (calidad del trabajo, salud) o con encuestas privadas españolas (sección 3).
- No hay tabla oficial 2023 de «despido» aislado: está dentro de «otras razones relacionadas con el trabajo» (6,3% ES; 2,8% UE).

## 3. Encuestas españolas que preguntan si los sénior quieren trabajar más

### Takeaway
Hay pocas encuestas españolas que pregunten directamente si los sénior quieren trabajar más, y miden cosas distintas. Solo el módulo EPA (INE/Eurostat) interroga a pensionistas reales: en 2012 preguntó a los jubilados fuera del mercado si habrían querido seguir (43,5%) y a los que trabajan su motivo principal (69,3% económico); en 2023 solo recoge el motivo de quienes siguieron. Las encuestas de entidades privadas (Santalucía, Mapfre, Aegon) miden actitudes o expectativas de la población general o de 55+, con fichas técnicas incompletas o inaccesibles, y ninguna distingue a quien trabaja por necesidad de quien sigue por proyecto.

### Cited Findings
**Ficha 3.1 — EPA/EU-LFS, módulo 2012 «Transición de la vida laboral a la jubilación» (INE y Eurostat; nota INE 18-jun-2013).**
- Patrocinador: estadística oficial (reglamento europeo, ejecuta el INE). Universo: personas de 50-69 años ocupadas o que han trabajado después de los 49 (8.486.200 personas analizadas de 10.745.800); el 33,6% cobraba alguna pensión — [INE nota módulo 2012](https://www.ine.es/prensa/np785.pdf) (S10).
- Preguntas: motivo principal para dejar de trabajar; si «hubiera deseado seguir trabajando» (Eurostat: «would have wished to stay longer in employment»); motivo principal para seguir trabajando cobrando pensión («económico»/«no económico»); cuándo prevé dejar de trabajar — [Eurostat ESMS lfso_12](https://ec.europa.eu/eurostat/cache/metadata/en/lfso_12_esms.htm) (S12).
- Resultados España: 43,5% de los 2,51 millones de pensionistas de 50-69 fuera del mercado habría querido seguir (68,2% a 50-54; 34,4% a 65-69); 69,3% de los 238,8 mil ocupados con pensión declara un motivo principal económico y 29,9% no económico (S10).
- Sesgos: el universo «pensión» incluye invalidez y prejubilación (el «no sabe» agrupa a quien solo cobra prejubilación); respuesta retrospectiva, posible racionalización; recesión (2012); el INE no detalla en la nota el tamaño muestral del módulo.
- ¿Necesidad o proyecto?: SÍ para quien sigue trabajando (motivo económico/no económico); NO distingue «proyecto» del «no económico» (satisfacción, contacto social).

**Ficha 3.2 — EPA/EU-LFS, módulo 2023 «Pensiones y participación en el mercado laboral» (INE 21-jun-2024; Eurostat lfso_23).** Ver secciones 1 y 2. Muestra de la EPA en sextas entrevistas (34.405 viviendas entrevistadas, 84,34% de respuesta), entrevista directa; universo 50-74 años; motivo principal único para seguir (6 categorías), referido a los 6 primeros meses de la pensión — [INE metodología](https://www.ine.es/daco/daco42/daco4211/metomodu23.pdf) (S09) y [Eurostat ESMS lfso_23](https://ec.europa.eu/eurostat/cache/metadata/en/lfso_23_esms.htm) (S07). No incluye «habría querido seguir».

**Ficha 3.3 — Instituto Santalucía, encuesta sobre longevidad y jubilación (nota publicada el 24-jun-2020; página actualizada el 28-may-2024).**
- Patrocinador: Instituto Santalucía (órgano de reflexión del Grupo Santalucía, aseguradora). Muestra, método, trabajo de campo y empresa de campo: NO consta en la página (solo «la última encuesta realizada por el Instituto Santalucía»). Universo: «españoles» sin precisar edad — [Santalucía, nota «El 88% de los españoles cree que seguiremos trabajando más allá de los 65 años»](https://institutosantalucia.es/sala-de-prensa/el-88-de-los-espanoles-cree-que-seguiremos-trabajando-mas-alla-de-los-65-anos/) (S17).
- Resultados: 88,3% cree que «en los próximos años la gente continuará trabajando más allá de los 65»; 89,9% opina que los mayores pueden aportar mucho al mercado laboral (80,2% experiencia y conocimiento; 57,1% formar a jóvenes). «En mi jubilación…»: 85,8% pasará más tiempo con seres queridos; 81,7% será una etapa activa; 76% nuevos proyectos personales; 56% viajará constantemente; 53,2% «buscaré una labor, aunque esté poco/nada remunerada, que tenga un propósito social»; 51,9% la salud no le permitirá hacer lo de antes; 35% gran cambio vital; 26,1% «mi propósito es no hacer nada» (S17).
- Sesgos: creencias y aspiraciones hipotéticas, no conducta; ningún ítem pregunta por trabajo remunerado propio tras la jubilación ni por su motivo; sin ficha técnica no se puede estimar el error.
- ¿Necesidad o proyecto?: NO lo mide. El 53,2% de «labor con propósito social» es actividad poco/nada remunerada (voluntariado), no empleo.
- El informe de febrero de 2026 del mismo instituto («La compatibilidad entre pensión y trabajo: avances y desafíos», Conde-Ruiz y Lahera) es un análisis jurídico-económico, no una encuesta; su nota de prensa afirma que «muchas personas podrían —y querrían— seguir activas al menos parcialmente» sin citar una encuesta que lo respalde — [Santalucía nota 10-feb-2026](https://institutosantalucia.es/wp-content/uploads/2026/02/260210_NP-INSTITUTO-SANTALUCIA-Espana-necesita-un-modelo-de-jubilacion-que-permita-e-incentive-seguir-trabajando-.pdf) (S16).

**Ficha 3.4 — Fundación Mapfre / Centro de Investigación Ageingnomics, VI Barómetro del Consumidor Sénior (publicado dic-2025; campo oct-2025).**
- Muestra: 2.260 entrevistas a residentes en España de 55 y más años (universo: más de 16,7 millones), error muestral ±2,1% con nivel de confianza del 95,5%; método mixto telefónico y online (CATI-CAWI). Temas declarados: comportamiento económico, vivienda, tecnología, movilidad, salud y «planes de vida» — [Ageingnomics, VI Barómetro](https://ageingnomics.fundacionmapfre.org/barometro/vi-barometro-del-consumidor-senior/) (S19). La serie existe desde 2020 («todos los años») con ediciones autonómicas — [Ageingnomics, Barómetro](https://ageingnomics.fundacionmapfre.org/barometro/) (S19).
- NO verificado: redacción y resultados de los ítems de trabajo/jubilación. Los dossiers PDF están en documentacion.fundacionmapfre.org, que devuelve HTTP 403 desde este entorno (sin acceso). Según un resultado de búsqueda (solo snippet, sin verificar) la III edición (dic-2022) incluiría un capítulo «Trabajo y jubilación».
- Sesgos probables (inferencia): universo 55+ completo (jubilados, ocupados, inactivos) sin aislar al pensionista que trabaja; el margen de ±2,1% con 95,5% coincide con el cálculo de muestreo aleatorio simple con 2 desviaciones típicas (2·√(0,25/2260)=2,1%), por lo que probablemente no incorpora efecto de diseño ni de cuotas; componente online no probabilístico; patrocinador con interés comercial en el consumo sénior.
- ¿Necesidad o proyecto?: no verificable con lo abierto.

**Ficha 3.5 — Aegon Retirement Readiness Survey, informe de España (primera edición; entrevistas en enero-febrero de 2012).**
- Patrocinador: Aegon (aseguradora), con Transamerica Center for Retirement Studies y Cicero Consulting; 9.000 personas en nueve países (tamaño por país no visible en el informe). Resultados España: 36% de los empleados actuales cree que, en lugar de jubilarse, seguirá con su patrón laboral actual; 47% de los jubilados dejó de trabajar de inmediato frente a 32% de los empleados que prevén hacerlo; solo 19% cree que podrá elegir cuándo dejar de trabajar; «seguir trabajando en el mismo campo» es una aspiración importante para el 8% (viajar 72%, familia y amigos 62%, aficiones 47%, voluntariado 21%, estudiar 14%, montar un negocio 9%) — [Aegon, Spain Retirement Readiness Survey Country Report](https://www.ta-retirement.com/resources/Spain-Retirement-Readiness-Survey-Country-Report-ENG.pdf) (S24).
- Sesgos: patrocinador comercial; muestra de edad laboral (incluye menores de 25); expectativas, no conducta; datos de 2012 (paro del 23,6% en febrero de 2012 según el propio informe); método de administración no indicado en el extracto.
- ¿Necesidad o proyecto?: mezcla ambos sin separarlos («tendré que trabajar más para tener los ingresos deseados» frente a «seguir en el mismo campo»).

**Ficha 3.6 — Fundación Adecco, «#TuEdadEsUnTesoro» (14.º informe, 14-jun-2022).**
- No es una encuesta de preferencias: «basa sus conclusiones en el análisis de los datos de la Encuesta de Población Activa» (1T 2022). Cifras: 11.231.400 de 23.259.400 activos tienen 45 o más años (48%; 36% en 2012; casi 60% en 2030); 9.902.200 ocupados de 45+ (49%); 1.329.200 parados de 45+ (42% de los parados), de ellos 58% de larga duración (47% en el resto), y 61% entre las mujeres sénior — [Fundación Adecco, 14.º informe](https://fundacionadecco.org/wp-content/uploads/2022/06/TuEdadEsUnTesoro-2022.pdf) (S20).
- Un resultado de búsqueda (solo snippet) menciona otra encuesta de la Fundación Adecco a 600 desempleados de 55+; no se abrió y no se usa.

**Ficha 3.7 — Randstad Research (informes sobre profesionales sénior).** No se abrió ningún informe original; los resultados de búsqueda (solo snippet) citan una «encuesta propia» (85% de los séniors buscando empleo; 55% atribuye su estancamiento a la edad) sin fecha. No se usa ninguna cifra; queda como hueco.

**Ficha 3.8 — Generation (con la OCDE), «The Midcareer Opportunity» (9-oct-2023).** Nota de prensa recogida por Forbes España («información remitida por la empresa firmante»): informe con datos de la OCDE y encuesta a miles de empresarios, solicitantes de empleo y empleados en ocho países de Europa y EE. UU.; la investigación en Europa financiada por Google.org y en EE. UU. por Clayton, Dubilier & Rice; las personas de 45-64 años fueron el 40% de la mano de obra de la OCDE en 2020 (28% en 1990) — [Forbes España](https://forbes.es/ultima-hora/347341/informe-de-generation-y-la-ocde-los-trabajadores-mayores-de-45-anos-representan-una-oportunidad-de-talento/) (S22). Trata de prejuicios de contratación hacia 45+ (no de la voluntad de seguir tras la pensión); no se pudo abrir el informe (la ficha de la OCDE devolvió HTTP 403).

**Fichas de índices (no son encuestas a trabajadores).**
- Natixis IM, Global Retirement Index 2025 (con CoreData Research): España 39.º de 44 países con 48/100, última de la UE por tercer año; mejor en esperanza de vida (5.º, 94%); el paro es el principal lastre — [Merca2, 10-sep-2025](https://www.merca2.es/2025/09/10/espana-peor-europeo-jubilacion-2229844/) y [The Local, 12-sep-2025](https://www.thelocal.es/20250912/spain-has-worst-quality-of-retirement-in-the-eu-study-claims) (S23; prensa, no se abrió la web de Natixis).
- Mercer/CFA Institute, Global Pension Index 2025: 52 sistemas, tres pilares (adecuación, sostenibilidad, integridad); España 63,8 — [Mercer](https://www.mercer.com/insights/investments/market-outlook-and-trends/mercer-cfa-global-pension-index/) (S26).
- Schroders (Global Investor Study 2018-2020): no se abrió ninguna publicación; solo snippets (S25), no se usan cifras.

### Inferences
- Ninguna fuente privada española abierta pregunta a pensionistas que trabajan «por qué» de forma comparable a la EPA; para el relato «necesidad frente a proyecto» solo el módulo INE/Eurostat sostiene cifras. Las encuestas de Santalucía, Mapfre y Aegon sirven como contexto de expectativas (p. ej., 88,3% espera que se trabaje más allá de 65; 36% de los activos en 2012 no se veía jubilándose), nunca como evidencia de motivos.
- El indicio más cercano a «proyecto» fuera del INE es el 53,2% de Santalucía que buscaría una labor con propósito social, pero es hipotético, poco o nada remunerado y de fiabilidad baja.
- Cuando una fuente privada afirme que «los sénior quieren seguir trabajando», hay que comprobar universo (¿pensionistas o población general?), redacción (¿intención o deseo?) y si se separa el motivo económico.

### Gaps
- Redacción y resultados de los ítems de empleo/jubilación de los Barómetros de Mapfre (III 2022, VI 2025): PDF inaccesibles (HTTP 403); pedir el dossier y las tablas («Tablas Barómetro Sénior Nacional») a la Fundación.
- Randstad Research, Schroders, Generation (informe original) y la encuesta de Adecco a 600 desempleados de 55+: no abiertos.
- No se han buscado/abierto otras encuestas españolas posibles (CIS, Eurobarómetro especial de envejecimiento activo de 2012, Fundación BBVA/Ivie): ampliar si se necesita.
- Ficha técnica de la encuesta Santalucía 2020 (muestra, método, campo): no publicada en la página.

## 4. Perfil de quienes compatibilizan pensión y trabajo en España (jubilación activa)

### Takeaway
No se ha podido obtener la estadística oficial de la Seguridad Social sobre «jubilación activa» (número de beneficiarios, reparto autónomos/asalariados, sectores, pensión media): no figura en los documentos abiertos y eSTADISS no es accesible desde este entorno. Lo que sí hay es (a) el módulo EPA/EU-LFS 2023, que mide a todos los pensionistas de jubilación que trabajan (no solo la figura legal): 7,6% de los de 50-74 años en España (21,4% en la UE), con más asalariados (51,6%) que autónomos (27,5%) en números absolutos pero mayor propensión relativa en autónomos (18,2% frente a 7,7%) y en ocupaciones cualificadas; y (b) indicios de que la jubilación activa legal es mayoritariamente de autónomos (Santalucía/Fedea, 2026) y de que los autónomos, con pensiones medias mucho más bajas, demoran más la jubilación (CCOO, 2026, vía prensa). Conjunto: mezcla de necesidad y proyecto sin base para decidir cuál predomina.

### Cited Findings
**Tamaño y composición (EPA/EU-LFS 2023, pensionistas de jubilación de 50-74 años).**
- Situación al empezar la pensión (INE, 3.806,7 mil pensionistas): dejó de trabajar 68,5%; siguió sin cambios 1,79% (68,1 mil); siguió con cambios 3,07% (116,7 mil); no trabajaba 25,5%. Siguieron trabajando 184,8 mil: 126,2 mil hombres (5,7% de los pensionistas hombres) y 58,7 mil mujeres (3,7%); por edad, 48,6 mil de 50-64 años (10,3% de los pensionistas de esa edad) y 136,3 mil de 65-74 (4,1%) — [INE tpx67853](https://www.ine.es/jaxiT3/Tabla.htm?t=67853) (S06; cálculo propio de agregados).
- Eurostat (universo con situación laboral conocida, 2.800,6 mil): siguió o reingresó el 7,6% (212,9 mil) frente al 21,4% de la UE-27; reingresar tras haber dejado de trabajar es residual (menos del 1% de los pensionistas en España) — [Eurostat lfso_23pens11](https://ec.europa.eu/eurostat/databrowser/view/lfso_23pens11/default/table) (S04) y [Statistics Explained](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Working_life_characteristics_and_the_transition_to_retirement) (S13).
- Composición de los 212,9 mil españoles: asalariados 109,9 mil (51,6%), autónomos 58,5 mil (27,5%), situación profesional no aplicable 41,4 mil (19,4%), ayuda familiar 3,2 mil (1,5%) (UE-27: 51,0%, 25,9%, 21,0%, 1,7%) (S04, cálculo propio).
- Propensión por situación profesional: asalariados 7,7% (UE 24,4%); autónomos 18,2% (UE 56,4%); por sexo en España, autónomos hombres 22,1% y autónomas 6,7% (baja fiabilidad) (S04, S08, S13).
- Advertencia de Eurostat: la información de situación profesional y ocupación solo existe para aproximadamente la mitad de los pensionistas; para quienes dejaron de trabajar refleja el momento de la primera pensión y para quienes siguen su empleo actual o último, por lo que la comparabilidad es limitada (S13).

**Propensión a seguir o reingresar por ocupación (CIUO-08), pensionistas de jubilación de 50-74 años, 2023 — Eurostat lfso_23pens12 ([tabla](https://ec.europa.eu/eurostat/databrowser/view/lfso_23pens12/default/table), S14; datos en `datos/brutos/encuestas/eurostat_lfs_modulo2023_2012/lfso_23pens12_ES_EU_Y50-74_T_PC.json`):**

| Ocupación | España (%) | UE-27 (%) |
|---|---|---|
| Directores y gerentes | 22,7 | 40,2 |
| Profesionales científicos e intelectuales | 12,0 | 38,5 |
| Técnicos y profesionales de apoyo | 12,6 | 30,2 |
| Empleados administrativos | 7,1 | 20,9 |
| Servicios y ventas | 7,7 | 32,3 |
| Agricultura, silvicultura y pesca cualificados | 13,8 | 40,2 |
| Oficios y artesanos | 6,3 | 23,3 |
| Operadores de maquinaria | 8,5 | 27,9 |
| Ocupaciones elementales | 6,1 | 25,9 |
| Sin ocupación aplicable | 4,0 | 10,1 |
| Total | 7,6 | 21,4 |

**Marco legal de la jubilación activa (informe Santalucía/Fedea, feb-2026).**
- Jubilación activa para asalariados tras el Real Decreto-ley 11/2024: se compatibiliza el 45% de la pensión el primer año, 55% el segundo, 65% el tercero, 80% el cuarto y 100% desde el quinto; ya no se exige el 100% de la base reguladora; las nuevas cotizaciones no mejoran la pensión futura ni generan complementos por demora; no existe contrato específico para jubilados activos. Autónomos con un trabajador indefinido a tiempo completo: 75% de la pensión desde el inicio, hasta el 100% en el cuarto año. Jubilación parcial: exige 33 años cotizados y contrato de relevo; la flexible/reversible estaba pendiente de desarrollo reglamentario — [Santalucía, nota 10-feb-2026](https://institutosantalucia.es/wp-content/uploads/2026/02/260210_NP-INSTITUTO-SANTALUCIA-Espana-necesita-un-modelo-de-jubilacion-que-permita-e-incentive-seguir-trabajando-.pdf) (S16) e [informe completo](https://institutosantalucia.es/wp-content/uploads/2026/02/informe_compatibilidad_entre_pension_y_trabajo_ISL.pdf) (S16).
- Afirmación sobre el perfil: «dado que la mayoría de los jubilados activos actuales lo son por cuenta propia, es razonable pensar» que existe un incentivo al falso autónomo; el informe no aporta en ese pasaje la cifra ni la fuente oficial (S16).
- Contexto comparado (OCDE 2019, datos 2014/2015, vía Santalucía): proporción de personas de 60-69 años que combinan trabajo y pensión: España hombres 0,3% y mujeres 1,8%; EE. UU. 19,2% y 16,8% — [Santalucía, «Prolongación de la vida laboral» (abr-2024)](https://institutosantalucia.es/wp-content/uploads/2024/04/05-prologacion-de-la-vida-laboral.pdf) (S18).
- Otros rasgos del paso a la pensión (INE 2023): 24,2% de los pensionistas tuvo reducción por jubilación anticipada y solo 1,4% (52,1 mil) bonificación por aplazamiento (S06, tpx67845).

**Autónomos, demora y nivel de pensión (CCOO, Observatorio Social de las Personas Mayores, 2026, citado por Vozpópuli).**
- Jubilación demorada: 17.651 personas en 2022 y 40.952 en 2025; los autónomos demoran un 31,1% frente al 6,0% del Régimen General (11% en el conjunto); en enero de 2026 las altas con demora de autónomos igualaron a las del Régimen General (unas 20.000 cada uno). Jubilación anticipada: 32% de asalariados frente al 13,4% de autónomos. Pensión media 2025: 1.698 €/mes por cuenta ajena y 1.052 € por cuenta propia (650 € menos) — [Vozpópuli](https://www.vozpopuli.com/economia/empleo/uno-de-cada-tres-autonomos-retrasa-su-jubilacion-sus-pensiones-son-650-euros-mas-bajas.html) (S35; prensa, no se abrió el informe de CCOO).

### Inferences
- Hay dos lecturas aparentemente contradictorias: Santalucía/Fedea dice que la mayoría de los jubilados activos legales son autónomos, mientras el módulo EPA 2023 muestra más asalariados que autónomos entre los pensionistas que trabajan. Pueden ser compatibles: el módulo mide cualquier trabajo con pensión de jubilación (incluida pensión anticipada y trabajos no acogidos a la figura legal de jubilación activa), mientras la «jubilación activa» exige edad ordinaria y condiciones específicas; esto es una hipótesis, no verificada por falta del dato oficial.
- Necesidad frente a proyecto: los autónomos combinan pensiones bajas (1.052 €/mes) con la mayor propensión a seguir (18,2% en ES) y a demorar (31,1%), lo que sugiere presión económica en parte del colectivo; pero el motivo «necesario» es solo 19,6% en el conjunto español y no hay cruce por situación profesional. La mayor propensión de directivos (22,7%) y profesionales apunta a una vía de proyecto/capital humano. Ninguna cifra abierta permite repartir el colectivo entre ambas.
- Para el relato del seguro/previsión: el segmento cuantitativamente relevante es pequeño (212,9 mil personas de 50-74 años cobrando pensión de jubilación y trabajando; ~185 mil si solo se cuentan las que siguieron al empezar), y se concentra en cualificados y autónomos.

### Gaps
- Estadística oficial de jubilación activa de la Seguridad Social (n.º de beneficiarios, % autónomos/asalariados, sectores, pensión media): NO obtenida (vía: eSTADISS/Estadística de Pensiones o Boletín de Estadísticas Laborales; o petición al Ministerio).
- Sectores (CNAE): no hay desglose; solo ocupación (CIUO) en lfso_23pens12.
- El informe de CCOO no se abrió (solo prensa); la pensión media por régimen de septiembre de 2026 y el Real Decreto 416/2026 sobre jubilación flexible aparecen únicamente en resultados de búsqueda (no abiertos) y en una actualización de julio de 2026 de Santalucía que devolvió 404.
- No hay cruce de motivo (necesario/disfrute) por situación profesional ni por tipo de pensión.

## 5. Gradiente socioeconómico (ingresos, salud, educación)

### Takeaway
La evidencia disponible es coherente: a mayor educación y cualificación, más se sigue trabajando tras cobrar la pensión y menos se desea jubilarse cuanto antes; a peor salud y menos renta, más deseo de salida temprana y más salidas forzadas. Entre quienes sí siguen, las rentas bajas y las deudas se asocian a volver «por dinero» (ONS, AARP). No existe tabla pública que cruce el motivo declarado (necesidad/disfrute) con educación o renta en el módulo 2023.

### Cited Findings
| Indicador | Bajo / peor | Medio | Alto / mejor | Fuente |
|---|---|---|---|---|
| UE-27 2023: % de pensionistas de jubilación que siguieron/reingresaron, por educación | 14,5% (CINE 0-2) | n. d. | 30,8% (CINE 5-8) | [Eurostat Statistics Explained](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Working_life_characteristics_and_the_transition_to_retirement) (S13) |
| España 2025: tasa de empleo 55-64 años por educación | 51,8% (CINE 0-2) | 64,2% (CINE 3-4) | 75,3% (CINE 5-8) | [Eurostat lfsa_ergaed](https://ec.europa.eu/eurostat/databrowser/view/lfsa_ergaed/default/table) (S15; marca «d»: definición distinta) |
| UE-27 2025: tasa de empleo 55-64 años | 50,6% | 67,0% | 80,3% | S15 |
| España 2025: tasa de empleo 65-74 años | 5,3% | 8,2% | 13,4% | S15 |
| UE-27 2025: tasa de empleo 65-74 años | 7,9% | 11,1% | 19,9% | S15 |
| España 2023: pensionistas que siguen, directivos frente a ocupaciones elementales | 6,1% | — | 22,7% | S14 |
| SHARE ola 1 (2004), empleados ≤65 años: «le gustaría jubilarse lo antes posible» (sí), por educación | 57,6% (baja) | 48,0% | 40,3% (alta) | [Siegrist et al. 2007](https://fenix.iseg.ulisboa.pt/downloadFile/281608120805128/Siegrist_etal_2006.pdf) (S27) |
| SHARE, por renta equivalente | 50,3% (baja) | 50,4% | 46,8% (alta) | S27 |
| SHARE, por salud autopercibida | 62,7% (peor que buena) | — | 44,8% (buena o mejor) | S27 |

- SHARE (S27): 6.836 empleados y autoempleados de hasta 65 años (3.520 hombres y 3.316 mujeres) de diez países, muestras probabilísticas, entrevista cara a cara; la intención de jubilación anticipada va de 29,7% en Países Bajos a 67,2% en España; pregunta literal: «Pensando en su trabajo actual, ¿le gustaría jubilarse lo antes posible?» (sí/no). Calidad de trabajo pobre (desequilibrio esfuerzo-recompensa OR 1,72; bajo control OR 1,51) predice la intención tras ajustar por bienestar (S27).
- Salud como causa de salida: en 2023, el 10,5% de los pensionistas españoles que dejaron de trabajar lo hizo por enfermedad o incapacidad propia (UE 6,8%) — [Eurostat lfso_23pens07](https://ec.europa.eu/eurostat/databrowser/view/lfso_23pens07/default/table) (S02); en 2012 era el 29,3% en España (universo con pensiones de invalidez) — [INE 2012](https://www.ine.es/prensa/np785.pdf) (S10).
- Edad y necesidad en el módulo 2023: «financieramente necesario» pesa más entre pensionistas de 50-64 años (UE 36,6%; España 33,7%) que entre los de 65-74 (UE 26,2%; España 15,3%); el disfrute pesa más a partir de 65 (UE 38,5% frente a 28,9%) (S01).
- Reino Unido (ONS, ago-2022, 50-65 años que dejaron su empleo desde la pandemia y volverían): quienes consideran volver pueden afrontar un gasto imprevisto en menor proporción (61% frente a 77% de quienes no consideran volver) y son menos propietarios sin hipoteca (57% frente a 78%); «por el dinero»: 69% (50-54), 62% (55-59), 59% (60-65), 68% con hipoteca o préstamo frente a 60% con vivienda en propiedad plena; quienes no tienen deudas eligieron retirarse en mayor proporción (28% frente a 19%) — [ONS](https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/economicinactivity/articles/returningtotheworkplacethemotivationsandbarriersforpeopleaged50yearsandovergreatbritain/august2022) (S29).
- EE. UU. (Pew, dic-2023, CPS): el 19% de los mayores de 65 trabajaba en 2023; 44% de los trabajadores de 65+ tiene grado universitario (18% en 1987); 62% a tiempo completo; 23% autónomos (10% de 25-64) — [Pew Research Center](https://www.pewresearch.org/social-trends/2023/12/14/older-workers-are-growing-in-number-and-earning-higher-wages/) (S33). Es evidencia de selección positiva de quienes siguen, no de motivos.

### Inferences
- El gradiente funciona en dos direcciones: los menos cualificados y con peor salud salen antes (a menudo sin querer), y quienes se quedan después de la pensión están positivamente seleccionados (educación, ocupación directiva/profesional, autoempleo). Por eso el 47,6% UE de «disfrute + integración social» describe a un colectivo selecto, no a la población sénior en general.
- La necesidad económica se concentra por edad (pensionistas de 50-64 años) más que por sexo; probablemente también por renta, pero ese cruce no está publicado (hipótesis).
- Los datos españoles de empleo por educación llevan marca «d» de Eurostat (definición distinta), de modo que la brecha de 23,5 puntos (75,3% frente a 51,8% a los 55-64) debe citarse con esa nota.

### Gaps
- Cruce motivo × educación/renta/salud en el módulo 2023: no publicado (microdatos EU-LFS).
- SHARE: no se han extraído olas recientes (7-9) ni resultados específicos de España por educación/renta; la cifra citada es de la ola 1 (2004).
- Gradiente por renta de los pensionistas españoles que trabajan: sin dato.

## 6. Encuestas internacionales (SHARE, Eurofound, ONS, AARP, Pew, HRS)

### Takeaway
Fuera de España, la evidencia es de dos tipos. Encuestas de panel probabilístico estadounidenses (AARP/NORC 2025-26) indican que quienes «desjubilan» vuelven sobre todo por dinero (48%) y solo el 14% por mantenerse activo, y que 39-41% de los 50+ que trabajan o buscan empleo lo hacen por gastos básicos. El análisis de la HRS (Maestas, 2010) matiza que la mayor parte de los reingresos estaba prevista y no responde a shocks. En el Reino Unido, el dinero motiva al 59-69% de los mayores de 50 que dejaron su empleo y considerarían volver (ONS, 2022). SHARE (2004) muestra que cerca de la mitad de los ocupados de 50-65 años querría jubilarse cuanto antes (67,2% en España). Eurofound no pudo abrirse.

### Cited Findings
**AARP / NORC Foresight 50+ (EE. UU.).**
- Nota de AARP de 5-feb-2026 («Retirement on Pause»): panel probabilístico de NORC representativo de los hogares estadounidenses de 50+; 2.083 adultos de 50+ (136 «unretirees», 1.323 jubilados, 1.124 en la población activa), entrevistas del 13-17 nov y 11-16 dic de 2025, online y por teléfono, ponderadas por edad, sexo, educación, raza/etnia, región y afiliación a AARP. Resultados: 7% de los jubilados «desjubiló» (volvió a la población activa) en los últimos seis meses; 48% declara como razón principal ganar dinero y 14% mantenerse activo; entre los 50+ que trabajan o buscan empleo, 41% dice que su motivo principal es afrontar el coste de la vida diaria; 24% teme perder el empleo en un año; 67% cree que sería difícil encontrar uno nuevo (35% lo atribuye a discriminación por edad y 22% a salud o discapacidad) — [AARP, nota de prensa](https://www.aarp.org/press/releases/2026-02-05-high-costs-older-americans-back-to-work.html) (S31).
- Ola de verano de 2026 (14-18 may y 17-22 jun de 2026; 2.065 adultos de 50+, 116 «unretirees»): 6% de los jubilados volvió a trabajar en los últimos seis meses (6% verano 2025; 7% invierno 2025), 48% por necesidad económica; entre los 50+ que trabajan o buscan empleo, 39% señala como razón más importante el dinero para gastos básicos y le siguen disfrutar del trabajo (10%), mantenerse ocupado (8%), ahorrar para la jubilación (7%) y mantener el seguro médico (6%); 20% espera jubilarse más tarde de lo previsto (23% en olas previas) y 46% en el momento previsto; 68% de quienes retrasan cita el coste de la vida; 71% de los jubilados cree que se jubiló en el momento adecuado y 24% demasiado pronto; razones iniciales para jubilarse: enfermedad o discapacidad 21%, dinero suficiente 21%, elegibilidad a la Seguridad Social 16%, pensión 15% — [AARP Public Policy Institute, Labor Force Pulse](https://www.aarp.org/pri/topics/work-finances-retirement/employers-workforce/retirement-decisions-working-job-hunting/) (S32).
- Cautelas: con n=116-136 el margen aproximado de los porcentajes de «unretirees» es de unos ±8-9 puntos (cálculo propio, sin efecto de diseño); pregunta de razón principal única; patrocinador con agenda de política pública.

**HRS (Health and Retirement Study).** Maestas (2010), «Back to Work: Expectations and Realizations of Work after Retirement», Journal of Human Resources 45(3): casi el 50% de los jubilados sigue una trayectoria no tradicional (jubilación parcial o «unretirement») y al menos el 26% de los jubilados vuelve a trabajar; el reingreso estaba previsto antes de jubilarse en la gran mayoría de los casos y no es resultado de shocks financieros, mala planificación o poca riqueza — [JHR, resumen](https://jhr.uwpress.org/content/45/3/718) (S34; solo se abrió el resumen; años de datos no verificados).

**Pew Research Center (dic-2023).** Basado en la Current Population Survey (Census) y la Survey of Household Economics and Decisionmaking 2022 de la Reserva Federal: 19% de los mayores de 65 en EE. UU. trabajaba en 2023; salario típico de 22 $/hora en 2022 (13 $ en 1987); 62% a tiempo completo; 7% de todos los salarios; el informe remite a una encuesta de Pew que halla a los trabajadores de 65+ más satisfechos con su empleo que los jóvenes — [Pew](https://www.pewresearch.org/social-trends/2023/12/14/older-workers-are-growing-in-number-and-earning-higher-wages/) (S33). No mide motivos de necesidad frente a elección.

**ONS Over 50s Lifestyle Study (Gran Bretaña, 2022).**
- Diseño: muestra de 43.250 personas de 50-65 años seleccionadas entre quienes habían respondido a la Labour Market Online Survey; 23.490 respuestas (54,4%) en agosto de 2022; pesos ajustados por no respuesta y calibrados por sexo × edad, región y grupo de empleo; estadísticas experimentales — [ONS, Returning to the workplace (ago-2022)](https://www.ons.gov.uk/employmentandlabourmarket/peoplenotinwork/economicinactivity/articles/returningtotheworkplacethemotivationsandbarriersforpeopleaged50yearsandovergreatbritain/august2022) (S29).
- Resultados (universo: 50-65 años que dejaron su empleo desde marzo de 2020, no han vuelto y volverían): motivos para dejar el empleo: jubilarse 24%, cambio de estilo de vida 17%, pandemia 17%, despido por reducción de plantilla 17%, estrés 15%; en la oleada 2, 72% de los de 50-59 años que habían dejado el trabajo consideraría volver (58% en la oleada 1); «por el dinero»: 65% de los de 50-59 (56% en la oleada 1); entre quienes tienen una enfermedad física o mental, volverían por dinero (67%), por compañía o un empleo agradable (46%) y por salud mental (42%) (S29).
- Oleada 2: entre quienes volverían, los factores más importantes al elegir empleo son horario flexible (32%), buen salario (23%) y teletrabajo (12%); 36% de quienes dejaron el empleo desde la pandemia y no han vuelto se fue para jubilarse (48% de 60-65, 9% de 50-54) — [ONS, Reasons for workers aged over 50 leaving employment (wave 2)](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/articles/reasonsforworkersagedover50yearsleavingemploymentsincethestartofthecoronaviruspandemic/wave2) (S30).
- Límites: universo de «salidas desde la pandemia» (selección), intención hipotética («consideraría volver»), panel online, no pensionistas.

**SHARE (Survey of Health, Ageing and Retirement in Europe).** Ver sección 5: Siegrist et al. (2007), ola 1 (2004), diez países, cara a cara, 6.836 ocupados: casi la mitad habría querido jubilarse cuanto antes; 67,2% en España y 29,7% en Países Bajos (S27). No se localizó una cifra más reciente de «jubilarse lo antes posible» para España.

**Eurofound.** El informe «Keeping older workers in the labour force» (31-mar-2025) y los informes nacionales (España e Italia, 28-mar-2025) existen según resultados de búsqueda, pero las páginas de Eurofound devolvieron un desafío anti-bot (HTTP 429, Vercel) y no se pudieron abrir; no se registra ninguna cifra (S28).

### Inferences
- Los resultados de AARP (necesidad dominante) y de la HRS (reingreso previsto, no por shock) no se contradicen: AARP pregunta el motivo principal de quienes ya volvieron o trabajan; Maestas analiza si el reingreso era anticipado. Un reingreso puede ser «planificado» y a la vez «por dinero».
- En EE. UU. y Reino Unido el dinero sube al 48-69% cuando el universo son quienes volvieron o volverían tras haber salido; en el módulo EU-LFS 2023 («financieramente necesario» 28,6% en la UE-27), el universo son quienes siguieron al empezar la pensión. La diferencia de universo y de redacción (motivo principal frente a motivos múltiples, con categoría «financieramente atractivo» aparte) explica parte de la brecha y desaconseja comparar cifras entre países sin ajustarlas.
- La HRS y SHARE ofrecen la base académica más sólida (paneles probabilísticos revisados por pares); AARP es sólido en diseño pero con n pequeño y agenda; ONS es oficial pero experimental y de población de salidas pandémicas.

### Gaps
- Eurofound (EWCS, informe 2025): no accesible.
- HRS/SHARE recientes: solo un resumen de 2010 y un artículo con datos de 2004; faltan olas posteriores y cifras de España.
- Eurobarómetro y OCDE (Pensions at a Glance, Ageing and Employment Policies: Spain): no consultados.

## Fichas de fiabilidad de las encuestas

PENDIENTE

## Registro de fuentes

PENDIENTE

## Matriz de verificación

PENDIENTE
