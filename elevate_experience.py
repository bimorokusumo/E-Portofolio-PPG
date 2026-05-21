import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html = """
<section class="one-screen" id="pengalaman" style="background-color: #fafcff; max-width: 100%; padding: 5rem 2rem; position: relative; overflow: hidden;">
    <div style="max-width: 1000px; margin: 0 auto; position: relative; z-index: 2;">
        <div style="text-align: center; margin-bottom: 4rem;">
            <h2 style="color: var(--kemendikbud-blue); font-size: 2.5rem; margin-bottom: 1rem;"><span style="font-size: 2.8rem; vertical-align: middle; margin-right: 10px;">💼</span> Jejak Profesional</h2>
            <p style="color: var(--text-light); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">Perjalanan karir dan pengalaman kerja yang membentuk dedikasi saya di bidang manufaktur, teknik mekanik, dan pendidikan vokasi.</p>
        </div>
        
        <div class="timeline-container">
            <!-- Timeline Item 1 -->
            <div class="timeline-item">
                <div class="timeline-dot" style="background-color: #3b82f6;"></div>
                <div class="timeline-date">Jun 2025 - Sekarang</div>
                <div class="timeline-content">
                    <h3 class="timeline-title">PIC & Supervisor <span class="timeline-company">@ PT Margo Mutiasa Susanto</span></h3>
                    <p class="timeline-desc">Memimpin operasional proyek kontraktor bangunan, MEP, dan dapur MBG. Mengelola tim, sumber daya, dan K3, serta menyusun rencana arsitektur dan MEP.</p>
                    <span class="timeline-tag">Management</span><span class="timeline-tag">MEP</span>
                </div>
            </div>
            
            <!-- Timeline Item 2 -->
            <div class="timeline-item">
                <div class="timeline-dot" style="background-color: #8b5cf6;"></div>
                <div class="timeline-date">Feb 2024 - Des 2024</div>
                <div class="timeline-content">
                    <h3 class="timeline-title">Project Manager & Mech. Engineer <span class="timeline-company">@ PT Stechoq Robotika</span></h3>
                    <p class="timeline-desc">Mengelola project pembuatan "Lembaga Pelatihan Kompetensi" (LMS). Merancang mesin pencacah plastik dan membuat ±20 modul pelatihan berbasis kompetensi.</p>
                    <span class="timeline-tag">Project Management</span><span class="timeline-tag">Mechanical Design</span>
                </div>
            </div>
            
            <!-- Timeline Item 3 -->
            <div class="timeline-item">
                <div class="timeline-dot" style="background-color: #10b981;"></div>
                <div class="timeline-date">Mar 2025 - Apr 2025</div>
                <div class="timeline-content">
                    <h3 class="timeline-title">Trainer LKS DIY <span class="timeline-company">@ SMK N 1 Sedayu</span></h3>
                    <p class="timeline-desc">Menjadi trainer untuk peserta Lomba Kompetensi Siswa (LKS) DIY 2025 di bidang Prototype Modeling menggunakan CAD 3D Fusion 360.</p>
                    <span class="timeline-tag">Training</span><span class="timeline-tag">CAD 3D</span>
                </div>
            </div>

            <!-- Timeline Item 4 -->
            <div class="timeline-item">
                <div class="timeline-dot" style="background-color: #f59e0b;"></div>
                <div class="timeline-date">Nov 2023 - Jan 2024</div>
                <div class="timeline-content">
                    <h3 class="timeline-title">Teacher Assistant ISS-MBKM <span class="timeline-company">@ SMK Muhammadiyah 2 Wates</span></h3>
                    <p class="timeline-desc">Membuat modul ajar pengelasan dan CAD 3D. Sukses menciptakan proyek inovasi <em>Standing Las Universal All Position</em>.</p>
                    <span class="timeline-tag">Education</span><span class="timeline-tag">Innovation</span>
                </div>
            </div>

            <!-- Timeline Item 5 -->
            <div class="timeline-item">
                <div class="timeline-dot" style="background-color: #ef4444;"></div>
                <div class="timeline-date">Aug 2023 - Sep 2023</div>
                <div class="timeline-content">
                    <h3 class="timeline-title">Trainer & Narasumber <span class="timeline-company">@ SMK Muhammadiyah 1 Bantul</span></h3>
                    <p class="timeline-desc">Trainer & Narasumber workshop 3D Printing untuk mold making Pengecoran Logam.</p>
                    <span class="timeline-tag">3D Printing</span><span class="timeline-tag">Mold Making</span>
                </div>
            </div>

            <!-- Timeline Item 6 -->
            <div class="timeline-item">
                <div class="timeline-dot" style="background-color: #06b6d4;"></div>
                <div class="timeline-date">Mar 2021 - Sep 2021</div>
                <div class="timeline-content">
                    <h3 class="timeline-title">Staff Marketing Sales <span class="timeline-company">@ Nusantara Sakti Group</span></h3>
                    <p class="timeline-desc">Memonitoring dan melakukan pengecekan data. Melakukan kegiatan pemasaran melalui digital marketing.</p>
                    <span class="timeline-tag">Marketing</span>
                </div>
            </div>

            <!-- Timeline Item 7 -->
            <div class="timeline-item">
                <div class="timeline-dot" style="background-color: #64748b;"></div>
                <div class="timeline-date">Aug 2020 - Mar 2021</div>
                <div class="timeline-content">
                    <h3 class="timeline-title">Magang Operator <span class="timeline-company">@ PT YPTI</span></h3>
                    <p class="timeline-desc">Operator Machining Mesin Hartford 3210 dan Mesin EDM. Terlibat dalam Project Jig & Fixture Mobil Toyota dan Mold Making.</p>
                    <span class="timeline-tag">CNC Machining</span><span class="timeline-tag">Jig & Fixture</span>
                </div>
            </div>
            
            <!-- Timeline Item 8 -->
            <div class="timeline-item">
                <div class="timeline-dot" style="background-color: #94a3b8;"></div>
                <div class="timeline-date">Sep 2019</div>
                <div class="timeline-content">
                    <h3 class="timeline-title">Diklat <span class="timeline-company">@ BLPT Yogyakarta</span></h3>
                    <p class="timeline-desc">Mendapatkan keahlian khusus dalam Pattern Making.</p>
                    <span class="timeline-tag">Training</span>
                </div>
            </div>

        </div>
    </div>
</section>
"""

