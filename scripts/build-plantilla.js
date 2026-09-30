// Genera plantillas/santalucia-plantilla.pptx: patrones (masters) con marcadores
// de posición + una diapositiva de ejemplo por diseño.
// Uso: npm run build   (coloca el logo oficial en assets/logo.png y assets/logo-blanco.png)
const fs = require("fs");
const path = require("path");
const pptxgen = require("pptxgenjs");

const ROOT = path.join(__dirname, "..");
const OUT = path.join(ROOT, "plantillas", "santalucia-plantilla.pptx");

// Paleta de marca (ajustar aquí si el manual corporativo indica otros valores)
const C = {
  azul: "00257A",      // azul corporativo (dominante)
  azulOsc: "001A57",   // variante oscura para fondos/profundidad
  azulMed: "3D5BA9",   // azul intermedio para gráficos
  azulClaro: "C9D5EE", // texto secundario sobre azul
  tinte: "EEF2FA",     // fondo suave para tarjetas
  amarillo: "FEDD42",  // acento: usar con moderación
  texto: "1A1F36",
  gris: "5B6477",
  blanco: "FFFFFF",
};
const F = { tit: "Arial", cuerpo: "Arial" };
const W = 13.333, H = 7.5, M = 0.6;

const logoColor = path.join(ROOT, "assets", "logo.png");
const logoBlanco = path.join(ROOT, "assets", "logo-blanco.png");

// Logo real si existe; si no, un marcador discreto que indica dónde va.
function logo(onDark, x, y, w, h) {
  const file = onDark ? logoBlanco : logoColor;
  if (fs.existsSync(file)) return [{ image: { path: file, x, y, w, h, sizing: { type: "contain", w, h } } }];
  const col = onDark ? C.azulClaro : C.gris;
  return [
    { rect: { x, y, w, h, fill: { type: "none" }, line: { color: col, width: 0.75, dashType: "dash" } } },
    { text: { text: "LOGO", options: { x, y, w, h, align: "center", valign: "middle", fontFace: F.cuerpo, fontSize: 9, bold: true, color: col, charSpacing: 3, margin: 0 } } },
  ];
}

// Los patrones de pptxgenjs no admiten "oval": se dibuja como texto vacío con forma de elipse
function circulo(x, y, d, color, transp = 0) {
  return { text: { text: "", options: { shape: "ellipse", x, y, w: d, h: d, fill: { color, transparency: transp }, line: { type: "none" } } } };
}

// Motivo visual: círculos concéntricos parcialmente fuera de la diapositiva
function circulos(x, y, d, color, transp) {
  return [
    circulo(x, y, d, color, transp),
    circulo(x + d * 0.2, y + d * 0.2, d * 0.6, C.azul, 0),
  ];
}

const numPag = { x: W - M - 0.6, y: H - 0.55, w: 0.6, h: 0.3, fontFace: F.cuerpo, fontSize: 10, color: C.gris, align: "right" };

