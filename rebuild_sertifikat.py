import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_sertifikat = """
    <section id="sertifikat" class="two-col-layout one-screen" style="max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;">
        <div class="sertifikat-left animate-on-scroll">
            <h2 class="section-title"><i class="fa-solid fa-certificate"></i> Daftar Sertifikat</h2>
            <div class="cert-list-container">
                <ul class="cert-list">
                    <li class="active"><i class="fa-solid fa-check-circle"></i> MSIB Batch 6 Kemendikbudristek</li>
                    <li><i class="fa-solid fa-check-circle"></i> MSIB Batch 7 Kemendikbudristek</li>
                    <li><i class="fa-solid fa-check-circle"></i> Asisten Juri Lomba dan Sertifikasi CAD</li>
                    <li><i class="fa-solid fa-check-circle"></i> Proyek Kemanusiaan</li>
                    <li><i class="fa-solid fa-check-circle"></i> MBKM Inovatif Mandiri Kampus Merdeka, LPDP</li>
                    <li><i class="fa-solid fa-check-circle"></i> DIKLAT BLPT Pemesinan Konvensional Pattern Making</li>
                    <li><i class="fa-solid fa-check-circle"></i> Pengurus Himpunan Mesin</li>
                    <li><i class="fa-solid fa-check-circle"></i> Magang PT. YPTI</li>
                    <li><i class="fa-solid fa-check-circle"></i> Workshop Car Design Using Solidworks</li>
                    <li><i class="fa-solid fa-check-circle"></i> Narasumber & Trainer Additive Manufacturing</li>
                    <li><i class="fa-solid fa-check-circle"></i> TOEFL</li>
                    <li><i class="fa-solid fa-check-circle"></i> CNC Training</li>
                    <li><i class="fa-solid fa-check-circle"></i> CAD Training</li>
                    <li><i class="fa-solid fa-check-circle"></i> BNSP Drafter CAD 3D</li>
                    <li><i class="fa-solid fa-check-circle"></i> HKI Modul Fusion 360</li>
                    <li><i class="fa-solid fa-check-circle"></i> DIKLAT Wawasan Kebhinekaan Global</li>
                    <li><i class="fa-solid fa-check-circle"></i> DILAT Anti Bullying</li>
                    <li><i class="fa-solid fa-check-circle"></i> Lulusan Terbaik Prodi</li>
                </ul>
            </div>
        </div>

        <div class="sertifikat-right animate-on-scroll">
            <div class="cert-preview-card">
                <div class="cert-preview-header">
                    <h3><i class="fa-solid fa-file-contract"></i> Bukti Fisik Sertifikat</h3>
                    <p>Semua bukti fisik (18 Dokumen) telah disatukan dalam satu portofolio digital.</p>
                </div>
                <div class="cert-preview-body" style="text-align: center; padding: 3rem 1rem;">
                    <i class="fa-brands fa-google-drive" style="font-size: 5rem; color: #1FA463; margin-bottom: 1.5rem;"></i>
                    <h4>Arsip Digital Lengkap</h4>
                    <p style="margin-bottom: 2rem;">Akses langsung ke Google Drive untuk melihat dokumen fisik resolusi tinggi.</p>
                    <a href="https://drive.google.com/file/d/17JOtNpFxW6cDOFSxvYvkgsQGL2jh9Ar-/view?usp=sharing" target="_blank" class="btn-industrial">
                        <i class="fa-solid fa-arrow-up-right-from-square"></i> Lihat Bukti Fisik
                    </a>
                </div>
            </div>
        </div>
    </section>

    <section id="galeri" class="two-col-layout one-screen" style="background-color: var(--bg-light-gray); max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;">
        <div class="galeri-left animate-on-scroll">
            <h2 class="section-title"><i class="fa-solid fa-camera"></i> Dokumentasi Kegiatan</h2>
            <div class="masonry-grid">
                <!-- Generating 20 image thumbnails -->
                """ + "".join([f'<div class="masonry-item" onclick="showLightbox({i})"><img src="assets/dokumentasi/{i}.jpg" alt="Dokumentasi {i}" onerror="this.parentElement.remove();"></div>' for i in range(1, 21)]) + """
            </div>
        </div>
        <div class="galeri-right animate-on-scroll" style="display: flex; align-items: center; justify-content: center;">
            <div class="lightbox-preview-card">
                <img id="lightbox-main-img" src="assets/dokumentasi/1.jpg" alt="Preview" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 2px solid var(--kemendikbud-blue);">
                <div class="lightbox-caption">
                    <h4>Dokumentasi Pilihan</h4>
                    <p>Klik salah satu thumbnail di sebelah kiri untuk melihat lebih jelas.</p>
                </div>
            </div>
        </div>
    </section>
"""

pattern = re.compile(r'<section id="sertifikat".*?(?=\s*<section id="artefak")', re.DOTALL)
html = pattern.sub(new_sertifikat, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Sertifikat & Galeri sections rebuilt.")
