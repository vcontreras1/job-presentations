"""Genera el newsletter rediseñado (HTML con cid:) y el .eml con las imágenes embebidas."""
import sys, os
from email.message import EmailMessage
from email.utils import format_datetime
from datetime import datetime, timezone

SRC_IMG, OUT = sys.argv[1], sys.argv[2]

FONT = "'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif"
INK, MUTED, LINE, BLUE, SOFT, BG = "#1F2430", "#5B6272", "#E6E9F0", "#1539C3", "#EEF2FF", "#F2F4F8"
ORANGE_BG, ORANGE_TX = "#FFEDE5", "#B4441B"
BASE = "https://santalucia.knowbox.es"

IMGS = {  # cid -> fichero
    "img0@radar": "header-top.jpg", "img1@radar": "header-podcast.jpg",
    "img2@radar": "momento-fases-v3.jpg", "img3@radar": "ultima-publicacion-v5.jpg",
    "img4@radar": "banner-nucleo.jpg", "img5@radar": "proxima-entrega-v3.jpg",
    "img6@radar": "footer-swoosh.jpg",
}

SIGNALS = [
    ("Hogar y entorno personal", "/2026/09/07/autoconsumo-energetico-en-hogares-por-que-cada-vez-mas-familias-espanolas-instalan-paneles-solares/",
     "/wp-content/uploads/2026/09/smartfox-beste-systeme-fuers-ueberschussladen-zuhause-1.jpg", "Paneles solares en vivienda",
     "Autoconsumo energético en hogares: por qué cada vez más familias españolas instalan paneles solares",
     "En 2025 se sumaron 71.600 nuevas instalaciones con 1.214 MW de potencia, 66.900 de ellas residenciales. El autoconsumo cubre ya el 4,1% de la demanda eléctrica del país."),
    ("Economía silver", "/2026/09/07/espana-afronta-un-fuerte-envejecimiento-habra-48-millones-mas-de-mayores-de-64-anos-en-2050/",
     "/wp-content/uploads/2026/09/images-15.jpg", "Población mayor en España",
     "España afronta un fuerte envejecimiento: habrá 4,8 millones más de mayores de 64 años en 2050",
     "De 11,5 millones en 2030 a 16,3 millones en 2050, un incremento del 41,7%. En paralelo se reduce la población en edad de trabajar."),
    ("IA y otras tecnologías", "/2026/10/06/crece-el-rechazo-social-a-los-centros-de-datos/",
     "/wp-content/uploads/2026/10/500_333.jpeg", "Centro de datos",
     "Crece el rechazo social a los centros de datos",
     "Crece el rechazo a los centros de datos por su impacto ambiental (54%), energético (50%) y vecinal (49%), de forma transversal a edades, ideologías y territorios."),
    ("Familia", "/2026/09/06/casi-un-tercio-de-menores-de-18-anos-en-espana-vivia-en-2025-bajo-el-umbral-de-la-pobreza/",
     "/wp-content/uploads/2026/09/pobreza-infantil-consecuencias.jpg", "Pobreza infantil",
     "Casi un tercio de menores de 18 años en España vivía en 2025 bajo el umbral de la pobreza",
     "El 28,3% de los menores de 18 años, unos 2,07 millones de niños. La Fundación de Estudios de Economía Aplicada publicó el estudio el 24 de agosto."),
    ("Movilidad inteligente", "/2026/09/05/espana-autoriza-la-conduccion-autonoma-de-nivel-3-en-autopistas-las-aseguradoras-deben-adaptar-las-polizas/",
     "/wp-content/uploads/2026/09/images-14.jpg", "Conducción autónoma",
     "España autoriza la conducción autónoma de nivel 3 en autopistas: aseguradoras atentas",
     "El conductor podrá soltar el volante en determinadas condiciones. La medida obliga a las aseguradoras a adaptar sus pólizas de auto."),
    ("Salud y bienestar", "/2026/10/06/la-menopausia-un-obstaculo-a-la-alta-direccion-femenina-2/",
     "/wp-content/uploads/2026/10/https___media.zenfs_.com_es_el_economista_434_bb4cb7fb8f23d44f4c9a02f46608e00a.jpg", "Salud y bienestar de la mujer",
     "La menopausia, un obstáculo a la alta dirección femenina",
     "El informe de Carrot revela que más del 80% de las mujeres experimenta síntomas durante la transición a la menopausia, afectando a su bienestar físico, salud mental y productividad laboral."),
]

