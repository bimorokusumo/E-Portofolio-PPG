import os
import glob

old_text = "Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian substansial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi jauh lebih sistematis, rinci, dan terukur. Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti integrasi video tutorial praktik dan pemodelan CAD 3D, yang secara khusus ditujukan untuk mengakomodasi dan memfasilitasi gaya belajar peserta didik yang beragam (visual, auditori, maupun kinestetik)."
new_text = "Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam."

html_files = glob.glob("*.html")
py_files = ["add_cards.py", "inject_reflection.py", "update_refleksi.py", "transform_refleksi.py", "update_py_scripts.py", "update_panjang.py", "update_inquiry.py"]

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

