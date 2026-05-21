import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the HTML for Refleksi Akhir PPL Terbimbing
# We will construct the new HTML completely and replace from <!-- Refleksi Akhir PPL Terbimbing --> to <!-- Filosofi Mengajar -->
new_refleksi = """<!-- Refleksi Akhir PPL Terbimbing -->
<section class="one-screen" id="ep2-analisis-artefak" style="max-width: 100%; padding: 4rem 2rem;">
<div style="max-width: 1160px; margin: 0 auto;">
<h2 style="color: var(--kemendikbud-blue); margin-bottom: 2rem; display: flex; align-items: center; justify-content: center; gap: 10px;"><span style="font-size: 2rem;">📝</span> Refleksi Akhir PPL Terbimbing</h2>

<!-- Tab Navigation EP2 -->
<div class="tab-nav" style="justify-content: center; margin-bottom: 3rem;">
<button class="tab-btn active" onclick="switchTabEP2('ep2-siklus-1', this)">Siklus 1</button>
<button class="tab-btn" onclick="switchTabEP2('ep2-siklus-2', this)">Siklus 2</button>
<button class="tab-btn" onclick="switchTabEP2('ep2-siklus-3', this)">Siklus 3</button>
</div>

<!-- Siklus 1 -->
<div class="ep2-tab-content" id="ep2-siklus-1" style="display: block; animation: fadeIn 0.5s ease;">
    <h3 style="color: var(--kemendikbud-blue); text-align: center; margin-bottom: 2rem; font-size: 1.5rem;">Dasar Proses Produksi</h3>
    <div class="article-grid">
        <div class="ep2-card">
            <span class="ep2-card-icon">📚</span>
            <h3 class="ep2-card-title">1. Apa yang Telah Saya Pelajari?</h3>
            <p class="ep2-card-summary">Esensi mengkondisikan siswa dari budaya SMP menuju budaya industri SMK serta urgensi K3 sebelum praktik.</p>
            <button class="btn-ep2-readmore" onclick="openEP2Modal('s1-1')">Baca Refleksi ➔</button>
        </div>
        <div class="ep2-card">
            <span class="ep2-card-icon">⛰️</span>
            <h3 class="ep2-card-title">2. Pengalaman Menantang & Solusi</h3>
            <p class="ep2-card-summary">Menghadapi siswa yang belum terbiasa dengan kedisiplinan dan merancang SOP ketat via tutor sebaya.</p>
            <button class="btn-ep2-readmore" onclick="openEP2Modal('s1-2')">Baca Refleksi ➔</button>
        </div>
        <div class="ep2-card">
            <span class="ep2-card-icon">💡</span>
            <h3 class="ep2-card-title">3. Umpan Balik & Saran</h3>
            <p class="ep2-card-summary">Alokasi waktu transisi dari teori ke praktik perlu diperbaiki dengan <i>micro-learning</i>.</p>
            <button class="btn-ep2-readmore" onclick="openEP2Modal('s1-3')">Baca Refleksi ➔</button>
        </div>
    </div>
</div>

<!-- Siklus 2 -->
<div class="ep2-tab-content" id="ep2-siklus-2" style="display: none; animation: fadeIn 0.5s ease;">
    <h3 style="color: var(--kemendikbud-blue); text-align: center; margin-bottom: 2rem; font-size: 1.5rem;">Dasar Sistem Mekanik</h3>
    <div class="article-grid">
        <div class="ep2-card">
            <span class="ep2-card-icon">⚙️</span>
            <h3 class="ep2-card-title">1. Apa yang Telah Saya Pelajari?</h3>
            <p class="ep2-card-summary">Menerjemahkan konsep fisika abstrak menjadi modul aplikatif dengan <i>scaffolding</i> yang terstruktur.</p>
            <button class="btn-ep2-readmore" onclick="openEP2Modal('s2-1')">Baca Refleksi ➔</button>
        </div>
        <div class="ep2-card">
            <span class="ep2-card-icon">🚧</span>
            <h3 class="ep2-card-title">2. Pengalaman Menantang & Solusi</h3>
            <p class="ep2-card-summary">Mengatasi disparitas kemampuan berhitung siswa melalui diferensiasi asesmen dan benda kerja nyata.</p>
            <button class="btn-ep2-readmore" onclick="openEP2Modal('s2-2')">Baca Refleksi ➔</button>
        </div>
        <div class="ep2-card">
            <span class="ep2-card-icon">💬</span>
            <h3 class="ep2-card-title">3. Umpan Balik & Saran</h3>
            <p class="ep2-card-summary">Perlunya lebih banyak instrumen sentuh (<i>hands-on</i>) daripada presentasi slide pasif di kelas.</p>
            <button class="btn-ep2-readmore" onclick="openEP2Modal('s2-3')">Baca Refleksi ➔</button>
        </div>
    </div>
</div>

<!-- Siklus 3 -->
<div class="ep2-tab-content" id="ep2-siklus-3" style="display: none; animation: fadeIn 0.5s ease;">
    <h3 style="color: var(--kemendikbud-blue); text-align: center; margin-bottom: 2rem; font-size: 1.5rem;">Pengelasan Dasar SMAW</h3>
    <div class="article-grid">
        <div class="ep2-card">
            <span class="ep2-card-icon">🔥</span>
            <h3 class="ep2-card-title">1. Apa yang Telah Saya Pelajari?</h3>
            <p class="ep2-card-summary">Krusialnya demonstrasi (modeling) dan rubrik detail untuk membimbing postur siswa mengelas.</p>
            <button class="btn-ep2-readmore" onclick="openEP2Modal('s3-1')">Baca Refleksi ➔</button>
        </div>
        <div class="ep2-card">
            <span class="ep2-card-icon">🛡️</span>
            <h3 class="ep2-card-title">2. Pengalaman Menantang & Solusi</h3>
            <p class="ep2-card-summary">Menghadapi ketakutan siswa pada panas/api las melalui sesi <i>dry run</i> dan pendampingan ekstra.</p>
            <button class="btn-ep2-readmore" onclick="openEP2Modal('s3-2')">Baca Refleksi ➔</button>
        </div>
        <div class="ep2-card">
            <span class="ep2-card-icon">🎯</span>
            <h3 class="ep2-card-title">3. Umpan Balik & Saran</h3>
            <p class="ep2-card-summary">Saran pamong untuk mengevaluasi hasil las setiap satu jalur (bead) secara langsung (instan).</p>
            <button class="btn-ep2-readmore" onclick="openEP2Modal('s3-3')">Baca Refleksi ➔</button>
        </div>
    </div>
</div>

<script>
function switchTabEP2(tabId, btnElement) {
    const contents = document.querySelectorAll('.ep2-tab-content');
    contents.forEach(el => el.style.display = 'none');
    
    const navDiv = btnElement.parentElement;
    const btns = navDiv.querySelectorAll('.tab-btn');
    btns.forEach(b => b.classList.remove('active'));
    
    document.getElementById(tabId).style.display = 'block';
    btnElement.classList.add('active');
}
</script>
</div>
</section>
"""

