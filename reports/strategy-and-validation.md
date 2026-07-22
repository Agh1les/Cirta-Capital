# Cirta Capital — posicionamiento, dirección creativa y validación

## 1. Posicionamiento

Cirta Capital se presenta como una **firma industrial internacional, liderada directamente por un profesional sénior y ampliable mediante especialistas seleccionados**. La marca debe percibirse antes que la figura personal: Aghiles Abdi aporta responsabilidad, experiencia y criterio, mientras que la estructura permite incorporar capacidad adicional bajo los estándares de Cirta Capital.

La propuesta no vende horas ni informes. Vende una mejora concreta de la situación del cliente:

**Technical uncertainty → clear decisions → controlled execution**

El espacio competitivo elegido no es la consultoría estratégica abstracta ni la ingeniería de catálogo. Es la intervención sénior cuando un proyecto, una puesta en marcha, una incidencia técnica o una relación posventa ha acumulado suficiente complejidad como para exigir visión transversal y proximidad a la ejecución.

La oferta se concentra en tres áreas comerciales coherentes:

1. **Critical Project Recovery & Troubleshooting**.
2. **Commissioning, Start-up & Operational Readiness**.
3. **Industrial Service, After-Sales & Lifecycle Support**.

Automatización, integración de sistemas, coordinación de obra, sourcing de especialistas y apoyo técnico-comercial aparecen como capacidades que refuerzan esas tres áreas, no como un catálogo inconexo.

## 2. Dirección visual

La identidad combina:

- azul marino profundo y grafito para autoridad, discreción y calma bajo presión;
- marfil cálido para lectura editorial y para evitar la estética tecnológica fría o financiera;
- latón apagado como acento de decisión y precisión, nunca como señal de lujo ostentoso;
- titulares serif editoriales y texto sans serif de sistema para transmitir criterio sénior sin penalizar rendimiento ni compatibilidad multilingüe;
- grids rigurosos, líneas finas y visuales inspirados en el símbolo de tres círculos;
- fotografía del fundador reservada principalmente para About;
- animación limitada a progresión y orientación, con respeto a `prefers-reduced-motion`.

El hero evita fotografías de stock y utiliza un diagrama propio que materializa la transición entre evidencia, decisión y ejecución. El resultado pretende parecer más próximo a una firma profesional de alto riesgo que a una ingeniería de bajo coste o a una startup.

## 3. Referencias visuales investigadas

Las referencias se utilizan únicamente para extraer principios; no se copian estructuras, textos, identidades ni recursos.

### Arup — https://www.arup.com/

Principios extraídos: apertura basada en grandes problemas, autoridad técnica sin saturar la interfaz, lenguaje que conecta asesoramiento y ejecución, y una arquitectura editorial capaz de organizar amplitud multidisciplinar. Es relevante para Cirta Capital porque demuestra cómo una firma técnica puede hablar a dirección sin perder credibilidad de ingeniería.

### Slaughter and May — https://www.slaughterandmay.com/

Principios extraídos: extrema sobriedad, uso medido del espacio, énfasis en juicio claro cuando el riesgo es alto y capacidad para comunicar complejidad sin grandilocuencia. Es la referencia más cercana a la percepción buscada de una firma selectiva y responsable bajo presión.

### Foster + Partners — https://www.fosterandpartners.com/studio

Principios extraídos: integración visible de disciplinas, composición rigurosa, ritmo arquitectónico y sofisticación basada en estructura, no en decoración. Resulta útil para expresar que Cirta Capital conecta ingeniería, operaciones, personas y ejecución como un sistema.

### McKinsey & Company — https://www.mckinsey.com/

Principios extraídos: jerarquía editorial clara, titulares orientados a decisiones, navegación sobria y contenido diseñado para directivos con poco tiempo. Se toma como referencia de escaneabilidad y autoridad, no de tono corporativo ni de escala.

## 4. Arquitectura

La primera versión adopta una estructura híbrida: cada idioma dispone de una Home completa con navegación interna a cinco áreas claras.

- Home
- Capabilities
- Industries
- About
- Contact

Rutas:

