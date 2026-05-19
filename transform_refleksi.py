import os
import re

html_files = [f for f in os.listdir('.') if f.startswith('refleksi') and f.endswith('.html')]

rows_html = """
        <!-- Area Analisis Artefak -->
        <div style="width: 100%; max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 1.5rem; text-align: left;">
            <!-- Row 1 -->
            <div style="background: white; border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                <h4 style="color: var(--kemendikbud-blue); margin-top: 0; margin-bottom: 0.5rem; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">
                    <span>🚧</span> Kendala Proses Penyusunan Perangkat
                </h4>
                <p style="color: var(--text-dark); margin: 0; line-height: 1.6;">Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).</p>
            </div>
            
            <!-- Row 2 -->
            <div style="background: white; border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                <h4 style="color: var(--kemendikbud-blue); margin-top: 0; margin-bottom: 0.5rem; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">
                    <span>📚</span> Teori Konsep Pedagogi
                </h4>
                <p style="color: var(--text-dark); margin: 0; line-height: 1.6;">Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).</p>
            </div>

            <!-- Row 3 -->
            <div style="background: white; border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                <h4 style="color: var(--kemendikbud-blue); margin-top: 0; margin-bottom: 0.5rem; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">
                    <span>✨</span> Faktor Keberhasilan
                </h4>
                <p style="color: var(--text-dark); margin: 0; line-height: 1.6;">Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.</p>
            </div>

            <!-- Row 4 -->
            <div style="background: white; border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                <h4 style="color: var(--kemendikbud-blue); margin-top: 0; margin-bottom: 0.5rem; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">
                    <span>🔄</span> Perubahan Komponen Penunjang Kelas
                </h4>
                <p style="color: var(--text-dark); margin: 0; line-height: 1.6;">Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.</p>
            </div>
        </div>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic replaces for texts
    content = content.replace("Refleksi Pembelajaran", "Analisis Artefak Pembelajaran")
    
    if file != 'refleksi.html':
        content = content.replace("Silakan unggah dan sematkan file <strong>Analisis Artefak Pembelajaran</strong> Anda untuk mata pelajaran", "Berikut adalah <strong>Analisis Artefak Pembelajaran</strong> Anda untuk mata pelajaran")
        
        # Replace the embed area with the 4 rows
        # The embed area usually looks like: <!-- Area Embed File --> ... </div>
        # Let's use regex to replace it
        pattern = re.compile(r'<!-- Area Embed File -->.*?</div>\s*</div>', re.DOTALL)
        content = pattern.sub(rows_html, content)
        
        # Just in case the second </div> didn't match perfectly, let's also try a more robust regex
        # since it's a div containing p and two inner divs.
        pattern2 = re.compile(r'<!-- Area Embed File -->.*?<div style="margin-top: 3rem;">', re.DOTALL)
        # We can replace everything from <!-- Area Embed File --> to the <div style="margin-top: 3rem;">
        content = re.sub(r'(<!-- Area Embed File -->.*?)(\s*<div style="margin-top: 3rem;">)', 
                         lambda m: rows_html + m.group(2), 
                         content, flags=re.DOTALL)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Transformed {file}")