new_filosofi = """<!-- Filosofi Mengajar -->
<section class="one-screen" id="ep2-filosofi" style="background-color: var(--bg-light-gray); max-width: 100%; padding: 4rem 2rem;">
<div style="max-width: 900px; margin: 0 auto;">
<h2 style="color: var(--kemendikbud-blue); margin-bottom: 3rem; display: flex; align-items: center; justify-content: center; gap: 10px;"><span style="font-size: 2rem;">💡</span> Filosofi Mengajar</h2>

<div class="ep2-accordion">
    <div class="ep2-accordion-item">
        <div class="ep2-accordion-header">
            <h3 class="ep2-accordion-title">
                <span style="background: var(--kemendikbud-blue); color: white; padding: 5px 12px; border-radius: 8px;">1</span> 
                Sistem Among (Ki Hajar Dewantara)
            </h3>
            <div class="ep2-accordion-icon">▼</div>
        </div>
        <div class="ep2-accordion-body">
            <div class="ep2-accordion-content">
                Prinsip dan keyakinan utama saya dalam mengajar berakar kuat pada filosofi pendidikan <strong>Ki Hajar Dewantara</strong> tentang <em>Sistem Among</em> (Ing Ngarso Sung Tulodo, Ing Madya Mangun Karso, Tut Wuri Handayani). Sebagai calon guru kejuruan, saya meyakini bahwa pendidikan sejati adalah proses "menuntun" segala kodrat yang ada pada peserta didik agar mereka mencapai keselamatan dan kebahagiaan setinggi-tingginya, baik sebagai individu maupun anggota masyarakat industri. <br><br>
                Dalam praktik pembelajaran terbimbing, filosofi ini saya wujudkan dengan memposisikan diri tidak sekadar sebagai instruktur teknis, melainkan sebagai teladan dan fasilitator yang mendampingi siswa menemukan potensi terbaiknya. Saya berupaya memahami kodrat alam dan kodrat zaman mereka melalui pendekatan yang humanis dan memerdekakan, sehingga proses belajar menjadi hal yang menyenangkan dan bermakna.
            </div>
        </div>
    </div>

    <div class="ep2-accordion-item">
        <div class="ep2-accordion-header">
            <h3 class="ep2-accordion-title">
                <span style="background: var(--kemendikbud-cyan); color: white; padding: 5px 12px; border-radius: 8px;">2</span> 
                Konstruktivisme Sosial (Lev Vygotsky)
            </h3>
            <div class="ep2-accordion-icon">▼</div>
        </div>
        <div class="ep2-accordion-body">
            <div class="ep2-accordion-content">
                Nilai Sistem Among tersebut berjalan selaras dengan teori <strong>Konstruktivisme Sosial dari Lev Vygotsky</strong>, khususnya mengenai konsep <em>Zone of Proximal Development</em> (ZPD) dan <em>Scaffolding</em>. Saya sangat percaya bahwa pengetahuan, kompetensi kerja, dan keterampilan <em>problem solving</em> tidak dapat begitu saja dipindahkan dari guru ke siswa. Kemampuan tersebut harus dibangun secara mandiri oleh siswa melalui interaksi sosial dan pengalaman aktif di bengkel praktik. <br><br>
                Oleh karena itu, saya selalu merancang aktivitas kolaboratif berbasis proyek (<em>Project-Based Learning</em>) di mana siswa didorong untuk berdiskusi, merancang alat, memecahkan permasalahan teknis secara berkelompok, dan saling belajar. Peran saya adalah memberikan bantuan terstruktur (<em>scaffolding</em>) saat mereka menemui hambatan kritis, lalu perlahan melepas bantuan tersebut saat mereka mulai mahir, demi menumbuhkan rasa percaya diri dan kemandirian.
            </div>
        </div>
    </div>

    <div class="ep2-accordion-item">
        <div class="ep2-accordion-header">
            <h3 class="ep2-accordion-title">
                <span style="background: var(--kemendikbud-green); color: white; padding: 5px 12px; border-radius: 8px;">3</span> 
                Experiential Learning (David Kolb)
            </h3>
            <div class="ep2-accordion-icon">▼</div>
        </div>
        <div class="ep2-accordion-body">
            <div class="ep2-accordion-content">
                Lebih lanjut, dalam konteks pendidikan vokasi yang berorientasi pada kesiapan kerja nyata, saya mengadopsi prinsip dasar teori <strong>Experiential Learning dari David Kolb</strong>. Saya memegang teguh keyakinan bahwa pembelajaran vokasi yang paling berdampak terjadi melalui transformasi pengalaman. Siklus dari melakukan pengalaman nyata di bengkel (<em>concrete experience</em>), melakukan observasi reflektif atas apa yang terjadi (<em>reflective observation</em>), menyusun konseptualisasi teknis (<em>abstract conceptualization</em>), hingga menguji coba kembali (<em>active experimentation</em>) menjadi fondasi pedagogis saya. <br><br>
                Praktik pengajaran saya selalu bermula dari memberi ruang bagi siswa untuk bereksperimen langsung dengan mesin, merefleksikan hasil karyanya, dan mencoba memperbaikinya. Filosofi ini membentuk ideologi saya bahwa kesalahan dalam praktik bukanlah sebuah kegagalan yang patut dihukum, melainkan instrumen esensial untuk membentuk mental teknisi yang adaptif, tangguh, kritis, dan berjiwa pembelajar sepanjang hayat.
            </div>
        </div>
    </div>
</div>

</div>
</section>
"""