# Extract everything between <section ... id="pengalaman" ...> and its closing </section>
# First find the start of the section
start_idx = html.find('id="pengalaman"')
if start_idx != -1:
    section_start = html.rfind('<section', 0, start_idx)
    # Find the closing tag for this section. Need to be careful about nested tags, but looking at index.html, it's just </section>
    section_end = html.find('</section>', start_idx) + len('</section>')
    
    # Replace
    result = html[:section_start] + new_html.strip() + "\n" + html[section_end:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print("Replaced section in index.html")
else:
    print("Could not find id='pengalaman'")

# Now update style.css
css_rules = """
/* Elegant Timeline Layout */
.timeline-container {
    position: relative;
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem 0;
}

.timeline-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50px;
    height: 100%;
    width: 4px;
    background: linear-gradient(to bottom, #3b82f6 0%, #8b5cf6 20%, #10b981 40%, #f59e0b 60%, #ef4444 80%, #94a3b8 100%);
    border-radius: 4px;
}

.timeline-item {
    position: relative;
    margin-bottom: 3.5rem;
    padding-left: 100px;
    transition: all 0.4s ease;
}

.timeline-item:last-child {
    margin-bottom: 0;
}

.timeline-dot {
    position: absolute;
    left: 41.5px;
    top: 5px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    border: 4px solid #fff;
    box-shadow: 0 0 0 3px rgba(0,0,0,0.05), 0 4px 10px rgba(0,0,0,0.1);
    z-index: 2;
    transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.timeline-item:hover .timeline-dot {
    transform: scale(1.4);
}

.timeline-date {
    display: inline-block;
    padding: 0.4rem 1.2rem;
    background: var(--kemendikbud-blue);
    color: white;
    font-size: 0.85rem;
    font-weight: 600;
    border-radius: 30px;
    margin-bottom: 1rem;
    box-shadow: 0 4px 15px rgba(0,89,178,0.25);
    letter-spacing: 0.5px;
}

.timeline-content {
    background: #ffffff;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    border: 1px solid rgba(0,0,0,0.04);
    position: relative;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.timeline-content::before {
    content: '';
    position: absolute;
    left: -10px;
    top: 22px;
    width: 20px;
    height: 20px;
    background: #ffffff;
    transform: rotate(45deg);
    border-left: 1px solid rgba(0,0,0,0.04);
    border-bottom: 1px solid rgba(0,0,0,0.04);
}

.timeline-item:hover .timeline-content {
    transform: translateY(-8px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.1);
    border-color: rgba(34, 211, 238, 0.3);
}

.timeline-title {
    font-size: 1.4rem;
    color: var(--text-dark);
    margin-top: 0;
    margin-bottom: 0.4rem;
    font-weight: 700;
}

.timeline-company {
    color: var(--kemendikbud-cyan);
    font-weight: 500;
    font-size: 1.1rem;
}

.timeline-desc {
    color: var(--text-light);
    font-size: 1rem;
    line-height: 1.7;
    margin-bottom: 1.5rem;
}

.timeline-tag {
    display: inline-block;
    padding: 0.35rem 0.9rem;
    background: #f1f5f9;
    color: #475569;
    font-size: 0.75rem;
    font-weight: 600;
    border-radius: 6px;
    margin-right: 0.6rem;
    margin-bottom: 0.6rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    transition: all 0.2s ease;
}

.timeline-tag:hover {
    background: #e2e8f0;
    color: #1e293b;
}

@media (max-width: 768px) {
    .timeline-container::before {
        left: 30px;
    }
    .timeline-item {
        padding-left: 70px;
    }
    .timeline-dot {
        left: 21px;
    }
    .timeline-content {
        padding: 1.5rem;
    }
    .timeline-title {
        font-size: 1.2rem;
    }
    .timeline-company {
        font-size: 1rem;
        display: block;
        margin-top: 0.3rem;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write("\n" + css_rules)
print("Updated style.css")
