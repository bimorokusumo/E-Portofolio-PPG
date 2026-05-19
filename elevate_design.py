with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update :root variables
old_root = """:root {
  --kemendikbud-cyan: #4BB1E4;
  --kemendikbud-blue: #0059B2;
  --kemendikbud-blue-hover: #004488;
  --text-dark: #333333;
  --text-black: #000000;
  --text-light: #666666;
  --bg-white: #FFFFFF;
  --bg-light-gray: #F5F5F5;
  --border-color: #E5E5E5;
  --radius-md: 8px;
  --radius-lg: 12px;
  --font-main: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --transition: all 0.2s ease-in-out;
}"""

new_root = """:root {
  --kemendikbud-cyan: #0284c7;
  --kemendikbud-blue: #0284c7;
  --kemendikbud-blue-hover: #0369a1;
  --kemendikbud-green: #10b981;
  --kemendikbud-green-hover: #059669;
  --text-dark: #1e293b;
  --text-black: #0f172a;
  --text-light: #64748b;
  --bg-white: #FFFFFF;
  --bg-light-gray: #f8fafc;
  --border-color: #e2e8f0;
  --radius-md: 12px;
  --radius-lg: 16px;
  --font-main: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}"""

if old_root in css:
    css = css.replace(old_root, new_root)

# 2. Update nav
old_nav = """nav {
  position: fixed;
  top: 0;
  width: 100%;
  background: var(--bg-white);
  border-bottom: 1px solid var(--border-color);
  z-index: 1000;
  padding: 0;
  height: 70px;
  display: flex;
  align-items: center;
}"""

new_nav = """nav {
  position: fixed;
  top: 0;
  width: 100%;
  background: rgba(255, 255, 255, 0.85) !important;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(226, 232, 240, 0.8);
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
  z-index: 1000;
  padding: 0;
  height: 70px;
  display: flex;
  align-items: center;
}"""

if old_nav in css:
    css = css.replace(old_nav, new_nav)

# 3. Update Hero
old_hero = """#home {
  margin-top: 70px; /* offset for nav */
  background-color: var(--kemendikbud-cyan);
  background-image: linear-gradient(rgba(75, 177, 228, 0.85), rgba(0, 89, 178, 0.85)), url('bg-hero.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 5rem 2rem;
  text-align: center;
  color: var(--bg-white);
  max-width: 100%;
}"""

new_hero = """#home {
  margin-top: 70px; /* offset for nav */
  background-color: var(--kemendikbud-blue);
  background-image: linear-gradient(135deg, rgba(2, 132, 199, 0.92), rgba(16, 185, 129, 0.88)), url('bg-hero.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 6rem 2rem;
  text-align: center;
  color: var(--bg-white);
  max-width: 100%;
}"""

if old_hero in css:
    css = css.replace(old_hero, new_hero)

# 4. Update hero img & btn-primary
old_btn = """.btn-primary {
  background-color: var(--kemendikbud-blue);
  color: var(--bg-white) !important;
  padding: 0.5rem 1.2rem;
  border-radius: 4px;
  font-weight: 500;
  border: 1px solid var(--kemendikbud-blue);
}

.btn-primary:hover {
  background-color: var(--bg-white);
  color: var(--kemendikbud-blue) !important;
  text-decoration: none;
}"""

new_btn = """.btn-primary {
  background-color: var(--kemendikbud-blue);
  color: var(--bg-white) !important;
  padding: 0.6rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  border: 1px solid var(--kemendikbud-blue);
  box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25);
  transition: var(--transition);
}

.btn-primary:hover {
  background-color: var(--kemendikbud-green);
  border-color: var(--kemendikbud-green);
  color: var(--bg-white) !important;
  box-shadow: 0 6px 16px rgba(16, 185, 129, 0.3);
  transform: translateY(-1px);
  text-decoration: none;
}"""

if old_btn in css:
    css = css.replace(old_btn, new_btn)

# 5. Update Category Cards
old_cat = """.card-category {
  background: var(--bg-light-gray);
  border-radius: var(--radius-md);
  padding: 2rem 1.5rem;
  text-align: justify;
  transition: var(--transition);
  cursor: pointer;
  border: 1px solid transparent;
}

.card-category:hover {
  border-color: var(--kemendikbud-cyan);
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}"""

new_cat = """.card-category {
  background: var(--bg-white);
  border-radius: 16px;
  padding: 2.2rem 1.8rem;
  text-align: justify;
  transition: var(--transition);
  cursor: pointer;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.01);
}

.card-category:hover {
  border-color: var(--kemendikbud-green);
  box-shadow: 0 12px 24px -4px rgba(16, 185, 129, 0.12), 0 4px 6px -2px rgba(16, 185, 129, 0.05);
  transform: translateY(-4px);
}"""

if old_cat in css:
    css = css.replace(old_cat, new_cat)

