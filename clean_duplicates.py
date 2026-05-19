import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to identify all `<div class="sintesis-container">...</div>` blocks.
# Let's find the exact regex pattern for sintesis-container block.
pattern = r'\s*<div class="sintesis-container">.*?</div>\s*(?=</section>)'

# Wait, let's be careful with non-greedy .*? matching across multiple divs.
# Since sintesis-container contains nested divs, regex .*? might stop at the first </div>.
# Instead of regex, let's find the exact literal string of the sintesis block.

sintesis_block = """        <div class="sintesis-container">
            <div class="sintesis-left">
                <span class="sintesis-tag">SINTESIS</span>
                <h3>Arah Perbaikan Produk Pembelajaran</h3>
                <p>Analisis ini menunjukkan bahwa produk pembelajaran perlu kuat secara rancangan, mudah dijalankan, dan cukup lentur untuk menyesuaikan kelas yang berbeda.</p>
            </div>
            <div class="sintesis-right">
                <div class="sintesis-box">
                    <h4>RPP</h4>
                    <p>RPP perlu menjadi peta pembelajaran yang jelas, tetapi tetap menyediakan ruang adaptasi. Bagian tujuan, kegiatan inti, asesmen, dan refleksi harus saling terhubung agar guru tidak hanya menjalankan langkah, tetapi memahami alasan pedagogis di balik setiap langkah.</p>
                </div>
                <div class="sintesis-box">
                    <h4>MEDIA</h4>
                    <p>Media perlu memperjelas konsep inti, memancing perhatian, dan membantu siswa melihat contoh sebelum masuk ke praktik. Media yang baik tidak hanya menarik secara visual, tetapi juga mengurangi miskonsepsi dan mempercepat pemahaman awal.</p>
                </div>
                <div class="sintesis-box">
                    <h4>LKM</h4>
                    <p>LKM perlu memandu langkah kerja secara bertahap agar siswa dapat belajar mandiri sambil tetap memiliki arah yang jelas. Petunjuk, contoh, ruang jawaban, dan urutan tugas harus membantu siswa berpikir, bukan sekadar mengisi lembar kerja.</p>
                </div>
                <div class="sintesis-box">
                    <h4>ASESMEN</h4>
                    <p>Asesmen tidak: hanya menilai hasil akhir, tetapi juga membaca proses, kesulitan, dan kebutuhan penguatan berikutnya. Hasil asesmen perlu menjadi dasar revisi media, perbaikan LKM, dan penguatan materi pada pertemuan berikutnya.</p>
                </div>
            </div>
        </div>"""

# Wait, let's check if there is a typo in my string: "Asesmen tidak: hanya" vs "Asesmen tidak hanya".
# Let's check the exact string in index.html first.
