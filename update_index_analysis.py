import os
from bs4 import BeautifulSoup
import re
import shutil

# Backup index.html
shutil.copy('index.html', 'index.html.backup')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

def get_analysis_for_title(title):
    title = title.lower()
    
    # Defaults
    konteks = "Artefak ini disusun berdasarkan hasil telaah karakteristik siswa di kelas vokasi, dengan mempertimbangkan kesiapan belajar dan kebutuhan industri."
    tujuan = "Menjadi panduan dan fasilitas belajar yang efektif untuk mencapai tujuan pembelajaran, selaras dengan filosofi KHD untuk menuntun siswa sesuai kodratnya."
    kelebihan = "Sistematis, terstruktur, dan menggunakan pendekatan yang relevan dengan pembelajaran abad 21 serta kebutuhan dunia kerja (DUDI)."
    kekurangan = "Masih membutuhkan penyesuaian berkelanjutan saat diterapkan pada kelas dengan tingkat pemahaman awal yang sangat heterogen."

    # RPP
    if 'rpp' in title:
        if 'manufaktur' in title:
            konteks = "RPP ini disusun khusus untuk kelas manufaktur dengan meninjau hasil asesmen diagnostik awal mengenai pemahaman mesin perkakas dasar."
            tujuan = "Memberikan arah (scaffolding) yang jelas bagi guru agar pembelajaran mesin manufaktur berjalan terukur, aman, dan berpusat pada murid."
            kelebihan = "Mengintegrasikan aspek K3 secara eksplisit dalam setiap langkah pembelajaran praktik, menyeimbangkan teori dan aktivitas bengkel."
            kekurangan = "Estimasi waktu pada RPP terkadang kurang fleksibel menghadapi trouble-shooting mesin yang sering terjadi di luar dugaan saat praktikum."
        elif 'mekanik' in title:
            konteks = "Disusun sebagai panduan pembelajaran dasar sistem mekanik, merespons kebutuhan siswa akan pemahaman kinematika sebelum praktik bengkel."
            tujuan = "Memastikan alur pengajaran dari konsep abstrak (gaya, momen) menuju aplikasi nyata pada mesin dapat dilalui siswa secara bertahap."
            kelebihan = "Menerapkan alur Understanding by Design (UbD) sehingga asesmen dan kegiatan sangat sinkron dengan capaian akhir mekanika dasar."
            kekurangan = "Kurangnya simulasi digital dalam RPP ini membuat guru harus bekerja ekstra dalam mendemonstrasikan pergerakan mekanik di kelas."
        elif 'smaw' in title:
            konteks = "Dirancang untuk PPL materi Pengelasan SMAW Dasar, di mana resiko kecelakaan kerja cukup tinggi sehingga butuh perencanaan matang."
            tujuan = "Menuntun siswa menguasai teknik dasar pengelasan dengan benar dan aman, mewujudkan peran guru sebagai 'pamong' di bengkel."
            kelebihan = "Fokus pada Project-Based Learning yang mengarahkan siswa menghasilkan sambungan las yang bisa langsung dievaluasi (visual check)."
            kekurangan = "Rasio jumlah mesin las dan siswa yang kurang ideal membuat skenario RPP harus terus dimodifikasi menggunakan metode shift."
    
    # MEDIA
    elif 'media' in title or 'bubut' in title or ('mekanik' in title and 'dasar' in title and 'rpp' not in title and 'lkm' not in title and 'bahan' not in title):
        if 'bubut' in title:
            konteks = "Media visual ini dibuat karena siswa kesulitan membayangkan proses pemakanan (cutting) di dalam mesin bubut jika hanya dari penjelasan lisan."
            tujuan = "Menghadirkan visualisasi yang konkret (Ing Ngarso Sung Tulodo) mengenai operasional mesin bubut sebelum siswa memegang mesin asli."
            kelebihan = "Terdapat ilustrasi keamanan kerja dan parameter potong yang sangat mudah dipahami oleh gaya belajar visual."
            kekurangan = "Tidak interaktif; siswa tidak bisa mensimulasikan parameter potong langsung dari media ini, sehingga tetap butuh mesin fisik."
        elif 'mekanik' in title:
            konteks = "Media presentasi untuk menjembatani konsep gaya dan torsi yang tak kasat mata agar dapat dipahami secara logis oleh siswa SMK."
            tujuan = "Meningkatkan engagement kelas melalui animasi pergerakan roda gigi dan sistem transmisi mekanik."
            kelebihan = "Mampu memvisualisasikan cara kerja sistem mekanik kompleks dengan animasi yang menyederhanakan pemahaman kognitif siswa."
            kekurangan = "Membutuhkan proyektor dan kondisi pencahayaan kelas yang baik agar detail mekanik pada media terlihat jelas oleh siswa di belakang."
        elif 'smaw' in title:
            konteks = "Dikembangkan untuk memberikan contoh nyata ayunan elektroda dan penetrasi las SMAW yang sulit dilihat langsung karena cahaya silau."
            tujuan = "Memfasilitasi siswa melihat secara 'micro' bagaimana logam cair menyatu, sesuatu yang mustahil dilihat jelas saat demonstrasi langsung."
            kelebihan = "Menggunakan rekaman jarak dekat (macro) proses pengelasan yang sangat efektif mengurangi kesalahan posisi tangan siswa."
            kekurangan = "Tidak bisa menggantikan feel/getaran elektroda yang hanya bisa dirasakan langsung oleh tangan siswa saat praktikum."

    # LKM / LKS
    elif 'lkm' in title or 'lks' in title or 'asesmen' in title or 'spesifikasi' in title or 'penyiapan' in title or 'identifikasi' in title or 'posisi pengelasan' in title or 'pemeriksaan' in title:
        if 'manufaktur' in title:
            konteks = "LKM ini diturunkan dari RPP manufaktur untuk menjadi lembar kontrol aktivitas siswa dari persiapan bahan hingga pengoperasian mesin."
            tujuan = "Membangun kemandirian belajar (kemerdekaan) di mana siswa secara aktif mengecek parameter kerjanya sendiri tanpa harus selalu disuapi instruksi."
            kelebihan = "Menyediakan rubrik penilaian (go/no-go) yang membiasakan siswa dengan standar Quality Control industri manufaktur."
            kekurangan = "Banyaknya form isian pada LKM terkadang membuat siswa merasa terbebani secara administratif sebelum mulai memegang mesin."
        elif 'mekanik' in title:
            konteks = "LKM berbasis inkuiri ini dibuat untuk melatih nalar kritis siswa saat menghitung rasio transmisi dan gaya mekanik."
            tujuan = "Menggeser paradigma belajar dari 'menghafal rumus' menjadi 'menemukan relasi' antar komponen mekanik."
            kelebihan = "Mendorong kolaborasi dan diskusi antar teman sejawat dalam menyelesaikan problem set perancangan mekanik."
            kekurangan = "Siswa dengan kemampuan numerasi rendah membutuhkan scaffolding dan waktu yang jauh lebih lama untuk menyelesaikan LKM ini."
        elif 'smaw' in title or 'spesifikasi' in title or 'penyiapan' in title or 'identifikasi' in title or 'posisi' in title or 'pemeriksaan' in title:
            konteks = "LKM/Jobsheet praktikum las SMAW disusun spesifik per kompetensi dasar (seperti penyiapan mesin, identifikasi elektroda, hingga inspeksi visual)."
            tujuan = "Memberikan pedoman langkah demi langkah (SOP) untuk memastikan keselamatan dan urutan kerja pengelasan berjalan sesuai standar WPS."
            kelebihan = "Disusun sangat ringkas, laminasi anti kotor, dan berisi checkpoint keselamatan (K3) pada setiap tahapan krusial."
            kekurangan = "Kurang mengeksplorasi 'troubleshooting'; ketika hasil las cacat, LKM tidak memberikan panduan analisis akar masalah secara mendalam."

    # BAHAN AJAR
    elif 'bahan ajar' in title:
        konteks = "Bahan ajar ini dikompilasi sebagai referensi tekstual utama siswa menghadapi minimnya literatur buku cetak vokasi yang update di perpustakaan."
        tujuan = "Menjadi sumber literasi mandiri yang bisa diakses kapan saja untuk memperkuat fondasi teori sebelum ujian atau praktikum."
        kelebihan = "Materi dikemas dengan bahasa yang relevan untuk anak muda dan diperkaya dengan glosarium istilah industri permesinan."
        kekurangan = "Ukurannya (jumlah halaman) cukup tebal, sehingga minat baca siswa SMK yang umumnya rendah menjadi tantangan tersendiri."

    # VIDEO
    elif 'video' in title:
        konteks = "Direkam secara langsung saat PPL atau sebagai video tutorial asinkronus untuk mengatasi keterbatasan waktu tatap muka di bengkel."
        tujuan = "Menjadi model pembelajaran (Tut Wuri Handayani) yang dapat diputar ulang oleh siswa kapanpun mereka merasa ragu dengan langkah kerja."
        kelebihan = "Sangat disukai siswa karena sifatnya yang audio-visual dan memuat contoh dari gurunya sendiri, sehingga kedekatan emosional (bonding) terbangun."
        kekurangan = "Kualitas audio kadang kurang maksimal akibat bisingnya suara mesin gerinda dan aktivitas bengkel saat perekaman."

    return konteks, tujuan, kelebihan, kekurangan


cards = soup.select('.doc-card-content')
updated_count = 0

for card in cards:
    h4 = card.find('h4')
    if not h4:
        continue
    
    title = h4.get_text(strip=True)
    details = card.find('details')
    
    if details:
        divs = details.find_all('div', recursive=False)
        # Inside details, there is a container div
        if len(divs) == 1:
            container = divs[0]
            inner_divs = container.find_all('div', recursive=False)
            if len(inner_divs) >= 4:
                konteks, tujuan, kelebihan, kekurangan = get_analysis_for_title(title)
                
                # Update Konteks
                span_konteks = inner_divs[0].find('span')
                if span_konteks: span_konteks.string = konteks
                
                # Update Tujuan
                span_tujuan = inner_divs[1].find('span')
                if span_tujuan: span_tujuan.string = tujuan
                
                # Update Kelebihan
                span_kelebihan = inner_divs[2].find('span')
                if span_kelebihan: span_kelebihan.string = kelebihan
                
                # Update Kekurangan
                span_kekurangan = inner_divs[3].find('span')
                if span_kekurangan: span_kekurangan.string = kekurangan
                
                updated_count += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"Successfully updated {updated_count} artifact analysis sections in index.html.")