- `/en/`
- `/fr/`
- `/es/`
- páginas legales independientes por idioma;
- root con redirección a inglés;
- página 404, sitemap, robots, manifest y datos estructurados.

La arquitectura permite añadir posteriormente casos de éxito, insights, artículos y publicaciones sin mostrar enlaces vacíos en la navegación actual.

## 5. Estrategia de conversión

El CTA principal es **Discuss a project** y sus equivalentes. La secuencia de conversión es deliberadamente sencilla:

1. reconocer una situación concreta de riesgo;
2. comprender las tres capacidades principales;
3. validar credibilidad mediante experiencia, sectores y método;
4. conocer la responsabilidad directa del fundador;
5. iniciar una consulta breve.

El formulario no simula procesamiento. Valida los campos, crea un correo precompletado y explica que los documentos se añaden después de abrir la aplicación de correo o mediante un canal seguro acordado.

## 6. Controles de credibilidad y compliance

- Las cifras se presentan como aproximadas cuando corresponde.
- No se atribuye a Cirta Capital la responsabilidad total de grandes infraestructuras.
- No se publican clientes, logotipos ni proyectos identificables.
- Las intervenciones urgentes están sujetas a ubicación y confirmación.
- Los resultados se formulan como objetivos, no como garantías.
- El pie de página aclara en los tres idiomas que la empresa no presta servicios financieros.
- Las páginas legales son preliminares e incluyen una advertencia de revisión profesional.
- No se instalan analítica, píxeles, CRM, chat, fuentes remotas ni cookies no esenciales.

## 7. Validación técnica

La entrega incluye un validador reproducible en `scripts/validate_site.py`. Comprueba:

- existencia de archivos internos, imágenes, hojas de estilo y scripts;
- enlaces internos y anclas;
- IDs duplicados;
- idioma, title, description, canonical, hreflang y Open Graph;
- jerarquía básica de encabezados;
- atributos alt de imágenes;
- campos y avisos del formulario estático;
- ausencia de trackers y recursos remotos no aprobados;
- sitemap, robots, CNAME, manifest, 404 y workflow de Pages;
- coherencia del aviso de servicios no financieros.

También se realizaron renderizados de control en 1440 px y 390 px, revisión de overflow horizontal, prueba del menú móvil y validación del estado de error del formulario.

## 8. Decisiones finales tras revisión crítica

### Como director industrial

La página abre con el problema y las consecuencias, no con una biografía. Los escenarios son reconocibles y el alcance está explicado con suficiente precisión para iniciar una conversación cualificada.

### Como cliente con un proyecto bloqueado

Se reduce la incertidumbre sobre qué puede hacer la firma, cómo se moviliza y qué información hace falta para empezar. El lenguaje evita promesas imposibles.

### Como director creativo premium

Se mantienen espacio negativo, contraste, ritmo editorial y un acento muy controlado. Se eliminan clichés industriales y señales visuales de finanzas.

### Como especialista en conversión

El CTA es consistente, el formulario pide contexto útil sin exigir un dossier completo y el canal alternativo por correo permanece visible.

### Como responsable de compliance

Se distingue claramente consultoría industrial de servicios financieros, se evita crear una relación profesional por el uso del sitio y se limita el tratamiento de datos a lo que el visitante decide enviar.

### Como desarrollador frontend

La solución no requiere compilación, backend ni dependencias en producción. Las rutas son relativas, el despliegue es compatible con dominio personalizado y subruta de GitHub Pages, y el mantenimiento se apoya en HTML, CSS y JavaScript legibles.

## 9. Estado previo a la publicación definitiva

1. `contact@cirtacapital.com` ha sido confirmado como correo operativo y supervisado.
2. La dirección registral y postal autorizada se ha incorporado exclusivamente a Privacy Policy y a la sección Legal Notice de Terms of Use en inglés, francés y español. No se presenta como oficina operativa ni abierta al público.
3. La revisión legal profesional de Privacy Policy y Terms of Use continúa pendiente y no debe considerarse completada.
4. La aprobación final de las cifras, de la fotografía y del símbolo continúa bajo responsabilidad de Cirta Capital LLC.
5. El dominio responde mediante HTTPS; tras cada actualización debe comprobarse que producción corresponde al paquete auditado más reciente.
