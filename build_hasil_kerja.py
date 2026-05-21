#!/usr/bin/env python3
"""
Script untuk membuat semua halaman hasil-kerja-*.html
dengan galeri foto premium yang tinggal taruh foto ke folder.
"""

TEMPLATE = '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hasil Kerja Siswa - {title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        .page-hero {{
            background: linear-gradient(135deg, #1565C0 0%, #0D47A1 60%, #1a237e 100%);
            color: white;
            padding: 5rem 2rem 3rem;
            text-align: center;
        }}
        .page-hero .breadcrumb {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            font-size: 0.85rem;
            opacity: 0.8;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }}
        .page-hero .breadcrumb a {{ color: white; text-decoration: none; }}
        .page-hero .breadcrumb a:hover {{ text-decoration: underline; }}
        .page-hero h1 {{ font-size: 2.2rem; font-weight: 700; margin-bottom: 0.75rem; line-height: 1.3; }}
        .page-hero p {{ font-size: 1rem; opacity: 0.85; max-width: 600px; margin: 0 auto; }}
        .analysis-box {{
            max-width: 900px;
            margin: 2.5rem auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            overflow: hidden;
        }}
        .analysis-box-header {{
            background: linear-gradient(90deg, #1565C0, #0D47A1);
            color: white;
            padding: 1rem 1.5rem;
            font-weight: 600;
            font-size: 0.95rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .analysis-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0;
        }}
        .analysis-item {{
            padding: 1.2rem 1.5rem;
            border-bottom: 1px solid #f0f0f0;
            border-right: 1px solid #f0f0f0;
        }}
        .analysis-item:nth-child(2n) {{ border-right: none; }}
        .analysis-item:nth-last-child(-n+2) {{ border-bottom: none; }}
        .analysis-item strong {{ display: block; color: #1565C0; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; }}
        .analysis-item p {{ font-size: 0.88rem; color: #555; line-height: 1.6; margin: 0; }}
        .gallery-container {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 2rem;
        }}
        .gallery-title {{
            text-align: center;
            font-size: 1.5rem;
            font-weight: 700;
            color: #1565C0;
            margin-bottom: 0.5rem;
        }}
        .gallery-subtitle {{
            text-align: center;
            color: #888;
            font-size: 0.88rem;
            margin-bottom: 2rem;
        }}
        .gallery-subtitle code {{ background: #f0f4ff; padding: 0.2rem 0.5rem; border-radius: 4px; color: #1565C0; }}
        .photo-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 1.25rem;
        }}
        .photo-card {{
            border-radius: 10px;
            overflow: hidden;
            background: white;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            transition: transform 0.25s ease, box-shadow 0.25s ease;
            cursor: pointer;
        }}
        .photo-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 24px rgba(0,0,0,0.14);
        }}
        .photo-card img {{
            width: 100%;
            height: 200px;
            object-fit: cover;
            display: block;
        }}
        .photo-card .photo-label {{
            padding: 0.75rem 1rem;
            font-size: 0.85rem;
            color: #444;
            font-weight: 500;
            border-top: 1px solid #f0f0f0;
        }}
        .empty-state {{
            text-align: center;
            padding: 4rem 2rem;
            color: #aaa;
            background: white;
            border-radius: 12px;
            border: 2px dashed #e0e0e0;
        }}
        .empty-state .icon {{ font-size: 3.5rem; margin-bottom: 1rem; }}
        .empty-state h3 {{ font-size: 1.1rem; color: #999; margin-bottom: 0.5rem; }}
        .empty-state p {{ font-size: 0.88rem; line-height: 1.7; }}
        .empty-state code {{ background: #f0f4ff; padding: 0.2rem 0.5rem; border-radius: 4px; color: #1565C0; font-size: 0.82rem; }}
        .lightbox-overlay {{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.88);
            z-index: 9999;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }}
        .lightbox-overlay.active {{ display: flex; }}
        .lightbox-content {{ position: relative; max-width: 90vw; max-height: 90vh; }}
        .lightbox-content img {{
            max-width: 100%;
            max-height: 85vh;
            border-radius: 8px;
            display: block;
            box-shadow: 0 8px 40px rgba(0,0,0,0.5);
        }}
        .lightbox-close {{
            position: absolute;
            top: -2.5rem;
            right: 0;
            color: white;
            font-size: 2rem;
            cursor: pointer;
            background: none;
            border: none;
            line-height: 1;
        }}
        .lightbox-caption {{
            color: white;
            text-align: center;
            margin-top: 0.75rem;
            font-size: 0.9rem;
            opacity: 0.85;
        }}
        .back-area {{
            max-width: 1100px;
            margin: 0 auto;
            padding: 0 2rem 3rem;
            text-align: center;
        }}
        @media (max-width: 640px) {{
            .analysis-grid {{ grid-template-columns: 1fr; }}
            .analysis-item {{ border-right: none; }}
            .photo-grid {{ grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 0.75rem; }}
            .photo-card img {{ height: 150px; }}
            .page-hero h1 {{ font-size: 1.6rem; }}
        }}
    </style>
</head>
<body>
    <nav>
        <div class="nav-container">
            <a href="hasil-kerja.html" class="logo">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--kemendikbud-blue)"><path d="m15 18-6-6 6-6"/></svg>
                Kembali ke Menu Hasil Kerja
            </a>
        </div>
    </nav>

    <div class="page-hero">
        <div class="breadcrumb">
            <a href="hasil-kerja.html">Hasil Kerja Siswa</a>
            <span>›</span>
            <span>{bagian}</span>
            <span>›</span>
            <span>{title}</span>
        </div>
        <h1>{icon} {title}</h1>
        <p>Dokumentasi hasil kerja nyata peserta didik selama proses pembelajaran berlangsung</p>
    </div>

    <div style="background: #f8faff; padding: 2rem 1rem;">
        <div class="analysis-box">
            <div class="analysis-box-header">📝 Analisis Artefak Hasil Kerja Siswa</div>
            <div class="analysis-grid">
                <div class="analysis-item">
                    <strong>🎯 Konteks</strong>
                    <p>{konteks}</p>
                </div>
                <div class="analysis-item">
                    <strong>💡 Tujuan</strong>
                    <p>{tujuan}</p>
                </div>
                <div class="analysis-item">
                    <strong>✅ Kelebihan</strong>
                    <p>{kelebihan}</p>
                </div>
                <div class="analysis-item">
                    <strong>⚠️ Kekurangan</strong>
                    <p>{kekurangan}</p>
                </div>
            </div>
        </div>
    </div>

    <div style="background: #f8faff; padding-bottom: 1rem;">
        <div class="gallery-container">
            <h2 class="gallery-title">🖼️ Galeri Foto Hasil Kerja</h2>
            <p class="gallery-subtitle">
                Folder foto: <code>assets/hasil-kerja/{folder}/</code> &nbsp;·&nbsp; Klik foto untuk memperbesar
            </p>

            <!-- ============================================================
                 CARA MENAMBAH FOTO:
                 1. Simpan foto ke folder: assets/hasil-kerja/{folder}/
                 2. Duplikat blok <div class="photo-card"> di bawah ini
                 3. Ganti "NAMA-FILE.jpg" dan keterangannya
                 ============================================================ -->

            <div class="photo-grid" id="photoGrid">

                <!-- CONTOH FORMAT (hapus tanda komentar dan isi nama file):
                <div class="photo-card" onclick="openLightbox(this)">
                    <img src="assets/hasil-kerja/{folder}/NAMA-FILE.jpg" alt="Keterangan foto">
                    <div class="photo-label">Keterangan singkat foto</div>
                </div>
                -->

            </div>

            <div class="empty-state" id="emptyState">
                <div class="icon">📂</div>
                <h3>Belum ada foto</h3>
                <p>
                    Simpan foto ke folder <code>assets/hasil-kerja/{folder}/</code><br>
                    lalu tambahkan blok foto di dalam <code>#photoGrid</code> sesuai<br>
                    petunjuk komentar di HTML.
                </p>
            </div>
        </div>
    </div>

    <div class="back-area">
        <a href="hasil-kerja.html" class="btn-primary">← Kembali ke Menu</a>
    </div>

    <footer>
        <p>&copy; 2026 Bimoro Kusumo. E-Portfolio PPG Universitas Sarjanawiyata Tamansiswa (UST).</p>
    </footer>

    <div class="lightbox-overlay" id="lightbox" onclick="closeLightbox(event)">
        <div class="lightbox-content">
            <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
            <img id="lightboxImg" src="" alt="">
            <div class="lightbox-caption" id="lightboxCaption"></div>
        </div>
    </div>

    <script>
        const grid = document.getElementById('photoGrid');
        const emptyState = document.getElementById('emptyState');
        const cards = grid.querySelectorAll('.photo-card');
        emptyState.style.display = cards.length === 0 ? 'block' : 'none';

        function openLightbox(card) {{
            const img = card.querySelector('img');
            const label = card.querySelector('.photo-label');
            document.getElementById('lightboxImg').src = img.src;
            document.getElementById('lightboxImg').alt = img.alt;
            document.getElementById('lightboxCaption').textContent = label ? label.textContent : '';
            document.getElementById('lightbox').classList.add('active');
            document.body.style.overflow = 'hidden';
        }}
        function closeLightbox(e) {{
            if (!e || e.target === document.getElementById('lightbox') || e.target.classList.contains('lightbox-close')) {{
                document.getElementById('lightbox').classList.remove('active');
                document.body.style.overflow = '';
            }}
        }}
        document.addEventListener('keydown', (e) => {{ if (e.key === 'Escape') closeLightbox(); }});
    </script>
</body>
</html>'''

# Definisi semua halaman
pages = [
    {
        "file": "hasil-kerja-wawasan.html",
        "title": "Wawasan Bidang Teknik Mesin",
        "icon": "⚙️",
        "bagian": "Teknik Pemesinan (TP)",
        "folder": "wawasan",
        "konteks": "Karya siswa berupa peta konsep, ringkasan, dan laporan eksplorasi wawasan dunia kerja di bidang teknik mesin.",
        "tujuan": "Menilai sejauh mana siswa memahami ruang lingkup profesi dan peluang kerja di industri manufaktur.",
        "kelebihan": "Melatih kemampuan literasi dan riset mandiri; siswa belajar mensintesis informasi dari berbagai sumber.",
        "kekurangan": "Kedalaman analisis siswa sangat bervariasi tergantung kemampuan literasi awal masing-masing individu.",
    },
    {
        "file": "hasil-kerja-k3.html",
        "title": "K3 dan Budaya Kerja",
        "icon": "🛡️",
        "bagian": "Teknik Pemesinan (TP)",
        "folder": "k3",
        "konteks": "Dokumentasi hasil observasi lapangan siswa terkait penerapan K3 dan budaya 5R di lingkungan bengkel sekolah.",
        "tujuan": "Membentuk kesadaran dan kebiasaan K3 sejak dini sebagai pondasi profesionalisme di dunia industri.",
        "kelebihan": "Hasil kerja bersifat kontekstual dan dapat diaplikasikan langsung; menumbuhkan tanggung jawab terhadap keselamatan.",
        "kekurangan": "Penilaian bersifat observasional sehingga membutuhkan rubrik yang sangat rinci agar hasilnya objektif.",
    },
    {
        "file": "hasil-kerja-bahan.html",
        "title": "Pengetahuan Bahan",
        "icon": "🧱",
        "bagian": "Teknik Pemesinan (TP)",
        "folder": "bahan",
        "konteks": "Laporan identifikasi material logam dan non-logam, termasuk uji kekerasan sederhana dan pengamatan struktur bahan.",
        "tujuan": "Melatih kemampuan analisis material sehingga siswa mampu memilih bahan yang tepat untuk aplikasi tertentu.",
        "kelebihan": "Langsung berhubungan dengan kompetensi industri nyata; siswa belajar menghubungkan sifat bahan dengan fungsinya.",
        "kekurangan": "Keterbatasan alat uji material di bengkel sekolah membuat beberapa pengujian tidak dapat dilakukan secara mendalam.",
    },
    {
        "file": "hasil-kerja-mekanik.html",
        "title": "Dasar Sistem Mekanik",
        "icon": "🔧",
        "bagian": "Teknik Pemesinan (TP)",
        "folder": "mekanik",
        "konteks": "Hasil perhitungan analitis dan laporan eksperimen siswa tentang sistem transmisi, gaya, torsi, dan mekanisme mekanik.",
        "tujuan": "Membuktikan penguasaan konsep mekanika terapan dan kemampuan berhitung siswa pada kondisi nyata.",
        "kelebihan": "Menggabungkan teori dan praktik secara terpadu; mendorong kemampuan berpikir rekayasa tingkat dasar.",
        "kekurangan": "Siswa dengan kemampuan matematika rendah seringkali kesulitan menyelesaikan analisis vektor dan rasio.",
    },
    {
        "file": "hasil-kerja-tflm-wawasan.html",
        "title": "Wawasan Dunia Kerja Bidang Fabrikasi Logam",
        "icon": "🌐",
        "bagian": "Teknik Fabrikasi Logam dan Manufaktur (TFLM)",
        "folder": "tflm-wawasan",
        "konteks": "Presentasi dan laporan riset siswa tentang peta industri fabrikasi logam, prospek kerja, dan peluang wirausaha.",
        "tujuan": "Membangun motivasi siswa dengan memperlihatkan peluang nyata di industri fabrikasi logam dan manufaktur.",
        "kelebihan": "Membuka wawasan siswa tentang dunia kerja yang lebih luas; meningkatkan orientasi karir sejak dini.",
        "kekurangan": "Informasi yang diperoleh siswa terkadang kurang akurat karena keterbatasan sumber referensi yang tersedia.",
    },
    {
        "file": "hasil-kerja-tflm-k3lh.html",
        "title": "K3LH Bidang Fabrikasi Logam",
        "icon": "🦺",
        "bagian": "Teknik Fabrikasi Logam dan Manufaktur (TFLM)",
        "folder": "tflm-k3lh",
        "konteks": "Dokumentasi inspeksi APD dan penerapan K3LH siswa di area pengelasan, pemotongan, dan penggerindaan logam.",
        "tujuan": "Menanamkan budaya keselamatan kerja yang tidak bisa dikompromikan sebagai fondasi praktik fabrikasi logam.",
        "kelebihan": "Langsung relevan dengan risiko nyata di bengkel las; membentuk habituasi keselamatan yang terstandar.",
        "kekurangan": "Beberapa siswa masih menganggap prosedur K3 sebagai formalitas dan bukan kebutuhan yang sesungguhnya.",
    },
    {
        "file": "hasil-kerja-tflm-perkakas.html",
        "title": "Penggunaan Perkakas Bengkel",
        "icon": "🛠️",
        "bagian": "Teknik Fabrikasi Logam dan Manufaktur (TFLM)",
        "folder": "tflm-perkakas",
        "konteks": "Jobsheet dan dokumentasi foto penggunaan perkakas tangan (gerinda, kikir, pahat) sesuai SOP bengkel fabrikasi.",
        "tujuan": "Memastikan siswa dapat menggunakan perkakas dengan benar, efisien, dan sesuai standar keselamatan industri.",
        "kelebihan": "Hasil kerja sangat konkret dan terukur; memudahkan guru menilai ketepatan teknik dan kepatuhan SOP.",
        "kekurangan": "Jumlah perkakas yang terbatas menyebabkan antrian panjang dan mengurangi waktu praktik efektif siswa.",
    },
    {
        "file": "hasil-kerja-tflm-smaw.html",
        "title": "Pengelasan SMAW Dasar",
        "icon": "⚡",
        "bagian": "Teknik Fabrikasi Logam dan Manufaktur (TFLM)",
        "folder": "tflm-smaw",
        "konteks": "Foto produk hasil las siswa (spesimen rigi-rigi las) beserta lembar inspeksi visual (VT) yang mereka isi sendiri.",
        "tujuan": "Menilai kualitas rigi-rigi las (kelurusan, lebar, konsistensi) sebagai indikator penguasaan teknik busur SMAW.",
        "kelebihan": "Hasil kerja berwujud produk logam nyata yang bisa diukur secara objektif menggunakan welding gauge.",
        "kekurangan": "Kelelahan fisik dan tekanan mental saat pengelasan pertama kali membuat konsistensi hasil antar siswa sangat bervariasi.",
    },
]

import os

base_dir = "/Users/macbookpro2017/Desktop/PPG 2025/KULIAH PPG/UTS/E-Portofolio-PPG"

for page in pages:
    content = TEMPLATE.format(
        title=page["title"],
        icon=page["icon"],
        bagian=page["bagian"],
        folder=page["folder"],
        konteks=page["konteks"],
        tujuan=page["tujuan"],
        kelebihan=page["kelebihan"],
        kekurangan=page["kekurangan"],
    )
    filepath = os.path.join(base_dir, page["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Dibuat: {page['file']}")

print("\n✅ Semua halaman hasil kerja berhasil dibuat!")
print("\nFolder foto yang tersedia:")
folders = ["wawasan", "k3", "bahan", "mekanik", "manufaktur",
           "tflm-wawasan", "tflm-k3lh", "tflm-perkakas", "tflm-smaw",
           "siklus-1", "siklus-2", "siklus-3"]
for f in folders:
    path = os.path.join(base_dir, "assets/hasil-kerja", f)
    os.makedirs(path, exist_ok=True)
    print(f"  📁 assets/hasil-kerja/{f}/")
