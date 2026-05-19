import re

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

start_marker = '<!-- 3. Analisis Artefak Produk Pembelajaran -->'
end_marker = '<!-- Analisis Produk Pembelajaran -->'

start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker)

artefak_html = html_content[start_idx:end_idx]

# Extract cards
cards = []
parts = artefak_html.split('<div class="doc-card gallery-card-item"')
# parts[0] is the content before the first card
for p in parts[1:]:
    card = '<div class="doc-card gallery-card-item"' + p
    # Now we need to split on the next card or the end of the container
    # Since we split on the start of the card, `p` contains exactly one card, followed by any trailing spaces or closing tags of the parent container before the next card or end.
    # Actually, the last `p` will contain the rest of the gallery-section and gallery-tflm section.
    # Let's clean up the end of each `p`. We can find the last `</div>` of the card.
    # A card looks like:
    # <div class="doc-card ...> ... <a ...>Lihat Dokumen</a>\n                </div>\n            </div>
    # Let's just find the closing </div></div> of the card.
    # A safe way is to find the index of `<div class="gallery-section"` if it's the last part.
    cards.append(card)

# Let's refine the extraction.
# The card always ends with `</a>\n                </div>\n            </div>` or similar.
clean_cards = []
for c in cards:
    # Find the end of the card
    # Usually it's `</div>\n            </div>`
    # Let's just balance divs.
    div_count = 0
    i = 0
    while i < len(c):
        if c.startswith('<div', i):
            div_count += 1
        elif c.startswith('</div', i):
            div_count -= 1
            if div_count == 0:
                # End of this card's main div
                clean_cards.append(c[:i+6])
                break
        i += 1

siklus1_cards = []
siklus2_cards = []
siklus3_cards = []

for c in clean_cards:
    text = c.lower()
    if 'mekanik' in text:
        siklus2_cards.append(c)
    elif 'smaw' in text or 'pengelasan' in text or 'elektroda' in text or 'tflm' in text or 'hasil las' in text or 'posisi pengelasan' in text:
        siklus3_cards.append(c)
    else:
        siklus1_cards.append(c)

def create_tab_content(tab_id, title, cards_list):
    cards_html = '\n'.join(cards_list)
    return f"""
        <div id="{tab_id}" class="tab-content {'active' if tab_id == 'siklus-1' else ''}">
            <div class="gallery-section">
                <h3 style="color: var(--kemendikbud-blue); text-align: center; margin-bottom: 2rem; font-size: 1.8rem;">📂 Koleksi Artefak: {title}</h3>
                <div class="search-container" style="margin: 0 auto 2rem auto; max-width: 800px; position: relative;">
                    <input type="text" class="search-input search-input-gallery" placeholder="Cari dokumen, RPP, Media, LKM..." style="width: 100%; padding: 1rem 1.5rem; border-radius: 50px; border: 2px solid var(--border-color); font-size: 1rem; outline: none; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: border-color 0.3s;">
                    <div class="search-icon search-btn" style="position: absolute; right: 20px; top: 50%; transform: translateY(-50%); cursor: pointer; font-size: 1.2rem;">🔍</div>
                </div>

                <div class="filter-container">
                    <button class="filter-btn active" data-filter="all">Semua</button>
                    <button class="filter-btn" data-filter="rpp">RPP</button>
                    <button class="filter-btn" data-filter="media">Media</button>
                    <button class="filter-btn" data-filter="lks">LKM dan Asesmen</button>
                    <button class="filter-btn" data-filter="bahan-ajar">Bahan Ajar</button>
                    <button class="filter-btn" data-filter="hasil-kerja">Hasil Kerja Siswa</button>
                    <button class="filter-btn" data-filter="video">Video Mengajar</button>
                    <button class="filter-btn" data-filter="penilaian">Penilaian GP & DPL</button>
                </div>

                <div class="doc-grid gallery-grid">
                    {cards_html}
                </div>
            </div>
        </div>
"""

new_artefak_html = f"""
    <!-- 3. Analisis Artefak Produk Pembelajaran -->
    <section id="artefak">
        <h2>Analisis Artefak Pembelajaran</h2>
        
        <!-- Keterangan Siklus -->
        <div style="background: white; box-shadow: 0 4px 15px rgba(0,0,0,0.05); max-width: 600px; margin: 0 auto 2rem auto; padding: 1.5rem 2rem; border-radius: 12px; border-left: 5px solid var(--kemendikbud-blue); text-align: left;">
            <h4 style="margin-top: 0; margin-bottom: 0.8rem; color: var(--kemendikbud-blue); font-size: 1.05rem; display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 1.2rem;">📌</span> Panduan Topik Siklus
            </h4>
            <ul style="margin: 0; padding-left: 1.2rem; color: var(--text-dark); font-size: 0.95rem; line-height: 1.8;">
                <li><strong>Siklus 1:</strong> Dasar Proses Produksi</li>
                <li><strong>Siklus 2:</strong> Dasar Sistem Mekanik</li>
                <li><strong>Siklus 3:</strong> Pengelasan Dasar SMAW</li>
            </ul>
        </div>

        <!-- Tab Navigation -->
        <div class="tab-nav">
            <button class="tab-btn active" onclick="switchTab('siklus-1')">Siklus 1</button>
            <button class="tab-btn" onclick="switchTab('siklus-2')">Siklus 2</button>
            <button class="tab-btn" onclick="switchTab('siklus-3')">Siklus 3</button>
        </div>

        <!-- Tab Contents -->
        {create_tab_content('siklus-1', 'Siklus 1 (Dasar Proses Produksi)', siklus1_cards)}
        {create_tab_content('siklus-2', 'Siklus 2 (Dasar Sistem Mekanik)', siklus2_cards)}
        {create_tab_content('siklus-3', 'Siklus 3 (Pengelasan Dasar SMAW)', siklus3_cards)}

    </section>
"""

before = html_content[:start_idx]
after = html_content[end_idx:]
new_html = before + new_artefak_html + '\n    ' + after

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print(f"HTML updated successfully. Found {len(clean_cards)} cards.")
