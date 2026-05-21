import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Restore Galeri and apply split layout
new_galeri = """
    <!-- Galeri / Dokumentasi -->
    <section id="galeri" class="one-screen" style="background-color: var(--bg-light-gray); max-width: 100%; padding: 4rem 2rem;">
        <div class="split-layout align-start">
            <div class="split-left">
                <h2 style="margin-bottom: 1rem; color: var(--kemendikbud-blue);"><span style="font-size: 2rem;">📸</span> Dokumentasi Kegiatan</h2>
                <p style="color: var(--text-dark); line-height: 1.6;">Berikut adalah rekam jejak kegiatan pengajaran, pelatihan, dan pengembangan profesional. Semua galeri disusun secara dinamis.</p>
                <div style="background: white; padding: 1.5rem; border-radius: 12px; border-left: 5px solid var(--kemendikbud-blue); box-shadow: 0 4px 6px rgba(0,0,0,0.03);">
                    <p style="margin: 0; color: var(--text-dark); font-style: italic;">Arahkan kursor Anda ke setiap gambar di samping untuk melihat versi penuh dari dokumentasi.</p>
                </div>
            </div>
            
            <div class="split-right">
                <div class="accordion-gallery">
                    """ + "".join([f'<div class="accordion-item"><img src="assets/dokumentasi/{i}.jpg" alt="Dokumentasi {i}" onerror="this.parentElement.remove();"></div>' for i in range(1, 21)]) + """
                </div>
            </div>
        </div>
    </section>
"""
# Insert galeri right after sertifikat
html = html.replace('</section>\n\n    <!-- 3. Analisis Artefak Produk Pembelajaran -->', f'</section>\n\n{new_galeri}\n\n    <!-- 3. Analisis Artefak Produk Pembelajaran -->')


