import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix ep5-refleksi
# Find: <section id="ep5-refleksi" style="padding: 4rem 2rem; max-width: 1160px; margin: 0 auto;">
# Replace with: <section id="ep5-refleksi" style="padding: 5rem 2rem; background: var(--bg-light-gray); width: 100%;"><div style="max-width: 1160px; margin: 0 auto;">
# and find the closing tag for ep5-refleksi and add </div> before it.

text = re.sub(
    r'<section id="ep5-refleksi" style="[^"]+">',
    r'<section id="ep5-refleksi" style="padding: 5rem 2rem; background: var(--bg-light-gray); width: 100%;">\n    <div style="max-width: 1160px; margin: 0 auto;">',
    text
)
text = text.replace('<!-- Refleksi Keseluruhan -->', '    </div>\n</section>\n<!-- Refleksi Keseluruhan -->')

# Wait, replacing <!-- Refleksi Keseluruhan --> will leave an extra </section> behind!
# I should remove the original </section> of ep5-refleksi.
# Let's do it safer:
text = text.replace('</section>\n<!-- Refleksi Keseluruhan -->', '    </div>\n</section>\n<!-- Refleksi Keseluruhan -->')

# 2. Fix ep5-keseluruhan (change to bg-white)
text = text.replace(
    '<section class="one-screen" id="ep5-keseluruhan" style="padding: 5rem 2rem; background: var(--bg-light-gray); text-align: center;">',
    '<section class="one-screen" id="ep5-keseluruhan" style="padding: 5rem 2rem; background: var(--bg-white); text-align: center;">'
)

# 3. Fix ep5-inovasi (change to bg-light-gray)
text = text.replace(
    '<section class="one-screen" id="ep5-inovasi" style="padding: 5rem 2rem; background: var(--bg-white); text-align: center;">',
    '<section class="one-screen" id="ep5-inovasi" style="padding: 5rem 2rem; background: var(--bg-light-gray); text-align: center;">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Backgrounds alternating pattern fixed.")
