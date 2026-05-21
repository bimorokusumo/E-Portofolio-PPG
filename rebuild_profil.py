import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_profil = """
    <section id="profil" class="two-col-layout one-screen" style="max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;">
        <div class="profil-left animate-on-scroll">
            <h2 class="section-title"><i class="fa-solid fa-user-gear"></i> Profil Singkat</h2>
            <div class="engraved-card">
                <div class="profile-avatar-wrap">
                    <img src="foto-profil-biru.jpg" alt="Bimoro Kusumo" class="profile-avatar">
                </div>
                <h3>Bimoro Kusumo, S.Pd.</h3>
                <p class="location"><i class="fa-solid fa-location-dot"></i> Gamping, Sleman, DIY</p>
                
                <div class="quote-engraving">
                    <i class="fa-solid fa-quote-left"></i>
                    <p>"Ambarketawang Sak Urat Nadi"</p>
                    <small>Menginternalisasi nilai-nilai kerja keras dan semangat pantang menyerah.</small>
                </div>
            </div>
        </div>
        
        <div class="profil-right animate-on-scroll">
            <div class="stats-container">
                <div class="stat-box">
                    <i class="fa-solid fa-star"></i>
                    <h3 class="counter" data-target="3.87">0</h3>
                    <p>IPK S1</p>
                </div>
                <div class="stat-box">
                    <i class="fa-solid fa-stopwatch"></i>
                    <h3><span class="counter" data-target="3">0</span>.<span class="counter" data-target="5">0</span></h3>
                    <p>Tahun Lulus</p>
                </div>
                <div class="stat-box">
                    <i class="fa-solid fa-award"></i>
                    <h3 class="counter" data-target="2026">0</h3>
                    <p>PPG Selesai</p>
                </div>
            </div>

            <div class="flip-card-container">
                <!-- Card 1 -->
                <div class="industrial-flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <i class="fa-solid fa-building-columns"></i>
                            <h4>Latar Belakang</h4>
                        </div>
                        <div class="flip-card-back">
                            <p>Lulusan S1 Pendidikan Teknik Mesin Sarjana Terapan (Pendidikan) Universitas Sarjanawiyata Tamansiswa (2020-2023). Mahasiswa PPG Prajabatan Gel. 1 UNY 2024 spesialisasi Teknik Pemesinan.</p>
                        </div>
                    </div>
                </div>
                <!-- Card 2 -->
                <div class="industrial-flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <i class="fa-solid fa-lightbulb"></i>
                            <h4>Inspirasi Mengajar</h4>
                        </div>
                        <div class="flip-card-back">
                            <p>Berasal dari keluarga pendidik, saya meyakini bahwa pendidikan vokasi adalah kunci membentuk generasi kompeten, disiplin, dan berdaya saing di industri.</p>
                        </div>
                    </div>
                </div>
                <!-- Card 3 -->
                <div class="industrial-flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <i class="fa-solid fa-bullseye"></i>
                            <h4>Tujuan Profesional</h4>
                        </div>
                        <div class="flip-card-back">
                            <p>Menciptakan lingkungan belajar inovatif, memadukan teori mekanik dengan praktik industri, serta membekali siswa keterampilan abad 21 untuk sukses berkarir.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# The existing profil section: <section id="profil" ... </section>
# Needs to handle nested divs correctly. We'll use re with DOTALL, making sure to match exactly up to the next section.
pattern = re.compile(r'<section id="profil".*?(?=\s*<section id="pengalaman")', re.DOTALL)
html = pattern.sub(new_profil, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Profil section rebuilt.")
