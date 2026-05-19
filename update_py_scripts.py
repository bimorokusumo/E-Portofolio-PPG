import os

target_content = """<details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                        <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Catatan Refleksi</summary>
                        <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                            <div><strong>Kelebihan:</strong> <br><span style="color: var(--text-light);">(Uraikan kelebihan)</span></div>
                            <div><strong>Kekurangan:</strong> <br><span style="color: var(--text-light);">(Uraikan kekurangan)</span></div>
                            <div><strong>Tantangan:</strong> <br><span style="color: var(--text-light);">(Tantangan terkait siswa/kelas)</span></div>
                            <div><strong>Cara Mengatasi:</strong> <br><span style="color: var(--text-light);">(Solusi yang diterapkan)</span></div>
                        </div>
                    </details>"""

replacement_content = """<details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                        <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                        <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                            <div><strong>Kendala proses penyusunan perangkat:</strong> <br><span style="color: var(--text-light);">Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).</span></div>
                            <div><strong>Teori konsep pedagogi:</strong> <br><span style="color: var(--text-light);">Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).</span></div>
                            <div><strong>Faktor keberhasilan:</strong> <br><span style="color: var(--text-light);">Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.</span></div>
                            <div><strong>Perubahan komponen penunjang kelas:</strong> <br><span style="color: var(--text-light);">Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.</span></div>
                        </div>
                    </details>"""

for file in ["add_cards.py", "inject_reflection.py", "update_refleksi.py"]:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the literal content block if present in add_cards.py
        # Actually in add_cards.py the indentation might be different. 
        # Let's do a more robust replace for Catatan Refleksi and its fields
        new_content = content.replace('📝 Catatan Refleksi', '📝 Analisis Artefak')
        new_content = new_content.replace('Kelebihan:', 'Kendala proses penyusunan perangkat:')
        new_content = new_content.replace('(Uraikan kelebihan)', 'Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).')
        
        new_content = new_content.replace('Kekurangan:', 'Teori konsep pedagogi:')
        new_content = new_content.replace('(Uraikan kekurangan)', 'Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).')
        
        new_content = new_content.replace('Tantangan:', 'Faktor keberhasilan:')
        new_content = new_content.replace('(Tantangan terkait siswa/kelas)', 'Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.')
        
        new_content = new_content.replace('Cara Mengatasi:', 'Perubahan komponen penunjang kelas:')
        new_content = new_content.replace('(Solusi yang diterapkan)', 'Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

