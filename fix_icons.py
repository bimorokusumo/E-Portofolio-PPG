import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all <div class="doc-icon"...>...</div> with a placeholder image
# We will use one of the existing drive thumbnails as a generic representation 
# for the folders so they look exactly like the other documents.
placeholder_img = '<img src="https://drive.google.com/thumbnail?id=1MYlooWJYg1XRj__1RhW0rCY6xiNFqLrJ&sz=w600" alt="Document Thumbnail" class="doc-thumb-img" style="filter: hue-rotate(15deg) brightness(0.9);">'

# Using regex to replace the doc-icon div
new_content = re.sub(r'<div class="doc-icon".*?</div>', placeholder_img, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html to replace folder icons with image thumbnails.")
