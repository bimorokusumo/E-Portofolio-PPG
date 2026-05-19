import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Read style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Read script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Parse the cards from index.html to reuse them
# We can just extract them one by one.
import bs4
soup = bs4.BeautifulSoup(html_content, 'html.parser')

cards = soup.find_all('div', class_='doc-card')

# Categorize cards
siklus1_cards = []
siklus2_cards = []
siklus3_cards = []

for card in cards:
    text = card.get_text().lower()
    if 'mekanik' in text:
        siklus2_cards.append(str(card))
    elif 'smaw' in text or 'pengelasan' in text or 'elektroda' in text or 'tflm' in text or 'hasil las' in text:
        siklus3_cards.append(str(card))
    else:
        # Default to Siklus 1 (proses produksi/manufaktur)
        siklus1_cards.append(str(card))

# Build new HTML structure
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

# We need to replace everything from <section id="artefak"> to </section> before <section id="analisis-produk" ...>
import re
start_pattern = r'<!-- 3\. Analisis Artefak Produk Pembelajaran -->'
end_pattern = r'<!-- Analisis Produk Pembelajaran -->'

# Ensure it's matching correctly
start_match = re.search(start_pattern, html_content)
end_match = re.search(end_pattern, html_content)

if start_match and end_match:
    before = html_content[:start_match.start()]
    after = html_content[end_match.start():]
    new_html = before + new_artefak_html + '\n    ' + after
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("HTML updated successfully.")
else:
    print("Could not find start or end markers for artefak section.")

# Add CSS if not present
if '.tab-nav' not in css_content:
    new_css = """
/* Tab Navigation */
.tab-nav {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 2rem auto;
    max-width: 800px;
    flex-wrap: wrap;
}

.tab-btn {
    padding: 0.8rem 2rem;
    font-size: 1.1rem;
    font-weight: 600;
    border: 2px solid var(--kemendikbud-blue);
    background-color: white;
    color: var(--kemendikbud-blue);
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.tab-btn:hover {
    background-color: #f0f7ff;
}

.tab-btn.active {
    background-color: var(--kemendikbud-blue);
    color: white;
    box-shadow: 0 4px 10px rgba(0, 89, 178, 0.2);
}

.tab-content {
    display: none;
    animation: fadeIn 0.4s ease;
}

.tab-content.active {
    display: block;
}
"""
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(new_css)
    print("CSS updated successfully.")

# Add JS if not present
if 'function switchTab' not in js_content:
    new_js = """
// Tab Switching Logic
window.switchTab = function(tabId) {
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    document.getElementById(tabId).classList.add('active');
    document.querySelector(`.tab-btn[onclick="switchTab('${tabId}')"]`).classList.add('active');
};
"""
    with open('script.js', 'a', encoding='utf-8') as f:
        f.write(new_js)
    print("JS updated successfully.")

