// =========================================================
// i18n.js — simple ID/EN translation engine
// Reads dictionary from <script id="i18n-data" type="application/json">
// Elements: data-i18n="key" (text), data-i18n-html="key" (innerHTML),
// data-i18n-placeholder="key" (placeholder attr)
// =========================================================
(function () {
  function getDict() {
    const el = document.getElementById('i18n-data');
    if (!el) return {};
    try { return JSON.parse(el.textContent); } catch (e) { return {}; }
  }
  const dict = getDict();

  function applyLang(lang) {
    lang = lang === 'en' ? 'en' : 'id';
    document.documentElement.lang = lang;

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (dict[key] && dict[key][lang] != null) el.textContent = dict[key][lang];
    });
    document.querySelectorAll('[data-i18n-html]').forEach(el => {
      const key = el.getAttribute('data-i18n-html');
      if (dict[key] && dict[key][lang] != null) el.innerHTML = dict[key][lang];
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      if (dict[key] && dict[key][lang] != null) el.setAttribute('placeholder', dict[key][lang]);
    });

    try { localStorage.setItem('fr_lang', lang); } catch (e) {}

    document.querySelectorAll('.lang-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.lang === lang);
    });
  }

  window.applyLang = applyLang;

  document.addEventListener('DOMContentLoaded', () => {
    let saved = 'id';
    try { saved = localStorage.getItem('fr_lang') || 'id'; } catch (e) {}
    applyLang(saved);
    document.querySelectorAll('.lang-btn').forEach(b => {
      b.addEventListener('click', () => applyLang(b.dataset.lang));
    });
  });
})();
