# Cirta Capital — checklist de lanzamiento

## Contenido y marca

- [ ] Cifras públicas aprobadas: ≈100 proyectos, 18 países, equipos de hasta 70 personas y ≈30 % de actividad en campo.
- [ ] Fotografía de Aghiles Abdi autorizada para publicación.
- [ ] Símbolo y denominación Cirta Capital autorizados.
- [x] Correo `contact@cirtacapital.com` confirmado como operativo y supervisado.
- [x] Dirección registral y postal autorizada añadida a Privacy Policy y Legal Notice en los tres idiomas, sin presentarla como oficina pública u operativa.

## Legal y privacidad

- [ ] Privacy Policy y Terms of Use revisados por un profesional.
- [ ] Proveedores reales de correo y hosting confirmados en la política cuando proceda.
- [ ] No se han añadido analítica, píxeles, CRM, chat o cookies no esenciales sin actualizar la política.

## GitHub Pages y dominio

- [ ] Repositorio creado y rama principal configurada como `main`.
- [ ] Settings → Pages → Source configurado en GitHub Actions.
- [ ] Dominio `cirtacapital.com` añadido en Settings → Pages.
- [x] DNS configurado y dominio público confirmado por el propietario.
- [x] HTTPS accesible en `https://cirtacapital.com/`.
- [ ] Desplegar este paquete auditado y comprobar que ha sustituido íntegramente la versión anterior.
- [ ] Workflow de la actualización completado sin errores.

## Pruebas finales

- [ ] Ejecutar `python3 scripts/validate_site.py`.
- [ ] Probar `/en/`, `/fr/`, `/es/` en móvil y escritorio.
- [ ] Probar menú con teclado y tecla Escape.
- [ ] Probar todos los enlaces de idioma y legales.
- [ ] Probar formulario con campos vacíos y completos.
- [ ] Probar apertura del correo en Windows, macOS, iOS y Android disponibles.
- [ ] Verificar que el correo precompletado está localizado en cada idioma.
- [ ] Comprobar Open Graph con una herramienta de previsualización social.
- [ ] Enviar sitemap a los motores de búsqueda después del lanzamiento.