modal_overlay = """
<!-- EP2 Glassmorphism Modal -->
<div class="ep2-modal-overlay" id="ep2ModalOverlay">
    <div class="ep2-modal-content">
        <div class="ep2-modal-header">
            <h3 class="ep2-modal-title">
                <span id="ep2ModalIcon"></span>
                <span id="ep2ModalTitleText">Title</span>
            </h3>
            <button class="ep2-modal-close" onclick="closeEP2Modal()">×</button>
        </div>
        <div class="ep2-modal-body" id="ep2ModalBody">
            Content
        </div>
    </div>
</div>
"""

# Find where to replace Refleksi Akhir and Filosofi Mengajar
pattern_refleksi = re.compile(r'<!-- Refleksi Akhir PPL Terbimbing -->.*?<!-- Filosofi Mengajar -->', re.DOTALL)
if pattern_refleksi.search(content):
    content = pattern_refleksi.sub(new_refleksi + "\n<!-- Filosofi Mengajar -->", content)

pattern_filosofi = re.compile(r'<!-- Filosofi Mengajar -->.*?</section>', re.DOTALL)
if pattern_filosofi.search(content):
    content = pattern_filosofi.sub(new_filosofi, content)

# Inject the modal overlay at the end of body if not exists
if "id=\"ep2ModalOverlay\"" not in content:
    content = content.replace("</body>", modal_overlay + "\n</body>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("HTML modified successfully")
