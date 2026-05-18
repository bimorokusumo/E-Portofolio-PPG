import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Create the 20 slides
slides_html = ""
for i in range(1, 21):
    slides_html += f"""                    <div class="carousel-slide">
                        <img src="assets/dokumentasi/{i}.jpg" alt="Dokumentasi {i}" onerror="this.parentElement.remove();">
                    </div>\n"""

pattern = re.compile(r'<div class="carousel-track">.*?</div>\s*</div>', re.DOTALL)
replacement = f'<div class="carousel-track">\n{slides_html}                </div>\n            </div>'

new_content = pattern.sub(replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done")