# 6. Update Article Cards
old_art = """.card-article {
  background: var(--bg-white);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  border: 1px solid var(--border-color);
  transition: var(--transition);
}

.card-article:hover {
  border-color: var(--kemendikbud-blue);
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}"""

new_art = """.card-article {
  background: var(--bg-white);
  border-radius: 16px;
  padding: 1.8rem;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
  transition: var(--transition);
}

.card-article:hover {
  border-color: var(--kemendikbud-blue);
  box-shadow: 0 12px 24px -4px rgba(2, 132, 199, 0.12);
  transform: translateY(-4px);
}"""

if old_art in css:
    css = css.replace(old_art, new_art)

# 7. Update Profile Container & Quote Box
old_prof = """.profile-container {
  background: var(--bg-white);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 3rem;
  margin-top: 2rem;
}

.profile-container p {
  color: var(--text-dark);
  font-size: 1.05rem;
}

.quote-box {
  margin-top: 2rem;
  padding: 1.5rem;
  background: #EAF5FA; /* Very light cyan */
  border-left: 4px solid var(--kemendikbud-blue);
  font-style: italic;
  color: var(--kemendikbud-blue);
}"""

new_prof = """.profile-container {
  background: var(--bg-white);
  border: 1px solid var(--border-color);
  border-top: 4px solid var(--kemendikbud-blue);
  border-radius: 20px;
  padding: 3.5rem;
  margin-top: 2rem;
  box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.03);
}

.profile-container p {
  color: var(--text-dark);
  font-size: 1.05rem;
  line-height: 1.7;
}

.quote-box {
  margin-top: 2.5rem;
  padding: 1.8rem;
  background: #f0fdf4; /* Very light emerald */
  border-left: 4px solid var(--kemendikbud-green);
  border-radius: 0 12px 12px 0;
  font-style: italic;
  color: #15803d;
  font-size: 1.1rem;
}"""

if old_prof in css:
    css = css.replace(old_prof, new_prof)

# 8. Update Doc Cards (Accordion Gallery)
old_doc = """.doc-card {
  background: #252836;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  text-align: left;
}

.doc-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.25);
}

.doc-card-thumb {
  height: 140px;
  background-color: #1F1D2B;
  background-image: linear-gradient(45deg, #1F1D2B 25%, #252836 25%, #252836 50%, #1F1D2B 50%, #1F1D2B 75%, #252836 75%, #252836 100%);
  background-size: 20px 20px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}"""

new_doc = """.doc-card {
  background: #1e293b;
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 10px 25px -5px rgba(0,0,0,0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
  display: flex;
  flex-direction: column;
  text-align: left;
}

.doc-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 35px -10px rgba(16, 185, 129, 0.25);
  border-color: rgba(16, 185, 129, 0.3);
}

.doc-card-thumb {
  height: 150px;
  background-color: #0f172a;
  background-image: linear-gradient(45deg, #0f172a 25%, #1e293b 25%, #1e293b 50%, #0f172a 50%, #0f172a 75%, #1e293b 75%, #1e293b 100%);
  background-size: 20px 20px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}"""

if old_doc in css:
    css = css.replace(old_doc, new_doc)

old_badge = """.doc-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: #8b5cf6;
  color: white;
  padding: 0.3rem 0.8rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: bold;
}"""

new_badge = """.doc-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: var(--kemendikbud-green);
  color: white;
  padding: 0.3rem 0.8rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 700;
  box-shadow: 0 4px 10px rgba(16, 185, 129, 0.3);
}"""

if old_badge in css:
    css = css.replace(old_badge, new_badge)

old_overlay_btn = """.doc-overlay-btn:hover {
  text-decoration: none;
  background: white;
  color: var(--kemendikbud-blue);
}"""

new_overlay_btn = """.doc-overlay-btn:hover {
  text-decoration: none;
  background: var(--kemendikbud-green);
  color: white;
  box-shadow: 0 6px 16px rgba(16, 185, 129, 0.4);
}"""

if old_overlay_btn in css:
    css = css.replace(old_overlay_btn, new_overlay_btn)

# 9. Update Analisis Cards
old_analisis_card = """.analisis-card {
    background: #232936;
    border-radius: 16px;
    padding: 2rem 1.5rem;
    position: relative;
    border: 1px solid rgba(255,255,255,0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
}"""

new_analisis_card = """.analisis-card {
    background: #1e293b;
    border-radius: 20px;
    padding: 2.2rem 1.8rem;
    position: relative;
    border: 1px solid rgba(255,255,255,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    display: flex;
    flex-direction: column;
    box-shadow: 0 10px 25px -5px rgba(0,0,0,0.2);
}"""

if old_analisis_card in css:
    css = css.replace(old_analisis_card, new_analisis_card)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Website design elevated successfully.")
