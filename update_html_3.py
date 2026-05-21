import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Keahlian
keahlian_pattern = re.compile(r'<section id="keahlian".*?</section>', re.DOTALL)
new_keahlian = """
    <section id="keahlian" class="one-screen" style="background-color: var(--bg-light-gray); max-width: 100%; padding: 4rem 2rem;">
        <div class="split-layout align-start">
            <div class="split-left">
                <h2 style="margin-bottom: 1rem; color: var(--kemendikbud-blue);"><span style="font-size: 2rem;">🔧</span> Kompetensi Teknis</h2>
                <div class="skills-container" style="justify-content: flex-start;">
                    <span class="skill-badge">CADD</span>
                    <span class="skill-badge">Machining</span>
                    <span class="skill-badge">Programming CNC</span>
                    <span class="skill-badge">Fabrikasi</span>
                    <span class="skill-badge">Architecture Design</span>
                    <span class="skill-badge">Civil Engineering</span>
                </div>
            </div>
            <div class="split-right">
                <h2 style="margin-bottom: 1rem; color: var(--kemendikbud-blue);"><span style="font-size: 2rem;">🧠</span> Kompetensi Pedagogik</h2>
                <div class="skills-container" style="justify-content: flex-start;">
                    <span class="skill-badge" style="background: var(--kemendikbud-cyan); color: white;">Pendidik</span>
                    <span class="skill-badge" style="background: var(--kemendikbud-cyan); color: white;">Education System</span>
                    <span class="skill-badge" style="background: var(--kemendikbud-cyan); color: white;">Project Management</span>
                </div>
            </div>
        </div>
    </section>
"""

# Sertifikat
sertifikat_pattern = re.compile(r'<section id="sertifikat".*?</section>', re.DOTALL)
new_sertifikat = """
    <section id="sertifikat" class="one-screen" style="max-width: 100%; padding: 4rem 2rem;">
        <div class="split-layout align-start">
            <div class="split-left">
                <h2 style="margin-bottom: 2rem; color: var(--kemendikbud-blue);"><span style="font-size: 2rem;">📜</span> Daftar Sertifikat</h2>
                <div style="display: grid; grid-template-columns: 1fr; gap: 1rem; max-height: 600px; overflow-y: auto; padding-right: 10px;">
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">1</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">MSIB Batch 6 Kemendikbudristek</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">2</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">MSIB Batch 7 Kemendikbudristek</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">3</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">Asisten Juri Lomba dan Sertifikasi CAD</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">4</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">Proyek Kemanusiaan</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">5</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">MBKM Inovatif Mandiri Kampus Merdeka, LPDP</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">6</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">DIKLAT BLPT Pemesinan Konvensional Pattern Making</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">7</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">Pengurus Himpunan Mesin</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">8</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">Magang PT. YPTI</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">9</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">Workshop Car Design Using Solidworks</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">10</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">Narasumber & Trainer Additive Manufacturing</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">11</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">TOEFL</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">12</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">CNC Training</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">13</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">CAD Training</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">14</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">BNSP Drafter CAD 3D</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">15</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">HKI Modul Fusion 360</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">16</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">DIKLAT Wawasan Kebhinekaan Global</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">17</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">DILAT Anti Bullying</span></div>
                    <div style="background: white; padding: 1rem; border-radius: 12px; border: 1px solid var(--border-color); display: flex; align-items: center; gap: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.03);"><span style="background: var(--kemendikbud-cyan); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 600; flex-shrink: 0; font-size: 0.9rem;">18</span><span style="font-weight: 500; font-size: 0.9rem; color: var(--text-dark);">Lulusan Terbaik Prodi</span></div>
                </div>
            </div>
            
            <div class="split-right" style="justify-content: center; align-items: center; text-align: center; height: 100%;">
                <div style="background: var(--bg-light-gray); padding: 3rem 2rem; border-radius: 20px; border: 1px dashed var(--border-color); box-shadow: 0 10px 30px rgba(0,0,0,0.05); width: 100%;">
                    <div style="font-size: 4rem; color: var(--kemendikbud-blue); margin-bottom: 1rem;">📁</div>
                    <h3 style="margin-top: 0;">Arsip Digital Lengkap</h3>
                    <p style="color: var(--text-light); margin-bottom: 2rem;">Semua bukti fisik dari 18 sertifikat di atas telah disatukan dalam satu dokumen digital beresolusi tinggi.</p>
                    
                    <a href="https://drive.google.com/file/d/17JOtNpFxW6cDOFSxvYvkgsQGL2jh9Ar-/view?usp=sharing" target="_blank" class="doc-btn" style="padding: 1rem 2rem; font-size: 1.1rem; border-radius: 50px; background-color: var(--kemendikbud-blue); color: white; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; text-decoration: none; font-weight: 600; box-shadow: 0 4px 15px rgba(0, 89, 178, 0.3); transition: transform 0.2s; width: 100%;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                        <span style="font-size: 1.3rem;">📄</span> Lihat Bukti Fisik
                    </a>
                </div>
            </div>
        </div>
    </section>
"""

html = keahlian_pattern.sub(new_keahlian, html)
html = sertifikat_pattern.sub(new_sertifikat, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Keahlian and Sertifikat")
