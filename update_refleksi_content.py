import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll replace the placeholder texts in index.html with generated generic analysis.

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "📝 Analisis Artefak" in content:
        new_content = content.replace(
            '(Analisis kendala proses penyusunan)',
            'Menyelaraskan tingkat kesulitan materi vokasi dengan kemampuan awal peserta didik yang beragam, serta keterbatasan waktu dalam merancang instrumen asesmen yang benar-benar autentik dan relevan dengan standar industri.'
        ).replace(
            '(Analisis teori konsep pedagogi yang digunakan)',
            'Mengintegrasikan pendekatan Understanding by Design (UbD) dengan model pembelajaran Project/Problem Based Learning (PjBL/PBL) untuk membimbing siswa dari pemahaman konsep dasar menuju praktik yang terstruktur.'
        ).replace(
            '(Analisis faktor keberhasilan)',
            'Tingginya antusiasme peserta didik ketika dihadapkan pada media pembelajaran interaktif atau demonstrasi praktik langsung, serta dukungan fasilitas bengkel yang memadai untuk simulasi.'
        ).replace(
            '(Analisis perubahan komponen penunjang kelas)',
            'Penyempurnaan Lembar Kerja Peserta Didik (LKPD) agar instruksinya lebih sistematis, serta penambahan media visual (seperti video atau model 3D) untuk memfasilitasi gaya belajar siswa yang bervariasi.'
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated content in {file}")

