import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Remove the specific line
html_content = re.sub(r'<p style="text-align: justify; color: var\(--text-light\); margin-bottom: 1\.5rem;">Topik refleksi perangkat pembelajaran Dasar-Dasar Kejuruan \(DDK\)\.</p>\s*', '', html_content)

# The section ID of the main content where we want to insert is `<section id="artefak"> ... </section>`
# We will find the closing `</section>` that comes before `<!-- 3.5 Analisis Artefak Pembelajaran -->` 
# or just `<section id="refleksi"`

insert_html = """
    <!-- Analisis Produk Pembelajaran -->
    <section id="analisis-produk" class="analisis-section">
        <div class="analisis-header">
            <p class="analisis-subtitle">ANALISIS & EVALUASI</p>
            <h2>Analisis Produk Pembelajaran</h2>
            <p class="analisis-desc">Refleksi terhadap proses penyusunan, dasar pedagogis, faktor penerapan, dan penyesuaian produk pembelajaran untuk kebutuhan kelas yang berbeda.</p>
        </div>
        
        <div class="analisis-grid">
            <div class="analisis-card card-cyan">
                <div class="card-header">
                    <span class="card-number cyan-bg">01</span>
                    <div class="card-title-group">
                        <div class="card-line cyan-line"></div>
                        <h3>Kendala Penyusunan Produk</h3>
                    </div>
                </div>
                <p class="card-text">Penyusunan produk pembelajaran tidak hanya berhenti pada pembuatan dokumen, tetapi...</p>
                <button class="btn-buka-analisis" onclick="openAnalysisModal('01')">BUKA ANALISIS &gt;</button>
            </div>

            <div class="analisis-card card-purple">
                <div class="card-header">
                    <span class="card-number purple-bg">02</span>
                    <div class="card-title-group">
                        <div class="card-line purple-line"></div>
                        <h3>Konsep Pedagogis yang Diadopsi</h3>
                    </div>
                </div>
                <p class="card-text">Produk pembelajaran disusun dengan dasar pedagogis yang menempatkan siswa sebagai...</p>
                <button class="btn-buka-analisis" onclick="openAnalysisModal('02')">BUKA ANALISIS &gt;</button>
            </div>

            <div class="analisis-card card-green">
                <div class="card-header">
                    <span class="card-number green-bg">03</span>
                    <div class="card-title-group">
                        <div class="card-line green-line"></div>
                        <h3>Faktor Keberhasilan Penerapan</h3>
                    </div>
                </div>
                <p class="card-text">Keberhasilan penerapan produk pembelajaran sangat dipengaruhi oleh sejauh mana...</p>
                <button class="btn-buka-analisis" onclick="openAnalysisModal('03')">BUKA ANALISIS &gt;</button>
            </div>

            <div class="analisis-card card-orange">
                <div class="card-header">
                    <span class="card-number orange-bg">04</span>
                    <div class="card-title-group">
                        <div class="card-line orange-line"></div>
                        <h3>Penyesuaian untuk Kelas Berbeda</h3>
                    </div>
                </div>
                <p class="card-text">Produk pembelajaran perlu disiapkan agar dapat menyesuaikan kelas dengan latar...</p>
                <button class="btn-buka-analisis" onclick="openAnalysisModal('04')">BUKA ANALISIS &gt;</button>
            </div>
        </div>
    </section>

    <!-- Modal Analysis HTML -->
    <div class="analysis-modal-overlay" id="analysisModalOverlay">
        <div class="analysis-modal-content">
            <div class="analysis-modal-header">
                <div class="header-left">
                    <span class="modal-number cyan-bg" id="modalNumber">01</span>
                    <div class="header-titles">
                        <span class="modal-kategori">ANALISIS PRODUK</span>
                        <h2 id="modalTitle">Kendala Penyusunan Produk</h2>
                    </div>
                </div>
                <button class="btn-close-modal" onclick="closeAnalysisModal()">&times;</button>
            </div>
            <p class="modal-subtitle" id="modalSubtitle">Penyusunan produk pembelajaran tidak hanya berhenti pada pembuatan dokumen, tetapi menjadi proses menerjemahkan kebutuhan kelas ke dalam rancangan yang dapat dijalankan secara nyata.</p>
            
            <div class="modal-grid-2">
                <div class="modal-box" id="boxDiagnosis">
                    <h4 id="labelDiagnosis">DIAGNOSIS</h4>
                    <p id="modalDiagnosis">Kendala paling besar muncul ketika rancangan ideal harus disesuaikan dengan kondisi kelas...</p>
                </div>
                <div class="modal-box" id="boxImplikasi">
                    <h4 id="labelImplikasi">IMPLIKASI</h4>
                    <p id="modalImplikasi">Implikasinya, produk pembelajaran harus dirancang sebagai perangkat yang hidup...</p>
                </div>
            </div>
            
            <div class="modal-box box-full">
                <h4>ANALISIS MENDALAM</h4>
                <p id="modalMendalam">Pada tahap awal penyusunan, tantangan utama terletak pada penyelarasan...</p>
            </div>
        </div>
    </div>
"""

