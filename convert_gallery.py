import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the carousel container with accordion gallery
carousel_pattern = re.compile(r'<div class="carousel-container" id="dokumentasi-carousel">.*?</div>\s*</div>', re.DOTALL)

accordion_html = """<div class="accordion-gallery">
"""
for i in range(1, 21):
    accordion_html += f'                <div class="accordion-item"><img src="assets/dokumentasi/{i}.jpg" alt="Dokumentasi {i}" onerror="this.parentElement.remove();"></div>\n'
accordion_html += '            </div>'

new_content = carousel_pattern.sub(accordion_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("index.html updated successfully.")
