with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Exact block string to remove from unwanted places
block = """        <div class="sintesis-container">
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
                    <p>Asesmen tidak hanya menilai hasil akhir, tetapi juga membaca proses, kesulitan, dan kebutuhan penguatan berikutnya. Hasil asesmen perlu menjadi dasar revisi media, perbaikan LKM, dan penguatan materi pada pertemuan berikutnya.</p>
                </div>
            </div>
        </div>
"""

# Split by the start of analisis-produk section
parts = content.split('<section id="analisis-produk"')

if len(parts) == 2:
    before = parts[0].replace(block, '')
    
    # In the second part (analisis-produk and after), keep the first occurrence, remove subsequent
    sub_parts = parts[1].split(block)
    
    if len(sub_parts) >= 2:
        # Reconstruct keeping the first block
        after = sub_parts[0] + block + "".join(sub_parts[1:])
        
        new_content = before + '<section id="analisis-produk"' + after
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Duplicates successfully removed. Exactly 1 instance remains in analisis-produk.")
    else:
        print("Could not find block in second part.")
else:
    print("Could not split by analisis-produk section.")
