# job-presentations

Plantillas de presentación alineadas con la imagen corporativa de Santalucía Seguros.

## Plantilla Santalucía

Archivo: [`plantillas/santalucia-plantilla.pptx`](plantillas/santalucia-plantilla.pptx) (16:9, PowerPoint / Keynote / Google Slides).

Incluye 7 diseños (Vista > Patrón de diapositivas) con marcadores de posición editables
y 10 diapositivas de ejemplo que puedes duplicar:

| Diseño | Uso |
|---|---|
| `SL_PORTADA` | Portada: título, subtítulo, ponente y fecha |
| `SL_SECCION` | Separador de sección con número destacado |
| `SL_CONTENIDO` | Título + texto/viñetas (también agenda, cronograma, gráficos) |
| `SL_DOS_COLUMNAS` | Comparativas (antes/después, pros/contras) |
| `SL_IMAGEN` | Fotografía a media página + texto |
| `SL_SUAVE` | Fondo tintado para cifras clave o tarjetas |
| `SL_CIERRE` | Agradecimiento y datos de contacto |

### Identidad aplicada

| Token | Color | Uso |
|---|---|---|
| Azul corporativo | `#00257A` | Color dominante: fondos de portada/sección, títulos |
| Azul oscuro | `#001A57` | Círculos decorativos sobre azul |
| Azul claro | `#C9D5EE` | Texto secundario sobre azul |
| Tinte | `#EEF2FA` | Fondos de tarjetas y diapositivas suaves |
| Amarillo acento | `#FEDD42` | Solo para destacar (cifra principal, fase actual). Nunca como color de texto sobre blanco |
| Texto | `#1A1F36` | Cuerpo de texto |

- Tipografía: Arial (presente en cualquier equipo). Si el manual corporativo indica otra
  fuente, cámbiala en `F` dentro de `scripts/build-plantilla.js`.
- Motivo gráfico: círculos concéntricos y un punto amarillo como acento.

> Los colores se han tomado de fuentes públicas de la marca. Contrástalos con el manual
> de identidad oficial si tienes acceso y ajústalos en el objeto `C` del script.

### Añadir el logo oficial

El logo no se incluye en el repositorio. Coloca los archivos oficiales en:

- `assets/logo.png` — versión a color (sobre fondo blanco)
- `assets/logo-blanco.png` — versión en blanco (sobre fondo azul)

y regenera la plantilla. Mientras no existan, se muestra un recuadro "LOGO" en su lugar.

### Regenerar

```bash
npm install
npm run build
```
