import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_keahlian = """
    <section id="keahlian" class="two-col-layout one-screen" style="max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;">
        <div class="keahlian-left animate-on-scroll">
            <h2 class="section-title"><i class="fa-solid fa-wrench"></i> Kompetensi & Keahlian</h2>
            <div class="skills-container">
                <div class="skill-bar-box">
                    <div class="skill-info">
                        <span>Pemesinan CNC (Mastercam, Solidworks)</span>
                        <span>90%</span>
                    </div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress-fill" data-width="90%"></div>
                    </div>
                </div>
                <div class="skill-bar-box">
                    <div class="skill-info">
                        <span>Pengelasan SMAW & Fabrikasi Logam</span>
                        <span>85%</span>
                    </div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress-fill" data-width="85%"></div>
                    </div>
                </div>
                <div class="skill-bar-box">
                    <div class="skill-info">
                        <span>Pemesinan Konvensional (Bubut, Frais)</span>
                        <span>95%</span>
                    </div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress-fill" data-width="95%"></div>
                    </div>
                </div>
                <div class="skill-bar-box">
                    <div class="skill-info">
                        <span>Pedagogi & Desain Pembelajaran (UbD, PjBL)</span>
                        <span>88%</span>
                    </div>
                    <div class="skill-progress-bg">
                        <div class="skill-progress-fill" data-width="88%"></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="keahlian-right animate-on-scroll" style="display: flex; justify-content: center; align-items: center; position: relative;">
            <div class="radar-chart-container" style="background: rgba(255,255,255,0.05); padding: 2rem; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); width: 100%; max-width: 500px; aspect-ratio: 1/1;">
                <canvas id="skillRadar"></canvas>
            </div>
        </div>
    </section>
"""

pattern = re.compile(r'<section id="keahlian".*?(?=\s*<section id="sertifikat")', re.DOTALL)
html = pattern.sub(new_keahlian, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Keahlian section rebuilt.")
