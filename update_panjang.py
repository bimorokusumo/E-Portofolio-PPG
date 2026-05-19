import os
import glob

old_text_1 = "Menyelaraskan tingkat kesulitan materi vokasi dengan kemampuan awal peserta didik yang beragam, serta keterbatasan waktu dalam merancang instrumen asesmen yang benar-benar autentik dan relevan dengan standar industri."
new_text_1 = "Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI)."

old_text_2 = "Mengintegrasikan pendekatan Understanding by Design (UbD) dengan model pembelajaran Project/Problem Based Learning (PjBL/PBL) untuk membimbing siswa dari pemahaman konsep dasar menuju praktik yang terstruktur."
new_text_2 = "Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS)."

old_text_3 = "Tingginya antusiasme peserta didik ketika dihadapkan pada media pembelajaran interaktif atau demonstrasi praktik langsung, serta dukungan fasilitas bengkel yang memadai untuk simulasi."
new_text_3 = "Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata."

old_text_4 = "Penyempurnaan Lembar Kerja Peserta Didik (LKPD) agar instruksinya lebih sistematis, serta penambahan media visual (seperti video atau model 3D) untuk memfasilitasi gaya belajar siswa yang bervariasi."
new_text_4 = "Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam."

html_files = glob.glob("*.html")
py_files = ["add_cards.py", "inject_reflection.py", "update_refleksi.py", "transform_refleksi.py", "update_py_scripts.py"]

files_to_check = html_files + py_files

for file in files_to_check:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text_1 in content or old_text_2 in content:
        content = content.replace(old_text_1, new_text_1)
        content = content.replace(old_text_2, new_text_2)
        content = content.replace(old_text_3, new_text_3)
        content = content.replace(old_text_4, new_text_4)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

