import os
import glob

old_text = "Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Project-Based Learning (PjBL) dan Problem-Based Learning (PBL). Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS)."
new_text = "Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS)."

html_files = glob.glob("*.html")
py_files = ["add_cards.py", "inject_reflection.py", "update_refleksi.py", "transform_refleksi.py", "update_py_scripts.py", "update_panjang.py"]

files_to_check = html_files + py_files

for file in files_to_check:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

