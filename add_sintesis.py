with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sintesis_html = """        <div class="sintesis-container">
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

# Find where to insert: right before `    </section>\n\n    <!-- 4. Lampiran Penilaian -->`
target = '    </section>\n\n    <!-- 4. Lampiran Penilaian -->'
if target in html:
    html = html.replace(target, '\n' + sintesis_html + target)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Sintesis HTML added.")
else:
    print("Could not find insertion point.")

sintesis_css = """
/* Sintesis Container */
.sintesis-container {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border-radius: 24px;
    padding: 3.5rem;
    margin-top: 4rem;
    max-width: 1160px;
    margin-left: auto;
    margin-right: auto;
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: 3rem;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    color: #f8fafc;
}

.sintesis-left {
    display: flex;
    flex-direction: column;
    text-align: left;
}

.sintesis-tag {
    font-size: 0.8rem;
    letter-spacing: 3px;
    color: #34d399; /* emerald accent */
    text-transform: uppercase;
    margin-bottom: 1rem;
    font-weight: 600;
}

.sintesis-left h3 {
    font-size: 2.2rem;
    line-height: 1.3;
    margin-top: 0;
    margin-bottom: 1.5rem;
    color: #f8fafc;
}

.sintesis-left p {
    color: #94a3b8;
    font-size: 1.05rem;
    line-height: 1.7;
    margin-bottom: 0;
}

.sintesis-right {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    text-align: left;
}

.sintesis-box {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 1.8rem;
    transition: all 0.3s ease;
}

.sintesis-box:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(52, 211, 153, 0.3);
    transform: translateY(-3px);
}

.sintesis-box h4 {
    color: #34d399;
    font-size: 0.9rem;
    letter-spacing: 2px;
    margin-top: 0;
    margin-bottom: 1rem;
    text-transform: uppercase;
    font-weight: 700;
}

.sintesis-box p {
    color: #cbd5e1;
    font-size: 0.95rem;
    line-height: 1.6;
    margin: 0;
}

@media (max-width: 992px) {
    .sintesis-container {
        grid-template-columns: 1fr;
        padding: 2.5rem 1.5rem;
        gap: 2rem;
    }
    .sintesis-right {
        grid-template-columns: 1fr;
    }
    .sintesis-left h3 {
        font-size: 1.8rem;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(sintesis_css)

print("Sintesis CSS added.")
