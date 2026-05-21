import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new content for EP2 Analisis Artefak
new_content = """<!-- Refleksi Akhir PPL Terbimbing -->
<section class="one-screen" id="ep2-analisis-artefak" style="max-width: 100%; padding: 4rem 2rem;">
<div style="max-width: 1160px; margin: 0 auto;">
<h2 style="color: var(--kemendikbud-blue); margin-bottom: 2rem; display: flex; align-items: center; gap: 10px;"><span style="font-size: 2rem;">📝</span> Refleksi Akhir PPL Terbimbing</h2>

<!-- Tab Navigation EP2 -->
<div class="tab-nav">
<button class="tab-btn active" onclick="switchTabEP2('ep2-siklus-1', this)">Siklus 1</button>
<button class="tab-btn" onclick="switchTabEP2('ep2-siklus-2', this)">Siklus 2</button>
<button class="tab-btn" onclick="switchTabEP2('ep2-siklus-3', this)">Siklus 3</button>
</div>

<!-- Siklus 1 -->
<div class="ep2-tab-content" id="ep2-siklus-1" style="display: block;">
    <h3 style="color: var(--kemendikbud-blue); text-align: center; margin-bottom: 2rem; font-size: 1.5rem;">Dasar Proses Produksi</h3>
    <div class="article-grid">
        <div class="card-article" style="border-top: 4px solid var(--kemendikbud-cyan);">
            <h3 style="color: var(--kemendikbud-blue); font-size: 1.2rem; margin-bottom: 1rem;">1. Apa yang Telah Saya Pelajari?</h3>
            <p style="color: var(--text-dark); line-height: 1.6; text-align: justify;">Pada Siklus 1, saya belajar esensi mengkondisikan siswa dari budaya SMP menuju budaya industri SMK (orientasi manufaktur). Saya menyusun produk pembelajaran awal yang menitikberatkan pada pengenalan proses produksi, mesin-mesin konvensional, serta menanamkan urgensi K3 (Kesehatan dan Keselamatan Kerja) sebelum mereka benar-benar bekerja di bengkel.</p>
        </div>
        <div class="card-article" style="border-top: 4px solid var(--kemendikbud-cyan);">
            <h3 style="color: var(--kemendikbud-blue); font-size: 1.2rem; margin-bottom: 1rem;">2. Pengalaman Menantang & Solusi</h3>
            <p style="color: var(--text-dark); line-height: 1.6; text-align: justify;">Tantangan utama adalah siswa masih belum terbiasa dengan kedisiplinan dan SOP bengkel, sehingga pengawasan harus ekstra ketat. Solusi yang saya rancang dalam produk pembelajaran (LKM) adalah membuat <i>checklist</i> wajib K3 dan menerapkan metode tutor sebaya (<i>peer-tutoring</i>) pada kelompok kecil untuk memastikan setiap siswa saling mengingatkan terkait prosedur aman berpraktik.</p>
        </div>
        <div class="card-article" style="border-top: 4px solid var(--kemendikbud-cyan);">
            <h3 style="color: var(--kemendikbud-blue); font-size: 1.2rem; margin-bottom: 1rem;">3. Umpan Balik & Saran Konstruktif</h3>
            <p style="color: var(--text-dark); line-height: 1.6; text-align: justify;">Guru Pamong memberikan masukan bahwa alokasi waktu transisi dari penyampaian teori di kelas menuju bengkel masih kurang efisien. Sebagai perbaikan, saya disarankan menyertakan materi <i>micro-learning</i> atau apersepsi visual (media animasi) yang singkat agar siswa lebih cepat menangkap instruksi dan sisa waktu praktik menjadi lebih maksimal.</p>
        </div>
    </div>
</div>

<!-- Siklus 2 -->
<div class="ep2-tab-content" id="ep2-siklus-2" style="display: none;">
    <h3 style="color: var(--kemendikbud-blue); text-align: center; margin-bottom: 2rem; font-size: 1.5rem;">Dasar Sistem Mekanik</h3>
    <div class="article-grid">
        <div class="card-article" style="border-top: 4px solid var(--kemendikbud-cyan);">
            <h3 style="color: var(--kemendikbud-blue); font-size: 1.2rem; margin-bottom: 1rem;">1. Apa yang Telah Saya Pelajari?</h3>
            <p style="color: var(--text-dark); line-height: 1.6; text-align: justify;">Siklus 2 mengajarkan saya cara menerjemahkan konsep fisika abstrak (seperti gaya, torsi, dan rasio roda gigi) menjadi modul ajar yang aplikatif. Saya belajar pentingnya <i>scaffolding</i> yang terstruktur agar siswa tidak merasa terintimidasi oleh perhitungan matematis yang krusial bagi seorang teknisi.</p>
        </div>
        <div class="card-article" style="border-top: 4px solid var(--kemendikbud-cyan);">
            <h3 style="color: var(--kemendikbud-blue); font-size: 1.2rem; margin-bottom: 1rem;">2. Pengalaman Menantang & Solusi</h3>
            <p style="color: var(--text-dark); line-height: 1.6; text-align: justify;">Tantangannya adalah disparitas kemampuan berhitung siswa yang cukup lebar, membuat sebagian siswa tertinggal dalam analisis rasio transmisi. Solusi yang saya lakukan adalah mendiferensiasi instrumen asesmen dan memanfaatkan alat peraga benda nyata (seperti transmisi sepeda motor bekas) di LKM, sehingga perhitungan terasa nyata, tidak hanya di atas kertas.</p>
        </div>
        <div class="card-article" style="border-top: 4px solid var(--kemendikbud-cyan);">
            <h3 style="color: var(--kemendikbud-blue); font-size: 1.2rem; margin-bottom: 1rem;">3. Umpan Balik & Saran Konstruktif</h3>
            <p style="color: var(--text-dark); line-height: 1.6; text-align: justify;">DPL menyarankan agar produk media pembelajaran tidak hanya berfokus pada presentasi <i>slide</i>, melainkan harus lebih banyak menggunakan instrumen sentuh (<i>hands-on</i>). Masukan ini menyadarkan saya bahwa pembelajaran kinestetik adalah inti dari pendidikan kejuruan, dan perbaikan ini akan saya terapkan pada desain LKM Siklus 3 dan PPL Mandiri.</p>
        </div>
    </div>
</div>

<!-- Siklus 3 -->
<div class="ep2-tab-content" id="ep2-siklus-3" style="display: none;">
    <h3 style="color: var(--kemendikbud-blue); text-align: center; margin-bottom: 2rem; font-size: 1.5rem;">Pengelasan Dasar SMAW</h3>
    <div class="article-grid">
        <div class="card-article" style="border-top: 4px solid var(--kemendikbud-cyan);">
            <h3 style="color: var(--kemendikbud-blue); font-size: 1.2rem; margin-bottom: 1rem;">1. Apa yang Telah Saya Pelajari?</h3>
            <p style="color: var(--text-dark); line-height: 1.6; text-align: justify;">Pada materi pengelasan SMAW yang berisiko tinggi, saya memelajari krusialnya integrasi antara demonstrasi guru (<i>modeling</i>) dan rubrik penilaian yang sangat detail. Perangkat ajar yang saya susun harus mampu memfasilitasi <i>Zone of Proximal Development</i> (ZPD) secara fisik, yaitu membimbing postur tangan siswa agar terbiasa mengendalikan busur las.</p>
        </div>
        <div class="card-article" style="border-top: 4px solid var(--kemendikbud-cyan);">
            <h3 style="color: var(--kemendikbud-blue); font-size: 1.2rem; margin-bottom: 1rem;">2. Pengalaman Menantang & Solusi</h3>
            <p style="color: var(--text-dark); line-height: 1.6; text-align: justify;">Ketakutan psikologis siswa terhadap panas dan percikan api las menghambat mereka memegang elektroda dengan rileks. Sebagai solusi, saya merombak strategi RPP dengan menambahkan sesi <i>dry run</i> (mengayunkan elektroda tanpa arus) sebelum mesin dinyalakan, serta memberikan pendampingan <i>hand-over-hand</i> (memandu gerakan tangan siswa secara langsung) saat pertama kali memantik busur.</p>
        </div>
        <div class="card-article" style="border-top: 4px solid var(--kemendikbud-cyan);">
            <h3 style="color: var(--kemendikbud-blue); font-size: 1.2rem; margin-bottom: 1rem;">3. Umpan Balik & Saran Konstruktif</h3>
            <p style="color: var(--text-dark); line-height: 1.6; text-align: justify;">Diskusi bersama praktisi dan pamong menekankan pentingnya umpan balik instan. Saya disarankan untuk mengevaluasi hasil las siswa setiap satu jalur (<i>bead</i>) selesai, jangan menunggu benda kerja penuh. Umpan balik langsung ini bertujuan agar siswa tidak mengulangi kesalahan gerakan berulang kali. Ini menjadi catatan emas untuk fase mandiri berikutnya.</p>
        </div>
    </div>
</div>
<script>
function switchTabEP2(tabId, btnElement) {
    // Hide all contents
    const contents = document.querySelectorAll('.ep2-tab-content');
    contents.forEach(el => el.style.display = 'none');
    
    // Remove active class from buttons in this specific tab-nav
    const navDiv = btnElement.parentElement;
    const btns = navDiv.querySelectorAll('.tab-btn');
    btns.forEach(b => b.classList.remove('active'));
    
    // Show selected and set active
    document.getElementById(tabId).style.display = 'block';
    btnElement.classList.add('active');
}
</script>
</div>
</section>
<!-- Filosofi Mengajar -->"""

# We need to replace from <!-- Refleksi Akhir PPL Terbimbing --> to <!-- Filosofi Mengajar -->
# Using regex to find the block
pattern = re.compile(r'<!-- Refleksi Akhir PPL Terbimbing -->.*?<!-- Filosofi Mengajar -->', re.DOTALL)
if pattern.search(content):
    new_html = pattern.sub(new_content, content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated successfully")
else:
    print("Could not find the block to replace")
