with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

subtitles = [
    '<p class="chooser-subtitle">Silakan pilih e-portfolio yang ingin Anda lihat</p>',
    '<p style="text-align: justify; color: var(--text-light); margin-bottom: 2rem;">Perjalanan karir dan pengalaman di bidang industri serta pendidikan.</p>',
    '<p style="text-align: justify; color: var(--text-light); margin-bottom: 2rem;">Latar belakang pendidikan formal.</p>',
    '<p style="color: var(--text-light); margin-bottom: 2rem;">Berbagai keterampilan teknis dan pedagogik yang mendukung profesionalisme.</p>',
    '<p style="text-align: justify; color: var(--text-light); margin-bottom: 2rem;">Inilah bukti pengembangan diri saya yang terus ingin belajar untuk membentuk pribadi yang maju sebagai penunjang menjadi seorang guru sebagai role model.</p>',
    '<p style="color: var(--text-light); margin-bottom: 2rem;">Dokumentasi berikut merupakan kumpulan kegiatan selama proses pembelajaran berlangsung yang mencerminkan berbagai aktivitas peserta didik dan guru dalam mencapai tujuan pembelajaran. Setiap dokumentasi menampilkan tahapan pembelajaran mulai dari penyampaian materi, diskusi, praktik, hingga refleksi pembelajaran sebagai bentuk implementasi kegiatan belajar yang aktif, kolaboratif, dan bermakna.</p>',
    '<p class="analisis-desc">Refleksi terhadap proses penyusunan, dasar pedagogis, faktor penerapan, dan penyesuaian produk pembelajaran untuk kebutuhan kelas yang berbeda.</p>',
    '<p style="text-align: justify; color: var(--text-light); margin-bottom: 2rem;">Karakter, kompetensi, dan visi pendidik masa depan.</p>',
    '<p style="text-align: justify; color: var(--text-light); margin-bottom: 3rem;">3 pertanyaan refleksi mendalam tentang pembelajaran, tantangan & umpan balik selama PPL.</p>',
    '<p style="text-align: justify; color: var(--text-light); margin-bottom: 3rem;">Prinsip, keyakinan, dan nilai yang mendasari praktik pengajaran saya.</p>'
]

for sub in subtitles:
    if sub in content:
        content = content.replace(sub, '')
    else:
        print(f"Warning: Could not find exact string:\n{sub}\n")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Subtitles successfully removed.")
