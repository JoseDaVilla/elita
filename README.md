 # Elita Arte & Diseño

Sitio de Daniela, arquitecta y artista plástica en Barranquilla. Página única, estática, sin dependencias: HTML, CSS y un poco de JavaScript.

## Editar

El HTML que se publica (`index.html`) se genera. No lo edites a mano:

1. Cambia textos y estilos en `src/index.html`.
2. Cambia la galería en la lista `OBRA` de `build.py` (archivo, categoría, título, detalle, texto alternativo).
3. Corre `python3 build.py` (necesita Pillow: `pip install pillow`).

Para ver el sitio en local: `python3 -m http.server` y abrir `http://localhost:8000`.

## Agregar una obra

1. Exporta la foto en WebP, máximo 1400 px por el lado largo, calidad 80, y guárdala en `assets/obra/<nombre>.webp`.
2. Agrégala a `OBRA` en `build.py` con categoría `cuadros` o `muros`.
3. Corre `python3 build.py`. Las fotos horizontales ocupan dos columnas solas.

## Diseño

- Colores: `--cal #F3F2EF` (fondo, pared encalada), `--tinta #2A2427` (texto), `--buganvilla #7E2B44` (color del logo), `--malva #E6D9D5` (banda de contacto), `--salvia #7F8C76`.
- Tipografía: Bellefair para títulos (eco del logo) y Hanken Grotesk para texto. Ambas OFL, incluidas en `assets/fonts/`.
- Íconos: Simple Icons (WhatsApp, Instagram) y Lucide, en `assets/icons/`, incrustados al compilar.
- La sombra de hojas de la portada sale de la foto original del logo (`assets/sombra-hojas.webp`).
- Logo: la imagen original está en `assets/marca/elita-logo-original.jpg`. De ahí salen el logo sin fondo (`elita-logo-sin-fondo.png`) y la versión horizontal del encabezado (`elita-horizontal.png`).

## Publicar

Cada push a `main` publica con GitHub Actions (`.github/workflows/pages.yml`). En Settings → Pages, la fuente debe ser "GitHub Actions". Para dominio propio, agregar un archivo `CNAME` con el dominio y configurar el DNS.

## Pendiente de Daniela

- Fotos originales en alta de las obras: las actuales salen de Instagram y algunas son de baja resolución.
- Aprobar los textos de "Sobre mí" y "Cómo funciona un encargo" (redactados a partir de su Instagram).
- Confirmar que se pueden nombrar las diseñadoras con las que trabajó y los nombres de los niños de los murales (Vale, Vittoria, Victoria, Sebastián).
- Títulos reales de las obras, medidas y año, si quiere mostrarlos.
- Ciudades donde trabaja y si hace envíos nacionales.
- Confirmar que el cuadro de la portada (verde con el espejo tallado) es obra suya y su técnica: el post de Instagram solo dice "pieza en acrílico".
- Correo de contacto, si quiere uno además de WhatsApp.
- Dominio (por ejemplo `elitaarte.com`): después de comprarlo, agregar `<link rel="canonical">` y URLs absolutas en las etiquetas `og:`.

## Intro

La primera vez que alguien abre la página, la flor del logo se dibuja sobre su fondo de sombras y luego aparecen las letras. Dura unos 4,5 segundos, se salta con un clic, tecla o scroll, y no vuelve a salir en ese navegador. Para verla otra vez: abrir la página con `?intro` al final de la dirección. No se muestra a quien tiene activado "reducir movimiento".

Las capas están en `assets/intro/` (flor, estambres, letras, subtítulo y fondo), separadas del logo original.
