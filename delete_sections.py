import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the nav links
nav_links_to_remove = [
    r'<li><a href="#artefak">Artefak</a></li>\n?',
    r'<li><a href="#analisis-produk">Analisis Artefak</a></li>\n?',
    r'<li><a href="#model-guru">Visi Guru</a></li>\n?'
]
for pattern in nav_links_to_remove:
    content = re.sub(pattern, '', content)

# Remove the footer links
footer_links_to_remove = [
    r'<li><a href="#artefak">» Siklus Artefak</a></li>\n?'
]
for pattern in footer_links_to_remove:
    content = re.sub(pattern, '', content)

# Remove from <!-- 3. Analisis Artefak Produk Pembelajaran --> to the end of portfolio 1
pattern = re.compile(r'<!-- 3\. Analisis Artefak Produk Pembelajaran -->.*?</section>\n*<!-- END PORTFOLIO 1 -->', re.DOTALL)
content = pattern.sub('<!-- END PORTFOLIO 1 -->', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Sections deleted successfully")
