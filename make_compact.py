import re

# 1. Update style.css
with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* One Screen Sections */
.one-screen {
    min-height: calc(100vh - 70px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 2rem 2rem !important;
    box-sizing: border-box;
}

.one-screen > div {
    width: 100%;
}

.one-screen h2 {
    margin-bottom: 1.5rem !important;
}

.one-screen .article-grid {
    gap: 1rem !important;
    margin-top: 1rem !important;
}

.one-screen .card-article {
    padding: 1.2rem !important;
}

.one-screen .profile-container {
    padding: 2rem !important;
}

.one-screen .skills-container {
    margin-top: 1rem !important;
}

.one-screen .accordion-gallery {
    margin: 1rem 0 !important;
    height: 350px !important; /* slightly smaller to fit */
}
""")

print("style.css updated.")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# List of section IDs to target
target_sections = [
    'profil', 'pengalaman', 'pendidikan', 'keahlian', 
    'sertifikat', 'galeri', 'penilaian', 'model-guru', 
    'ep2-analisis-artefak', 'ep2-filosofi'
]

for section_id in target_sections:
    # Find the tag like `<section id="profil" ...>`
    # We use regex to find `<section id="section_id"` and add the class
    pattern = f'<section id="{section_id}"'
    
    # Let's see if it already has a class or style
    # We will just insert `class="one-screen"` or append to existing class.
    # Since most have inline styles and no class, we can just replace `<section id="id"` with `<section id="id" class="one-screen"`
    
    # Wait, let's check if it already has a class.
    # From grep output:
    # id="analisis-produk" class="analisis-section" -> This one is excluded.
    # Others seem to have only style or nothing.
    
    html = html.replace(f'<section id="{section_id}"', f'<section id="{section_id}" class="one-screen"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated.")