EVENTS = [
    ("OCT", "13", "Startup Olé ’26", "Salamanca · Horario por confirmar", "https://startupole.eu/",
     "Conecta emprendedores y startups con inversores, corporaciones y otros agentes del ecosistema internacional, en un formato diseñado para generar sinergias y captar inversión."),
    ("OCT", "22", "MCSA: Encuentro de marketing y comunicación en el sector asegurador", "INESE · VP Sognio Metropolitano, Madrid", "https://marketing.inese.es/",
     "Encuentro anual de INESE dedicado a marketing y comunicación en seguros: reputación de marca, relación con el cliente y nuevos canales de captación en un mercado cada vez más digital."),
    ("NOV", "12", "Insurance Revolution", "C/ de Salamanca 23, Tetuán · Madrid", "https://www.insurancerevolution.es/",
     "Encuentro sobre la transformación del sector asegurador: tecnología aplicada al negocio, nuevos modelos de distribución y evolución de la relación con el cliente."),
]


def t(style=""):
    return f'<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="width:100%;border-collapse:separate;{style}">'


def pill(text, bg, color):
    return (f'<span style="display:inline-block;margin:0 6px 6px 0;background:{bg};border-radius:999px;font-family:{FONT};font-size:11px;line-height:16px;'
            f'font-weight:700;letter-spacing:.06em;color:{color};padding:5px 12px;white-space:nowrap">{text}</span>')


def pills(*items):
    return f'<div style="font-size:0;line-height:0;margin-bottom:-6px">{"".join(pill(*i) for i in items)}</div>'


def button(href, label, width):
    return (f'<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{href}" '
            f'style="height:44px;v-text-anchor:middle;width:{width}px;" arcsize="50%" stroke="f" fillcolor="{BLUE}"><w:anchorlock/>'
            f'<center style="color:#ffffff;font-family:Arial,sans-serif;font-size:14px;font-weight:700;">{label}</center></v:roundrect><![endif]-->'
            f'<!--[if !mso]><!--><a href="{href}" target="_blank" style="display:inline-block;background:{BLUE};color:#ffffff;border-radius:999px;'
            f'font-family:{FONT};font-size:14px;line-height:20px;font-weight:700;text-decoration:none;padding:12px 26px">{label}</a><!--<![endif]-->')


def link(href, label):
    return (f'<a href="{href}" target="_blank" style="font-family:{FONT};font-size:13px;line-height:18px;font-weight:700;'
            f'color:{BLUE};text-decoration:none">{label}&nbsp;&rarr;</a>')


def card(inner, pad="24px", extra=""):
    return (f'<tr><td class="sp" style="padding:0 0 16px">{t()}<tr><td class="card" bgcolor="#ffffff" style="background:#ffffff;'
            f'border:1px solid {LINE};border-radius:24px;padding:{pad};{extra}">{inner}</td></tr></table></td></tr>')


def section_head(num, anchor, title, note=""):
    note_html = f'<p style="margin:4px 0 0;font-family:{FONT};font-size:14px;line-height:20px;color:{MUTED}">{note}</p>' if note else ""
    return (f'<tr><td id="{anchor}" class="sp" style="padding:24px 4px 14px"><a name="{anchor}"></a>'
            f'<table role="presentation" cellspacing="0" cellpadding="0" border="0" style="border-collapse:separate"><tr>'
            f'<td width="34" height="34" align="center" valign="middle" bgcolor="{SOFT}" style="width:34px;height:34px;background:{SOFT};border-radius:12px;'
            f'font-family:{FONT};font-size:13px;line-height:34px;font-weight:700;color:{BLUE};text-align:center">{num}</td>'
            f'<td width="12" style="width:12px;font-size:0">&nbsp;</td>'
            f'<td valign="middle"><h2 class="h2" style="margin:0;font-family:{FONT};font-size:22px;line-height:28px;font-weight:700;color:{INK};letter-spacing:-.01em">{title}</h2></td>'
            f'</tr></table>{note_html}</td></tr>')


