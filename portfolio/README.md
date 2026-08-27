# Portofolio Fitria Rozi

Website portofolio statis (HTML/CSS/JS murni — tanpa build step) untuk melamar posisi
AI Engineer, Software Engineer, Data Engineer, Data Analyst, dan QA Automation Engineer.

## Struktur
```
index.html          → Home (hero interaktif, ringkasan, preview)
projects.html        → Semua project + filter kategori
certificates.html    → Semua sertifikat
careers.html          → Halaman khusus recruiter (tab per role + timeline)
faq.html              → FAQ accordion
contact.html          → Let's Talk (form + info kontak)
css/style.css         → Semua styling & design tokens
js/main.js            → Animasi oscilloscope, filter, tab, accordion, form
assets/photos/        → Foto profil
assets/cv/            → 3 versi CV (AI Engineer / Software Engineer / QA Automation)
```

## Cara deploy ke Vercel (paling gampang)

**Opsi A — lewat GitHub (disarankan, auto-update tiap push):**
1. Buat repository baru di GitHub, upload semua isi folder ini (bukan foldernya, isinya).
2. Buka [vercel.com](https://vercel.com) → New Project → Import repo tadi.
3. Framework Preset: pilih **Other** (karena ini static HTML, bukan Next.js).
4. Build Command: kosongkan. Output Directory: kosongkan (root).
5. Klik Deploy. Selesai — dapat URL `namamu.vercel.app`.

**Opsi B — drag & drop cepat (tanpa GitHub):**
1. Install Vercel CLI: `npm i -g vercel`
2. Di folder ini, jalankan: `vercel`
3. Ikuti instruksi di terminal (login, pilih project baru). Selesai.

## Yang masih perlu kamu cek/ganti
- Link LinkedIn di semua halaman memakai `linkedin.com/in/fitriarozi-6a344a1b1` (dari data CV) —
  pastikan ini username LinkedIn yang benar-benar aktif.
- Form di halaman **Let's Talk** saat ini membuka email client (mailto) karena situs statis
  tidak punya backend. Kalau nanti mau pesan benar-benar masuk ke database/email otomatis,
  perlu ditambah layanan seperti Formspree, Resend, atau serverless function di Vercel — bilang
  saja kalau mau saya bantu sambungkan.
- Ganti/tambah foto di `assets/photos/` kalau ingin versi foto lain yang tampil di Home.
