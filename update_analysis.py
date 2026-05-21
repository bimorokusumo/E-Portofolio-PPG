import re
import os

html_path = 'index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

contents = {
    'rpp': {
        'konteks': 'Disusun untuk memandu pelaksanaan PPL Terbimbing, merespons kebutuhan belajar siswa berdasarkan hasil observasi dan diagnostik awal sesuai prinsip TaRL (Teaching at the Right Level).',
        'tujuan': 'Menjadi pedoman sistematis (scaffolding) guru dalam mendesain pengalaman belajar yang bermakna (Understanding by Design), serta mewujudkan peran "Pamomong" yang menuntun kodrat anak menurut ajaran KHD.',
        'kelebihan': 'Mengintegrasikan TPACK dan pendekatan diferensiasi, selaras dengan filosofi KHD <em>Tut Wuri Handayani</em> (memberikan dorongan dari belakang untuk kemandirian).',
        'kekurangan': 'Masih memerlukan adaptasi waktu yang lebih fleksibel mengingat dinamika kelas dan beragamnya "kodrat alam" peserta didik yang tidak selalu sesuai dengan alur waktu RPP.'
    },
    'media': {
        'konteks': 'Dikembangkan sebagai alat bantu visual dan interaktif untuk menjembatani pemahaman siswa terhadap materi vokasi yang kompleks, mengacu pada "Kodrat Zaman" KHD agar siswa relevan dengan perkembangan teknologinya.',
        'tujuan': 'Memfasilitasi berbagai gaya belajar siswa (visual, auditori, kinestetik) sesuai prinsip pembelajaran berdiferensiasi dan <em>Culturally Responsive Teaching</em> (CRT) pada PPL Terbimbing.',
        'kelebihan': 'Mampu mengonkretkan konsep abstrak, meningkatkan motivasi, dan mewujudkan peran guru <em>Ing Madya Mangun Karso</em> (membangun semangat di tengah siswa) melalui media interaktif.',
        'kekurangan': 'Bergantung pada ketersediaan sarana prasarana bengkel/sekolah (proyektor, internet, listrik), sehingga terkadang tidak dapat diimplementasikan secara optimal di semua ruang kelas.'
    },
    'lks': {
        'konteks': 'Dirancang sebagai instrumen untuk mengukur pemahaman dan keterampilan praktikal siswa secara formatif maupun sumatif selama proses pembelajaran PPL Terbimbing.',
        'tujuan': 'Memberikan umpan balik yang konstruktif (feedback) serta melatih kemandirian berpikir kritis siswa, sesuai dengan Sistem Among KHD yang menghargai kemerdekaan belajar.',
        'kelebihan': 'Menggunakan rubrik penilaian yang terukur dan menyajikan studi kasus nyata dari dunia industri untuk menjembatani kompetensi sekolah dengan kebutuhan DUDI.',
        'kekurangan': 'Proses penyusunan instrumen LKPD/Asesmen yang benar-benar autentik dan mengukur <em>Higher Order Thinking Skills</em> (HOTS) membutuhkan kalibrasi dan waktu yang panjang bagi guru.'
    },
    'bahan-ajar': {
        'konteks': 'Disusun sebagai referensi utama siswa dalam menggali informasi esensial, disesuaikan dengan tuntutan kurikulum dan kesiapan kognitif peserta didik di jenjang vokasi menengah.',
        'tujuan': 'Membangun fondasi literasi dan kemandirian belajar siswa agar mampu secara aktif mencari tahu, bukan sekadar diberi tahu, selaras dengan esensi kemerdekaan belajar dalam filosofi KHD.',
        'kelebihan': 'Materi dikemas secara kontekstual dan komunikatif, mengedepankan peran <em>Ing Ngarso Sung Tulodo</em> (memberikan teladan) melalui pemaparan contoh-contoh kasus nyata di lapangan.',
        'kekurangan': 'Beberapa materi teknis manufaktur berkembang sangat cepat sehingga literatur bahan ajar ini masih membutuhkan pembaruan berkala agar tidak tertinggal dengan standar industri terkini.'
    },
    'default': {
        'konteks': 'Merupakan dokumentasi dan evaluasi dari implementasi pembelajaran di kelas selama PPL Terbimbing, mencerminkan interaksi pedagogik yang terjadi secara nyata.',
        'tujuan': 'Menjadi bahan refleksi bagi guru untuk terus memperbaiki siklus pembelajaran demi tercapainya keselamatan dan kebahagiaan siswa setinggi-tingginya sesuai konsep pendidikan KHD.',
        'kelebihan': 'Memberikan bukti nyata (eviden) perkembangan siswa dan menunjukkan efektivitas Sistem Among serta model pembelajaran inovatif yang telah diterapkan.',
        'kekurangan': 'Masih ada potensi bias dalam dokumentasi atau penilaian subjektif, yang perlu diimbangi dengan instrumen refleksi dan evaluasi rekan sejawat yang lebih terstandar.'
    }
}

