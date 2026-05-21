# Append massive CSS for EP2 redesign
css_content = """
/* =========================================
   EP2: REFLEKSI AKHIR PPL TERBIMBING (10 SECTIONS)
   THEME: VOKASI TEKNIK MESIN (INDUSTRIAL)
========================================= */

:root {
  --ep2-navy: #0B192C;        /* Biru tua gelap khas industrial */
  --ep2-blue: #1A365D;        /* Biru profesional */
  --ep2-steel: #718096;       /* Abu-abu industrial */
  --ep2-orange: #DD6B20;      /* Aksen orange teknik/safety */
  --ep2-yellow: #ECC94B;      /* Aksen kuning */
  --ep2-light: #F7FAFC;       /* Putih abu-abu bersih */
  --ep2-white: #FFFFFF;
  --ep2-dark: #1A202C;        /* Hitam arang */
}

/* Animations */
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
.reveal.active {
  opacity: 1;
  transform: translateY(0);
}

/* Base EP2 Typography & Spacing */
.ep2-section {
  padding: 6rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
}
.ep2-section-title {
  text-align: center;
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--ep2-navy);
  margin-bottom: 3.5rem;
  position: relative;
}
.ep2-section-title::after {
  content: '';
  display: block;
  width: 80px;
  height: 4px;
  background: var(--ep2-orange);
  margin: 1rem auto 0;
  border-radius: 2px;
}
.ep2-section-title.light {
  color: var(--ep2-white);
}

/* HERO SECTION */
#ep2-hero-full {
  background: linear-gradient(rgba(11, 25, 44, 0.85), rgba(11, 25, 44, 0.95)), url('assets/hero-bengkel.jpg') center/cover no-repeat;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0 2rem;
  color: var(--ep2-white);
}
.ep2-hero-content {
  max-width: 900px;
}
.ep2-hero-badge {
  display: inline-block;
  background: rgba(221, 107, 32, 0.2);
  color: var(--ep2-yellow);
  padding: 0.5rem 1.5rem;
  border-radius: 50px;
  font-weight: 600;
  border: 1px solid var(--ep2-orange);
  margin-bottom: 2rem;
  letter-spacing: 1px;
  text-transform: uppercase;
  font-size: 0.85rem;
}
.ep2-hero-title {
  font-size: 4rem;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 1.5rem;
  background: linear-gradient(to right, #fff, #ECC94B);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.ep2-hero-subtitle {
  font-size: 1.2rem;
  line-height: 1.8;
  color: #CBD5E0;
  margin-bottom: 3rem;
  max-width: 700px;
  margin-inline: auto;
}
.ep2-btn-group {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
}
.ep2-btn-primary {
  background: var(--ep2-orange);
  color: white;
  padding: 1rem 2rem;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
  border: none;
}
.ep2-btn-primary:hover {
  background: #C05621;
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(221, 107, 32, 0.3);
  text-decoration: none;
  color: white;
}
.ep2-btn-outline {
  background: transparent;
  color: white;
  padding: 1rem 2rem;
  border-radius: 8px;
  font-weight: 600;
  border: 2px solid white;
  transition: all 0.3s ease;
}
.ep2-btn-outline:hover {
  background: white;
  color: var(--ep2-navy);
  transform: translateY(-3px);
  text-decoration: none;
}

/* SEC 1: PENDAHULUAN */
#ep2-pendahuluan { background: var(--ep2-light); }
.ep2-info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
}
.ep2-info-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  border-bottom: 4px solid var(--ep2-blue);
  transition: transform 0.3s ease;
}
.ep2-info-card:hover { transform: translateY(-5px); }
.ep2-info-icon { font-size: 2.5rem; color: var(--ep2-orange); margin-bottom: 1rem; }
.ep2-info-title { font-size: 0.9rem; color: var(--ep2-steel); text-transform: uppercase; font-weight: 700; margin-bottom: 0.5rem; }
.ep2-info-val { font-size: 1.2rem; font-weight: 700; color: var(--ep2-navy); }

/* SEC 2: KOMPETENSI */
.ep2-kompetensi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}
.ep2-comp-card {
  background: white;
  border-radius: 16px;
  padding: 2.5rem 2rem;
  border: 1px solid #E2E8F0;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
}
.ep2-comp-card::before {
  content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  background: radial-gradient(circle at top right, rgba(221, 107, 32, 0.1), transparent 70%);
  opacity: 0; transition: opacity 0.4s ease;
}
.ep2-comp-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(11, 25, 44, 0.08);
  border-color: var(--ep2-orange);
}
.ep2-comp-card:hover::before { opacity: 1; }
.ep2-comp-icon { font-size: 3rem; margin-bottom: 1.5rem; display: block; }
.ep2-comp-card h3 { color: var(--ep2-navy); font-size: 1.3rem; margin-bottom: 1rem; }
.ep2-comp-card p { color: var(--ep2-steel); font-size: 0.95rem; line-height: 1.6; margin-bottom: 2rem; }
.ep2-progress-bg { background: #EDF2F7; height: 6px; border-radius: 3px; width: 100%; position: relative; }
.ep2-progress-bar { background: var(--ep2-blue); height: 100%; border-radius: 3px; width: 0; transition: width 1.5s ease; }
.ep2-comp-card:hover .ep2-progress-bar { background: var(--ep2-orange); }

/* SEC 3: PENGALAMAN BERMAKNA (STORYTELLING) */
#ep2-pengalaman { background: var(--ep2-navy); color: white; }
.ep2-story-container { display: flex; flex-direction: column; gap: 4rem; }
.ep2-story-row {
  display: flex;
  gap: 3rem;
  align-items: center;
}
.ep2-story-row:nth-child(even) { flex-direction: row-reverse; }
.ep2-story-img {
  flex: 1;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0,0,0,0.3);
  position: relative;
}
.ep2-story-img img { width: 100%; height: auto; display: block; }
.ep2-story-img::after {
  content: ''; position: absolute; inset: 0;
  border: 2px solid var(--ep2-orange); border-radius: 12px; transform: translate(15px, 15px); z-index: -1;
}
.ep2-story-text { flex: 1; }
.ep2-story-quote {
  font-size: 1.4rem; font-style: italic; color: var(--ep2-yellow);
  border-left: 4px solid var(--ep2-orange); padding-left: 1.5rem; margin-bottom: 1.5rem; line-height: 1.6;
}
.ep2-story-text p { color: #A0AEC0; line-height: 1.8; font-size: 1.05rem; }

/* SEC 4: TANTANGAN (INTERACTIVE DASHBOARD) */
.ep2-table-container {
  overflow-x: auto;
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}
.ep2-table { width: 100%; border-collapse: collapse; min-width: 800px; }
.ep2-table th { background: var(--ep2-blue); color: white; padding: 1.2rem; text-align: left; font-weight: 600; }
.ep2-table td { padding: 1.2rem; border-bottom: 1px solid #E2E8F0; color: var(--ep2-dark); vertical-align: top; }
.ep2-table tr:hover td { background: var(--ep2-light); }
.status-badge { display: inline-flex; align-items: center; gap: 8px; padding: 6px 12px; border-radius: 50px; font-size: 0.85rem; font-weight: 600; }
.status-warning { background: #FEFCBF; color: #B7791F; }
.status-action { background: #EBF8FF; color: #2B6CB0; }
.status-success { background: #F0FFF4; color: #2F855A; }

/* SEC 5: INOVASI (CARD GALLERY) */
#ep2-inovasi { background: var(--ep2-light); }
.ep2-inovasi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
.ep2-inovasi-card {
  background: white; border-radius: 12px; overflow: hidden;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: transform 0.3s ease;
}
.ep2-inovasi-card:hover { transform: translateY(-8px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); }
.ep2-inovasi-img { height: 200px; overflow: hidden; background: #CBD5E0; }
.ep2-inovasi-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
.ep2-inovasi-card:hover .ep2-inovasi-img img { transform: scale(1.1); }
.ep2-inovasi-content { padding: 1.5rem; }
.ep2-inovasi-content h3 { color: var(--ep2-navy); margin-bottom: 0.5rem; font-size: 1.2rem; }
.ep2-inovasi-content p { color: var(--ep2-steel); font-size: 0.95rem; line-height: 1.5; }

/* SEC 6: DOKUMENTASI (HORIZONTAL GALLERY) */
.ep2-gallery-scroll {
  display: flex; gap: 1.5rem; overflow-x: auto; padding: 1rem 0 3rem;
  scrollbar-width: thin; scrollbar-color: var(--ep2-orange) #EDF2F7;
}
.ep2-gallery-scroll::-webkit-scrollbar { height: 8px; }
.ep2-gallery-scroll::-webkit-scrollbar-track { background: #EDF2F7; border-radius: 4px; }
.ep2-gallery-scroll::-webkit-scrollbar-thumb { background: var(--ep2-orange); border-radius: 4px; }
.ep2-gallery-item {
  min-width: 300px; height: 400px; border-radius: 16px; overflow: hidden; position: relative;
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
.ep2-gallery-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
.ep2-gallery-item:hover img { transform: scale(1.05); }
.ep2-gallery-caption {
  position: absolute; bottom: 0; left: 0; width: 100%; padding: 2rem 1.5rem 1.5rem;
  background: linear-gradient(transparent, rgba(11,25,44,0.9)); color: white;
}
.ep2-gallery-caption h4 { color: white; margin-bottom: 0.5rem; font-size: 1.1rem; }

/* SEC 7: UMPAN BALIK (GLASSMORPHISM TESTIMONIAL) */
#ep2-evaluasi {
  background: linear-gradient(135deg, var(--ep2-navy), var(--ep2-blue)); color: white;
}
.ep2-testi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
.ep2-testi-card {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 2rem; border-radius: 16px; position: relative;
}
.ep2-testi-quote { font-size: 3rem; color: var(--ep2-orange); position: absolute; top: 1rem; right: 1.5rem; opacity: 0.5; }
.ep2-testi-text { font-style: italic; line-height: 1.8; margin-bottom: 2rem; color: #E2E8F0; z-index: 2; position: relative; }
.ep2-testi-author { display: flex; align-items: center; gap: 1rem; }
.ep2-testi-author-info h4 { color: var(--ep2-yellow); margin-bottom: 0.2rem; font-size: 1rem; }
.ep2-testi-author-info p { color: #A0AEC0; font-size: 0.85rem; margin: 0; }

/* SEC 8: DAMPAK (VISUAL DASHBOARD) */
.ep2-impact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
.ep2-impact-stats { display: flex; flex-direction: column; gap: 2rem; }
.ep2-stat-item h4 { display: flex; justify-content: space-between; margin-bottom: 0.8rem; color: var(--ep2-navy); }
.ep2-stat-item h4 span { color: var(--ep2-orange); font-weight: 800; }
.ep2-stat-desc { font-size: 0.95rem; color: var(--ep2-steel); margin-top: 0.8rem; line-height: 1.5; }
.ep2-impact-chart { background: var(--ep2-light); padding: 3rem; border-radius: 20px; text-align: center; border: 1px dashed #CBD5E0; }

/* SEC 9: TIMELINE */
#ep2-rencana { background: var(--ep2-light); }
.ep2-timeline { position: relative; max-width: 800px; margin: 0 auto; }
.ep2-timeline::before {
  content: ''; position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 4px; height: 100%; background: var(--ep2-blue);
}
.ep2-timeline-item { position: relative; margin-bottom: 3rem; width: 50%; padding-right: 3rem; }
.ep2-timeline-item:nth-child(even) { margin-left: auto; padding-right: 0; padding-left: 3rem; }
.ep2-timeline-dot {
  position: absolute; right: -12px; top: 0; width: 24px; height: 24px; border-radius: 50%;
  background: var(--ep2-orange); border: 4px solid var(--ep2-light); z-index: 2; box-shadow: 0 0 0 4px rgba(221,107,32,0.2);
}
.ep2-timeline-item:nth-child(even) .ep2-timeline-dot { right: auto; left: -12px; }
.ep2-timeline-content {
  background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);
}
.ep2-timeline-date { color: var(--ep2-orange); font-weight: 700; margin-bottom: 0.5rem; font-size: 0.9rem; }
.ep2-timeline-content h3 { color: var(--ep2-navy); margin-bottom: 1rem; }
.ep2-timeline-content p { color: var(--ep2-steel); line-height: 1.6; font-size: 0.95rem; }

/* SEC 10: PENUTUP */
#ep2-penutup {
  background: var(--ep2-dark); color: white; text-align: center; padding: 8rem 2rem;
  border-top: 5px solid var(--ep2-orange);
}
.ep2-penutup-content { max-width: 800px; margin: 0 auto; }
.ep2-penutup-content p { font-size: 1.25rem; line-height: 1.9; color: #CBD5E0; margin-bottom: 3rem; }
.ep2-final-quote {
  font-size: 1.8rem; font-weight: 800; font-style: italic; color: var(--ep2-yellow); line-height: 1.4;
  background: linear-gradient(135deg, rgba(255,255,255,0.05), transparent); padding: 3rem; border-radius: 20px;
}

@media (max-width: 768px) {
  .ep2-hero-title { font-size: 2.5rem; }
  .ep2-btn-group { flex-direction: column; }
  .ep2-story-row, .ep2-story-row:nth-child(even) { flex-direction: column; }
  .ep2-impact-grid { grid-template-columns: 1fr; }
  .ep2-timeline::before { left: 30px; }
  .ep2-timeline-item { width: 100%; padding-left: 80px !important; padding-right: 0 !important; }
  .ep2-timeline-dot { left: 18px !important; right: auto !important; }
  .ep2-final-quote { font-size: 1.3rem; padding: 2rem 1.5rem; }
}
"""
with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
print("Massive CSS for EP2 Overhaul Appended")
