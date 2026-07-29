with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

insert_idx = -1
for i in range(len(lines)):
    if '<footer>' in lines[i]:
        insert_idx = i - 1 # right before the </div> that closes portfolio5
        break

html_to_inject = """
<!-- Identifikasi Diri (Interactive) -->
<section class="one-screen" id="ep5-identifikasi" style="max-width: 100%; padding: 4rem 2rem; background: var(--bg-white);">
    <div style="text-align: center; margin-bottom: 3rem;">
        <h2 style="color: var(--kemendikbud-blue); font-size: 2.5rem; margin-bottom: 1rem;"><span style="font-size: 2.5rem; vertical-align: middle; margin-right: 10px;">👤</span> Identifikasi Diri</h2>
        <p style="color: var(--text-light); font-size: 1.1rem; max-width: 600px; margin: 0 auto;">Klik bagian ilustrasi tubuh (kepala, dada, kaki) di bawah ini untuk melihat visi pribadi dan langkah konkret saya sebagai pendidik.</p>
    </div>
    
    <div style="max-width: 1100px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 3rem; align-items: center; justify-content: center;">
        
        <!-- Interactive Teacher SVG -->
        <div style="flex: 1; min-width: 300px; max-width: 400px; display: flex; justify-content: center; position: relative;">
            <svg viewBox="0 0 400 500" width="100%" height="auto" style="filter: drop-shadow(0 15px 30px rgba(0,0,0,0.1)); overflow: visible;">
                <!-- SVG Animations -->
                <defs>
                    <style>
                        @keyframes spin { 100% { transform: rotate(360deg); } }
                        .interactive-part { cursor: pointer; transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
                        .interactive-part:hover { filter: brightness(0.95); }
                        .identifikasi-card { display: none; animation: fadeIn 0.4s ease forwards; }
                        .identifikasi-card.active { display: block; }
                        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
                    </style>
                </defs>
                
                <!-- Background glow for head -->
                <circle cx="200" cy="100" r="55" fill="transparent" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5,5" style="animation: spin 15s linear infinite; transform-origin: 200px 100px; opacity: 0.5;"/>

                <!-- Head: Visi Pribadi Calon Guru -->
                <g id="svg-head" class="interactive-part" onmouseover="this.style.transform='scale(1.08)'; this.style.transformOrigin='200px 100px';" onmouseout="this.style.transform='scale(1)';" onclick="showIdentifikasi('head')">
                    <circle cx="200" cy="100" r="45" fill="#f8fafc" stroke="#0369a1" stroke-width="5"/>
                    <path d="M190 90 Q200 80 210 90 T210 110 Q200 120 190 110 T190 90" fill="none" stroke="#38bdf8" stroke-width="3"/>
                    <text x="200" y="60" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7" opacity="0.8">VISI GURU</text>
                </g>
                
                <!-- Body: Visi Pendidikan Indonesia -->
                <g id="svg-body" class="interactive-part" onmouseover="this.style.transform='scale(1.03)'; this.style.transformOrigin='200px 220px';" onmouseout="this.style.transform='scale(1)';" onclick="showIdentifikasi('body')">
                    <rect x="140" y="160" width="120" height="130" rx="25" fill="#f8fafc" stroke="#1d4ed8" stroke-width="5"/>
                    <path d="M200 210 C200 210 185 195 175 205 C165 215 175 230 200 250 C225 230 235 215 225 205 C215 195 200 210 200 210" fill="#ef4444" opacity="0.9"/>
                    <path d="M140 180 Q100 200 110 260" fill="none" stroke="#1d4ed8" stroke-width="5" stroke-linecap="round"/>
                    <path d="M260 180 Q300 200 290 260" fill="none" stroke="#1d4ed8" stroke-width="5" stroke-linecap="round"/>
                    <text x="110" y="280" text-anchor="middle" font-size="12" font-weight="bold" fill="#dc2626" opacity="0.8">PENDIDIKAN</text>
                </g>
                
                <!-- Legs: Langkah Konkret -->
                <g id="svg-legs" class="interactive-part" onmouseover="this.style.transform='scale(1.05)'; this.style.transformOrigin='200px 380px';" onmouseout="this.style.transform='scale(1)';" onclick="showIdentifikasi('legs')">
                    <path d="M170 300 L170 410" fill="none" stroke="#10b981" stroke-width="6" stroke-linecap="round"/>
                    <path d="M230 300 L230 410" fill="none" stroke="#10b981" stroke-width="6" stroke-linecap="round"/>
                    <path d="M170 410 L150 410" fill="none" stroke="#10b981" stroke-width="6" stroke-linecap="round"/>
                    <path d="M230 410 L250 410" fill="none" stroke="#10b981" stroke-width="6" stroke-linecap="round"/>
                    <text x="250" y="430" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669" opacity="0.8">LANGKAH</text>
                </g>
            </svg>
        </div>
        
        <!-- Dynamic Content Panel -->
        <div style="flex: 1; min-width: 320px; max-width: 600px; background: white; border: 1px solid var(--border-color); border-radius: 20px; padding: 3rem 2.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.05); min-height: 420px; position: relative; display: flex; flex-direction: column; justify-content: center;">
            
            <!-- Default State -->
            <div id="identifikasi-default" class="identifikasi-card active" style="text-align: center;">
                <div style="font-size: 5rem; opacity: 0.2; margin-bottom: 1rem;">👆</div>
                <h3 style="color: var(--kemendikbud-blue); font-weight: 700; margin-bottom: 0.5rem;">Eksplorasi Visi</h3>
                <p style="color: var(--text-light); font-size: 1.05rem;">Silakan klik bagian <strong style="color: #0284c7;">Kepala</strong>, <strong style="color: #dc2626;">Dada</strong>, atau <strong style="color: #059669;">Kaki</strong> pada ilustrasi guru di samping untuk membaca detail identifikasi diri.</p>
            </div>
            
            <!-- Head Content (Visi Pribadi Guru) -->
            <div id="identifikasi-head" class="identifikasi-card">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 1.5rem; border-bottom: 2px solid #e0f2fe; padding-bottom: 1rem;">
                    <div style="width: 50px; height: 50px; background: #e0f2fe; color: #0284c7; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0;">🧠</div>
                    <h3 style="margin: 0; color: #0284c7; font-size: 1.35rem; font-weight: 700; line-height: 1.3;">Visi Pribadi Sebagai Calon Guru</h3>
                </div>
                <p style="color: #475569; line-height: 1.8; text-align: justify; font-size: 1.05rem; margin: 0;">
                    Sebagai calon guru, saya memiliki visi untuk menjadi pendidik yang inspiratif, inovatif, dan profesional dalam membimbing peserta didik agar memiliki kompetensi yang sesuai dengan kebutuhan dunia kerja dan industri. Saya ingin menjadi guru yang tidak hanya mengajarkan teori, tetapi juga menanamkan karakter, etos kerja, budaya industri, serta semangat belajar sepanjang hayat.
                </p>
            </div>
            
            <!-- Body Content (Visi Pendidikan Indonesia) -->
            <div id="identifikasi-body" class="identifikasi-card">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 1.5rem; border-bottom: 2px solid #fee2e2; padding-bottom: 1rem;">
                    <div style="width: 50px; height: 50px; background: #fee2e2; color: #dc2626; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0;">❤️</div>
                    <h3 style="margin: 0; color: #dc2626; font-size: 1.35rem; font-weight: 700; line-height: 1.3;">Visi Pribadi Untuk Pendidikan di Indonesia</h3>
                </div>
                <p style="color: #475569; line-height: 1.8; text-align: justify; font-size: 1.05rem; margin: 0;">
                    Saya memiliki visi agar pendidikan vokasi di Indonesia menjadi pilihan utama dan menjadi tolok ukur keberhasilan pendidikan nasional. Pendidikan vokasi tidak hanya berfokus pada penguasaan keterampilan, tetapi juga menjadi tempat membentuk karakter, etos kerja, kedisiplinan, tanggung jawab, serta kemampuan beradaptasi dengan perkembangan zaman dan dunia industri.
                </p>
            </div>
            
            <!-- Legs Content (Langkah Konkret) -->
            <div id="identifikasi-legs" class="identifikasi-card">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 1.5rem; border-bottom: 2px solid #d1fae5; padding-bottom: 1rem;">
                    <div style="width: 50px; height: 50px; background: #d1fae5; color: #059669; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0;">👣</div>
                    <h3 style="margin: 0; color: #059669; font-size: 1.35rem; font-weight: 700; line-height: 1.3;">Langkah-langkah Konkret</h3>
                </div>
                <div style="color: #475569; line-height: 1.6; text-align: justify; font-size: 0.95rem; display: flex; flex-direction: column; gap: 0.6rem; max-height: 280px; overflow-y: auto; padding-right: 10px;">
                    <div style="display: flex; gap: 10px;"><span style="color: #10b981;">•</span><span>Meningkatkan kompetensi diri melalui pelatihan, seminar, dan pengembangan profesional yang berkaitan dengan pendidikan vokasi dan perkembangan teknologi.</span></div>
                    <div style="display: flex; gap: 10px;"><span style="color: #10b981;">•</span><span>Mengintegrasikan pembelajaran dengan kebutuhan dunia kerja dan industri melalui penerapan pembelajaran berbasis proyek (Project Based Learning) dan studi kasus nyata.</span></div>
                    <div style="display: flex; gap: 10px;"><span style="color: #10b981;">•</span><span>Menanamkan nilai-nilai karakter, kedisiplinan, tanggung jawab, dan etos kerja kepada peserta didik dalam setiap kegiatan pembelajaran.</span></div>
                    <div style="display: flex; gap: 10px;"><span style="color: #10b981;">•</span><span>Memanfaatkan teknologi dan media pembelajaran yang inovatif untuk meningkatkan motivasi dan keterlibatan peserta didik.</span></div>
                    <div style="display: flex; gap: 10px;"><span style="color: #10b981;">•</span><span>Menjalin kerja sama dengan dunia usaha dan dunia industri (DUDI) untuk memberikan pengalaman belajar yang lebih kontekstual.</span></div>
                    <div style="display: flex; gap: 10px;"><span style="color: #10b981;">•</span><span>Melakukan refleksi dan evaluasi secara berkala terhadap proses pembelajaran guna meningkatkan kualitas pengajaran.</span></div>
                    <div style="display: flex; gap: 10px;"><span style="color: #10b981;">•</span><span>Mendorong peserta didik untuk terus mengembangkan keterampilan, kreativitas, dan kemampuan beradaptasi agar siap menghadapi tantangan masa depan.</span></div>
                </div>
            </div>
            
        </div>
    </div>
    
    <script>
        function showIdentifikasi(part) {
            // Hide all cards
            document.querySelectorAll('.identifikasi-card').forEach(el => {
                el.classList.remove('active');
            });
            
            // Show target card
            const target = document.getElementById('identifikasi-' + part);
            if(target) target.classList.add('active');
            
            // Reset SVG Colors
            document.getElementById('svg-head').querySelector('circle').style.fill = '#f8fafc';
            document.getElementById('svg-body').querySelector('rect').style.fill = '#f8fafc';
            document.getElementById('svg-legs').querySelectorAll('path').forEach(p => p.style.stroke = '#10b981');
            
            // Highlight selected part
            if (part === 'head') {
                document.getElementById('svg-head').querySelector('circle').style.fill = '#e0f2fe';
            } else if (part === 'body') {
                document.getElementById('svg-body').querySelector('rect').style.fill = '#fee2e2';
            } else if (part === 'legs') {
                document.getElementById('svg-legs').querySelectorAll('path').forEach(p => p.style.stroke = '#059669');
            }
        }
    </script>
</section>
"""

lines.insert(insert_idx, html_to_inject + "\n")

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Successfully injected identifikasi diri section.")
