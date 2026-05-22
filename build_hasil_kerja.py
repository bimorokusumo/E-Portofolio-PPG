import os
import glob

pages = [
    {
        "file": "hasil-kerja-wawasan.html",
        "title": "Wawasan Bidang Teknik Mesin",
        "folder": "wawasan",
        "bagian": "TP",
        "icon": "⚙️",
        "konteks": "Karya siswa berupa peta konsep, ringkasan, dan laporan eksplorasi wawasan dunia kerja di bidang teknik mesin.",
        "tujuan": "Menilai sejauh mana siswa memahami ruang lingkup profesi dan peluang kerja di industri manufaktur.",
        "kelebihan": "Melatih kemampuan literasi dan riset mandiri; siswa belajar mensintesis informasi dari berbagai sumber.",
        "kekurangan": "Kedalaman analisis siswa sangat bervariasi tergantung kemampuan literasi awal masing-masing individu."
    },
    {
        "file": "hasil-kerja-k3.html",
        "title": "K3 dan Budaya Kerja",
        "folder": "k3",
        "bagian": "TP",
        "icon": "🛡️",
        "konteks": "Dokumentasi hasil observasi lapangan siswa terkait penerapan K3 dan budaya 5R di lingkungan bengkel sekolah.",
        "tujuan": "Membentuk kesadaran dan kebiasaan K3 sejak dini sebagai pondasi profesionalisme di dunia industri.",
        "kelebihan": "Hasil kerja bersifat kontekstual dan dapat diaplikasikan langsung; menumbuhkan tanggung jawab terhadap keselamatan.",
        "kekurangan": "Penilaian bersifat observasional sehingga membutuhkan rubrik yang sangat rinci agar hasilnya objektif."
    },
    {
        "file": "hasil-kerja-bahan.html",
        "title": "Pengetahuan Bahan",
        "folder": "bahan",
        "bagian": "TP",
        "icon": "🧱",
        "konteks": "Laporan identifikasi material logam dan non-logam, termasuk uji kekerasan sederhana dan pengamatan struktur bahan.",
        "tujuan": "Melatih kemampuan analisis material sehingga siswa mampu memilih bahan yang tepat untuk aplikasi tertentu.",
        "kelebihan": "Langsung berhubungan dengan kompetensi industri nyata; siswa belajar menghubungkan sifat bahan dengan fungsinya.",
        "kekurangan": "Keterbatasan alat uji material di bengkel sekolah membuat beberapa pengujian tidak dapat dilakukan secara mendalam."
    },
    {
        "file": "hasil-kerja-mekanik.html",
        "title": "Dasar Sistem Mekanik",
        "folder": "mekanik",
        "bagian": "TP",
        "icon": "🔧",
        "konteks": "Hasil perhitungan analitis dan laporan eksperimen siswa tentang sistem transmisi, gaya, torsi, dan mekanisme mekanik.",
        "tujuan": "Membuktikan penguasaan konsep mekanika terapan dan kemampuan berhitung siswa pada kondisi nyata.",
        "kelebihan": "Menggabungkan teori dan praktik secara terpadu; mendorong kemampuan berpikir rekayasa tingkat dasar.",
        "kekurangan": "Siswa dengan kemampuan matematika rendah seringkali kesulitan menyelesaikan analisis vektor dan rasio."
    },
    {
        "file": "hasil-kerja-tflm-wawasan.html",
        "title": "Wawasan Dunia Kerja Bidang Fabrikasi Logam",
        "folder": "tflm-wawasan",
        "bagian": "TFLM",
        "icon": "🌐",
        "konteks": "Presentasi dan laporan riset siswa tentang peta industri fabrikasi logam, prospek kerja, dan peluang wirausaha.",
        "tujuan": "Membangun motivasi siswa dengan memperlihatkan peluang nyata di industri fabrikasi logam dan manufaktur.",
        "kelebihan": "Membuka wawasan siswa tentang dunia kerja yang lebih luas; meningkatkan orientasi karir sejak dini.",
        "kekurangan": "Informasi yang diperoleh siswa terkadang kurang akurat karena keterbatasan sumber referensi yang tersedia."
    },
    {
        "file": "hasil-kerja-tflm-k3lh.html",
        "title": "K3LH Bidang Fabrikasi Logam",
        "folder": "tflm-k3lh",
        "bagian": "TFLM",
        "icon": "🦺",
        "konteks": "Dokumentasi inspeksi APD dan penerapan K3LH siswa di area pengelasan, pemotongan, dan penggerindaan logam.",
        "tujuan": "Menanamkan budaya keselamatan kerja yang tidak bisa dikompromikan sebagai fondasi praktik fabrikasi logam.",
        "kelebihan": "Langsung relevan dengan risiko nyata di bengkel las; membentuk habituasi keselamatan yang terstandar.",
        "kekurangan": "Beberapa siswa masih menganggap prosedur K3 sebagai formalitas dan bukan kebutuhan yang sesungguhnya."
    },
    {
        "file": "hasil-kerja-tflm-perkakas.html",
        "title": "Penggunaan Perkakas Bengkel",
        "folder": "tflm-perkakas",
        "bagian": "TFLM",
        "icon": "🛠️",
        "konteks": "Jobsheet dan dokumentasi foto penggunaan perkakas tangan (gerinda, kikir, pahat) sesuai SOP bengkel fabrikasi.",
        "tujuan": "Memastikan siswa dapat menggunakan perkakas dengan benar, efisien, dan sesuai standar keselamatan industri.",
        "kelebihan": "Hasil kerja sangat konkret dan terukur; memudahkan guru menilai ketepatan teknik dan kepatuhan SOP.",
        "kekurangan": "Jumlah perkakas yang terbatas menyebabkan antrian panjang dan mengurangi waktu praktik efektif siswa."
    },
    {
        "file": "hasil-kerja-tflm-smaw.html",
        "title": "Pengelasan SMAW Dasar",
        "folder": "tflm-smaw",
        "bagian": "TFLM",
        "icon": "⚡",
        "konteks": "Foto produk hasil las siswa (spesimen rigi-rigi las) beserta lembar inspeksi visual (VT) yang mereka isi sendiri.",
        "tujuan": "Menilai kualitas rigi-rigi las (kelurusan, lebar, konsistensi) sebagai indikator penguasaan teknik busur SMAW.",
        "kelebihan": "Hasil kerja berwujud produk logam nyata yang bisa diukur secara objektif menggunakan welding gauge.",
        "kekurangan": "Kelelahan fisik dan tekanan mental saat pengelasan pertama kali membuat konsistensi hasil antar siswa sangat bervariasi."
    }
]

TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hasil Kerja Siswa - {title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body style="background: var(--bg-light-gray);">
    <nav>
        <div class="nav-container">
            <a href="hasil-kerja.html" class="logo" style="text-decoration: none; display: flex; align-items: center; gap: 0.5rem; color: var(--text-dark);">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--kemendikbud-blue)"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>
                Kembali ke Menu Utama
            </a>
        </div>
    </nav>

    <!-- Header Section -->
    <header style="background: white; padding: 4rem 2rem 2rem; border-bottom: 1px solid var(--border-color); text-align: center; margin-bottom: 2rem;">
        <span style="font-size: 4rem; display: block; margin-bottom: 1rem;">📝</span>
        <h1 style="color: var(--kemendikbud-blue); margin-bottom: 0.5rem;">{title}</h1>
        <p style="color: var(--text-light); max-width: 600px; margin: 0 auto;">Galeri hasil kerja dan dokumentasi praktik siswa terkait materi pembelajaran.</p>
    </header>

    <!-- Split Layout: Photo (Left) & Analysis (Right) -->
    <section style="max-width: 1200px; margin: 0 auto; padding: 0 1rem 4rem;">
        <div class="split-layout align-start" style="gap: 3rem;">
            
            <!-- Left Side: Full Photo Gallery -->
            <div class="split-left" style="flex: 1.5;">
                <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); border: 1px solid var(--border-color);">
                    <h3 style="color: var(--kemendikbud-blue); margin-bottom: 1rem; border-bottom: 1px solid #eee; padding-bottom: 0.5rem;">📸 Bukti Fisik / Dokumentasi</h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        {gallery_html}
                    </div>
                </div>
            </div>

            <!-- Right Side: Full Analysis (Sama dengan card yang lain) -->
            <div class="split-right" style="flex: 1; position: sticky; top: 100px;">
                <div class="doc-card-content" style="background: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); border: 1px solid var(--border-color); padding: 1.5rem;">
                    <h4 style="margin-bottom: 1rem;">Analisis Hasil Kerja Siswa</h4>
                    <p style="margin-bottom: 1rem;">Detail analisis kontekstual terkait pembelajaran {title}.</p>
                    
                    <details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;" open>
                        <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                        <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                            <div><strong>Konteks:</strong> <br><span style="color: var(--text-light);">{konteks}</span></div>
                            <div><strong>Tujuan:</strong> <br><span style="color: var(--text-light);">{tujuan}</span></div>
                            <div><strong>Kelebihan:</strong> <br><span style="color: var(--text-light);">{kelebihan}</span></div>
                            <div><strong>Kekurangan:</strong> <br><span style="color: var(--text-light);">{kekurangan}</span></div>
                        </div>
                    </details>
                </div>
            </div>

        </div>
    </section>
    
    <footer>
        <p>&copy; 2026 Bimoro Kusumo. E-Portfolio PPG Universitas Sarjanawiyata Tamansiswa (UST).</p>
    </footer>
</body>
</html>
"""

def build_pages():
    for page in pages:
        folder_path = os.path.join("assets", "hasil-kerja", page["folder"])
        os.makedirs(folder_path, exist_ok=True)
        
        images = glob.glob(os.path.join(folder_path, "*.jpg")) + glob.glob(os.path.join(folder_path, "*.png"))
        gallery_html = ""
        
        if not images:
            gallery_html = f"""
            <div style="text-align: center; padding: 4rem 2rem; background: #f8faff; border-radius: 8px; border: 1px dashed #ccc;">
                <span style="font-size: 3rem; opacity: 0.5;">📸</span>
                <p style="margin-top: 1rem; color: #666;">Belum ada foto dokumentasi di folder <strong>assets/hasil-kerja/{page['folder']}/</strong></p>
            </div>
            """
        else:
            for img in sorted(images):
                web_path = img.replace("\\", "/")
                filename = os.path.basename(img)
                gallery_html += f"""
                <div style="border-radius: 8px; overflow: hidden; border: 1px solid #eee;">
                    <img src="{web_path}" alt="{filename}" style="width: 100%; height: auto; display: block; object-fit: contain;">
                </div>
                """
                
        html_content = TEMPLATE.format(
            title=page["title"],
            konteks=page["konteks"],
            tujuan=page["tujuan"],
            kelebihan=page["kelebihan"],
            kekurangan=page["kekurangan"],
            gallery_html=gallery_html
        )
        
        with open(page["file"], "w", encoding="utf-8") as f:
            f.write(html_content)
    print("Generated all 8 individual pages.")

if __name__ == "__main__":
    build_pages()
