// =========================================================
// FITRIA ROZI — PORTFOLIO — main.js
// =========================================================

/* ---------- Mobile nav ---------- */
document.addEventListener('DOMContentLoaded', () => {
  const burger = document.querySelector('.burger');
  const links = document.querySelector('.nav-links');
  if (burger) {
    burger.addEventListener('click', () => links.classList.toggle('open'));
  }

  /* ---------- Language toggle (ID / EN) ---------- */
  const langToggle = document.getElementById('lang-toggle');
  if (langToggle) {
    const idBtn = langToggle.querySelector('.lang-id-btn');
    const enBtn = langToggle.querySelector('.lang-en-btn');
    const setLang = (lang) => {
      document.documentElement.classList.toggle('lang-en', lang === 'en');
      idBtn.classList.toggle('active', lang !== 'en');
      enBtn.classList.toggle('active', lang === 'en');
      localStorage.setItem('lang', lang);
    };
    idBtn.addEventListener('click', () => setLang('id'));
    enBtn.addEventListener('click', () => setLang('en'));
    setLang(localStorage.getItem('lang') === 'en' ? 'en' : 'id');
  }

  /* ---------- Skill bar animation ---------- */
  const bars = document.querySelectorAll('.bar-fill');
  if (bars.length && 'IntersectionObserver' in window) {
    const barIo = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.style.width = e.target.dataset.pct + '%';
          barIo.unobserve(e.target);
        }
      });
    }, { threshold: 0.4 });
    bars.forEach(b => barIo.observe(b));
  } else {
    bars.forEach(b => b.style.width = b.dataset.pct + '%');
  }

  /* ---------- Scroll reveal ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('in'));
  }

  /* ---------- Role cycle (hero) ---------- */
  const roleEl = document.getElementById('role-cycle');
  if (roleEl) {
    const roles = JSON.parse(roleEl.dataset.roles);
    let i = 0;
    roleEl.textContent = '> ' + roles[0];
    setInterval(() => {
      i = (i + 1) % roles.length;
      roleEl.style.opacity = 0;
      setTimeout(() => {
        roleEl.textContent = '> ' + roles[i];
        roleEl.style.opacity = 1;
      }, 220);
    }, 2400);
  }

  /* ---------- Project filter ---------- */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.project-card');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const f = btn.dataset.filter;
      cards.forEach(c => {
        const show = f === 'all' || c.dataset.cat.includes(f);
        c.style.display = show ? '' : 'none';
      });
    });
  });

  /* ---------- Career tabs ---------- */
  const roleTabs = document.querySelectorAll('.role-tab');
  const rolePanels = document.querySelectorAll('.role-panel');
  roleTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      roleTabs.forEach(t => t.classList.remove('active'));
      rolePanels.forEach(p => p.classList.remove('active'));
      tab.classList.add('active');
      document.getElementById(tab.dataset.role).classList.add('active');
    });
  });

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll('.faq-q').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.parentElement;
      const answer = item.querySelector('.faq-a');
      const wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(o => {
        o.classList.remove('open');
        o.querySelector('.faq-a').style.maxHeight = null;
      });
      if (!wasOpen) {
        item.classList.add('open');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  /* ---------- Contact form -> mailto ---------- */
  const form = document.getElementById('talk-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = form.name.value.trim();
      const role = form.role.value;
      const message = form.message.value.trim();
      const subject = encodeURIComponent(`Peluang kolaborasi — ${role || 'Umum'} (via portofolio)`);
      const body = encodeURIComponent(
        `Nama: ${name}\nRole yang dibicarakan: ${role}\n\nPesan:\n${message}`
      );
      window.location.href = `mailto:fitriarozi03@gmail.com?subject=${subject}&body=${body}`;
    });
  }
});

/* ---------- Oscilloscope hero animation ---------- */
(function () {
  const canvas = document.getElementById('scope');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let w, h, dpr = Math.min(window.devicePixelRatio || 1, 2);

  function resize() {
    const rect = canvas.getBoundingClientRect();
    w = rect.width; h = rect.height;
    canvas.width = w * dpr; canvas.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  resize();
  window.addEventListener('resize', resize);

  let mouseAmp = 0.5;
  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouseAmp = Math.max(0.15, Math.min(1, (e.clientY - rect.top) / rect.height));
  });
  canvas.addEventListener('mouseleave', () => { mouseAmp = 0.5; });

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let t = 0;

  function drawGrid() {
    ctx.strokeStyle = 'rgba(237,239,243,0.06)';
    ctx.lineWidth = 1;
    for (let x = 0; x < w; x += 32) {
      ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
    }
    for (let y = 0; y < h; y += 32) {
      ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
    }
  }

  function drawTrace(fn, color, glow) {
    ctx.beginPath();
    for (let x = 0; x <= w; x += 2) {
      const y = fn(x);
      if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.shadowColor = color;
    ctx.shadowBlur = glow;
    ctx.stroke();
    ctx.shadowBlur = 0;
  }

  function frame() {
    ctx.clearRect(0, 0, w, h);
    drawGrid();
    const midY = h / 2;
    const amp = (h * 0.28) * mouseAmp;

    // CH1 — physics: smooth sine (measured signal)
    drawTrace((x) => midY - 20 - amp * 0.6 * Math.sin((x / w) * Math.PI * 4 + t), '#4FD8C4', 10);

    // CH2 — code: quantized / pulse-like signal (digital)
    drawTrace((x) => {
      const base = midY + 30;
      const step = Math.sin((x / w) * Math.PI * 10 + t * 1.3);
      const quant = Math.sign(step) * amp * 0.35;
      return base - quant;
    }, '#F5A623', 8);

    t += reduceMotion ? 0 : 0.018;
    requestAnimationFrame(frame);
  }
  frame();
})();
