# Cirta Capital — sitio corporativo multilingüe

Primera versión de producción de `cirtacapital.com`, desarrollada como sitio estático sin backend y compatible con GitHub Pages y GitHub Actions.

## Qué incluye

- Home completa en inglés, francés y español.
- Capabilities, Industries, About y Contact dentro de una arquitectura híbrida ampliable.
- Formulario estático que valida datos y prepara un correo mediante `mailto:`.
- Privacy Policy y Terms of Use preliminares en los tres idiomas.
- SEO técnico: metadata, canonical, `hreflang`, Open Graph, JSON-LD, sitemap, robots, manifest, favicon y 404.
- Diseño responsive, navegación por teclado, foco visible y movimiento reducido.
- Workflow de GitHub Pages con validación previa al despliegue.
- Informes de estrategia, control de calidad y checklist de lanzamiento.

## Estructura

- `docs/en/`, `docs/fr/`, `docs/es/`: contenido público por idioma.
- `docs/assets/css/styles.css`: sistema visual y responsive.
- `docs/assets/js/main.js`: menú, animaciones y formulario por correo.
- `docs/assets/img/`: símbolo, diagrama, retrato e imagen social optimizados.
- `scripts/validate_site.py`: validación automática del sitio.
- `.github/workflows/pages.yml`: validación y despliegue automático.
- `reports/strategy-and-validation.md`: posicionamiento, referencias y revisión crítica.
- `reports/launch-checklist.md`: tareas previas al lanzamiento.

## Ejecutar localmente

Desde la raíz del repositorio:

```bash
python3 -m http.server 8000 --directory docs
```

Abrir:

- `http://localhost:8000/en/`
- `http://localhost:8000/fr/`
- `http://localhost:8000/es/`

No es necesario instalar Node, un framework ni un generador estático.

## Validar antes de publicar

Ejecutar:

```bash
python3 scripts/validate_site.py
```

La misma validación se ejecuta en GitHub Actions antes de cada despliegue.

## Publicar en GitHub Pages

1. Crear un repositorio y subir el contenido de esta carpeta.
2. Usar `main` como rama principal.
3. En **Settings → Pages → Build and deployment**, seleccionar **GitHub Actions**.
4. Hacer `push` a `main` o ejecutar manualmente **Deploy static site to GitHub Pages**.
5. Añadir `cirtacapital.com` como dominio personalizado en **Settings → Pages**.
6. Configurar el DNS según las instrucciones mostradas por GitHub.
7. Activar HTTPS cuando GitHub confirme el dominio.

`docs/CNAME` contiene el dominio final. El workflow publica exclusivamente la carpeta `docs`.

## Editar contenido

- Inglés: `docs/en/index.html`
- Francés: `docs/fr/index.html`
- Español: `docs/es/index.html`

El inglés es la versión canónica. Mantener alineadas entre idiomas las cifras, promesas, nombres de servicios y avisos legales.

## Cambiar el correo

La entrega utiliza `contact@cirtacapital.com` como correo corporativo operativo y supervisado.

Buscar y reemplazar esa dirección en todo el repositorio, incluido:

- contenido visible;
- datos estructurados JSON-LD;
- `docs/assets/js/main.js`;
- páginas legales;
- documentación.

Comando orientativo:

```bash
grep -RIn "contact@cirtacapital.com" .
```

## Cambiar imágenes

- Retrato: sustituir `aghiles-abdi-480.webp` y `aghiles-abdi-656.webp`, o actualizar `src` y `srcset`.
- Símbolo: editar `logo-symbol.svg` y `favicon.svg`.
- Imagen social: sustituir `cirta-capital-og.png` manteniendo 1200 × 630 px.
- Diagrama del hero: editar `decision-system.svg`.

Optimizar imágenes antes de publicar. No incorporar material de clientes, instalaciones o proyectos sin autorización.

## Formulario

El formulario no transmite datos a un servidor y no muestra una confirmación de envío. Al completarlo:

1. valida los campos;
2. prepara un asunto y cuerpo localizados;
3. abre la aplicación de correo del visitante;
4. permite revisar, adjuntar documentos y enviar.

Los navegadores no pueden adjuntar archivos automáticamente mediante `mailto:`. El texto de la página lo explica expresamente.

## Privacidad y textos legales

Las páginas legales son borradores proporcionados para una primera versión sin analítica, píxeles ni cookies no esenciales. Incluyen la dirección registral y postal autorizada exclusivamente en las páginas legales. Antes de considerarlas definitivas:

- confirmar los proveedores reales utilizados y actualizar el texto si cambia la infraestructura;
- obtener revisión profesional.

## Añadir contenido futuro

Para casos, insights o artículos, se recomienda crear rutas por idioma y mantener:

- canonical y `hreflang`;
- títulos y descripciones únicos;
- enlaces internos desde la Home cuando exista contenido real;
- sitemap actualizado;
- ausencia de secciones vacías o “coming soon”.
