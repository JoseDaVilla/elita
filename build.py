#!/usr/bin/env python3
"""Genera index.html a partir de src/index.html.

- {{icon:nombre}}  -> SVG en línea desde assets/icons/<nombre>.svg
- {{obra}}         -> galería generada desde OBRA (abajo)
- {{wa}}           -> enlace de WhatsApp con mensaje inicial

Uso: python3 build.py
Requiere Pillow solo para leer el tamaño de las imágenes.
"""
import re, html, pathlib, urllib.parse
from PIL import Image

ROOT = pathlib.Path(__file__).parent
WHATSAPP = "573186012345"
WA_TEXT = "Hola Daniela, vi tu página y quiero contarte de un proyecto."

# (archivo en assets/obra, categoría, título, detalle, texto alternativo)
# Categorías: cuadros | muros
OBRA = [
    ("mural-safari", "muros", "Safari para Vale", "Mural a mano en tonos crema, Cartagena",
     "Habitación infantil con mural de selva y animales en tonos crema"),
    ("cartagena-palenquera", "cuadros", "Cartagena", "Acrílico texturizado sobre lienzo",
     "Pintura de una palenquera con frutas caminando por una calle colonial"),
    ("mural-bosque-rosa", "muros", "Bosque rosa para Vittoria", "Mural y molduras",
     "Mural de árboles en rosa pálido sobre la cuna de una habitación de bebé"),
    ("meraki-gran-formato", "cuadros", "Proyecto Meraki", "Gran formato, acrílico texturizante sobre lienzo",
     "Dos cuadros grandes de formas orgánicas blancas sobre un sofá gris"),
    ("molduras-rayas", "muros", "Molduras y mural", "",
     "Pared de rayas azules onduladas con moldura color vino junto a una cuna"),
    ("pieza-unica-verde", "cuadros", "Pieza única", "",
     "Cuadro enmarcado con una trama de gotas verdes que se aclaran hacia abajo"),
    ("mural-arcoiris", "muros", "Mural para Victoria", "",
     "Mural de arcoíris pastel con flores lila y amarillas"),
    ("water-paint", "cuadros", "Water Paint", "Acrílico sobre lienzo, hoy en Medellín",
     "Detalle de pintura con manchas de verde profundo, salvia y arena"),
    ("mural-cuadros", "muros", "Mural de recuadros", "Patrón a cuadros hecho a mano",
     "Pasillo con una pared pintada a cuadros en rosa y crema"),
    ("cartagena-hotel", "cuadros", "Hotel en Cartagena", "Piezas de arte para un hotel",
     "Cuadro de la Torre del Reloj de Cartagena sobre un sofá"),
    ("mural-mariposas", "muros", "Mariposas monarca", "Mural a mano",
     "Detalle de mural con una flor blanca y una mariposa monarca"),
    ("arena-boho", "cuadros", "Arte boho", "Pieza por encargo, 1,0 × 0,70 m",
     "Detalle de textura en relieve color arena con una curva suave"),
    ("relieve-floral", "muros", "Mural", "",
     "Pared de comedor con un relieve botánico blanco sobre fondo gris"),
    ("mural-avion", "muros", "Para Sebastián", "Mural hecho a mano",
     "Mural infantil de un osito piloto en avioneta"),
]

CATS = {"cuadros": "Cuadro", "muros": "Mural y molduras"}


def icon(name):
    svg = (ROOT / "assets/icons" / f"{name}.svg").read_text()
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    svg = re.sub(r"<title>.*?</title>", "", svg)
    svg = re.sub(r'\s(class|width|height|role)="[^"]*"', "", svg)
    svg = re.sub(r"\s+", " ", svg).strip()
    if 'fill="none"' not in svg:
        svg = svg.replace("<svg ", '<svg fill="currentColor" ', 1)
    return svg.replace("<svg ", '<svg class="i" aria-hidden="true" focusable="false" ', 1)


def obra():
    out = []
    for i, (f, cat, title, detail, alt) in enumerate(OBRA):
        w, h = Image.open(ROOT / "assets/obra" / f"{f}.webp").size
        e = html.escape
        out.append(
            f'<figure class="work{" wide" if w > h else ""}" data-cat="{cat}">'
            f'<button class="work-open" type="button" data-index="{i}" aria-label="Ampliar: {e(title)}">'
            f'<img src="assets/obra/{f}.webp" width="{w}" height="{h}" alt="{e(alt)}" loading="lazy" decoding="async">'
            f"</button>"
            f'<figcaption><span class="work-title">{e(title)}</span>'
            + (f'<span class="work-detail">{e(detail)}</span>' if detail else '') + '</figcaption></figure>'
        )
    return "\n".join(out)


def main():
    src = (ROOT / "src/index.html").read_text()
    wa = f"https://wa.me/{WHATSAPP}?text=" + urllib.parse.quote(WA_TEXT)
    src = src.replace("{{wa}}", html.escape(wa))
    src = src.replace("{{obra}}", obra())
    src = re.sub(r"\{\{icon:([\w-]+)\}\}", lambda m: icon(m.group(1)), src)
    (ROOT / "index.html").write_text(src)
    print("index.html listo,", len(src) // 1024, "KB")


if __name__ == "__main__":
    main()
