import re

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

start_marker = '<!-- 3. Analisis Artefak Produk Pembelajaran -->'
end_marker = '<!-- Analisis Produk Pembelajaran -->'

start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker)

artefak_html = html_content[start_idx:end_idx]

# Extract cards
# This time we can just use regex to find all cards because the HTML structure is consistent.
# A card starts with <div class="doc-card gallery-card-item" and ends with the last </div> before the next card or end of container.
# Wait, a safer way is to split by `<div class="doc-card gallery-card-item"` as before.

parts = artefak_html.split('<div class="doc-card gallery-card-item"')

clean_cards = []
for p in parts[1:]:
    card_str = '<div class="doc-card gallery-card-item"' + p
    # find the end of this card
    div_count = 0
    i = 0
    while i < len(card_str):
        if card_str.startswith('<div', i):
            div_count += 1
        elif card_str.startswith('</div', i):
            div_count -= 1
            if div_count == 0:
                clean_cards.append(card_str[:i+6])
                break
        i += 1

siklus1_cards = []
siklus2_cards = []
siklus3_cards = []

for c in clean_cards:
    # Extract the h4 title to classify
    h4_match = re.search(r'<h4>(.*?)</h4>', c)
    if h4_match:
        title = h4_match.group(1).lower()
        if 'mekanik' in title:
            siklus2_cards.append(c)
        elif 'smaw' in title or 'pengelasan' in title or 'elektroda' in title or 'tflm' in title or 'hasil las' in title or 'posisi' in title:
            siklus3_cards.append(c)
        else:
            siklus1_cards.append(c)
    else:
        siklus1_cards.append(c) # fallback

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

print(f"Reparsed {len(clean_cards)} cards. S1: {len(siklus1_cards)}, S2: {len(siklus2_cards)}, S3: {len(siklus3_cards)}")
