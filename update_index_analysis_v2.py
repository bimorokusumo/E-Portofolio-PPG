import os
from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

def get_unique_analysis(title):
    title_lower = title.lower()
    
    # --- RPP ---
    if "rpp teknik dasar produksi bidang manufaktur" in title_lower:
        return (
            "Disusun pasca observasi awal, fokus pada pembentukan mindset industri dan pengenalan ragam proses permesinan yang relevan dengan DUDI lokal.",
            "Menjadi cetak biru (blueprint) bagi guru untuk memandu siswa memahami alur proses dari raw material menjadi produk jadi.",
            "Menyajikan tahapan Problem-Based Learning yang mengkondisikan siswa berpikir seperti engineer, bukan sekadar operator.",
            "Alokasi waktu di RPP sering terlampaui saat diskusi kelas karena antusiasme siswa bertanya soal aplikasi nyata di pabrik."
        )
    elif "rpp dasar sistem mekanik" in title_lower:
        return (
            "Didesain khusus untuk menjembatani nalar logika fisika dasar ke aplikasi mekanik praktis di mesin-mesin industri.",
            "Menggiring siswa memahami prinsip mekanika (gaya, momen, transmisi) sebelum mereka terjun menganalisis kerusakan mesin.",
            "Integrasi asesmen formatif yang kuat pada tiap sintaks, memudahkan guru mendeteksi miskonsepsi siswa lebih awal.",
            "Membutuhkan banyak alat peraga mekanik di kelas agar RPP ini berjalan sempurna, yang mana tidak selalu tersedia di lab."
        )
    elif "rpp pengelasan dasar smaw" in title_lower:
        return (
            "Disusun dengan pendekatan Project-Based Learning, merespons kebutuhan mendesak akan kompetensi las yang safety-first.",
            "Menuntun siswa menguasai teknik penyalaan busur dan pengaturan ampere dengan kemandirian penuh namun tetap aman.",
            "Sangat detail pada alur Keselamatan dan Kesehatan Kerja (K3), mencerminkan filosofi KHD dalam melindungi kodrat anak.",
            "Tingkat stres guru cukup tinggi saat implementasi karena harus memonitor nyala api dari puluhan bilik las secara bersamaan."
        )
    
    # --- MEDIA BAHAN AJAR VIDEO ---
    elif "proses produksi dengan mesin bubut" in title_lower and "media" not in title_lower and "bahan" not in title_lower: # Media Bubut
        return (
            "Media animasi dan slide interaktif yang dibuat untuk mengatasi minimnya rasio mesin bubut dibanding jumlah siswa.",
            "Memberikan visualisasi proses pemotongan logam (cutting) dari berbagai sudut pandang tanpa resiko kecelakaan.",
            "Mampu menyederhanakan penjelasan parameter potong (speed, feed) lewat visualisasi pergerakan pahat yang jelas.",
            "Siswa cenderung pasif jika guru tidak terus memancing diskusi interaktif selama penayangan media ini."
        )
    elif "media pembelajaran tentang pengelasan dasar smaw" in title_lower:
        return (
            "Media berupa cuplikan makro (jarak dekat) proses peleburan flux elektroda yang tidak bisa diamati dengan mata telanjang.",
            "Menghubungkan teori ayunan elektroda (zig-zag, spiral) dengan bentuk rigi-rigi las yang dihasilkan.",
            "Sangat efektif mengurangi trial-and-error berlebih saat siswa pertama kali memegang stang las di bengkel.",
            "Detail warna logam cair pada layar proyektor kadang tidak secerah aslinya, mengurangi keakuratan identifikasi slag vs molten metal."
        )
    elif "bahan ajar teknik dasar proses produksi bidang manufaktur" in title_lower:
        return (
            "Modul ringkas hasil kurasi dari berbagai sumber industri, disesuaikan dengan kemampuan literasi siswa SMK.",
            "Menjadi pedoman belajar mandiri di rumah sehingga waktu di bengkel bisa difokuskan murni untuk praktik.",
            "Bahasa yang digunakan sangat aplikatif, dilengkapi diagram alir yang memudahkan retensi memori siswa.",
            "Belum sepenuhnya mengintegrasikan teknologi manufaktur terkini (seperti CNC 5-axis) karena fokus pada dasar."
        )
    elif "bahan ajar dasar sistem mekanik" in title_lower:
        return (
            "Buku ajar internal yang menyederhanakan perhitungan fisika mekanik rumit menjadi rumus praktis ala teknisi.",
            "Membekali siswa dengan kemampuan berhitung cepat (rule of thumb) untuk menentukan rasio roda gigi dan transmisi.",
            "Banyak menyajikan contoh kasus (studi kasus) nyata dari kerusakan mesin yang sering ditemui di lapangan.",
            "Beberapa bagian perhitungan analitis masih dirasa terlalu matematis oleh sebagian siswa dengan kemampuan dasar rendah."
        )
    elif "bahan ajar tentang pengelasan dasar smaw" in title_lower:
        return (
            "Handout saku yang anti-air dan dirancang khusus untuk dibawa langsung ke dalam bilik pengelasan.",
            "Memberikan akses instan bagi siswa untuk mengecek referensi setting ampere berdasarkan diameter elektroda.",
            "Sangat praktis (bite-sized learning) dan berfokus langsung pada tabel parameter serta identifikasi cacat las.",
            "Isinya sangat padat; kurang memberikan ruang untuk pembahasan mendalam mengenai metalurgi las."
        )
    elif "video mengajar tentang pelasan dasar smaw" in title_lower:
        return (
            "Video demonstrasi langsung oleh guru yang direkam dari balik topeng las (welding helmet camera).",
            "Menunjukkan secara langsung 'POV' (Point of View) seorang welder agar siswa bisa meniru posisi tubuh yang benar.",
            "Sangat disukai siswa karena bisa diputar ulang berulang kali (rewind) saat mereka ragu sebelum mempraktekkan.",
            "Kualitas audio video terganggu oleh suara kipas exhaust dan desisan busur las yang bising."
        )
    elif "dasar sistem mekanik" in title_lower and not ("rpp" in title_lower or "bahan" in title_lower or "lkm" in title_lower):
        return (
            "Media interaktif berupa simulator linkage (mekanisme tuas) berbasis web yang bisa dimainkan siswa di gawai mereka.",
            "Mendorong eksplorasi inkuiri; siswa bisa mengubah panjang tuas dan langsung melihat perubahan output gaya secara live.",
            "Pendekatan gamifikasi ini sukses meningkatkan keterlibatan (engagement) dan minat siswa pada materi teoritis.",
            "Sangat bergantung pada koneksi internet sekolah yang terkadang tidak stabil saat diakses puluhan siswa serentak."
        )

    # --- LKM MANUFAKTUR ---
    elif "lkm 1 pertemuan 1 materi proses produksi" in title_lower:
        return (
            "LKM ini difokuskan pada pengenalan (orientation) klasifikasi proses manufaktur: pemotongan, pembentukan, dan pengecoran.",
            "Melatih nalar klasifikasi siswa dalam menentukan proses yang paling efisien untuk membuat suatu produk.",
            "Menggunakan pendekatan studi kasus produk sehari-hari (seperti panci atau baut) yang dekat dengan kehidupan siswa.",
            "Butuh panduan ketat dari guru karena siswa sering keliru membedakan antara proses stamping dan machining."
        )
    elif "lkm 2 pertemuan 2 materi proses produksi" in title_lower:
        return (
            "LKM praktik awal yang memperkenalkan anatomi mesin konvensional (bubut dan frais) beserta fungsi tiap tuasnya.",
            "Mengembangkan kesadaran spasial dan mekanis siswa sebelum mesin dihidupkan.",
            "Disertai diagram visual mesin yang jelas sehingga siswa tinggal mencocokkan dengan mesin fisik di bengkel.",
            "Kurang memberikan stimulasi problem-solving tingkat tinggi (HOTS) karena sifatnya masih hafalan/identifikasi dasar."
        )
    elif "lkm 3 pertemuan 3 materi proses produksi" in title_lower:
        return (
            "LKM hitungan parameter potong (Cutting Speed, RPM) yang mengintegrasikan matematika terapan ke dalam praktik.",
            "Membiasakan siswa bekerja dengan data numerik yang akurat demi menjaga keawetan pahat potong.",
            "Korelasi yang sangat kuat antara teori di kelas dengan kualitas hasil potongan di bengkel langsung terlihat.",
            "Siswa yang kurang teliti dalam konversi satuan (mm ke meter) kerap melakukan kesalahan perhitungan krusial."
        )
    elif "lkm 4 pertemuan 4 materi proses produksi" in title_lower:
        return (
            "Fokus pada observasi Keselamatan Kerja dan 5R (Ringkas, Rapi, Resik, Rawat, Rajin) di lingkungan bengkel.",
            "Menanamkan karakter disiplin dan budaya industri (soft skills) sedini mungkin sesuai visi Tut Wuri Handayani.",
            "Mewajibkan siswa melakukan peer-assessment (menilai temannya) terkait kepatuhan APD, melatih objektivitas.",
            "Terkadang dianggap sepele oleh siswa karena tidak langsung menghasilkan produk logam."
        )
    elif "lkm 5 pertemuan 5 materi proses produksi" in title_lower:
        return (
            "LKM tentang metrologi dasar; siswa diminta mengukur dimensi spesimen dengan jangka sorong dan mikrometer presisi.",
            "Melatih ketelitian absolut dan kejujuran data, sebuah sikap mental yang krusial bagi seorang teknisi manufaktur.",
            "Dilengkapi dengan toleransi standar industri, membuat siswa paham bahwa 'hampir pas' itu tidak cukup di manufaktur.",
            "Keterbatasan alat ukur presisi membuat pengerjaan LKM ini harus dilakukan dengan sistem antrean panjang."
        )
    elif "lkm 6 pertemuan 6 materi proses produksi" in title_lower:
        return (
            "LKM evaluasi sumatif berupa instruksi kerja pembuatan project sederhana (misal poros bertingkat).",
            "Mensintesis seluruh pengetahuan dari pertemuan 1-5 menjadi satu alur kerja yang terpadu.",
            "Menciptakan kebanggaan (pride) bagi siswa karena akhirnya mereka membawa pulang hasil karya logam perdananya.",
            "Proses penilaian (grading) sangat menyita waktu guru karena setiap produk harus diukur dimensinya satu per satu."
        )

    # --- LKM MEKANIK ---
    elif "lkm 1 pertemuan 1 materi dasar sistem mekanik" in title_lower:
        return (
            "LKM eksplorasi tentang jenis-jenis gaya, vektor, dan resultan gaya yang bekerja pada struktur jembatan/rangka.",
            "Membantu siswa menvisualisasikan bahwa benda diam sebenarnya menahan berbagai gaya yang saling menyeimbangkan.",
            "LKM ini menggunakan pendekatan eksperimen sederhana dengan pegas dan neraca ohaus yang mudah dipahami.",
            "Analisis vektor menggunakan sudut (trigonometri) kerap membuat pusing siswa yang dasar matematikanya lemah."
        )
    elif "lkm 2 pertemuan 2 materi dasar sistem mekanik" in title_lower:
        return (
            "LKM aplikasi konsep Torsi (Momen Gaya) pada penggunaan berbagai macam perkakas tangan (kunci pas, dongkrak).",
            "Memberikan jawaban logis 'mengapa kunci yang gagangnya lebih panjang terasa lebih ringan' melalui eksperimen riil.",
            "Sangat kontekstual (CTL) dan langsung bisa diterapkan siswa ketika mereka memperbaiki motor di rumah.",
            "LKM kurang efektif jika hanya dikerjakan di atas kertas tanpa simulasi pengencangan baut sungguhan."
        )
    elif "lkm 3 pertemuan 3 materi dasar sistem mekanik" in title_lower:
        return (
            "LKM analisis sistem transmisi daya (sabuk, puli, roda gigi) dan perhitungan rasio putaran (Gear Ratio).",
            "Melatih siswa merancang kombinasi puli untuk menurunkan RPM motor listrik tanpa kehilangan torsi.",
            "Mendorong kemampuan perancangan (design thinking) tingkat dasar yang menuntut logika rasio perbandingan.",
            "Menghabiskan banyak waktu pada sesi diskusi kelompok karena sering terjadi perdebatan logika putaran arah jarum jam."
        )

    # --- LKM SMAW ---
    elif "spesifikasi mesin las smaw" in title_lower:
        return (
            "LKM orientasi peralatan, fokus pada pemahaman tipe arus (AC/DC) dan Duty Cycle pada nameplate mesin las.",
            "Mencegah kerusakan mesin akibat overheat dengan melatih siswa membaca batas maksimal penggunaan mesin.",
            "Menanamkan rasa tanggung jawab dan 'sense of belonging' siswa terhadap inventaris bengkel sekolah.",
            "Materi terkesan teoritis; siswa sering tidak sabar ingin langsung menyalakan api las."
        )
    elif "penyiapan mesin dan bahan pengelasan" in title_lower:
        return (
            "Jobsheet prosedural tentang pemasangan kabel massa, setting polaritas (DCEP/DCEN), dan gerinda persiapan kampuh.",
            "Menstandarkan prosedur awal agar siswa tidak panik jika terjadi masalah arc-strike di awal pengelasan.",
            "SOP yang detail meniadakan resiko korsleting dan memastikan penetrasi las awal berjalan mulus.",
            "Sering terjadi bottleneck (antrean) pada area mesin gerinda statis saat penyiapan spesimen material."
        )
    elif "identifikasi elektroda" in title_lower:
        return (
            "LKM pembacaan kode standar AWS (seperti E6013, E7018) dan pemahaman kuat tarik serta posisi pengelasan.",
            "Menghindarkan siswa dari kesalahan fatal penggunaan jenis elektroda yang salah untuk material tertentu.",
            "Ringkas dan to the point, langsung menghubungkan kode angka dengan setting ampere rekomendasi.",
            "Fokus yang terlalu sempit membuat siswa kurang memahami perbedaan bahan kimia pembentuk flux (salutan)."
        )
    elif "posisi pengelasan" in title_lower:
        return (
            "LKM praktik inti untuk melatih ayunan elektroda pada posisi di bawah tangan (1F/1G).",
            "Membangun memori otot (muscle memory) siswa untuk menjaga jarak busur (arc length) tetap konstan.",
            "Berisi parameter rubrik penilaian yang sangat jelas terkait lebar jalur dan kestabilan riak las.",
            "Keletihan fisik (mata dan tangan) siswa cukup tinggi, sehingga durasi pengerjaan LKM ini harus dipecah."
        )
    elif "pemeriksaan hasil las" in title_lower:
        return (
            "LKM inspeksi visual (Visual Test / VT) di mana siswa menilai hasil las temannya mencari undercut, porosity, atau cacat lain.",
            "Melatih kejelian mata dan pemahaman kriteria keberterimaan (Acceptance Criteria) standar fabrikasi.",
            "Membangun budaya evaluasi kritis; siswa belajar dari kesalahan temannya tanpa merasa digurui oleh guru.",
            "Dibutuhkan alat bantu seperti kaca pembesar atau welding gauge yang jumlahnya terbatas di sekolah."
        )
        
    # --- DEFAULT FOR PLACEHOLDERS ---
    elif "lembar kerja siswa (contoh)" in title_lower:
        return (
            "Dokumen placeholder sementara untuk desain tata letak UI galeri portofolio.",
            "Memastikan responsivitas dan struktur grid tetap utuh saat konten aslinya ditambahkan.",
            "Memberikan gambaran visual yang rapi bagi evaluator sebelum dokumen asli diunggah.",
            "Hanya berupa tiruan, belum memiliki nilai pedagogis riil."
        )
    elif "instrumen asesmen (contoh)" in title_lower:
        return (
            "Dokumen placeholder sementara untuk rubrik dan instrumen penilaian.",
            "Mempertahankan konsistensi desain sistem tab dan filter pada presentasi E-Portfolio.",
            "Membantu memetakan porsi konten asesmen dalam keseluruhan struktur web.",
            "Tidak dapat digunakan untuk analisis pembelajaran karena isinya kosong."
        )

    # --- FALLBACK ---
    return (
        f"Konteks analisis untuk {title} dirancang sesuai dengan kurikulum vokasi dan kebutuhan industri terkini.",
        "Mendukung capaian kompetensi keahlian secara komprehensif, mulai dari kognitif hingga psikomotorik.",
        "Terstruktur dengan baik dan mengakomodir kebutuhan gaya belajar siswa yang beragam.",
        "Masih memerlukan kalibrasi waktu implementasi dan peningkatan sarana pendukung di bengkel."
    )

updated_count = 0

for card in soup.select('.doc-card-content'):
    h4 = card.find('h4')
    if not h4:
        continue
    
    title = h4.get_text(strip=True)
    details = card.find('details')
    
    if details:
        divs = details.find_all('div', recursive=False)
        if len(divs) == 1:
            container = divs[0]
            inner_divs = container.find_all('div', recursive=False)
            if len(inner_divs) >= 4:
                konteks, tujuan, kelebihan, kekurangan = get_unique_analysis(title)
                
                def update_span(parent_div, new_text):
                    span = parent_div.find('span')
                    if span:
                        span.string = new_text

                update_span(inner_divs[0], konteks)
                update_span(inner_divs[1], tujuan)
                update_span(inner_divs[2], kelebihan)
                update_span(inner_divs[3], kekurangan)
                
                updated_count += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"Updated {updated_count} cards with unique content.")
