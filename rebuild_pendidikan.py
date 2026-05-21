import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_pendidikan = """
    <section id="pendidikan" class="two-col-layout one-screen" style="max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;">
        <div class="pendidikan-left animate-on-scroll">
            <h2 class="section-title"><i class="fa-solid fa-graduation-cap"></i> Riwayat Pendidikan</h2>
            <div class="edu-cards-container">
                <!-- SMK -->
                <div class="edu-flip-card">
                    <div class="edu-flip-inner">
                        <div class="edu-flip-front">
                            <h3>SMK N 1 Sedayu</h3>
                            <p>2017 - 2020</p>
                        </div>
                        <div class="edu-flip-back">
                            <p><strong>Jurusan:</strong> Teknik Pemesinan</p>
                            <p>Mempelajari dasar-dasar permesinan bubut, frais, dan gambar teknik.</p>
                        </div>
                    </div>
                </div>
                <!-- S1 -->
                <div class="edu-flip-card">
                    <div class="edu-flip-inner">
                        <div class="edu-flip-front">
                            <img src="logo-ust.png" alt="UST Logo" class="edu-logo">
                            <h3>Univ. Sarjanawiyata Tamansiswa</h3>
                            <p>2020 - 2023</p>
                        </div>
                        <div class="edu-flip-back">
                            <p><strong>Program:</strong> S1 Terapan Pendidikan Teknik Mesin</p>
                            <p>IPK: 3.87. Fokus pada perancangan mekanik dan metodologi pengajaran vokasi.</p>
                        </div>
                    </div>
                </div>
                <!-- PPG -->
                <div class="edu-flip-card">
                    <div class="edu-flip-inner">
                        <div class="edu-flip-front">
                            <img src="logo-uny.png" alt="UNY Logo" class="edu-logo">
                            <h3>Universitas Negeri Yogyakarta</h3>
                            <p>2024 - Sekarang</p>
                        </div>
                        <div class="edu-flip-back">
                            <p><strong>Program:</strong> Pendidikan Profesi Guru (PPG) Prajabatan Gel. 1</p>
                            <p>Bidang Studi: Teknik Pemesinan. Praktik Mengajar & Asesmen.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="pendidikan-right animate-on-scroll">
            <div class="process-flow-diagram">
                <div class="flow-step">
                    <div class="flow-icon"><i class="fa-solid fa-cogs"></i></div>
                    <div class="flow-text">
                        <h4>Foundation</h4>
                        <p>SMK Teknik Pemesinan</p>
                    </div>
                </div>
                <div class="flow-arrow"><i class="fa-solid fa-arrow-down-long"></i></div>
                <div class="flow-step">
                    <div class="flow-icon"><i class="fa-solid fa-laptop-code"></i></div>
                    <div class="flow-text">
                        <h4>Specialization</h4>
                        <p>S1 Terapan (Desain & Manufaktur)</p>
                    </div>
                </div>
                <div class="flow-arrow"><i class="fa-solid fa-arrow-down-long"></i></div>
                <div class="flow-step highlight">
                    <div class="flow-icon"><i class="fa-solid fa-chalkboard-user"></i></div>
                    <div class="flow-text">
                        <h4>Professional</h4>
                        <p>PPG Vokasi (Pedagogik Modern)</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

pattern = re.compile(r'<section id="pendidikan".*?(?=\s*<section id="keahlian")', re.DOTALL)
html = pattern.sub(new_pendidikan, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Pendidikan section rebuilt.")
