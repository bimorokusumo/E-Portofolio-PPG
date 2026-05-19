with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find the `.one-screen .article-grid` block and update it
old_block = """.one-screen .article-grid {
    gap: 1rem !important;
    margin-top: 1rem !important;
}"""

new_block = """.one-screen .article-grid {
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)) !important;
    gap: 1rem !important;
    margin-top: 1rem !important;
}"""

if old_block in css:
    css = css.replace(old_block, new_block)
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Grid optimized for one-screen.")
else:
    print("Could not find block to optimize.")
