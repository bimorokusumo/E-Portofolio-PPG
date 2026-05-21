import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 2. Pengalaman
pengalaman_pattern = re.compile(r'<section id="pengalaman".*?</section>', re.DOTALL)
new_pengalaman = """
    <section id="pengalaman" class="one-screen" style="background-color: var(--bg-light-gray); max-width: 100%; padding: 4rem 2rem;">
        <div class="split-layout align-start">
            <div class="split-left">
                <h2 style="margin-bottom: 2rem; color: var(--kemendikbud-blue);"><span style="font-size: 2rem;">💼</span> Pengalaman Kerja & Profesional</h2>
                <div class="article-grid" style="grid-template-columns: 1fr;">
                    <div class="card-article">
                        <h3>🏢 PT Margo Mutiasa Susanto</h3>
                        <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Jun 2025 - Sekarang | PIC & Supervisor</p>
                        <p>Memimpin operasional proyek kontraktor bangunan, MEP, dan dapur MBG. Mengelola tim, sumber daya, dan K3, serta menyusun rencana arsitektur dan MEP.</p>
                    </div>
                    <div class="card-article">
                        <h3>🤖 PT Stechoq Robotika Indonesia</h3>
                        <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Feb 2024 - Des 2024 | Project Manager & Mechanical Engineer</p>
                        <p>Mengelola project pembuatan "Lembaga Pelatihan Kompetensi" (LMS). Merancang mesin pencacah plastik dan membuat ±20 modul pelatihan berbasis kompetensi.</p>
                    </div>
                    <div class="card-article">
                        <h3>👨‍🏫 SMK N 1 Sedayu</h3>
                        <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Mar 2025 - Apr 2025 | Trainer LKS DIY</p>
                        <p>Menjadi trainer untuk peserta Lomba Kompetensi Siswa (LKS) DIY 2025 di bidang Prototype Modeling menggunakan CAD 3D Fusion 360.</p>
                    </div>
                    <div class="card-article">
                        <h3>🏫 SMK Muhammadiyah 2 Wates</h3>
                        <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Nov 2023 - Jan 2024 | Teacher Assistant ISS-MBKM</p>
                        <p>Membuat modul ajar pengelasan dan CAD 3D. Sukses menciptakan proyek inovasi <em>Standing Las Universal All Position</em>.</p>
                    </div>
                </div>
            </div>
            <div class="split-right" style="padding-top: 5rem;">
                <div class="article-grid" style="grid-template-columns: 1fr;">
                    <div class="card-article">
                        <h3>👨‍🏫 SMK Muhammadiyah 1 Bantul</h3>
                        <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Aug 2023 - Sep 2023 | Trainer & Narasumber</p>
                        <p>Trainer & Narasumber workshop 3D Printing untuk mold making Pengecoran Logam.</p>
                    </div>
                    <div class="card-article">
                        <h3>🏢 Nusantara Sakti Group</h3>
                        <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Mar 2021 - Sep 2021 | Staff Marketing Sales</p>
                        <p>Memonitoring dan melakukan pengecekan data. Melakukan kegiatan pemasaran melalui digital marketing.</p>
                    </div>
                    <div class="card-article">
                        <h3>⚙️ PT YPTI</h3>
                        <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Aug 2020 - Mar 2021 | Magang Operator</p>
                        <p>Operator Machining Mesin Hartford 3210 dan Mesin EDM. Terlibat dalam Project Jig & Fixture Mobil Toyota dan Mold Making.</p>
                    </div>
                    <div class="card-article">
                        <h3>🏫 BLPT Yogyakarta</h3>
                        <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Sep 2019 | Diklat</p>
                        <p>Mendapatkan keahlian khusus dalam Pattern Making.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# 3. Pendidikan
pendidikan_pattern = re.compile(r'<section id="pendidikan".*?</section>', re.DOTALL)
new_pendidikan = """
    <section id="pendidikan" class="one-screen" style="max-width: 100%; padding: 4rem 2rem; background: white;">
        <div class="split-layout align-start">
            <div class="split-left">
                <h2 style="margin-bottom: 2rem; color: var(--kemendikbud-blue);"><span style="font-size: 2rem;">🎓</span> Riwayat Pendidikan</h2>
                
                <div class="card-article" style="border-left: 4px solid var(--kemendikbud-cyan); background: var(--bg-light-gray);">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 0.5rem;">
                        <img src="logo-smk.png" alt="Logo SMK" style="height: 50px; width: auto; object-fit: contain;">
                        <h3 style="margin: 0;">SMK N 1 Seyegan</h3>
                    </div>
                    <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Aug 2017 - Jun 2021 | Teknik Fabrikasi Logam dan Manufaktur</p>
                    <p>Lulusan SMK satu satunya siswa yang berhasil diterima di Perguruan Tinggi Negeri (PTN) melalui jalur SNMPTN 2021.</p>
                </div>
                
                <div style="background: white; border-radius: 12px; padding: 2rem; border: 1px dashed var(--border-color); text-align: center; margin-top: 1rem;">
                    <span style="font-size: 3rem; color: var(--kemendikbud-cyan); opacity: 0.5;">📈</span>
                    <p style="margin-top: 1rem; color: var(--text-light); font-style: italic;">Pendidikan adalah tiket ke masa depan. Hari esok dimiliki oleh orang-orang yang mempersiapkan dirinya sejak hari ini.</p>
                </div>
            </div>
            
            <div class="split-right">
                <div class="card-article" style="border-left: 4px solid var(--kemendikbud-cyan); background: var(--bg-light-gray);">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 0.5rem;">
                        <img src="logo-uny.png" alt="Logo UNY" style="height: 50px; width: auto; object-fit: contain;">
                        <h3 style="margin: 0;">Universitas Negeri Yogyakarta</h3>
                    </div>
                    <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Sep 2021 - Apr 2025 | S1 Pendidikan Teknik Mesin</p>
                    <p>Lulusan Terbaik Fakultas Teknik dengan IPK 3.87/4.00 (Masa studi 3.5 Tahun). Aktif dalam berbagai organisasi dan kepanitiaan.<br><strong style="color: var(--text-dark);">Judul Skripsi:</strong> <em>PENGEMBANGAN MODUL PELATIHAN BERBASIS KOMPETENSI MENGGAMBAR CAD 3D PADA KOMPETENSI MEMBUAT MODEL 3D DENGAN SISTEM CAD DI PT STECHOQ ROBOTIKA INDONESIA</em></p>
                </div>
                
                <div class="card-article" style="border-left: 4px solid var(--kemendikbud-cyan); background: var(--bg-light-gray);">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 0.5rem;">
                        <img src="logo-ust.png" alt="Logo UST" style="height: 50px; width: auto; object-fit: contain;">
                        <h3 style="margin: 0;">Universitas Sarjanawiyata Tamansiswa</h3>
                    </div>
                    <p style="font-size: 0.85rem; color: var(--kemendikbud-blue); font-weight: bold; margin-bottom: 0.5rem;">Jan 2026 - Sekarang | PPG Prajabatan 2026</p>
                    <p>Sedang menempuh program Pendidikan Profesi Guru (PPG) Prajabatan.</p>
                </div>
            </div>
        </div>
    </section>
"""

html = pengalaman_pattern.sub(new_pengalaman, html)
html = pendidikan_pattern.sub(new_pendidikan, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Pengalaman and Pendidikan")
