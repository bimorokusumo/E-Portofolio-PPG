import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <head> to add CDNs
head_pattern = re.compile(r'(<link rel="stylesheet" href="style\.css">)')
html = head_pattern.sub(r'<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n    \1', html)

# Add scripts before </body>
body_end_pattern = re.compile(r'(<script src="script\.js"></script>\s*</body>)')
html = body_end_pattern.sub(r'<script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>\n    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>\n    \1', html)

# Rewrite #home section
new_home = """
    <section id="home" class="two-col-layout hero-section">
        <div id="particles-js" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none;"></div>
        <div class="hero-content" style="position: relative; z-index: 1;">
            <div class="profile-container animate-on-scroll">
                <div class="profile-glow"></div>
                <img src="foto-profil-biru.jpg" alt="Bimoro Kusumo" class="profile-img">
                <h1 style="font-family: 'Rajdhani', sans-serif; font-weight: 700; color: #f8fafc; letter-spacing: 2px;">BIMORO KUSUMO</h1>
                <p class="tagline"><span id="typewriter" class="typewriter-text"></span><span class="cursor">|</span></p>
                <div class="social-links">
                    <a href="https://wa.me/6282243003058" class="social-btn" target="_blank">
                        <i class="fa-brands fa-whatsapp"></i> WhatsApp
                    </a>
                    <a href="mailto:bimorokusumo@gmail.com" class="social-btn">
                        <i class="fa-solid fa-envelope"></i> Email
                    </a>
                </div>
                <div class="achievements-badge" style="margin-top: 1.5rem; display: flex; gap: 10px; justify-content: flex-start; flex-wrap: wrap;">
                    <span class="badge badge-industrial"><i class="fa-solid fa-graduation-cap"></i> Lulusan Terbaik UNY IPK 3.87</span>
                    <span class="badge badge-industrial"><i class="fa-solid fa-bolt"></i> 3.5 Tahun Lulus S1</span>
                </div>
            </div>
        </div>
        <div class="hero-graphic" style="position: relative; z-index: 1; display: flex; justify-content: center; align-items: center;">
            <!-- Decorative rotating gear and industrial SVG -->
            <svg class="spinning-gear" viewBox="0 0 100 100" width="300" height="300" style="opacity: 0.15; fill: var(--kemendikbud-blue);">
                <path d="M92.1 42.6h-7.6c-1.1-4-2.8-7.7-5-11.1l5.4-5.4c1.9-1.9 1.9-5 0-6.9l-4.2-4.2c-1.9-1.9-5-1.9-6.9 0l-5.4 5.4c-3.4-2.2-7.1-3.9-11.1-5V7.9c0-2.7-2.2-4.9-4.9-4.9h-6c-2.7 0-4.9 2.2-4.9 4.9v7.6c-4 1.1-7.7 2.8-11.1 5l-5.4-5.4c-1.9-1.9-5-1.9-6.9 0l-4.2 4.2c-1.9 1.9-1.9 5 0 6.9l5.4 5.4c-2.2 3.4-3.9 7.1-5 11.1H7.9C5.2 42.6 3 44.8 3 47.5v6c0 2.7 2.2 4.9 4.9 4.9h7.6c1.1 4 2.8 7.7 5 11.1l-5.4 5.4c-1.9 1.9-1.9 5 0 6.9l4.2 4.2c1.9 1.9 5 1.9 6.9 0l5.4-5.4c3.4 2.2 7.1 3.9 11.1 5v7.6c0 2.7 2.2 4.9 4.9 4.9h6c2.7 0 4.9-2.2 4.9-4.9v-7.6c4-1.1 7.7-2.8 11.1-5l5.4 5.4c1.9 1.9 5 1.9 6.9 0l4.2-4.2c1.9-1.9 1.9-5 0-6.9l-5.4-5.4c2.2-3.4 3.9-7.1 5-11.1h7.6c2.7 0 4.9-2.2 4.9-4.9v-6C97 44.8 94.8 42.6 92.1 42.6zM50 70c-11 0-20-9-20-20s9-20 20-20 20 9 20 20S61 70 50 70z"/>
            </svg>
            <div class="hero-overlay-graphic" style="position: absolute; text-align: center;">
                <h2 style="font-size: 3rem; color: rgba(255,255,255,0.8); font-family: 'Rajdhani', sans-serif;">TEKNIK<br><span style="color: var(--accent-amber);">PEMESINAN</span></h2>
            </div>
        </div>
    </section>
"""

home_pattern = re.compile(r'<section id="home">.*?</section>', re.DOTALL)
html = home_pattern.sub(new_home, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Hero section rebuilt.")
