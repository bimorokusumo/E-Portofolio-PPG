with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update nav styles
old_nav_container = """.nav-container {
  max-width: 1160px;
  width: 100%;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}"""

new_nav_container = """.nav-container {
  max-width: 1350px;
  width: 100%;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}"""

old_nav_links = """.nav-links {
  display: flex;
  list-style: none;
  gap: 1.5rem;
  align-items: center;
}

.nav-links a {
  color: var(--text-dark);
  font-weight: 400;
  font-size: 0.95rem;
}"""

new_nav_links = """.nav-links {
  display: flex;
  list-style: none;
  gap: 1.1rem;
  align-items: center;
}

.nav-links a {
  color: var(--text-dark);
  font-weight: 500;
  font-size: 0.92rem;
  white-space: nowrap;
}"""

if old_nav_container in css:
    css = css.replace(old_nav_container, new_nav_container)
if old_nav_links in css:
    css = css.replace(old_nav_links, new_nav_links)

# 2. Update analisis-section styles
old_analisis = """/* Analisis Produk Section */
.analisis-section {
    background-color: #1a1e29;
    background-image: radial-gradient(circle at top right, #1d2538, #1a1e29);
    padding: 5rem 2rem;
    color: #fff;
    font-family: 'Inter', sans-serif;
}

.analisis-header {
    text-align: center;
    max-width: 800px;
    margin: 0 auto 4rem auto;
}

.analisis-subtitle {
    color: #a0aec0;
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.analisis-header h2 {
    font-size: 2.5rem;
    margin-top: 0;
    margin-bottom: 1rem;
    color: #e2e8f0;
}

.analisis-desc {
    color: #94a3b8;
    line-height: 1.6;
    font-size: 1.05rem;
}"""

new_analisis = """/* Analisis Produk Section */
.analisis-section {
    background-color: var(--bg-white);
    padding: 5rem 2rem;
    color: var(--text-dark);
    font-family: 'Inter', sans-serif;
    border-top: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
}

.analisis-header {
    text-align: center;
    max-width: 800px;
    margin: 0 auto 4rem auto;
}

.analisis-subtitle {
    color: var(--kemendikbud-blue);
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.analisis-header h2 {
    font-size: 2.5rem;
    margin-top: 0;
    margin-bottom: 1rem;
    color: var(--text-black);
}

.analisis-desc {
    color: var(--text-light);
    line-height: 1.6;
    font-size: 1.05rem;
}"""

if old_analisis in css:
    css = css.replace(old_analisis, new_analisis)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Styles refined successfully.")