# Regex to find each card and replace its details block
# A doc card looks like <div class="doc-card gallery-card-item" data-category="rpp">
# and inside it has <summary ...>📝 Analisis Artefak</summary> ... </details>

def replace_details(match):
    full_match = match.group(0)
    category = match.group(1)
    
    cat_data = contents.get(category, contents['default'])
    
    new_details_inner = f"""
                        <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                            <div><strong>Konteks:</strong> <br><span style="color: var(--text-light);">{cat_data['konteks']}</span></div>
                            <div><strong>Tujuan:</strong> <br><span style="color: var(--text-light);">{cat_data['tujuan']}</span></div>
                            <div><strong>Kelebihan:</strong> <br><span style="color: var(--text-light);">{cat_data['kelebihan']}</span></div>
                            <div><strong>Kekurangan:</strong> <br><span style="color: var(--text-light);">{cat_data['kekurangan']}</span></div>
                        </div>"""

    # We need to replace the content inside the <details> that has "📝 Analisis Artefak"
    # Find the <summary> and the </div> closing the inner div
    
    def repl_inner(m_inner):
        summary = m_inner.group(1)
        return summary + new_details_inner
        
    new_card = re.sub(r'(<summary[^>]*>📝 Analisis Artefak</summary>)\s*<div style="padding-top: 0.8rem;.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>', lambda m: m.group(1) + new_details_inner, full_match, flags=re.DOTALL)
    
    # Wait, the regex for inner details might be tricky because of nested divs.
    # The inner div has <div style="padding-top: 0.8rem; ..."> ... </div> (but with 4 nested <div>s inside it).
    # Actually, it's safer to just split and replace based on known strings.
    return full_match

# Let's do a more robust approach
new_html = ""
parts = re.split(r'(<div class="doc-card gallery-card-item" data-category="([^"]+)">)', html)

# parts[0] is everything before the first card
# parts[1] is the matched group 1 (the full <div> tag)
# parts[2] is the matched group 2 (the category)
# parts[3] is everything inside and after the card until the next card... wait, split works like this:
# parts = [text, separator1, group2, text2, separator2, group2, text3...]

new_html = parts[0]
i = 1
while i < len(parts):
    div_tag = parts[i]
    category = parts[i+1]
    content_after = parts[i+2]
    
    cat_data = contents.get(category, contents['default'])
    new_details_inner = f"""
                        <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                            <div><strong>Konteks:</strong> <br><span style="color: var(--text-light);">{cat_data['konteks']}</span></div>
                            <div><strong>Tujuan:</strong> <br><span style="color: var(--text-light);">{cat_data['tujuan']}</span></div>
                            <div><strong>Kelebihan:</strong> <br><span style="color: var(--text-light);">{cat_data['kelebihan']}</span></div>
                            <div><strong>Kekurangan:</strong> <br><span style="color: var(--text-light);">{cat_data['kekurangan']}</span></div>
                        </div>"""

    # We want to replace the part right after <summary...>📝 Analisis Artefak</summary> up to the end of the outer div.
    # The old structure is exactly:
    # <summary style="...">📝 Analisis Artefak</summary>
    # <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
    #    <div><strong>Kendala proses penyusunan perangkat:</strong> <br><span style="color: var(--text-light);">...</span></div>
    #    <div><strong>Teori konsep pedagogi:</strong> <br><span style="color: var(--text-light);">...</span></div>
    #    <div><strong>Faktor keberhasilan:</strong> <br><span style="color: var(--text-light);">...</span></div>
    #    <div><strong>Perubahan komponen penunjang kelas:</strong> <br><span style="color: var(--text-light);">...</span></div>
    # </div>
    # </details>
    
    pattern = r'(<summary[^>]*>📝 Analisis Artefak</summary>)\s*<div style="padding-top: 0.8rem[^>]*>.*?</div>\s*</details>'
    
    new_content_after = re.sub(
        pattern, 
        r'\1\n' + new_details_inner + '\n                    </details>', 
        content_after, 
        flags=re.DOTALL
    )
    
    new_html += div_tag + new_content_after
    i += 3

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated index.html successfully.")
