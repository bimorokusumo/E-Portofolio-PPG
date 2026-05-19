with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert the navigation link for Analisis Artefak
old_nav = '<li><a href="#artefak">Artefak</a></li>'
new_nav = '<li><a href="#artefak">Artefak</a></li>\n                <li><a href="#analisis-produk">Analisis Artefak</a></li>'

if old_nav in content:
    content = content.replace(old_nav, new_nav, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Navigation updated successfully.")
else:
    print("Could not find target nav link.")
