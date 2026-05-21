with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_profil_html = """
<!-- 2. Profil Singkat -->
<section class="one-screen" id="profil" style="max-width: 100%; padding: 5rem 2rem; background: linear-gradient(135deg, #f8fafc 0%, #eef2f6 100%); min-height: 80vh; display: flex; flex-direction: column; justify-content: center; position: relative; overflow: hidden;">
    
    <!-- Decorative background elements -->
    <div style="position: absolute; top: -100px; right: -100px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(14, 165, 233, 0.05) 0%, rgba(255,255,255,0) 70%); border-radius: 50%; z-index: 0;"></div>
    <div style="position: absolute; bottom: -100px; left: -100px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(16, 185, 129, 0.05) 0%, rgba(255,255,255,0) 70%); border-radius: 50%; z-index: 0;"></div>

    <div style="text-align: center; margin-bottom: 3.5rem; position: relative; z-index: 1;">
        <h2 style="color: var(--kemendikbud-blue); font-size: 2.5rem; margin-bottom: 0.8rem; font-weight: 800;"><span style="font-size: 2.5rem; vertical-align: middle; margin-right: 10px;">👨‍🏫</span> Profil Singkat</h2>
        <p style="color: #64748b; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">Mengenal lebih dekat latar belakang, visi, dan inspirasi saya dalam dunia pendidikan.</p>
    </div>

    <div style="max-width: 1160px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem; position: relative; z-index: 1;">
        
        <!-- Latar Belakang -->
        <div style="background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(12px); padding: 2.5rem; border-radius: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.04); border: 1px solid rgba(255,255,255,1); transition: all 0.4s ease; cursor: default;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 45px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 15px 35px rgba(0,0,0,0.04)';">
            <div style="width: 55px; height: 55px; background: linear-gradient(135deg, #e0f2fe, #bae6fd); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.8rem;">
                <span style="font-size: 1.8rem;">🌍</span>
            </div>
            <h4 style="color: #0369a1; font-size: 1.35rem; margin-top: 0; margin-bottom: 1rem; font-weight: 700;">Latar Belakang</h4>
            <p style="color: #475569; line-height: 1.7; font-size: 1.05rem; margin: 0;">
                Berakar dari <strong>Ambarketawang, Gamping, Sleman</strong>, sebuah kawasan dengan histori pesanggrahan pertama Keraton Yogyakarta. Harmoni kearifan lokal ini membentuk karakter saya menjadi pribadi yang menjunjung etika, ulet, adaptif, serta bertekad kuat membangun masyarakat melalui pendidikan kejuruan.
            </p>
        </div>

        <!-- Tujuan Profesional -->
        <div style="background: linear-gradient(145deg, #0284c7, #1d4ed8); padding: 2.5rem; border-radius: 24px; box-shadow: 0 20px 40px rgba(29, 78, 216, 0.25); position: relative; overflow: hidden; color: white; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-8px) scale(1.02)';" onmouseout="this.style.transform='translateY(0) scale(1)';">
            <!-- Glass decoration -->
            <div style="position: absolute; top: -30px; right: -30px; width: 180px; height: 180px; background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 100%); border-radius: 50%; backdrop-filter: blur(10px);"></div>
            <div style="position: absolute; bottom: -20px; left: -20px; width: 100px; height: 100px; background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 100%); border-radius: 50%;"></div>
            
            <div style="position: relative; z-index: 2;">
                <div style="width: 55px; height: 55px; background: rgba(255,255,255,0.2); border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-bottom: 1.8rem; backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.3);">
                    <span style="font-size: 1.8rem;">🎯</span>
                </div>
                <h4 style="color: white; font-size: 1.35rem; margin-top: 0; margin-bottom: 1rem; font-weight: 700;">Tujuan Profesional</h4>
                <p style="color: rgba(255,255,255,0.95); line-height: 1.7; font-size: 1.05rem; margin: 0; text-align: justify;">
                    Melalui program PPG Prajabatan 2026, saya berkomitmen meningkatkan kompetensi pedagogik, profesional, dan sosial. Saya bertekad menjadi guru Teknik Pemesinan yang menghadirkan pembelajaran aplikatif, relevan dengan industri, serta mampu mencetak generasi yang kompeten dan adaptif di era global.
                </p>
            </div>
        </div>

        <!-- Inspirasi & Quote -->
        <div style="display: flex; flex-direction: column; gap: 1.5rem;">
            <!-- Inspirasi -->
            <div style="background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(12px); padding: 2rem; border-radius: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.04); border: 1px solid rgba(255,255,255,1); flex: 1; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-6px)';" onmouseout="this.style.transform='translateY(0)';">
                <h4 style="color: #d97706; font-size: 1.25rem; margin-top: 0; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 10px; font-weight: 700;">
                    <span style="font-size: 1.5rem;">💡</span> Inspirasi Guru
                </h4>
                <p style="color: #475569; line-height: 1.65; font-size: 1rem; margin: 0;">
                    Melihat besarnya potensi anak muda vokasi memotivasi saya. Saya percaya pendidikan yang tepat tak hanya membekali teori, tapi juga <em>skill</em> teknis yang mampu mengubah nasib dan masa depan mereka.
                </p>
            </div>
            
            <!-- Quote -->
            <div style="background: #ffffff; padding: 2rem; border-radius: 24px; border-left: 6px solid #10b981; position: relative; box-shadow: 0 10px 25px rgba(0,0,0,0.03);">
                <span style="position: absolute; top: -5px; right: 20px; font-size: 5rem; color: #f1f5f9; font-family: Georgia, serif; line-height: 1;">"</span>
                <p style="color: #334155; font-style: italic; font-weight: 500; font-size: 1.1rem; line-height: 1.6; margin: 0; position: relative; z-index: 1;">
                    Pendidikan bukan sekadar mengisi wadah yang kosong, melainkan menyalakan api yang akan terus berkobar menerangi masa depan.
                </p>
            </div>
        </div>

    </div>
</section>
"""

start_idx = html.find('id="profil"')
if start_idx != -1:
    section_start = html.rfind('<!-- 2. Profil Singkat -->', 0, start_idx)
    section_end = html.find('<!-- 2.5 Pengalaman Kerja -->', start_idx)
    
    result = html[:section_start] + new_profil_html.strip() + "\n" + html[section_end:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print("Replaced profil section")
else:
    print("Could not find id='profil'")
