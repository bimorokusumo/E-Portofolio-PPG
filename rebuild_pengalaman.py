import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_pengalaman = """
    <section id="pengalaman" class="two-col-layout one-screen" style="max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;">
        <div class="pengalaman-left animate-on-scroll">
            <h2 class="section-title"><i class="fa-solid fa-industry"></i> Pengalaman Kerja</h2>
            <div class="vertical-timeline">
                <!-- Timeline item 1 -->
                <div class="timeline-item active" onclick="showExperience('komatsu')">
                    <div class="timeline-icon"><i class="fa-solid fa-robot"></i></div>
                    <div class="timeline-content">
                        <h4>PT Komatsu Undercarriage Indonesia</h4>
                        <span>Januari - April 2022</span>
                    </div>
                </div>
                <!-- Timeline item 2 -->
                <div class="timeline-item" onclick="showExperience('smk2')">
                    <div class="timeline-icon"><i class="fa-solid fa-chalkboard-user"></i></div>
                    <div class="timeline-content">
                        <h4>SMK N 2 Depok Sleman</h4>
                        <span>PPL 1 & 2 (2024 - Sekarang)</span>
                    </div>
                </div>
                <div class="welding-arc-line"></div>
            </div>
        </div>

        <div class="pengalaman-right animate-on-scroll">
            <div id="exp-komatsu" class="experience-detail-card active">
                <h3><i class="fa-solid fa-cogs"></i> Praktik Industri</h3>
                <h4>PT Komatsu Undercarriage Indonesia</h4>
                <span class="exp-date">Januari - April 2022 | Cikarang, Jawa Barat</span>
                <p>Terlibat langsung dalam divisi produksi komponen alat berat. Pengalaman ini memberikan wawasan mendalam mengenai:</p>
                <ul>
                    <li>Budaya kerja industri 5R (Ringkas, Rapi, Resik, Rawat, Rajin)</li>
                    <li>Sistem Keselamatan dan Kesehatan Kerja (K3) standar internasional</li>
                    <li>Proses <em>Quality Control</em> (QC) yang ketat pada produk permesinan</li>
                </ul>
                <p class="exp-highlight">Pengalaman ini memperkuat kompetensi teknis saya yang kini saya aplikasikan dalam merancang pembelajaran kejuruan.</p>
            </div>

            <div id="exp-smk2" class="experience-detail-card" style="display: none;">
                <h3><i class="fa-solid fa-chalkboard-user"></i> Guru Praktik (PPL)</h3>
                <h4>SMK Negeri 2 Depok Sleman</h4>
                <span class="exp-date">2024 - Sekarang | Yogyakarta</span>
                <p>Melaksanakan Praktik Pengalaman Lapangan (PPL) 1 dan 2 sebagai Guru Teknik Pemesinan.</p>
                <ul>
                    <li>Mengampu mata pelajaran Dasar Teknik Mesin dan Fabrikasi Logam</li>
                    <li>Merancang modul ajar berbasis <em>Project Based Learning (PjBL)</em></li>
                    <li>Mendampingi siswa dalam pengoperasian mesin CNC dan pengelasan SMAW</li>
                    <li>Melakukan asesmen formatif dan sumatif secara komprehensif</li>
                </ul>
                <p class="exp-highlight">Pengalaman ini mengasah kemampuan pedagogik saya dalam menghadapi dinamika kelas yang sesungguhnya.</p>
            </div>
        </div>
    </section>
"""

pattern = re.compile(r'<section id="pengalaman".*?(?=\s*<section id="pendidikan")', re.DOTALL)
html = pattern.sub(new_pengalaman, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Pengalaman section rebuilt.")
