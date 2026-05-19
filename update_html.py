import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Remove <section id="karya-dokumentasi"> and its closing tag, but keep its contents.
# The section starts with <section id="karya-dokumentasi" ...> and ends with </section>
# It has a heading <h2>Karya & Dokumentasinya</h2> etc. We will remove the heading and just integrate it into #artefak.

# Let's find the exact bounds.
# It starts around:
#     <!-- 3.1 Karya & Dokumentasi (Filtered Gallery) -->
#     <section id="karya-dokumentasi" style="text-align: justify; max-width: 1160px; margin: 0 auto 4rem auto; padding: 0 2rem;">
#         <h2>Karya & Dokumentasinya</h2>
#         <p style="color: var(--text-light); margin-bottom: 2rem;">Koleksi perangkat pembelajaran, media, dan dokumentasi kegiatan profesional</p>

# We can replace all of this with the start of our TP wrapper.
# Wait, the search container comes after this.

search_pattern = r'<!-- 3\.1 Karya & Dokumentasi \(Filtered Gallery\) -->.*?<div class="search-container"'
# Replace it with a wrapper for TP
replace_start = """
        <!-- Galeri TP -->
        <div class="gallery-section" id="gallery-tp" style="margin-top: 3rem; padding-top: 2rem; border-top: 2px dashed var(--border-color);">
            <h3 style="color: var(--kemendikbud-blue); text-align: center; margin-bottom: 2rem; font-size: 1.8rem;">📂 Koleksi Artefak: Teknik Pemesinan (TP)</h3>
            <div class="search-container" """
            
html = re.sub(search_pattern, replace_start.strip('\n'), html, flags=re.DOTALL)

# Also we need to change id="searchInput" to class="search-input-gallery" so we can have multiple
html = html.replace('id="searchInput"', 'class="search-input search-input-gallery"')
# And id="searchBtn" to class="search-icon search-btn"
html = html.replace('id="searchBtn"', 'class="search-icon search-btn"')
# Remove the old id="portfolio-gallery" because we'll use a class
html = html.replace('id="portfolio-gallery"', 'class="doc-grid gallery-grid"')

# Now we need to find the end of the doc-grid, close the gallery-section, and then append the new gallery-tflm.
# Since doc-grid contains many doc-cards, we'll find the end of the section.
# The section ends with:
#         </div>
#     </section>
# 
#     <!-- 4. Penutup / Refleksi -->

end_pattern = r'(        </div>\n    </section>\n\n    <!-- 4\. Penutup / Refleksi)'
# We will insert the closing of gallery-tp, and the entire new gallery-tflm block before the end.

tflm_block = """
        </div> <!-- End of gallery-tp -->

        <!-- Galeri TFLM -->
        <div class="gallery-section" id="gallery-tflm" style="margin-top: 4rem; padding-top: 3rem; border-top: 2px dashed var(--border-color);">
            <h3 style="color: var(--kemendikbud-blue); text-align: center; margin-bottom: 2rem; font-size: 1.8rem;">📂 Koleksi Artefak: Teknik Fabrikasi Logam dan Manufaktur (TFLM)</h3>
            
            <div class="search-container" style="margin: 0 auto 2rem auto; max-width: 800px; position: relative;">
                <input type="text" class="search-input search-input-gallery" placeholder="Cari dokumen, RPP, Media, LKS..." style="width: 100%; padding: 1rem 1.5rem; border-radius: 50px; border: 2px solid var(--border-color); font-size: 1rem; outline: none; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: border-color 0.3s;">
                <div class="search-icon search-btn" style="position: absolute; right: 20px; top: 50%; transform: translateY(-50%); cursor: pointer; font-size: 1.2rem;">🔍</div>
            </div>

            <div class="filter-container">
                <button class="filter-btn active" data-filter="all">Semua</button>
                <button class="filter-btn" data-filter="rpp">RPP</button>
                <button class="filter-btn" data-filter="media">Media</button>
                <button class="filter-btn" data-filter="lks">LKS</button>
                <button class="filter-btn" data-filter="asesmen">Asesmen</button>
                <button class="filter-btn" data-filter="bahan-ajar">Bahan Ajar</button>
                <button class="filter-btn" data-filter="hasil-kerja">Hasil Kerja Siswa</button>
                <button class="filter-btn" data-filter="video">Video Mengajar</button>
                <button class="filter-btn" data-filter="penilaian">Penilaian GP & DPL</button>
            </div>

            <div class="doc-grid gallery-grid">
                <!-- Kartu Artefak TFLM akan ditambahkan di sini nantinya -->
                <p style="text-align: center; grid-column: 1 / -1; color: var(--text-light); padding: 3rem 0; font-style: italic;">
                    Belum ada artefak yang diunggah untuk jurusan ini.
                </p>
            </div>
        </div>
    </section>

    <!-- 4. Penutup / Refleksi"""

html = re.sub(end_pattern, tflm_block.lstrip('\n'), html)

with open('index.html', 'w') as f:
    f.write(html)

print("Done")
