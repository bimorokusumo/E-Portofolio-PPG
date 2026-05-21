import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update root variables
root_pattern = re.compile(r':root\s*\{[^}]*\}', re.DOTALL)
new_root = """
:root {
    /* Industrial Theme Colors */
    --primary-dark: #0f172a;
    --primary-blue: #1e40af;
    --kemendikbud-blue: #1e40af; /* Overriding previous to match theme */
    --accent-amber: #f59e0b;
    --bg-white: #ffffff;
    --bg-light-gray: #f8fafc;
    --text-dark: #334155;
    --text-light: #64748b;
    --border-color: #e2e8f0;
    --kemendikbud-cyan: #38bdf8;
    --kemendikbud-green: #10b981;
    --font-heading: 'Rajdhani', 'Inter', sans-serif;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    --radius-md: 12px;
}
"""
css = root_pattern.sub(new_root, css, count=1)

# Append new redesign styles
new_styles = """
/* ========================================================================= */
/* REDESIGN: TWO COLUMN INDUSTRIAL THEME STYLES                              */
/* ========================================================================= */

body {
    background-color: var(--bg-light-gray);
    color: var(--text-dark);
}

/* Two Column Layout Base */
.two-col-layout {
    display: grid !important;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: center;
}

.section-title {
    font-family: var(--font-heading);
    font-size: 2.5rem;
    color: var(--primary-dark);
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    font-weight: 700;
    text-transform: uppercase;
}

.section-title i {
    color: var(--accent-amber);
}

/* 1. Hero Section */
.hero-section {
    background-color: var(--primary-dark);
    background-image: 
        linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.95)),
        url('data:image/svg+xml;utf8,<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h40v40H0V0zm20 20h20v20H20V20zM0 20h20v20H0V20z" fill="%231e40af" fill-opacity="0.05" fill-rule="evenodd"/></svg>');
    color: white;
    min-height: 100vh;
    padding: 6rem 2rem;
    position: relative;
    overflow: hidden;
}

.typewriter-text {
    border-right: 2px solid var(--accent-amber);
    padding-right: 5px;
    animation: blink 0.75s step-end infinite;
    font-size: 1.2rem;
    color: #cbd5e1;
}
@keyframes blink { 50% { border-color: transparent; } }

.badge-industrial {
    background: rgba(245, 158, 11, 0.1) !important;
    color: var(--accent-amber) !important;
    border: 1px solid rgba(245, 158, 11, 0.3) !important;
}

.spinning-gear {
    animation: spin-slow 20s linear infinite;
}
@keyframes spin-slow { 100% { transform: rotate(360deg); } }

/* 2. Profil Singkat */
.engraved-card {
    background: linear-gradient(135deg, #ffffff, #f1f5f9);
    border: 1px solid #cbd5e1;
    border-radius: 20px;
    padding: 3rem 2rem;
    box-shadow: inset 0 2px 5px rgba(255,255,255,0.8), 0 10px 25px rgba(0,0,0,0.05);
    text-align: center;
    position: relative;
}

.profile-avatar-wrap {
    width: 150px;
    height: 150px;
    margin: 0 auto 1.5rem;
    border-radius: 50%;
    padding: 5px;
    background: linear-gradient(135deg, var(--primary-blue), var(--accent-amber));
}
.profile-avatar {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid white;
}

.quote-engraving {
    margin-top: 2rem;
    padding-top: 2rem;
    border-top: 2px dashed #cbd5e1;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    color: var(--primary-blue);
}
.quote-engraving i {
    font-size: 2rem;
    color: rgba(30, 64, 175, 0.2);
    position: absolute;
}

.stats-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}
.stat-box {
    background: var(--primary-dark);
    color: white;
    padding: 1.5rem 1rem;
    border-radius: 12px;
    text-align: center;
    border-bottom: 4px solid var(--accent-amber);
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}
.stat-box i { color: var(--accent-amber); font-size: 1.5rem; margin-bottom: 0.5rem; }
.stat-box h3 { font-size: 2rem; margin: 0; font-family: var(--font-heading); }
.stat-box p { font-size: 0.8rem; margin: 0; color: #94a3b8; text-transform: uppercase; }

.flip-card-container { display: flex; flex-direction: column; gap: 1rem; }
.industrial-flip-card {
    background-color: transparent;
    height: 100px;
    perspective: 1000px;
}
.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: left;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    transform-style: preserve-3d;
}
.industrial-flip-card:hover .flip-card-inner {
    transform: rotateX(180deg);
}
.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 12px;
    padding: 1.5rem;
    display: flex;
    align-items: center;
    border: 1px solid var(--border-color);
}
.flip-card-front {
    background-color: white;
    color: var(--primary-dark);
    gap: 1rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
.flip-card-front i { font-size: 2rem; color: var(--primary-blue); }
.flip-card-front h4 { margin: 0; font-size: 1.2rem; font-family: var(--font-heading); }
.flip-card-back {
    background-color: var(--primary-blue);
    color: white;
    transform: rotateX(180deg);
    font-size: 0.9rem;
    line-height: 1.5;
}

/* 3. Pengalaman Kerja (Vertical Timeline) */
.vertical-timeline {
    position: relative;
    padding-left: 2rem;
}
.welding-arc-line {
    position: absolute;
    top: 0; bottom: 0; left: 0;
    width: 4px;
    background: #cbd5e1;
    border-radius: 2px;
}
.welding-arc-line::after {
    content: '';
    position: absolute;
    top: 0; left: -2px; width: 8px; height: 30px;
    background: var(--accent-amber);
    border-radius: 10px;
    box-shadow: 0 0 10px var(--accent-amber), 0 0 20px var(--accent-amber);
    animation: weld-down 4s infinite linear;
}
@keyframes weld-down { 0% { top: 0; } 100% { top: 100%; } }

.timeline-item {
    position: relative;
    margin-bottom: 2rem;
    cursor: pointer;
    transition: var(--transition);
}
.timeline-icon {
    position: absolute;
    left: -3rem; top: 0;
    width: 40px; height: 40px;
    background: white;
    border: 3px solid #cbd5e1;
    border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    color: #cbd5e1;
    transition: var(--transition);
    z-index: 1;
}
.timeline-item.active .timeline-icon, .timeline-item:hover .timeline-icon {
    border-color: var(--accent-amber);
    color: var(--primary-dark);
    box-shadow: 0 0 15px rgba(245, 158, 11, 0.4);
}
.timeline-content {
    background: white;
    padding: 1.2rem;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    box-shadow: 0 2px 10px rgba(0,0,0,0.02);
}
.timeline-item.active .timeline-content {
    border-left: 4px solid var(--accent-amber);
}

.experience-detail-card {
    background: white;
    border-radius: 16px;
    padding: 3rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    border-top: 5px solid var(--primary-blue);
    display: none;
    animation: fadeIn 0.5s;
}
.experience-detail-card.active { display: block; }

/* 4. Pendidikan */
.edu-cards-container { display: flex; flex-direction: column; gap: 1rem; }
.edu-flip-card { height: 120px; perspective: 1000px; }
.edu-flip-inner { position: relative; width: 100%; height: 100%; text-align: left; transition: transform 0.6s; transform-style: preserve-3d; }
.edu-flip-card:hover .edu-flip-inner { transform: rotateY(180deg); }
.edu-flip-front, .edu-flip-back {
    position: absolute; width: 100%; height: 100%; backface-visibility: hidden;
    border-radius: 12px; padding: 1.5rem; display: flex; flex-direction: column; justify-content: center;
    border: 1px solid var(--border-color); background: white;
}
.edu-flip-front { align-items: flex-start; }
.edu-logo { position: absolute; right: 1rem; top: 1rem; width: 40px; height: 40px; object-fit: contain; opacity: 0.2; }
.edu-flip-back { background: var(--primary-dark); color: white; transform: rotateY(180deg); }

.process-flow-diagram {
    display: flex; flex-direction: column; align-items: center;
}
.flow-step {
    background: white; border: 2px solid var(--primary-blue); border-radius: 50px;
    padding: 1rem 2rem; display: flex; align-items: center; gap: 1rem; width: 80%;
    box-shadow: 0 10px 20px rgba(0,0,0,0.05); position: relative;
}
.flow-step.highlight { background: var(--primary-blue); color: white; }
.flow-icon { width: 50px; height: 50px; background: rgba(30, 64, 175, 0.1); border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 1.5rem; color: var(--primary-blue); }
.flow-step.highlight .flow-icon { background: rgba(255,255,255,0.2); color: white; }
.flow-text h4 { margin: 0; font-family: var(--font-heading); font-size: 1.2rem; }
.flow-text p { margin: 0; font-size: 0.85rem; opacity: 0.8; }
.flow-arrow { color: var(--accent-amber); font-size: 2rem; margin: 1rem 0; animation: bounce-down 2s infinite; }
@keyframes bounce-down { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(10px); } }

/* 5. Keahlian (Gauges & Radar) */
.skills-container { display: flex; flex-direction: column; gap: 1.5rem; }
.skill-bar-box { background: white; padding: 1.2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.03); }
.skill-info { display: flex; justify-content: space-between; font-weight: 600; margin-bottom: 0.8rem; font-family: var(--font-heading); }
.skill-progress-bg { height: 10px; background: #e2e8f0; border-radius: 5px; overflow: hidden; position: relative; }
.skill-progress-fill { position: absolute; top: 0; left: 0; height: 100%; background: linear-gradient(90deg, var(--primary-blue), var(--kemendikbud-cyan)); width: 0; transition: width 1.5s cubic-bezier(0.4, 0, 0.2, 1); }
.radar-chart-container { background: white !important; border: none !important; box-shadow: 0 20px 40px rgba(0,0,0,0.08); }

/* 6. Sertifikat */
.cert-list { list-style: none; padding: 0; margin: 0; max-height: 500px; overflow-y: auto; }
.cert-list li {
    padding: 1rem; border-bottom: 1px solid var(--border-color); cursor: pointer; transition: var(--transition);
    display: flex; align-items: center; gap: 1rem; background: white;
}
.cert-list li:hover { background: var(--bg-light-gray); }
.cert-list li.active { background: var(--primary-blue); color: white; }
.cert-preview-card { background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.08); }
.cert-preview-header { background: var(--primary-dark); color: white; padding: 1.5rem; text-align: center; }

/* 7. Galeri Masonry */
.masonry-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
.masonry-item { height: 100px; border-radius: 8px; overflow: hidden; cursor: pointer; }
.masonry-item img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s; }
.masonry-item:hover img { transform: scale(1.1); }
.lightbox-preview-card { text-align: center; background: white; padding: 1rem; border-radius: 16px; }

/* Responsive adjustments */
@media (max-width: 992px) {
    .two-col-layout { grid-template-columns: 1fr !important; }
    .hero-section { padding: 8rem 2rem 4rem; text-align: center; }
    .stats-container { grid-template-columns: 1fr; }
    .social-links { justify-content: center; }
    .achievements-badge { justify-content: center; }
    .hero-graphic { margin-top: 3rem; }
}

.btn-industrial {
    display: inline-block;
    background: var(--primary-blue);
    color: white;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    transition: var(--transition);
}
.btn-industrial:hover { background: var(--primary-dark); transform: translateY(-3px); }
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(new_styles)

print("style.css updated with redesign styles.")
