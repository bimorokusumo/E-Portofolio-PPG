import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Hero & Profil
hero_profil_pattern = re.compile(r'<section id="home">.*?</section>\s*<!-- 2\. Profil Singkat -->\s*<section id="profil".*?</section>', re.DOTALL)

new_hero_profil = """
    <section id="home" style="padding: 6rem 2rem; background: white; text-align: left;">
        <div class="split-layout">
            <div class="split-left" style="align-items: center; justify-content: center;">
                <img src="foto-profil-biru.jpg" alt="Foto Bimoro Kusumo" style="width: 280px; height: 280px; border-radius: 50%; object-fit: cover; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 6px solid var(--kemendikbud-blue);">
            </div>
            <div class="split-right" style="justify-content: center;">
                <h1 class="hero-title" style="margin-top: 0; text-align: left;">Hai, Saya Bimoro Kusumo</h1>
                <p style="font-size: 1.1rem; margin: 0; color: var(--text-dark); line-height: 1.6;">
                    Mahasiswa Pendidikan Profesi Guru (PPG) LPTK Universitas Sarjanawiyata Tamansiswa (UST).<br>
                    Mengajar di SMK Negeri 2 Depok Sleman, salah satu sekolah vokasi menengah favorit di Yogyakarta.<br>
                    Mata pelajaran DDK Teknik Pemesinan dan Teknik Fabrikasi Logam dan Manufaktur.
                </p>
                
                <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
                    <span style="background: var(--bg-light-gray); padding: 0.6rem 1.2rem; border-radius: 30px; font-size: 0.95rem; font-weight: 500; color: var(--text-dark); display: inline-flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.1rem;">🎓</span> Lulusan Terbaik S1 UNY (IPK 3.87)</span>
                    <span style="background: var(--bg-light-gray); padding: 0.6rem 1.2rem; border-radius: 30px; font-size: 0.95rem; font-weight: 500; color: var(--text-dark); display: inline-flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.1rem;">🏫</span> PPG Prajabatan UST 2026</span>
                </div>

                <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem;">
                    <a href="https://wa.me/6289669258175" target="_blank" class="btn-primary" style="display: flex; align-items: center; gap: 8px; background-color: #25D366; border-color: #25D366; font-size: 0.9rem; padding: 0.6rem 1.2rem;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
                    </a>
                    <a href="mailto:bimoro7@gmail.com" target="_blank" class="btn-primary" style="display: flex; align-items: center; gap: 8px; background-color: #EA4335; border-color: #EA4335; font-size: 0.9rem; padding: 0.6rem 1.2rem;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    </a>
                    <a href="https://instagram.com/Bimoo_id" target="_blank" class="btn-primary" style="display: flex; align-items: center; gap: 8px; background-color: #E1306C; border-color: #E1306C; font-size: 0.9rem; padding: 0.6rem 1.2rem;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                    </a>
                    <a href="https://www.linkedin.com/feed/" target="_blank" class="btn-primary" style="display: flex; align-items: center; gap: 8px; background-color: #0077b5; border-color: #0077b5; font-size: 0.9rem; padding: 0.6rem 1.2rem;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                    </a>
                    <a href="https://www.youtube.com/@bimorokusumo" target="_blank" class="btn-primary" style="display: flex; align-items: center; gap: 8px; background-color: #FF0000; border-color: #FF0000; font-size: 0.9rem; padding: 0.6rem 1.2rem;">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.5 12 3.5 12 3.5s-7.505 0-9.377.55a3.016 3.016 0 0 0-2.122 2.136C0 8.07 0 12 0 12s0 3.93.501 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.55 9.377.55 9.377.55s7.505 0 9.377-.55a3.016 3.016 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. Profil Singkat -->
    <section id="profil" class="one-screen" style="max-width: 100%; padding: 4rem 2rem; background-color: var(--bg-light-gray);">
        <div class="split-layout align-start">
            <div class="split-left">
                <h2 style="margin-bottom: 1rem; color: var(--kemendikbud-blue); display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 2rem;">👨‍🏫</span> Profil Singkat
                </h2>
                
                <div style="background: white; padding: 1.5rem 1.8rem; border-radius: 12px; border-left: 5px solid var(--kemendikbud-blue); box-shadow: 0 4px 6px rgba(0,0,0,0.03);">
                    <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: var(--kemendikbud-blue); font-size: 1.1rem;">🌍 Latar Belakang</h4>
                    <p style="margin: 0; color: var(--text-dark); line-height: 1.7;">
                        Saya berasal dan tumbuh besar di <strong>Ambarketawang, Gamping, Sleman</strong>, sebuah daerah yang kaya akan nilai historis sebagai lokasi pesanggrahan pertama Keraton Yogyakarta dan sangat ikonik dengan tradisi budaya gotong royong <em>Saparan Bekakak</em>. Tumbuh dalam harmoni kearifan lokal yang kental ini membentuk karakter saya menjadi pribadi yang menjunjung tinggi etika, ulet, adaptif, serta memiliki tekad kuat untuk membangun masyarakat melalui pendidikan kejuruan.
                    </p>
                </div>

                <div style="background: white; padding: 1.5rem 1.8rem; border-radius: 12px; border-left: 5px solid #F59E0B; box-shadow: 0 4px 6px rgba(0,0,0,0.03);">
                    <h4 style="margin-top: 0; margin-bottom: 0.5rem; color: #D97706; font-size: 1.1rem;">💡 Inspirasi Menjadi Guru</h4>
                    <p style="margin: 0; color: var(--text-dark); line-height: 1.7;">
                        Melihat besarnya potensi anak muda di bidang kejuruan memotivasi saya untuk membagikan keahlian yang saya miliki. Saya percaya bahwa pendidikan vokasi yang tepat dapat mengubah hidup seseorang. Oleh karena itu, saya tergerak untuk mendampingi siswa agar tidak hanya cerdas berteori, namun juga memiliki keterampilan teknis yang mumpuni.
                    </p>
                </div>
            </div>

            <div class="split-right">
                <div style="background: white; border-radius: 20px; padding: 3rem 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.06); border: 1px solid var(--border-color); position: relative; overflow: hidden; height: 100%;">
                    <div style="position: absolute; top: 0; left: 0; right: 0; height: 6px; background: linear-gradient(90deg, var(--kemendikbud-blue), var(--kemendikbud-cyan));"></div>
                    
                    <h4 style="margin-top: 0; margin-bottom: 1rem; color: #059669; font-size: 1.2rem; display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 1.5rem;">🎯</span> Tujuan Profesional
                    </h4>
                    <p style="margin: 0; color: var(--text-dark); line-height: 1.7; font-size: 1rem; text-align: justify;">
                        Tujuan saya mengikuti program PPG Prajabatan 2026 adalah untuk meningkatkan kompetensi pedagogik, profesional, sosial, dan kepribadian sebagai calon guru di bidang Teknik Pemesinan. Melalui program ini, saya ingin memperdalam pemahaman tentang perencanaan pembelajaran yang efektif, pengelolaan kelas yang kondusif, serta penerapan asesmen yang autentik dan bermakna. Saya berkomitmen untuk menjadi guru yang mampu menghadirkan pengalaman belajar yang aplikatif, relevan dengan kebutuhan dunia industri, serta mampu membentuk karakter peserta didik yang kompeten, adaptif, dan siap bersaing di era global.
                    </p>
                    
                    <div style="background: #EAF5FA; padding: 1.5rem; border-radius: 12px; font-style: italic; color: var(--text-light); margin-top: 2rem; text-align: center;">
                        <div style="font-size: 2rem; color: var(--kemendikbud-cyan); line-height: 0.5; text-align: left; margin-bottom: 0.5rem;">❝</div>
                        Pendidikan bukan sekadar mengisi wadah yang kosong, melainkan menyalakan api yang akan terus berkobar menerangi masa depan.
                        <div style="font-size: 2rem; color: var(--kemendikbud-cyan); line-height: 0.5; text-align: right; margin-top: 1rem;">❞</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

html = hero_profil_pattern.sub(new_hero_profil, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Hero and Profil")
