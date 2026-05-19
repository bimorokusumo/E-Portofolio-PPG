with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Refleksi Pembelajaran', 'Analisis Artefak Pembelajaran')
content = content.replace('Refleksi PPL', 'Analisis Artefak PPL')
content = content.replace('ep2-refleksi', 'ep2-analisis-artefak')
content = content.replace('Lihat Refleksi', 'Lihat Analisis Artefak')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