# Find the insertion point: immediately after `    </section>\n    <!-- 3.5 Analisis Artefak Pembelajaran -->`
# We'll replace `    <!-- 3.5 Analisis Artefak Pembelajaran -->` with `insert_html + "    <!-- 3.5 Analisis Artefak Pembelajaran -->"`

html_content = html_content.replace('<!-- 3.5 Analisis Artefak Pembelajaran -->', insert_html + '\n    <!-- 3.5 Analisis Artefak Pembelajaran -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Update style.css
css_content = """
/* Analisis Produk Section */
.analisis-section {
    background-color: #1a1e29;
    background-image: radial-gradient(circle at top right, #1d2538, #1a1e29);
    padding: 5rem 2rem;
    color: #fff;
    font-family: 'Inter', sans-serif;
}

.analisis-header {
    text-align: center;
    max-width: 800px;
    margin: 0 auto 4rem auto;
}

.analisis-subtitle {
    color: #a0aec0;
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.analisis-header h2 {
    font-size: 2.5rem;
    margin-top: 0;
    margin-bottom: 1rem;
    color: #e2e8f0;
}

.analisis-desc {
    color: #94a3b8;
    line-height: 1.6;
    font-size: 1.05rem;
}

.analisis-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    max-width: 1160px;
    margin: 0 auto;
}

.analisis-card {
    background: #232936;
    border-radius: 16px;
    padding: 2rem 1.5rem;
    position: relative;
    border: 1px solid rgba(255,255,255,0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
}

.analisis-card:hover {
    transform: translateY(-5px);
}

.card-cyan:hover { box-shadow: 0 10px 30px rgba(6, 182, 212, 0.15); border-color: rgba(6, 182, 212, 0.3); }
.card-purple:hover { box-shadow: 0 10px 30px rgba(168, 85, 247, 0.15); border-color: rgba(168, 85, 247, 0.3); }
.card-green:hover { box-shadow: 0 10px 30px rgba(16, 185, 129, 0.15); border-color: rgba(16, 185, 129, 0.3); }
.card-orange:hover { box-shadow: 0 10px 30px rgba(245, 158, 11, 0.15); border-color: rgba(245, 158, 11, 0.3); }

.card-header {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.card-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    font-weight: 700;
    font-size: 0.9rem;
    flex-shrink: 0;
}

.cyan-bg { background-color: #22d3ee; color: #083344; }
.purple-bg { background-color: #c084fc; color: #3b0764; }
.green-bg { background-color: #34d399; color: #064e3b; }
.orange-bg { background-color: #fbbf24; color: #78350f; }

.card-title-group {
    display: flex;
    flex-direction: column;
}

.card-line {
    width: 30px;
    height: 3px;
    margin-bottom: 0.8rem;
    border-radius: 2px;
}

.cyan-line { background-color: #22d3ee; }
.purple-line { background-color: #c084fc; }
.green-line { background-color: #34d399; }
.orange-line { background-color: #fbbf24; }

.analisis-card h3 {
    font-size: 1.2rem;
    margin: 0;
    color: #e2e8f0;
    line-height: 1.4;
}

.card-cyan h3 { color: #22d3ee; }
.card-purple h3 { color: #c084fc; }
.card-green h3 { color: #34d399; }
.card-orange h3 { color: #fbbf24; }

.card-text {
    color: #cbd5e1;
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 2rem;
    flex-grow: 1;
}

.btn-buka-analisis {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    color: #94a3b8;
    padding: 0.8rem 1.2rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 1px;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: left;
    display: inline-block;
    width: fit-content;
}

.btn-buka-analisis:hover {
    background: rgba(255,255,255,0.1);
    color: #fff;
}

/* Modal CSS */
.analysis-modal-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(8px);
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
}

.analysis-modal-overlay.active {
    opacity: 1;
    visibility: visible;
}

.analysis-modal-content {
    background: #1a1e29;
    width: 90%;
    max-width: 900px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.1);
    padding: 2.5rem;
    box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
    transform: translateY(20px) scale(0.95);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    max-height: 90vh;
    overflow-y: auto;
}

.analysis-modal-overlay.active .analysis-modal-content {
    transform: translateY(0) scale(1);
}

.analysis-modal-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1.5rem;
}

.header-left {
    display: flex;
    align-items: center;
    gap: 1.2rem;
}

.modal-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    font-weight: 700;
    font-size: 1.1rem;
    flex-shrink: 0;
    color: #fff;
}

.header-titles {
    display: flex;
    flex-direction: column;
}

.modal-kategori {
    font-size: 0.75rem;
    letter-spacing: 2px;
    margin-bottom: 0.3rem;
    color: #22d3ee;
}

.analysis-modal-content h2 {
    color: #f8fafc;
    font-size: 1.8rem;
    margin: 0;
}

.btn-close-modal {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    color: #94a3b8;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    font-size: 1.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-close-modal:hover {
    background: rgba(255,255,255,0.2);
    color: #fff;
}

.modal-subtitle {
    color: #cbd5e1;
    font-size: 1.05rem;
    line-height: 1.6;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

.modal-grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
}

.modal-box {
    background: #232936;
    border: 1px solid rgba(34, 211, 238, 0.2);
    border-radius: 12px;
    padding: 1.5rem;
}

.modal-box h4 {
    color: #22d3ee;
    font-size: 0.85rem;
    letter-spacing: 1px;
    margin-top: 0;
    margin-bottom: 1rem;
}

.modal-box p {
    color: #cbd5e1;
    font-size: 0.95rem;
    line-height: 1.7;
    margin: 0;
}

.box-full {
    border-color: rgba(34, 211, 238, 0.2);
}
.box-full h4 {
    color: #22d3ee;
}

@media (max-width: 768px) {
    .modal-grid-2 {
        grid-template-columns: 1fr;
    }
    .analysis-modal-content {
        padding: 1.5rem;
    }
    .analysis-modal-content h2 {
        font-size: 1.4rem;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

# 3. Update script.js
js_content = """
// Data Analisis Produk
const analysisData = {
    '01': {
        title: 'Kendala Penyusunan Produk',
        subtitle: 'Penyusunan produk pembelajaran tidak hanya berhenti pada pembuatan dokumen, tetapi menjadi proses menerjemahkan kebutuhan kelas ke dalam rancangan yang dapat dijalankan secara nyata.',
        diagnosis: 'Kendala paling besar muncul ketika rancangan ideal harus disesuaikan dengan kondisi kelas, kemampuan awal siswa, ketersediaan waktu, dan kesiapan media. Produk pembelajaran harus tetap sistematis, tetapi tidak boleh terlalu kaku karena situasi kelas dapat berubah ketika pembelajaran berlangsung.',
        implikasi: 'Implikasinya, produk pembelajaran harus dirancang sebagai perangkat yang hidup: jelas secara alur, kuat secara pedagogis, tetapi tetap fleksibel ketika menghadapi dinamika kelas. Produk yang baik bukan hanya lengkap, melainkan mampu membantu guru mengambil keputusan saat pembelajaran berlangsung.',
        mendalam: 'Pada tahap awal penyusunan, tantangan utama terletak pada penyelarasan antara tujuan pembelajaran, materi, kegiatan, LKM, media, dan asesmen. Jika salah satu komponen tidak saling terhubung, produk pembelajaran berisiko hanya menjadi dokumen administratif, bukan alat bantu yang benar-benar mengarahkan pembelajaran. Kendala berikutnya adalah menentukan tingkat kedalaman materi. Materi perlu cukup kuat secara konsep, tetapi tetap dapat dipahami oleh peserta didik dengan latar kemampuan yang beragam. Hal ini menuntut guru untuk memilih contoh, urutan penjelasan, dan bentuk latihan yang bertahap. Kendala teknis juga muncul pada pengaturan waktu. Dalam pembelajaran kejuruan, waktu tidak hanya digunakan untuk menjelaskan materi, tetapi juga untuk demonstrasi, latihan, pendampingan, koreksi, dan refleksi. Produk pembelajaran yang terlalu padat dapat membuat guru tergesa-gesa dan siswa kehilangan kesempatan memperbaiki pemahamannya.',
        theme: 'cyan'
    },
    '02': {
        title: 'Konsep Pedagogis yang Diadopsi',
        subtitle: 'Pemilihan kerangka pedagogis bertujuan untuk memastikan bahwa produk pembelajaran yang dihasilkan berpusat pada siswa dan memfasilitasi pemahaman tingkat tinggi.',
        diagnosis: 'Pemilihan metode pengajaran (seperti Understanding by Design dan Inquiry Learning) seringkali dihadapkan pada realita siswa yang terbiasa dengan metode konvensional. Dibutuhkan adaptasi agar konsep ini dapat diterapkan efektif tanpa menimbulkan kebingungan pada siswa.',
        implikasi: 'Guru bertindak lebih sebagai fasilitator (pamong) daripada pusat informasi. Hal ini menuntut produk pembelajaran seperti modul dan media memiliki instruksi yang sangat jelas dan scaffolding yang bertahap agar siswa dapat membangun pengetahuannya sendiri secara mandiri.',
        mendalam: 'Penerapan Understanding by Design (UbD) memaksa saya sebagai penyusun untuk mulai dari tujuan akhir (kompetensi yang diharapkan) sebelum menyusun langkah-langkah pembelajaran. Pendekatan ini memastikan bahwa setiap media, LKS, dan asesmen yang dibuat memiliki relevansi langsung dengan tujuan akhir tersebut. Sementara itu, sintaks Inquiry Learning diintegrasikan untuk mendorong rasa ingin tahu dan kemampuan problem-solving siswa, khususnya dalam konteks permesinan dan manufaktur. Kolaborasi kedua konsep ini melahirkan produk pembelajaran yang sistematis, menantang, dan bermakna. Siswa tidak hanya menghafal prosedur, tetapi memahami "mengapa" dan "bagaimana" suatu proses produksi dilakukan. Tantangannya adalah menyeimbangkan antara kebebasan eksplorasi (Inquiry) dengan standar keselamatan dan presisi teknis yang ketat di area bengkel manufaktur.',
        theme: 'purple'
    },
    '03': {
        title: 'Faktor Keberhasilan Penerapan',
        subtitle: 'Efektivitas produk pembelajaran diukur dari sejauh mana rancangan tersebut berhasil diterapkan, dipahami, dan meningkatkan kompetensi siswa di dalam kelas.',
        diagnosis: 'Tingkat keberhasilan berbanding lurus dengan kejelasan instruksi pada Lembar Kerja (LKM/LKS) serta kesesuaian media visual (video/presentasi) dalam menjembatani kesenjangan antara teori abstrak dengan praktik nyata di bengkel.',
        implikasi: 'Produk pembelajaran yang sukses adalah produk yang adaptif. Saat fasilitas mendukung dan siswa merespons positif terhadap media interaktif, tingkat ketercapaian kompetensi meningkat tajam, yang dibuktikan dengan hasil asesmen sumatif dan produk kerja praktik siswa.',
        mendalam: 'Faktor penentu utama keberhasilan penerapan produk ini adalah kombinasi antara materi yang terstruktur (melalui modul/RPP) dan media pembelajaran yang representatif. Penggunaan media visual seperti animasi 3D CAD atau video demonstrasi las SMAW terbukti sangat krusial dalam membantu siswa memvisualisasikan konsep abstrak sebelum mereka mengeksekusinya di mesin nyata. Selain itu, Lembar Kerja Siswa (LKS) yang dirancang dengan format step-by-step (SOP) memberikan panduan yang aman dan terukur selama praktikum. Keberhasilan juga didukung oleh pengelolaan kelas yang baik, di mana alokasi waktu untuk briefing K3, eksekusi praktik, dan evaluasi hasil kerja telah terdistribusi secara proporsional. Antusiasme siswa melonjak signifikan ketika mereka diberikan proyek nyata (Project-Based Learning) yang hasil akhirnya dapat mereka lihat dan gunakan, sehingga produk pembelajaran benar-benar dirasakan manfaat dan relevansinya.',
        theme: 'green'
    },
    '04': {
        title: 'Penyesuaian untuk Kelas Berbeda',
        subtitle: 'Tidak ada satu rancangan pembelajaran yang sempurna untuk semua kondisi; produk pembelajaran harus selalu diuji dan disesuaikan secara berkesinambungan.',
        diagnosis: 'Setiap kelas memiliki dinamika unik: ada kelas dengan mayoritas pembelajar visual, ada yang lebih kinestetik, dan ada yang membutuhkan pendampingan ekstra (scaffolding) pada materi dasar pemesinan.',
        implikasi: 'Asesmen awal (diagnostik) menjadi kunci. Produk pembelajaran tidak dirancang secara statis, melainkan menyediakan opsi diferensiasi, baik dari segi konten (tingkat kesulitan latihan), proses (kelompok vs individu), maupun produk akhir yang diharapkan.',
        mendalam: 'Dalam implementasinya, saya menyadari bahwa satu modul ajar yang sama bisa memberikan hasil yang berbeda pada dua rombongan belajar (rombel) yang berbeda. Oleh karena itu, penyesuaian (diferensiasi) adalah sebuah keharusan. Pada kelas yang kemampuan teknis awalnya rendah, produk pembelajaran disesuaikan dengan memperbanyak porsi demonstrasi langsung (modeling) dan memperkecil rasio kesulitan pada LKS awal. Sebaliknya, pada kelas yang lebih cekatan, penyesuaian dilakukan dengan memberikan studi kasus (troubleshooting) atau proyek fabrikasi dengan tingkat presisi yang lebih menantang. Fleksibilitas ini juga tercermin pada media pembelajaran; saya menyiapkan alternatif simulasi digital (CAD/CAM) bagi siswa yang menunggu giliran menggunakan mesin fisik. Proses adaptasi berkelanjutan ini membuktikan bahwa produk pembelajaran yang baik harus berfungsi sebagai kompas, bukan rel kereta api, yang memungkinkan guru untuk mengambil jalur alternatif demi mencapai tujuan kompetensi akhir yang sama.',
        theme: 'orange'
    }
};

const themeColors = {
    'cyan': '#22d3ee',
    'purple': '#c084fc',
    'green': '#34d399',
    'orange': '#fbbf24'
};

function openAnalysisModal(id) {
    const data = analysisData[id];
    if (!data) return;

    // Set texts
    document.getElementById('modalNumber').textContent = id;
    document.getElementById('modalTitle').textContent = data.title;
    document.getElementById('modalSubtitle').textContent = data.subtitle;
    document.getElementById('modalDiagnosis').textContent = data.diagnosis;
    document.getElementById('modalImplikasi').textContent = data.implikasi;
    document.getElementById('modalMendalam').textContent = data.mendalam;

    // Set theme colors
    const color = themeColors[data.theme];
    
    // Update number bg class
    const numEl = document.getElementById('modalNumber');
    numEl.className = `modal-number ${data.theme}-bg`;
    
    // Update category text color
    document.querySelector('.modal-kategori').style.color = color;
    
    // Update borders and text colors of boxes
    const boxDiagnosis = document.getElementById('boxDiagnosis');
    const boxImplikasi = document.getElementById('boxImplikasi');
    const labelDiagnosis = document.getElementById('labelDiagnosis');
    const labelImplikasi = document.getElementById('labelImplikasi');
    const boxFull = document.querySelector('.box-full');
    const labelFull = boxFull.querySelector('h4');

    // Convert hex to rgba for border
    let r = parseInt(color.slice(1, 3), 16),
        g = parseInt(color.slice(3, 5), 16),
        b = parseInt(color.slice(5, 7), 16);
    
    const borderColor = `rgba(${r}, ${g}, ${b}, 0.2)`;

    boxDiagnosis.style.borderColor = borderColor;
    boxImplikasi.style.borderColor = borderColor;
    boxFull.style.borderColor = borderColor;
    
    labelDiagnosis.style.color = color;
    labelImplikasi.style.color = color;
    labelFull.style.color = color;

    // Show modal
    const overlay = document.getElementById('analysisModalOverlay');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
}

function closeAnalysisModal() {
    const overlay = document.getElementById('analysisModalOverlay');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
}

// Close when clicking outside modal content
document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.getElementById('analysisModalOverlay');
    if(overlay) {
        overlay.addEventListener('click', function(e) {
            if (e.target === this) {
                closeAnalysisModal();
            }
        });
    }
});
"""

with open('script.js', 'a', encoding='utf-8') as f:
    f.write(js_content)

print("Implementation applied.")