def signal_card(cat, path, img, alt, title, desc):
    url = BASE + path
    return (f'<td width="292" valign="top" class="col" bgcolor="#ffffff" style="width:292px;height:100%;vertical-align:top;background:#ffffff;border:1px solid {LINE};border-radius:20px;padding:0">'
            f'{t("height:100%")}'
            f'<tr><td style="padding:8px 8px 0;font-size:0;line-height:0"><a href="{url}" target="_blank">'
            f'<img width="274" height="164" alt="{alt}" class="fluid" src="{BASE}{img}" style="display:block;width:274px;height:164px;object-fit:cover;border:0;border-radius:14px;background:#dfe3ea" /></a></td></tr>'
            f'<tr><td valign="top" height="100%" style="vertical-align:top;height:100%;padding:16px 18px 0">'
            f'{pills((cat.upper(), ORANGE_BG, ORANGE_TX))}'
            f'<p style="margin:12px 0 0;font-family:{FONT};font-size:16px;line-height:22px;font-weight:700"><a href="{url}" target="_blank" style="color:{INK};text-decoration:none">{title}</a></p>'
            f'<p style="margin:8px 0 0;font-family:{FONT};font-size:14px;line-height:21px;color:{MUTED}">{desc}</p></td></tr>'
            f'<tr><td valign="bottom" style="vertical-align:bottom;padding:16px 18px 20px">{link(url, "Ver señal")}</td></tr>'
            f'</table></td>')


def signals_grid():
    rows = []
    for i in range(0, len(SIGNALS), 2):
        a, b = SIGNALS[i], SIGNALS[i + 1]
        rows.append(
            f'<tr><td class="sp gridrow" style="padding:0 0 16px">'
            f'<!--[if mso]><table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0"><tr><td><![endif]-->'
            f'<table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" class="grid" height="1" style="width:600px;height:1px;border-collapse:separate"><tr>'
            f'{signal_card(*a)}<td width="16" class="gut" style="width:16px;font-size:0;line-height:0">&nbsp;</td>{signal_card(*b)}'
            f'</tr></table><!--[if mso]></td></tr></table><![endif]--></td></tr>')
    return "".join(rows)


def events():
    out = []
    for i, (mon, day, title, meta, url, desc) in enumerate(EVENTS):
        border = f"border-top:1px solid {LINE};" if i else ""
        out.append(
            f'<tr><td style="{border}padding:{"0" if i == 0 else "20px"} 0 {"20px" if i < len(EVENTS) - 1 else "0"}">'
            f'<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="width:100%;border-collapse:separate"><tr>'
            f'<td width="64" valign="top" style="width:64px;vertical-align:top">'
            f'<table role="presentation" width="64" cellspacing="0" cellpadding="0" border="0" style="width:64px;border-collapse:separate"><tr>'
            f'<td align="center" bgcolor="{SOFT}" style="background:{SOFT};border-radius:16px;padding:10px 0;text-align:center;font-family:{FONT}">'
            f'<p style="margin:0;font-size:11px;line-height:14px;font-weight:700;letter-spacing:.1em;color:{BLUE}">{mon}</p>'
            f'<p style="margin:2px 0 0;font-size:26px;line-height:30px;font-weight:700;color:{BLUE}">{day}</p></td></tr></table></td>'
            f'<td width="16" style="width:16px;font-size:0">&nbsp;</td>'
            f'<td valign="top" style="vertical-align:top;font-family:{FONT}">'
            f'<p style="margin:0;font-size:16px;line-height:22px;font-weight:700"><a href="{url}" target="_blank" style="color:{INK};text-decoration:none">{title}</a></p>'
            f'<p style="margin:4px 0 0;font-size:13px;line-height:18px;color:{MUTED}">{meta}</p>'
            f'<p style="margin:8px 0 0;font-size:14px;line-height:21px;color:{MUTED}">{desc}</p>'
            f'<p style="margin:10px 0 0">{link(url, "Ver evento")}</p></td>'
            f'</tr></table></td></tr>')
    return t() + "".join(out) + "</table>"


