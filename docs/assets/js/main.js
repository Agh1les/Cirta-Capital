(() => {
  const toggle = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('[data-nav]');
  if (toggle && nav) {
    const openLabel = toggle.dataset.labelOpen || 'Open menu';
    const closeLabel = toggle.dataset.labelClose || 'Close menu';
    const close = (restoreFocus = false) => {
      nav.classList.remove('open');
      document.body.classList.remove('nav-open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', openLabel);
      if (restoreFocus) toggle.focus();
    };
    const open = () => {
      nav.classList.add('open');
      document.body.classList.add('nav-open');
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', closeLabel);
      nav.querySelector('a')?.focus();
    };
    toggle.addEventListener('click', () => nav.classList.contains('open') ? close() : open());
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => close()));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && nav.classList.contains('open')) close(true);
    });
    window.addEventListener('resize', () => { if (window.innerWidth > 1040) close(); });
  }

  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: .08, rootMargin: '0px 0px -40px' });
    reveals.forEach(el => io.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('is-visible'));
  }

  const form = document.querySelector('[data-mailto-form]');
  if (!form) return;

  const status = form.querySelector('.form-status');
  const labels = {
    en: {
      subject: 'Industrial project enquiry',
      invalid: 'Please complete the required fields and use a valid email address.',
      ready: 'Your email application should open. Review the message, attach any documents and send it.',
      copied: 'Request summary copied to the clipboard.',
      fail: 'Copying was not available. Select the text manually or email contact@cirtacapital.com.',
      attachment: 'Documents can be attached after the email application opens.',
      keys: ['Full name', 'Company', 'Corporate email', 'Country', 'Type of need', 'Project stage', 'Urgency', 'Situation']
    },
    fr: {
      subject: 'Demande concernant un projet industriel',
      invalid: 'Veuillez compléter les champs obligatoires et utiliser une adresse e-mail valide.',
      ready: 'Votre application de messagerie devrait s’ouvrir. Vérifiez le message, ajoutez les documents puis envoyez-le.',
      copied: 'Résumé de la demande copié.',
      fail: 'La copie automatique n’est pas disponible. Écrivez à contact@cirtacapital.com.',
      attachment: 'Les documents peuvent être joints après ouverture de l’application de messagerie.',
      keys: ['Nom complet', 'Entreprise', 'E-mail professionnel', 'Pays', 'Type de besoin', 'Stade du projet', 'Urgence', 'Situation']
    },
    es: {
      subject: 'Consulta sobre proyecto industrial',
      invalid: 'Completa los campos obligatorios y utiliza un correo válido.',
      ready: 'Tu aplicación de correo debería abrirse. Revisa el mensaje, añade los documentos y envíalo.',
      copied: 'Resumen de la solicitud copiado.',
      fail: 'No se pudo copiar automáticamente. Escribe a contact@cirtacapital.com.',
      attachment: 'Los documentos pueden adjuntarse después de que se abra la aplicación de correo.',
      keys: ['Nombre completo', 'Empresa', 'Correo corporativo', 'País', 'Tipo de necesidad', 'Fase del proyecto', 'Urgencia', 'Situación']
    }
  };
  const lang = form.dataset.lang || 'en';
  const t = labels[lang] || labels.en;
  const fields = ['fullName', 'company', 'email', 'country', 'need', 'stage', 'urgency', 'situation'];

  const build = () => {
    const data = new FormData(form);
    return fields.map((key, index) => `${t.keys[index]}: ${String(data.get(key) || '').trim()}`).join('\r\n');
  };

  const validate = () => {
    let ok = true;
    form.querySelectorAll('[required]').forEach(el => {
      const valid = el.checkValidity() && String(el.value).trim() !== '';
      el.setAttribute('aria-invalid', String(!valid));
      if (!valid) ok = false;
    });
    if (!ok) {
      status.textContent = t.invalid;
      form.querySelector('[aria-invalid="true"]')?.focus();
    }
    return ok;
  };

  form.addEventListener('input', event => {
    if (event.target.matches('[aria-invalid="true"]') && event.target.checkValidity()) {
      event.target.setAttribute('aria-invalid', 'false');
    }
  });

  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!validate()) return;
    const data = new FormData(form);
    const subject = `${t.subject} — ${data.get('company')} — ${data.get('need')}`;
    const body = `${build()}\r\n\r\n${t.attachment}`;
    status.textContent = t.ready;
    window.location.href = `mailto:contact@cirtacapital.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });

  form.querySelector('[data-copy-summary]')?.addEventListener('click', async () => {
    if (!validate()) return;
    try {
      await navigator.clipboard.writeText(build());
      status.textContent = t.copied;
    } catch {
      status.textContent = t.fail;
    }
  });
})();