# Penilaian
penilaian_pattern = re.compile(r'<section id="penilaian".*?</section>', re.DOTALL)
new_penilaian = """
    <section id="penilaian" class="one-screen" style="background-color: var(--bg-light-gray); max-width: 100%; padding: 4rem 2rem;">
        <div class="split-layout align-start">
            <div class="split-left">
                <h2 style="margin-bottom: 2rem; color: var(--kemendikbud-blue);"><span style="font-size: 2rem;">📝</span> Penilaian Perangkat</h2>
                <div class="card-article" style="height: 100%;">
                    <h3>📄 Lampiran 7: Penilaian Perangkat Pembelajaran</h3>
                    <p>Instrumen penilaian ini mencakup evaluasi kelengkapan, kesesuaian tujuan, dan kualitas media ajar yang telah disusun.</p>
                    <ul style="margin-top: 1rem; padding-left: 1.2rem; color: var(--text-light); font-size: 0.9rem;">
                        <li><strong>Siklus 1:</strong> Baik - Perbaikan pada instrumen rubrik.</li>
                        <li><strong>Siklus 2:</strong> Sangat Baik - Indikator tercapai.</li>
                        <li><strong>Siklus 3:</strong> Sangat Baik - Integrasi TPACK optimal.</li>
                    </ul>
                    <div style="margin-top: 1.5rem; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;">
                        <h4 style="background-color: #f5f5f5; padding: 0.75rem 1rem; margin: 0; font-size: 0.9rem; border-bottom: 1px solid #e0e0e0; color: #333; display: flex; justify-content: space-between; align-items: center;">
                            <span>Preview Penilaian (PDF)</span>
                            <span style="font-size: 0.8rem; background-color: #ffe0b2; color: #e65100; padding: 0.2rem 0.5rem; border-radius: 4px;">File Menyusul</span>
                        </h4>
                        <iframe src="" style="width: 100%; height: 300px; border: none; background-color: #fafafa;" title="Preview Lampiran 7"></iframe>
                    </div>
                </div>
            </div>
            
            <div class="split-right">
                <h2 style="margin-bottom: 2rem; color: var(--kemendikbud-blue);"><span style="font-size: 2rem;">👨‍🏫</span> Penilaian Praktik</h2>
                <div class="card-article" style="height: 100%;">
                    <h3>👨‍🏫 Lampiran 8: Penilaian Praktik Mengajar</h3>
                    <p>Instrumen ini menilai performa di dalam kelas, penguasaan kelas, hingga evaluasi penutup dari observasi Guru Pamong.</p>
                    <ul style="margin-top: 1rem; padding-left: 1.2rem; color: var(--text-light); font-size: 0.9rem;">
                        <li><strong>Siklus 1:</strong> Baik - Manajemen waktu ditingkatkan.</li>
                        <li><strong>Siklus 2:</strong> Sangat Baik - Interaksi kelas efektif.</li>
                        <li><strong>Siklus 3:</strong> Sangat Baik - Penguasaan materi sempurna.</li>
                    </ul>
                    <div style="margin-top: 1.5rem; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden;">
                        <h4 style="background-color: #f5f5f5; padding: 0.75rem 1rem; margin: 0; font-size: 0.9rem; border-bottom: 1px solid #e0e0e0; color: #333; display: flex; justify-content: space-between; align-items: center;">
                            <span>Preview Penilaian (PDF)</span>
                            <span style="font-size: 0.8rem; background-color: #ffe0b2; color: #e65100; padding: 0.2rem 0.5rem; border-radius: 4px;">File Menyusul</span>
                        </h4>
                        <iframe src="" style="width: 100%; height: 300px; border: none; background-color: #fafafa;" title="Preview Lampiran 8"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Model Guru
model_guru_pattern = re.compile(r'<section id="model-guru".*?</section>', re.DOTALL)
new_model_guru = """
    <section id="model-guru" class="one-screen" style="max-width: 100%; padding: 4rem 2rem;">
        <div class="split-layout align-start">
            <div class="split-left">
                <h2 style="margin-bottom: 2rem; color: var(--kemendikbud-blue);"><span style="font-size: 2rem;">🌟</span> Model Guru Profesional</h2>
                <div class="card-article" style="background: white;">
                    <h3 style="color: var(--text-black); font-size: 1.5rem; margin-bottom: 1rem;"><span style="font-size: 1.5rem;">🔭</span> Visi & Misi</h3>
                    <p><strong>Visi:</strong> Menjadi pendidik profesional yang visioner, mencetak lulusan terampil dengan karakter yang kuat.</p>
                    <p style="margin-top: 1rem;"><strong>Misi:</strong> Menghadirkan suasana belajar yang inklusif, inovatif, dan memotivasi siswa untuk menjadi pembelajar sepanjang hayat.</p>
                </div>
                <div style="text-align: center; margin-top: 2rem;">
                    <span style="font-size: 5rem; opacity: 0.1;">👨‍🏫</span>
                </div>
            </div>
            
            <div class="split-right">
                <h2 style="margin-bottom: 2rem; color: transparent; user-select: none;">.</h2>
                <div class="card-article" style="background: white;">
                    <h3 style="color: var(--text-black); font-size: 1.5rem; margin-bottom: 1rem;"><span style="font-size: 1.5rem;">🎯</span> Kompetensi Target</h3>
                    <p>Terus mengasah <strong>Kompetensi Pedagogik</strong> (model belajar baru), <strong>Profesional</strong> (perkembangan industri), serta <strong>Sosial dan Kepribadian</strong> (teladan sekolah).</p>
                </div>
                
                <div class="card-article" style="background: white;">
                    <h3 style="color: var(--text-black); font-size: 1.5rem; margin-bottom: 1rem;"><span style="font-size: 1.5rem;">💎</span> Karakter Utama</h3>
                    <ul style="padding-left: 1.2rem; margin-top: 0.5rem; color: var(--text-dark); line-height: 1.6;">
                        <li><strong>Disiplin:</strong> Contoh nyata etos kerja.</li>
                        <li><strong>Reflektif:</strong> Evaluasi pengalaman mengajar secara konsisten.</li>
                        <li><strong>Inovatif:</strong> Berani mencoba metode teknologi baru dalam proses pembelajaran.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""

html = penilaian_pattern.sub(new_penilaian, html)
html = model_guru_pattern.sub(new_model_guru, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Penilaian, Model Guru, and restored Galeri")
