with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_model_guru_html = """
<!-- 5. Model Guru yang Dituju -->
<section class="one-screen" id="model-guru" style="max-width: 100%; padding: 5rem 2rem; background: linear-gradient(180deg, #ffffff 0%, #f9fafb 100%); position: relative; overflow: hidden;">

    <!-- Decorative -->
    <div style="position: absolute; top: -80px; left: -80px; width: 300px; height: 300px; background: radial-gradient(circle, rgba(14,165,233,0.06) 0%, transparent 70%); border-radius: 50%;"></div>
    <div style="position: absolute; bottom: -80px; right: -80px; width: 350px; height: 350px; background: radial-gradient(circle, rgba(168,85,247,0.05) 0%, transparent 70%); border-radius: 50%;"></div>

    <div style="max-width: 1100px; margin: 0 auto; position: relative; z-index: 1;">

        <!-- Header -->
        <div style="text-align: center; margin-bottom: 4rem;">
            <h2 style="color: var(--kemendikbud-blue); font-size: 2.5rem; margin-bottom: 0.8rem; font-weight: 800;">
                Model Guru Profesional
            </h2>
        </div>

        <!-- Misi & Kompetensi Split -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem;">
            
            <!-- Misi Menjadi Guru -->
            <div>
                <h3 style="font-size: 1.6rem; color: var(--text-dark); margin-bottom: 2rem; border-bottom: 3px solid var(--kemendikbud-blue); padding-bottom: 0.5rem; display: inline-block;">Misi Menjadi Guru</h3>
                
                <div style="display: flex; flex-direction: column; gap: 2rem;">
                    <!-- Misi 1 -->
                    <div style="display: flex; gap: 1.5rem; align-items: flex-start; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(10px)';" onmouseout="this.style.transform='translateX(0)';">
                        <div style="width: 50px; height: 50px; border-radius: 50%; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; background: white; flex-shrink: 0; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
                            <span style="font-size: 1.2rem;">🤝</span>
                        </div>
                        <div>
                            <h4 style="font-size: 1.15rem; color: var(--text-dark); margin: 0 0 0.6rem 0; font-weight: 700;">Memutus Rantai Keterbatasan Melalui Pendidikan Inklusif</h4>
                            <p style="color: var(--text-light); line-height: 1.65; margin: 0; font-size: 0.95rem;">Menghadirkan pendidikan vokasi yang adil, bermakna, dan menyenangkan agar setiap peserta didik memiliki kesempatan meraih masa depan yang lebih baik di dunia industri.</p>
                        </div>
                    </div>

                    <!-- Misi 2 -->
                    <div style="display: flex; gap: 1.5rem; align-items: flex-start; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(10px)';" onmouseout="this.style.transform='translateX(0)';">
                        <div style="width: 50px; height: 50px; border-radius: 50%; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; background: white; flex-shrink: 0; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
                            <span style="font-size: 1.2rem;">🔗</span>
                        </div>
                        <div>
                            <h4 style="font-size: 1.15rem; color: var(--text-dark); margin: 0 0 0.6rem 0; font-weight: 700;">Menjembatani Pendidikan Vokasi dan Industri</h4>
                            <p style="color: var(--text-light); line-height: 1.65; margin: 0; font-size: 0.95rem;">Membekali peserta didik dengan keterampilan teknologi manufaktur, DDK TP, dan TFLM yang relevan dengan kebutuhan dunia industri modern.</p>
                        </div>
                    </div>

                    <!-- Misi 3 -->
                    <div style="display: flex; gap: 1.5rem; align-items: flex-start; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(10px)';" onmouseout="this.style.transform='translateX(0)';">
                        <div style="width: 50px; height: 50px; border-radius: 50%; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; background: white; flex-shrink: 0; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
                            <span style="font-size: 1.2rem;">♾️</span>
                        </div>
                        <div>
                            <h4 style="font-size: 1.15rem; color: var(--text-dark); margin: 0 0 0.6rem 0; font-weight: 700;">Mencetak Pembelajar Sepanjang Hayat</h4>
                            <p style="color: var(--text-light); line-height: 1.65; margin: 0; font-size: 0.95rem;">Menumbuhkan semangat belajar, ketekunan, dan kemampuan beradaptasi agar peserta didik siap menghadapi tantangan inovasi manufaktur masa depan.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Kompetensi yang Ingin Dibangun -->
            <div>
                <h3 style="font-size: 1.6rem; color: var(--text-dark); margin-bottom: 2rem; border-bottom: 3px solid var(--kemendikbud-blue); padding-bottom: 0.5rem; display: inline-block;">Kompetensi yang Ingin Dibangun</h3>
                
                <div style="display: flex; flex-direction: column; gap: 2rem;">
                    <!-- Komp 1 -->
                    <div style="display: flex; gap: 1.5rem; align-items: flex-start; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(10px)';" onmouseout="this.style.transform='translateX(0)';">
                        <div style="width: 50px; height: 50px; border-radius: 50%; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; background: white; flex-shrink: 0; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
                            <span style="font-size: 1.2rem;">⚙️</span>
                        </div>
                        <div>
                            <h4 style="font-size: 1.15rem; color: var(--text-dark); margin: 0 0 0.6rem 0; font-weight: 700;">Kompetensi Profesional Berbasis Industri (Teknologi Manufaktur)</h4>
                            <p style="color: var(--text-light); line-height: 1.65; margin: 0; font-size: 0.95rem;">Mengembangkan keahlian teknis Dasar-Dasar Kejuruan Teknik Pemesinan (DDK TP) dan Teknik Fabrikasi Logam & Manufaktur (TFLM) agar pembelajaran selalu selaras dengan industri terkini.</p>
                        </div>
                    </div>

                    <!-- Komp 2 -->
                    <div style="display: flex; gap: 1.5rem; align-items: flex-start; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(10px)';" onmouseout="this.style.transform='translateX(0)';">
                        <div style="width: 50px; height: 50px; border-radius: 50%; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; background: white; flex-shrink: 0; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
                            <span style="font-size: 1.2rem;">👨‍🏫</span>
                        </div>
                        <div>
                            <h4 style="font-size: 1.15rem; color: var(--text-dark); margin: 0 0 0.6rem 0; font-weight: 700;">Kompetensi Pedagogik yang Transformatif</h4>
                            <p style="color: var(--text-light); line-height: 1.65; margin: 0; font-size: 0.95rem;">Merancang pembelajaran praktik perbengkelan yang aktif, bermakna, dan mudah dipahami, dengan mengutamakan keselamatan kerja sesuai karakteristik peserta didik.</p>
                        </div>
                    </div>

                    <!-- Komp 3 -->
                    <div style="display: flex; gap: 1.5rem; align-items: flex-start; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(10px)';" onmouseout="this.style.transform='translateX(0)';">
                        <div style="width: 50px; height: 50px; border-radius: 50%; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center; background: white; flex-shrink: 0; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
                            <span style="font-size: 1.2rem;">👤</span>
                        </div>
                        <div>
                            <h4 style="font-size: 1.15rem; color: var(--text-dark); margin: 0 0 0.6rem 0; font-weight: 700;">Kompetensi Kepribadian sebagai Pembelajar Sejati</h4>
                            <p style="color: var(--text-light); line-height: 1.65; margin: 0; font-size: 0.95rem;">Memiliki semangat belajar sepanjang hayat, terbuka terhadap evaluasi diri, dan menjadikan keberhasilan kompetensi peserta didik sebagai motivasi utama.</p>
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
    </div>
</section>
"""

start_idx = html.find('id="model-guru"')
if start_idx != -1:
    section_start = html.rfind('<!-- 5. Model Guru yang Dituju -->', 0, start_idx)
    section_end = html.find('<!-- END PORTFOLIO 1 -->', start_idx)
    
    result = html[:section_start] + new_model_guru_html.strip() + "\n" + html[section_end:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print("Replaced model-guru section")
else:
    print("Could not find id='model-guru'")