def toc():
    items = [("01", "Última publicación", "publicacion"), ("02", "Señales", "senales"),
             ("03", "Eventos", "eventos"), ("04", "Próxima entrega", "proxima")]
    chips = "".join(
        f'<a href="#{a}" style="display:inline-block;margin:0 6px 8px 0;background:{BG};border-radius:999px;padding:8px 14px;'
        f'font-family:{FONT};font-size:13px;line-height:18px;font-weight:600;color:{INK};text-decoration:none">'
        f'<span style="color:{BLUE};font-weight:700">{n}</span>&nbsp;&nbsp;{label}</a>' for n, label, a in items)
    return chips


def build(img_src):
    """img_src: función cid -> src (cid: para el email, ruta local para la vista previa)."""
    S = img_src
    head = f"""<!DOCTYPE html>
<html dir="ltr" lang="es" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="x-apple-disable-message-reformatting" />
<meta name="format-detection" content="telephone=no" />
<meta name="color-scheme" content="light" />
<meta name="supported-color-schemes" content="light" />
<title>Santalucía · Radar de Oportunidades · Octubre 2026</title>
<!--[if mso]>
<xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml>
<style type="text/css">table, td, div, p, a, h1, h2, h3 {{ font-family: Arial, Helvetica, sans-serif !important; }}</style>
<![endif]-->
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet" />
<!--<![endif]-->
<style type="text/css">
body {{ margin:0 !important; padding:0 !important; width:100% !important; }}
img {{ -ms-interpolation-mode:bicubic; }}
a {{ text-decoration:none; }}
#outlook a {{ padding:0; }}
a[x-apple-data-detectors] {{ color:inherit !important; text-decoration:none !important; font-size:inherit !important; font-family:inherit !important; font-weight:inherit !important; line-height:inherit !important; }}
@media only screen and (max-width:640px) {{
  .wrap, .grid {{ width:100% !important; max-width:100% !important; }}
  .outer {{ padding:12px !important; }}
  .col {{ display:block !important; width:100% !important; max-width:100% !important; margin:0 0 16px 0 !important; box-sizing:border-box; }}
  .col img.fluid {{ width:100% !important; height:auto !important; aspect-ratio:5/3; }}
  .gut {{ display:none !important; width:0 !important; max-height:0 !important; overflow:hidden !important; }}
  .gridrow {{ padding-bottom:0 !important; }}
  .grid {{ height:auto !important; }}
  .col {{ height:auto !important; }}
  .fluid {{ width:100% !important; max-width:100% !important; height:auto !important; }}
  .card {{ padding:20px !important; }}
  .h1 {{ font-size:22px !important; line-height:28px !important; }}
  .h2 {{ font-size:20px !important; line-height:26px !important; }}
}}
</style>
</head>"""

    body = f"""
<body style="margin:0;padding:0;background:{BG};color:{INK};font-family:{FONT}">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all">IA aplicada a los cuidadores, 6 nuevas señales, eventos de octubre y noviembre, y lo que llega el 27/10.&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;</div>
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="width:100%;background:{BG};border-collapse:collapse">
<tr><td align="center" class="outer" style="padding:32px 16px">
<!--[if mso]><table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0"><tr><td><![endif]-->
<table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" class="wrap" style="width:600px;max-width:600px;border-collapse:separate">

<!-- CABECERA -->
<tr><td class="sp" style="padding:0 0 16px">{t()}<tr><td bgcolor="#ffffff" style="background:#ffffff;border:1px solid {LINE};border-radius:24px;padding:0;font-size:0;line-height:0">
<a href="{BASE}/" target="_blank"><img width="598" height="255" alt="Santalucía Impulsa — Radar de Oportunidades" class="fluid" src="{S('img0@radar')}" style="display:block;width:598px;max-width:100%;height:auto;border:0;border-radius:24px 24px 0 0" /></a>
<a href="{BASE}/wp-content/uploads/2026/10/ElevenLabs_2026-10-07T08_21_15_Laura-Lopez-Bright-Clear-and-Dynamic_pvc_sp112_s39_sb75_v4.mp3" target="_blank"><img width="598" height="89" alt="¿Quieres conocer los principales contenidos de esta newsletter? Escuchar podcast" class="fluid" src="{S('img1@radar')}" style="display:block;width:598px;max-width:100%;height:auto;border:0" /></a>
</td></tr>
<tr><td bgcolor="#ffffff" style="background:#ffffff;border:1px solid {LINE};border-top:0;border-radius:0 0 24px 24px;padding:4px 24px 20px">
<p style="margin:0 0 12px;font-family:{FONT};font-size:12px;line-height:16px;font-weight:700;letter-spacing:.12em;color:{MUTED}">OCTUBRE 2026 &nbsp;·&nbsp; EN ESTE NÚMERO</p>
<div style="font-size:0;line-height:0">{toc()}</div>
</td></tr></table></td></tr>

<!-- MOMENTO DEL PROCESO -->
{card(f'''<p style="margin:0;font-family:{FONT};font-size:12px;line-height:16px;font-weight:700;letter-spacing:.12em;color:{MUTED}">¿EN QUÉ MOMENTO ESTAMOS?</p>
<p style="margin:6px 0 0;font-family:{FONT};font-size:16px;line-height:23px;font-weight:600;color:{INK}">Fase 6 de 6 · <span style="color:{ORANGE_TX}">Exploración de oportunidades en portfolio</span> (Q4)</p>
<div style="margin-top:12px;font-size:0;line-height:0"><img width="550" height="218" alt="Seis fases: inspiración y evaluación de tendencias (Q1), análisis de ámbitos (Q1), áreas de oportunidad (Q2), lista larga de potenciales oportunidades (Q2), lista corta de oportunidades priorizadas (Q3) y exploración de oportunidades en portfolio (Q4, estamos aquí)" class="fluid" src="{S('img2@radar')}" style="display:block;width:550px;max-width:100%;height:auto;border:0;border-radius:12px" /></div>''', pad="24px 24px 16px")}

<!-- 01 ÚLTIMA PUBLICACIÓN -->
{section_head("01", "publicacion", "Última publicación en el Radar")}
{card(f'''<a href="{BASE}/informes/ia-aplicada-a-los-cuidadores-domiciliarios-y-residenciales/" target="_blank"><img width="582" height="328" alt="IA aplicada a los cuidadores domiciliarios y residenciales" class="fluid" src="{S('img3@radar')}" style="display:block;width:582px;max-width:100%;height:auto;border:0;border-radius:16px" /></a>
<div style="padding:20px 16px 16px">
{pills(("NOVEDAD", "#F1E3F7", "#6B2A86"), ("EXPLORACIÓN", SOFT, BLUE), ("23/09/2026", BG, MUTED))}
<h1 class="h1" style="margin:14px 0 0;font-family:{FONT};font-size:26px;line-height:33px;font-weight:700;letter-spacing:-.01em"><a href="{BASE}/informes/ia-aplicada-a-los-cuidadores-domiciliarios-y-residenciales/" target="_blank" style="color:{INK};text-decoration:none">IA aplicada a los cuidadores domiciliarios y residenciales</a></h1>
<p style="margin:12px 0 0;font-family:{FONT};font-size:15px;line-height:24px;color:{MUTED}">El benchmark analiza diez startups que aplican IA a los cuidados de mayores en domicilio y residencias, agrupadas por su papel en la cadena de valor. El mercado sigue inmaduro y la relación con el sector asegurador es escasa, lo que abre espacio a alianzas para Santalucía.</p>
<div style="margin-top:20px">{button(BASE + "/informes/ia-aplicada-a-los-cuidadores-domiciliarios-y-residenciales/", "Leer el informe &rarr;", 200)}</div>
</div>''', pad="8px")}

<!-- BANNER NÚCLEO -->
<tr><td class="sp" style="padding:0 0 16px;font-size:0;line-height:0"><a href="{BASE}/iris/" target="_blank"><img width="600" height="200" alt="Asistente conversacional NÚCLEO: lee y procesa todo el contenido publicado en el Radar y permite consultarlo mediante lenguaje natural" class="fluid" src="{S('img4@radar')}" style="display:block;width:600px;max-width:100%;height:auto;border:0;border-radius:24px" /></a></td></tr>

<!-- 02 SEÑALES -->
{section_head("02", "senales", "Principales señales identificadas", "Seis movimientos del entorno que conviene tener en el radar.")}
{signals_grid()}
<tr><td align="center" style="padding:4px 0 8px;text-align:center">{button(BASE + "/senales/", "Ver todas las señales", 220)}</td></tr>

<!-- 03 EVENTOS -->
{section_head("03", "eventos", "Próximos eventos de interés")}
{card(events())}

<!-- 04 PRÓXIMA ENTREGA -->
{section_head("04", "proxima", "Próxima entrega")}
{card(f'''<img width="582" height="328" alt="Futuro del Empleado Sénior" class="fluid" src="{S('img5@radar')}" style="display:block;width:582px;max-width:100%;height:auto;border:0;border-radius:16px" />
<div style="padding:20px 16px 16px">
{pills(("PRÓXIMAMENTE", BLUE, "#ffffff"), ("EXPLORACIÓN", SOFT, BLUE), ("27/10/2026", BG, MUTED))}
<h2 class="h1" style="margin:14px 0 0;font-family:{FONT};font-size:26px;line-height:33px;font-weight:700;letter-spacing:-.01em;color:{INK}">Futuro del Empleado Sénior</h2>
<p style="margin:12px 0 0;font-family:{FONT};font-size:15px;line-height:24px;color:{MUTED}">Análisis del empleado sénior en un mercado laboral que envejece: prolongación de la vida activa, reciclaje de competencias y nuevas fórmulas de transición hacia la jubilación. Explora qué papel pueden jugar las aseguradoras en el acompañamiento de esta etapa y qué servicios abre para Santalucía.</p>
</div>''', pad="8px")}

<!-- PIE -->
<tr><td style="padding:8px 0 0">{t()}<tr><td bgcolor="#1035BF" style="background:#1035BF;border-radius:24px;padding:0">
{t()}
<tr><td style="padding:24px 24px 0;font-family:{FONT}">
<p style="margin:0;font-size:15px;line-height:22px;font-weight:700;color:#ffffff">Radar de Oportunidades</p>
<p style="margin:4px 0 0;font-size:13px;line-height:20px;color:#C9D3FF"><a href="{BASE}/" target="_blank" style="color:#C9D3FF;text-decoration:none">santalucia.knowbox.es</a> &nbsp;·&nbsp; © 2026 Santalucía Seguros. Todos los derechos reservados.</p>
</td></tr>
<tr><td align="right" style="text-align:right;padding:0;font-size:0;line-height:0">
<img width="380" height="38" alt="" class="fluid" src="{S('img6@radar')}" style="display:block;margin-left:auto;width:380px;max-width:100%;height:auto;border:0;border-radius:0 0 24px 0" />
</td></tr></table>
</td></tr></table></td></tr>

</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr>
</table>
</body>
</html>
"""
    return head + body


os.makedirs(OUT, exist_ok=True)
html_cid = build(lambda c: "cid:" + c)
open(os.path.join(OUT, "newsletter.html"), "w").write(html_cid)
open(os.path.join(OUT, "preview.html"), "w").write(build(lambda c: "images/" + IMGS[c]))

msg = EmailMessage()
msg["From"] = "Radar de Oportunidades <radar@santalucia.knowbox.es>"
msg["Subject"] = "Radar de Oportunidades · Octubre 2026"
msg["Date"] = format_datetime(datetime(2026, 10, 9, 11, 25, 8, tzinfo=timezone.utc))
msg.set_content("Radar de Oportunidades · Octubre 2026. Abre este correo en un cliente compatible con HTML.")
msg.add_alternative(html_cid, subtype="html")
html_part = msg.get_payload()[1]
for cid, fn in IMGS.items():
    with open(os.path.join(SRC_IMG, fn), "rb") as f:
        html_part.add_related(f.read(), "image", "jpeg", cid=f"<{cid}>", filename=fn)
open(os.path.join(OUT, "Radar-Oportunidades-Octubre-2026.eml"), "wb").write(bytes(msg))
print("ok")