function build() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.title = "Plantilla Santalucía";
  pres.company = "Santalucía Seguros";
  pres.theme = { headFontFace: F.tit, bodyFontFace: F.cuerpo };

  // ---------- Patrones ----------
  pres.defineSlideMaster({
    title: "SL_PORTADA",
    background: { color: C.azul },
    objects: [
      ...circulos(W - 5.2, -1.6, 7.5, C.azulOsc, 20),
      circulo(W - 2.3, H - 2.1, 1.1, C.amarillo),
      ...logo(true, M, 0.55, 2.2, 0.7),
      { placeholder: { options: { name: "titulo", type: "title", x: M, y: 2.3, w: 8.2, h: 1.9, align: "left", fontFace: F.tit, fontSize: 44, bold: true, color: C.blanco, valign: "bottom", margin: 0 }, text: "Título de la presentación" } },
      { placeholder: { options: { name: "subtitulo", type: "body", x: M, y: 4.35, w: 8.2, h: 0.9, fontFace: F.cuerpo, fontSize: 20, color: C.azulClaro, valign: "top", margin: 0 }, text: "Subtítulo o propósito de la reunión" } },
      { placeholder: { options: { name: "fecha", type: "body", x: M, y: H - 1.1, w: 6, h: 0.45, fontFace: F.cuerpo, fontSize: 12, color: C.blanco, margin: 0 }, text: "Nombre del ponente · Fecha" } },
    ],
  });

  pres.defineSlideMaster({
    title: "SL_SECCION",
    background: { color: C.azul },
    objects: [
      ...circulos(-2.2, H - 3.8, 6, C.azulOsc, 20),
      ...logo(true, W - M - 1.6, H - 0.95, 1.6, 0.5),
      { placeholder: { options: { name: "numero", type: "body", x: 4.6, y: 1.6, w: 3, h: 1.4, align: "left", fontFace: F.tit, fontSize: 72, bold: true, color: C.amarillo, margin: 0 }, text: "01" } },
      { placeholder: { options: { name: "titulo", type: "title", x: 4.6, y: 3.1, w: 8, h: 1.6, align: "left", fontFace: F.tit, fontSize: 40, bold: true, color: C.blanco, valign: "top", margin: 0 }, text: "Título de la sección" } },
    ],
  });

  const cabecera = { name: "titulo", type: "title", x: M, y: 0.45, w: W - 2 * M - 1.8, h: 0.9, align: "left", fontFace: F.tit, fontSize: 32, bold: true, color: C.azul, valign: "middle", margin: 0 };
  const pieContenido = [...logo(false, W - M - 1.4, 0.55, 1.4, 0.45)];

  pres.defineSlideMaster({
    title: "SL_CONTENIDO",
    background: { color: C.blanco },
    slideNumber: numPag,
    objects: [
      ...pieContenido,
      { placeholder: { options: cabecera, text: "Título de la diapositiva" } },
      { placeholder: { options: { name: "cuerpo", type: "body", x: M, y: 1.65, w: W - 2 * M, h: H - 2.5, align: "left", fontFace: F.cuerpo, fontSize: 20, color: C.texto, valign: "top", margin: 0 }, text: "Texto del contenido" } },
    ],
  });

  pres.defineSlideMaster({
    title: "SL_DOS_COLUMNAS",
    background: { color: C.blanco },
    slideNumber: numPag,
    objects: [
      ...pieContenido,
      { placeholder: { options: cabecera, text: "Título de la diapositiva" } },
      { placeholder: { options: { name: "izquierda", type: "body", x: M, y: 1.65, w: 5.8, h: H - 2.5, fontFace: F.cuerpo, fontSize: 16, color: C.texto, valign: "top", margin: 0 }, text: "Columna izquierda" } },
      { placeholder: { options: { name: "derecha", type: "body", x: W - M - 5.8, y: 1.65, w: 5.8, h: H - 2.5, fontFace: F.cuerpo, fontSize: 16, color: C.texto, valign: "top", margin: 0 }, text: "Columna derecha" } },
    ],
  });

  pres.defineSlideMaster({
    title: "SL_IMAGEN",
    background: { color: C.blanco },
    slideNumber: numPag,
    objects: [
      { rect: { x: 0, y: 0, w: W * 0.45, h: H, fill: { color: C.tinte } } },
      { placeholder: { options: { name: "imagen", type: "pic", x: 0, y: 0, w: W * 0.45, h: H }, text: "Insertar imagen" } },
      ...logo(false, W - M - 1.4, 0.55, 1.4, 0.45),
      { placeholder: { options: { name: "titulo", type: "title", x: W * 0.45 + 0.7, y: 1.4, w: W * 0.55 - 0.7 - M, h: 1.5, align: "left", fontFace: F.tit, fontSize: 32, bold: true, color: C.azul, valign: "bottom", margin: 0 }, text: "Título" } },
      { placeholder: { options: { name: "cuerpo", type: "body", x: W * 0.45 + 0.7, y: 3.1, w: W * 0.55 - 0.7 - M, h: 3.4, fontFace: F.cuerpo, fontSize: 16, color: C.texto, valign: "top", margin: 0 }, text: "Texto descriptivo" } },
    ],
  });

  pres.defineSlideMaster({
    title: "SL_SUAVE",
    background: { color: C.tinte },
    slideNumber: numPag,
    objects: [
      ...pieContenido,
      { placeholder: { options: cabecera, text: "Título de la diapositiva" } },
    ],
  });

  pres.defineSlideMaster({
    title: "SL_CIERRE",
    background: { color: C.azul },
    objects: [
      ...circulos(W - 5.2, H - 4.4, 7.5, C.azulOsc, 20),
      circulo(W - 3.4, 0.9, 0.9, C.amarillo),
      ...logo(true, M, 0.55, 2.2, 0.7),
      { placeholder: { options: { name: "titulo", type: "title", x: M, y: 2.4, w: 8, h: 1.4, align: "left", fontFace: F.tit, fontSize: 54, bold: true, color: C.blanco, valign: "bottom", margin: 0 }, text: "Gracias" } },
      { placeholder: { options: { name: "contacto", type: "body", x: M, y: 4.0, w: 8, h: 1.6, fontFace: F.cuerpo, fontSize: 18, color: C.azulClaro, valign: "top", margin: 0 }, text: "nombre@correo.com · +34 600 000 000" } },
    ],
  });

  // ---------- Diapositivas de ejemplo ----------
  let s;
  const nota = (sl, t) => sl.addNotes(t);

  s = pres.addSlide({ masterName: "SL_PORTADA" });
  s.addText("Propuesta de transformación digital del canal agencial", { placeholder: "titulo" });
  s.addText("Presentación para el proceso de selección", { placeholder: "subtitulo" });
  s.addText("Nombre Apellido · Octubre 2026", { placeholder: "fecha" });
  nota(s, "Portada (SL_PORTADA). Sustituye título, subtítulo y ponente. El logo se toma de assets/logo-blanco.png.");

  // Agenda
  s = pres.addSlide({ masterName: "SL_CONTENIDO" });
  s.addText("Agenda", { placeholder: "titulo" });
  const agenda = ["Contexto y punto de partida", "Diagnóstico", "Propuesta", "Plan de implantación", "Próximos pasos"];
  agenda.forEach((t, i) => {
    const y = 1.8 + i * 0.95;
    s.addShape(pres.shapes.OVAL, { x: M, y, w: 0.65, h: 0.65, fill: { color: i === 0 ? C.amarillo : C.azul } });
    s.addText(String(i + 1).padStart(2, "0"), { x: M, y, w: 0.65, h: 0.65, align: "center", valign: "middle", fontFace: F.tit, fontSize: 16, bold: true, color: i === 0 ? C.azul : C.blanco, margin: 0, isTextBox: true });
    s.addText(t, { x: M + 0.95, y, w: 8, h: 0.65, valign: "middle", fontFace: F.cuerpo, fontSize: 20, color: C.texto, margin: 0, isTextBox: true });
  });
  nota(s, "Agenda sobre SL_CONTENIDO. El círculo amarillo marca el punto actual; muévelo si repites la agenda entre secciones.");

  s = pres.addSlide({ masterName: "SL_SECCION" });
  s.addText("01", { placeholder: "numero" });
  s.addText("Contexto y punto de partida", { placeholder: "titulo" });
  nota(s, "Separador de sección (SL_SECCION).");

  s = pres.addSlide({ masterName: "SL_CONTENIDO" });
  s.addText("Qué hemos observado", { placeholder: "titulo" });
  s.addText([
    { text: "Los clientes esperan contratar y gestionar sus pólizas desde el móvil", options: { bullet: true, breakLine: true } },
    { text: "La red agencial sigue siendo el principal canal de confianza", options: { bullet: true, breakLine: true } },
    { text: "Los procesos de siniestros concentran la mayor parte de las consultas", options: { bullet: true, breakLine: true } },
    { text: "Existe una oportunidad clara en la venta cruzada de productos de ahorro", options: { bullet: true } },
  ], { placeholder: "cuerpo", paraSpaceAfter: 16, h: 3.2 });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y: 5.1, w: W - 2 * M, h: 1.3, rectRadius: 0.12, fill: { color: C.tinte }, line: { type: "none" } });
  s.addShape(pres.shapes.OVAL, { x: M + 0.35, y: 5.45, w: 0.6, h: 0.6, fill: { color: C.amarillo } });
  s.addText("!", { x: M + 0.35, y: 5.45, w: 0.6, h: 0.6, align: "center", valign: "middle", fontFace: F.tit, fontSize: 20, bold: true, color: C.azul, margin: 0, isTextBox: true });
  s.addText("Mensaje clave: el agente es el centro de la experiencia digital, no su sustituto.", { x: M + 1.25, y: 5.1, w: W - 2 * M - 1.6, h: 1.3, valign: "middle", fontFace: F.cuerpo, fontSize: 18, bold: true, color: C.azul, margin: 0, isTextBox: true });
  nota(s, "Contenido con viñetas (SL_CONTENIDO). Máximo 5-6 líneas por diapositiva.");

  s = pres.addSlide({ masterName: "SL_DOS_COLUMNAS" });
  s.addText("Situación actual frente a propuesta", { placeholder: "titulo" });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: W - M - 6.1, y: 1.4, w: 6.1, h: 3.1, rectRadius: 0.12, fill: { color: C.tinte }, line: { type: "none" } });
  s.addText([
    { text: "Hoy", options: { bold: true, color: C.gris, fontSize: 14, breakLine: true } },
    { text: "Alta de pólizas en papel", options: { bullet: true, breakLine: true } },
    { text: "Seguimiento de siniestros por teléfono", options: { bullet: true, breakLine: true } },
    { text: "Datos de cliente dispersos", options: { bullet: true } },
  ], { placeholder: "izquierda", paraSpaceAfter: 10 });
  s.addText([
    { text: "Propuesta", options: { bold: true, color: C.azul, fontSize: 14, breakLine: true } },
    { text: "Contratación digital con firma electrónica", options: { bullet: true, breakLine: true } },
    { text: "Estado del siniestro en tiempo real", options: { bullet: true, breakLine: true } },
    { text: "Visión 360º del cliente para el agente", options: { bullet: true } },
  ], { placeholder: "derecha", paraSpaceAfter: 10 });
  nota(s, "Comparativa en dos columnas (SL_DOS_COLUMNAS).");

  // Cifras clave
  s = pres.addSlide({ masterName: "SL_SUAVE" });
  s.addText("Cifras clave", { placeholder: "titulo" });
  const kpis = [["+25%", "clientes con gestión digital en 12 meses"], ["-30%", "tiempo medio de tramitación de siniestros"], ["4,6/5", "satisfacción objetivo del cliente"]];
  const cw = (W - 2 * M - 2 * 0.4) / 3;
  kpis.forEach(([n, l], i) => {
    const x = M + i * (cw + 0.4);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 2.0, w: cw, h: 3.8, rectRadius: 0.15, fill: { color: i === 0 ? C.azul : C.blanco }, line: { type: "none" } });
    s.addText(n, { x: x + 0.4, y: 2.5, w: cw - 0.8, h: 1.4, align: "left", fontFace: F.tit, fontSize: 60, bold: true, color: i === 0 ? C.amarillo : C.azul, margin: 0, isTextBox: true });
    s.addText(l, { x: x + 0.4, y: 4.0, w: cw - 0.8, h: 1.2, fontFace: F.cuerpo, fontSize: 16, color: i === 0 ? C.blanco : C.texto, valign: "top", margin: 0, isTextBox: true });
  });
  nota(s, "Cifras destacadas (SL_SUAVE). Destaca en azul solo la cifra principal.");

  s = pres.addSlide({ masterName: "SL_IMAGEN" });
  s.addText("Cerca de las personas", { placeholder: "titulo" });
  s.addText("Usa este diseño para casos de cliente, testimonios o para presentar un producto. Haz clic en el icono del marcador de la izquierda para insertar una fotografía.", { placeholder: "cuerpo" });
  nota(s, "Imagen + texto (SL_IMAGEN). Usa fotografía real, luminosa y con personas.");

  // Plan / cronograma
  s = pres.addSlide({ masterName: "SL_CONTENIDO" });
  s.addText("Plan de implantación", { placeholder: "titulo" });
  const fases = [["T1", "Diagnóstico", "Entrevistas con la red y análisis de datos"], ["T2", "Piloto", "Tres oficinas y un producto"], ["T3", "Escalado", "Despliegue por territorios"], ["T4", "Consolidación", "Medición y mejora continua"]];
  const fw = (W - 2 * M) / 4;
  s.addShape(pres.shapes.LINE, { x: M + 0.3, y: 3.15, w: W - 2 * M - fw + 0.1, h: 0, line: { color: C.azulClaro, width: 2 } });
  fases.forEach(([t, h, d], i) => {
    const x = M + i * fw;
    s.addShape(pres.shapes.OVAL, { x, y: 2.8, w: 0.7, h: 0.7, fill: { color: i === 1 ? C.amarillo : C.azul } });
    s.addText(t, { x, y: 2.8, w: 0.7, h: 0.7, align: "center", valign: "middle", fontFace: F.tit, fontSize: 14, bold: true, color: i === 1 ? C.azul : C.blanco, margin: 0, isTextBox: true });
    s.addText(h, { x, y: 3.8, w: fw - 0.4, h: 0.5, align: "left", fontFace: F.tit, fontSize: 20, bold: true, color: C.azul, margin: 0, isTextBox: true });
    s.addText(d, { x, y: 4.35, w: fw - 0.4, h: 1.2, fontFace: F.cuerpo, fontSize: 15, color: C.texto, valign: "top", margin: 0, isTextBox: true });
  });
  nota(s, "Cronograma sobre SL_CONTENIDO. El hito amarillo marca la fase actual o crítica.");

  // Gráfico
  s = pres.addSlide({ masterName: "SL_CONTENIDO" });
  s.addText("Evolución de clientes digitales", { placeholder: "titulo" });
  s.addChart(pres.charts.BAR, [{ name: "Clientes digitales (%)", labels: ["2023", "2024", "2025", "2026", "2027e"], values: [18, 24, 31, 38, 47] }], {
    x: M, y: 1.65, w: 8.2, h: 5.0, barDir: "col", chartColors: [C.azul],
    showValue: true, dataLabelPosition: "outEnd", dataLabelColor: C.texto, dataLabelFontSize: 12, dataLabelFontFace: F.cuerpo,
    catAxisLabelColor: C.gris, catAxisLabelFontFace: F.cuerpo, valAxisHidden: true,
    valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false, barGapWidthPct: 60,
  });
  s.addText([
    { text: "47%", options: { fontSize: 48, bold: true, color: C.azul, breakLine: true } },
    { text: "de los clientes gestionarán sus pólizas en digital en 2027", options: { fontSize: 16, color: C.texto } },
  ], { x: 9.4, y: 2.4, w: W - M - 9.4, h: 2.6, fontFace: F.cuerpo, valign: "top", margin: 0, isTextBox: true });
  nota(s, "Gráfico nativo editable (clic derecho > Editar datos). Datos de ejemplo.");

  s = pres.addSlide({ masterName: "SL_CIERRE" });
  s.addText("Gracias", { placeholder: "titulo" });
  s.addText("Nombre Apellido\nnombre@correo.com · linkedin.com/in/usuario", { placeholder: "contacto" });
  nota(s, "Cierre (SL_CIERRE).");

  return pres.writeFile({ fileName: OUT });
}

build().then((f) => console.log("Generado:", f));
