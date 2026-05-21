import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_penilaian_model = """
    <section id="penilaian" class="two-col-layout one-screen" style="max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;">
        <div class="penilaian-left animate-on-scroll">
            <h2 class="section-title"><i class="fa-solid fa-clipboard-check"></i> Lampiran Penilaian</h2>
            <div class="article-grid" style="grid-template-columns: 1fr;">
                <div class="card-article" onclick="switchPenilaian('lamp7')" style="cursor: pointer; border-left: 4px solid var(--kemendikbud-blue);">
                    <h3>📄 Lampiran 7: Penilaian Perangkat Pembelajaran</h3>
                    <p>Instrumen penilaian kelengkapan, kesesuaian tujuan, dan kualitas media ajar.</p>
                </div>
                <div class="card-article" onclick="switchPenilaian('lamp8')" style="cursor: pointer; border-left: 4px solid transparent;">
                    <h3>👨‍🏫 Lampiran 8: Penilaian Praktik Mengajar</h3>
                    <p>Instrumen penilaian performa kelas dan observasi Guru Pamong.</p>
                </div>
            </div>
        </div>
        
        <div class="penilaian-right animate-on-scroll">
            <div id="penilaian-preview" class="pdf-preview-box" style="border: 2px solid var(--border-color); border-radius: 12px; overflow: hidden; height: 100%; min-height: 400px; background: white;">
                <h4 id="penilaian-title" style="background-color: var(--kemendikbud-blue); color: white; padding: 1rem; margin: 0; font-size: 1rem; display: flex; justify-content: space-between;">
                    <span>Preview Lampiran 7 (PDF)</span>
                    <span style="font-size: 0.8rem; background-color: #f59e0b; color: white; padding: 0.2rem 0.6rem; border-radius: 4px;">File Menyusul</span>
                </h4>
                <div style="padding: 2rem; text-align: center; color: var(--text-light); display: flex; flex-direction: column; align-items: center; justify-content: center; height: 350px;">
                    <i class="fa-solid fa-file-pdf" style="font-size: 4rem; color: #cbd5e1; margin-bottom: 1rem;"></i>
                    <p>Dokumen PDF belum tersedia.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="model-guru" class="two-col-layout one-screen" style="background-color: var(--bg-light-gray); max-width: 1200px; margin: 0 auto; padding: 6rem 2rem;">
        <div class="model-guru-left animate-on-scroll" style="display: flex; flex-direction: column; justify-content: center;">
            <h2 class="section-title"><i class="fa-solid fa-user-tie"></i> Visi Guru Profesional</h2>
            <div class="graphic-element" style="text-align: center; margin-top: 2rem;">
                <i class="fa-solid fa-gears" style="font-size: 8rem; color: var(--kemendikbud-blue); opacity: 0.2;"></i>
                <h3 style="margin-top: 1rem; color: var(--kemendikbud-blue); font-family: 'Rajdhani', sans-serif;">Pendidikan Vokasi<br>Berkarakter Industri</h3>
            </div>
        </div>
        
        <div class="model-guru-right animate-on-scroll">
            <div class="article-grid" style="grid-template-columns: 1fr; gap: 1.5rem;">
                <div class="card-article industrial-card">
                    <h3 style="color: var(--primary-dark);"><i class="fa-solid fa-eye" style="color: var(--accent-amber);"></i> Visi & Misi</h3>
                    <p><strong>Visi:</strong> Pendidik visioner mencetak lulusan terampil berkarakter kuat.</p>
                    <p><strong>Misi:</strong> Menghadirkan suasana belajar inklusif, inovatif, memotivasi pembelajar sepanjang hayat.</p>
                </div>
                
                <div class="card-article industrial-card">
                    <h3 style="color: var(--primary-dark);"><i class="fa-solid fa-bullseye" style="color: var(--accent-amber);"></i> Kompetensi Target</h3>
                    <p>Mengasah <strong>Pedagogik</strong> (metode baru), <strong>Profesional</strong> (standar industri), dan <strong>Sosial Kepribadian</strong> (teladan moral).</p>
                </div>
                
                <div class="card-article industrial-card">
                    <h3 style="color: var(--primary-dark);"><i class="fa-solid fa-star" style="color: var(--accent-amber);"></i> Karakter Utama</h3>
                    <ul style="padding-left: 1.5rem; margin-top: 0.5rem;">
                        <li><strong>Disiplin:</strong> Etos kerja K3 industri.</li>
                        <li><strong>Reflektif:</strong> Evaluasi berkelanjutan.</li>
                        <li><strong>Inovatif:</strong> Adaptasi teknologi manufaktur.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""

pattern = re.compile(r'<section id="penilaian".*?(?=\s*</div> <!-- END PORTFOLIO 1 -->)', re.DOTALL)
html = pattern.sub(new_penilaian_model, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Penilaian & Model Guru sections rebuilt.")
