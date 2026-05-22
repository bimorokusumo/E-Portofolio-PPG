import re
import os

target_dir = "/Users/macbookpro2017/Desktop/PPG 2025/KULIAH PPG/UTS/E-Portofolio-PPG"
build_script_path = os.path.join(target_dir, "build_hasil_kerja.py")
menu_path = os.path.join(target_dir, "hasil-kerja.html")

# 1. Update build_hasil_kerja.py to use <details> instead of .analysis-box
with open(build_script_path, "r", encoding="utf-8") as f:
    build_code = f.read()

analysis_box_pattern = re.compile(r'<div style="background: #f8faff; padding: 2rem 1rem;">\s*<div class="analysis-box">.*?</div>\s*</div>\s*</div>', re.DOTALL)

details_block = """    <div style="background: #f8faff; padding: 2rem 1rem; display: flex; justify-content: center;">
        <div style="max-width: 900px; width: 100%;">
            <details style="margin: 1rem 0; font-size: 0.95rem; text-align: left; background: white; border: 1px solid var(--border-color); padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);" open>
                <summary style="cursor: pointer; font-weight: 700; color: #1565C0; outline: none; font-size: 1.1rem; border-bottom: 1px solid #f0f0f0; padding-bottom: 0.8rem; margin-bottom: 1rem;">📝 Analisis Artefak Hasil Kerja Siswa</summary>
                <div style="display: flex; flex-direction: column; gap: 1rem; color: #333;">
                    <div><strong>🎯 Konteks:</strong> <br><span style="color: #555; line-height: 1.6;">{konteks}</span></div>
                    <div><strong>💡 Tujuan:</strong> <br><span style="color: #555; line-height: 1.6;">{tujuan}</span></div>
                    <div><strong>✅ Kelebihan:</strong> <br><span style="color: #555; line-height: 1.6;">{kelebihan}</span></div>
                    <div><strong>⚠️ Kekurangan:</strong> <br><span style="color: #555; line-height: 1.6;">{kekurangan}</span></div>
                </div>
            </details>
        </div>
    </div>"""

# Ensure we replace exactly what is needed
build_code = re.sub(r'<div style="background: #f8faff; padding: 2rem 1rem;">\s*<div class="analysis-box">.*?</div>\s*</div>\s*</div>', details_block, build_code, flags=re.DOTALL)

with open(build_script_path, "w", encoding="utf-8") as f:
    f.write(build_code)

# Execute the script to update all pages
os.system(f'cd "{target_dir}" && python3 build_hasil_kerja.py')


# 2. Update hasil-kerja.html menu (in case that was what they meant)
import sys
sys.path.insert(0, target_dir)
from build_hasil_kerja import pages

template_tp = ""
template_tflm = ""

for page in pages:
    card = f"""
            <div class="doc-card gallery-card-item" data-category="hasil-kerja">
                <div class="doc-card-thumb" style="background: #f8faff; display: flex; align-items: center; justify-content: center; height: 180px; border-bottom: 1px solid #eee;">
                    <span style="font-size: 5rem;">{page['icon']}</span>
                    <a href="{page['file']}" class="doc-overlay-btn" target="_blank">📄 Buka Galeri</a>
                </div>
                <div class="doc-card-content">
                    <h4>Hasil Kerja Siswa - {page['title']}</h4>
                    <p>Dokumentasi hasil kerja nyata peserta didik selama proses pembelajaran berlangsung.</p>
                    <details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                        <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                        <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                            <div><strong>Konteks:</strong> <br><span style="color: var(--text-light);">{page['konteks']}</span></div>
                            <div><strong>Tujuan:</strong> <br><span style="color: var(--text-light);">{page['tujuan']}</span></div>
                            <div><strong>Kelebihan:</strong> <br><span style="color: var(--text-light);">{page['kelebihan']}</span></div>
                            <div><strong>Kekurangan:</strong> <br><span style="color: var(--text-light);">{page['kekurangan']}</span></div>
                        </div>
                    </details>
                    <a href="{page['file']}" class="doc-btn" target="_blank">Lihat Galeri Lengkap</a>
                </div>
            </div>"""
    if "TP" in page['bagian']:
        template_tp += card
    else:
        template_tflm += card

with open(menu_path, "r", encoding="utf-8") as f:
    html = f.read()

tp_pattern = re.compile(r'<h4.*?Bagian TP.*?</h4>.*?</div>', re.DOTALL)
new_tp = f'<h4 style="margin-bottom: 1rem; color: var(--kemendikbud-blue); text-align: left; max-width: 1000px; margin-left: auto; margin-right: auto; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">Bagian TP (Teknik Pemesinan)</h4>\n        <div class="doc-grid gallery-grid" style="max-width: 1000px; margin: 0 auto 2rem;">{template_tp}\n        </div>'
if tp_pattern.search(html):
    html = tp_pattern.sub(new_tp, html)

tflm_pattern = re.compile(r'<h4.*?Bagian TFLM.*?</h4>.*?</div>', re.DOTALL)
new_tflm = f'<h4 style="margin-bottom: 1rem; color: var(--kemendikbud-blue); text-align: left; max-width: 1000px; margin-left: auto; margin-right: auto; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">Bagian TFLM (Teknik Fabrikasi Logam dan Manufaktur)</h4>\n        <div class="doc-grid gallery-grid" style="max-width: 1000px; margin: 0 auto 3rem;">{template_tflm}\n        </div>'
if tflm_pattern.search(html):
    html = tflm_pattern.sub(new_tflm, html)

# Remove the global summary block if it's still there
summary_pattern = re.compile(r'<div style="text-align: left; background: var\(--bg-light-gray\); padding: 1.5rem;.*?</div>', re.DOTALL)
html = summary_pattern.sub('', html, count=1)

with open(menu_path, "w", encoding="utf-8") as f:
    f.write(html)

print("ALL DONE")
