import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Siklus 1 - Manufaktur
card_siklus1 = """<div class="doc-card gallery-card-item" data-category="hasil-kerja">
<div class="doc-card-thumb">
<span class="doc-badge">Hasil Kerja</span>
<img alt="Hasil Kerja Manufaktur" class="doc-thumb-img" src="assets/hasil-kerja/manufaktur/cover.jpg" onerror="this.src='https://via.placeholder.com/600x400?text=Galeri+Foto'"/>
<a class="doc-overlay-btn" href="hasil-kerja-manufaktur.html">Buka Galeri</a>
</div>
<div class="doc-card-content">
<h4>Galeri Hasil Kerja: Manufaktur</h4>
<p>Kumpulan foto dan dokumentasi hasil praktik peserta didik.</p>
<details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
<summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
<div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
<div><strong>Konteks:</strong> <br/><span style="color: var(--text-light);">Galeri dokumentasi pengerjaan benda kerja oleh siswa.</span></div>
<div><strong>Tujuan:</strong> <br/><span style="color: var(--text-light);">Menunjukkan hasil nyata penguasaan kompetensi dasar.</span></div>
</div>
</details>
<a class="doc-btn" href="hasil-kerja-manufaktur.html">Buka Galeri Foto</a>
</div>
</div>
"""

# Siklus 2 - Mekanik
card_siklus2 = """<div class="doc-card gallery-card-item" data-category="hasil-kerja">
<div class="doc-card-thumb">
<span class="doc-badge">Hasil Kerja</span>
<img alt="Hasil Kerja Mekanik" class="doc-thumb-img" src="assets/hasil-kerja/mekanik/cover.jpg" onerror="this.src='https://via.placeholder.com/600x400?text=Galeri+Foto'"/>
<a class="doc-overlay-btn" href="hasil-kerja-mekanik.html">Buka Galeri</a>
</div>
<div class="doc-card-content">
<h4>Galeri Hasil Kerja: Dasar Sistem Mekanik</h4>
<p>Kumpulan foto dan dokumentasi hasil perhitungan serta eksperimen siswa.</p>
<details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
<summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
<div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
<div><strong>Konteks:</strong> <br/><span style="color: var(--text-light);">Galeri dokumentasi observasi sistem mekanik.</span></div>
<div><strong>Tujuan:</strong> <br/><span style="color: var(--text-light);">Menunjukkan pemahaman logika transmisi gaya oleh siswa.</span></div>
</div>
</details>
<a class="doc-btn" href="hasil-kerja-mekanik.html">Buka Galeri Foto</a>
</div>
</div>
"""

# Siklus 3 - SMAW
card_siklus3 = """<div class="doc-card gallery-card-item" data-category="hasil-kerja">
<div class="doc-card-thumb">
<span class="doc-badge">Hasil Kerja</span>
<img alt="Hasil Kerja SMAW" class="doc-thumb-img" src="assets/hasil-kerja/tflm-smaw/cover.jpg" onerror="this.src='https://via.placeholder.com/600x400?text=Galeri+Foto'"/>
<a class="doc-overlay-btn" href="hasil-kerja-tflm-smaw.html">Buka Galeri</a>
</div>
<div class="doc-card-content">
<h4>Galeri Hasil Kerja: Pengelasan SMAW</h4>
<p>Kumpulan foto dan dokumentasi hasil rigi-rigi las siswa.</p>
<details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
<summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
<div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
<div><strong>Konteks:</strong> <br/><span style="color: var(--text-light);">Galeri hasil praktik pengelasan SMAW.</span></div>
<div><strong>Tujuan:</strong> <br/><span style="color: var(--text-light);">Menunjukkan kemajuan skill pengelasan siswa dari waktu ke waktu.</span></div>
</div>
</details>
<a class="doc-btn" href="hasil-kerja-tflm-smaw.html">Buka Galeri Foto</a>
</div>
</div>
"""

# Insert Siklus 1
if 'alt="Bahan Ajar 1"' in content and '<h4>Galeri Hasil Kerja: Manufaktur</h4>' not in content:
    # Find the end of doc-grid in siklus-1
    pattern1 = r'(<div class="doc-card gallery-card-item" data-category="bahan-ajar">.*?<img alt="Bahan Ajar 1".*?Lihat Dokumen</a>\n</div>\n</div>\n)(</div>\n</div>\n</div>\n<div class="tab-content" id="siklus-2">)'
    content = re.sub(pattern1, r'\1' + card_siklus1 + r'\2', content, flags=re.DOTALL)

# Insert Siklus 2
if 'alt="Bahan Ajar 2"' in content and '<h4>Galeri Hasil Kerja: Dasar Sistem Mekanik</h4>' not in content:
    pattern2 = r'(<div class="doc-card gallery-card-item" data-category="bahan-ajar">.*?<img alt="Bahan Ajar 2".*?Lihat Dokumen</a>\n</div>\n</div>\n)(</div>\n</div>\n</div>\n<div class="tab-content" id="siklus-3">)'
    content = re.sub(pattern2, r'\1' + card_siklus2 + r'\2', content, flags=re.DOTALL)

# Insert Siklus 3
if 'alt="LKS 5"' in content and '<h4>Galeri Hasil Kerja: Pengelasan SMAW</h4>' not in content:
    pattern3 = r'(<div class="doc-card gallery-card-item" data-category="lks">.*?<img alt="LKS 5".*?Lihat Dokumen</a>\n</div>\n</div>\n)(</div>\n</div>\n</div>\n</section>)'
    content = re.sub(pattern3, r'\1' + card_siklus3 + r'\2', content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done inserting Hasil Kerja cards to index.html")
