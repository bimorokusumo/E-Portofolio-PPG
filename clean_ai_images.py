import re

with open('index.html.noemoji', 'r', encoding='utf-8') as f:
    content = f.read()

# The wrapper div pattern:
# <div style="width: 50px; height: 50px; border-radius: 50%; ...">
#     <img src="assets/..." ...>
# </div>
# OR for the seed icon:
# <div style="width: 50px; height: 50px; border-radius: 50%; ...">
#     
# </div>  <-- (since emoji was removed, it might just be empty now)

pattern = re.compile(
    r'<div style="width: 50px; height: 50px; border-radius: 50%;[^>]*>\s*(<img[^>]*>)?\s*</div>',
    re.DOTALL
)

content_cleaned = pattern.sub('', content)

# Write to the final index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content_cleaned)

print("Cleaned AI images.")
