import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = """
<style>
.exp-interactive-container {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    max-width: 1000px;
    margin: 0 auto;
}
@media (min-width: 768px) {
    .exp-interactive-container {
        flex-direction: row;
        align-items: flex-start;
    }
}
.exp-list-nav {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
    max-height: 450px;
    overflow-y: auto;
    padding-right: 10px;
}
.exp-list-nav::-webkit-scrollbar {
    width: 6px;
}
.exp-list-nav::-webkit-scrollbar-thumb {
    background-color: var(--kemendikbud-cyan);
    border-radius: 10px;
}
.exp-btn-item {
    text-align: left;
    padding: 1.2rem;
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.exp-btn-item:hover {
    border-color: var(--kemendikbud-blue);
    background: #f8fafc;
    transform: translateX(5px);
}
.exp-btn-item.active {
    background: var(--kemendikbud-blue);
    color: white;
    border-color: var(--kemendikbud-blue);
    box-shadow: 0 4px 12px rgba(0,89,178,0.2);
    transform: translateX(5px);
}
.exp-btn-item.active .exp-date, .exp-btn-item.active .exp-company-name {
    color: #e2e8f0;
}
.exp-date {
    font-size: 0.85rem;
    color: var(--text-light);
    font-weight: 500;
}
.exp-role-name {
    font-size: 1.1rem;
    font-weight: 700;
}
.exp-company-name {
    font-size: 0.9rem;
    color: var(--kemendikbud-blue);
    font-weight: 600;
}
.exp-details-pane {
    flex: 1.5;
    background: white;
    border-radius: 16px;
    padding: 2.5rem;
    border: 1px solid var(--border-color);
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    min-height: 350px;
    position: relative;
    overflow: hidden;
}
.exp-detail-content {
    display: none;
    animation: fadeInExp 0.4s ease forwards;
}
.exp-detail-content.active {
    display: block;
}
@keyframes fadeInExp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
.exp-detail-content h3 {
    color: var(--kemendikbud-blue);
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}
.exp-detail-content h4 {
    color: var(--text-dark);
    font-size: 1.2rem;
    margin-bottom: 1.5rem;
}
.exp-detail-content p {
    color: var(--text-light);
    line-height: 1.6;
    margin-bottom: 2rem;
}
.exp-badge-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.exp-badge-item {
    background: #eff6ff;
    color: var(--kemendikbud-blue);
    padding: 0.4rem 1rem;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 600;
    border: 1px solid #bfdbfe;
}
</style>

<div class="exp-interactive-container">
    <div class="exp-list-nav">
        <button class="exp-btn-item active" onclick="showExpDetail('exp1', this)">
            <span class="exp-date">Jun 2025 - Februari 2026</span>
            <span class="exp-role-name">PIC & Supervisor</span>
            <span class="exp-company-name">PT Margo Mutiasa Susanto</span>
        </button>
        <button class="exp-btn-item" onclick="showExpDetail('exp2', this)">
            <span class="exp-date">Feb 2024 - Des 2024</span>
            <span class="exp-role-name">Project Manager & Mech. Engineer</span>
            <span class="exp-company-name">PT Stechoq Robotika</span>
        </button>
        <button class="exp-btn-item" onclick="showExpDetail('exp3', this)">
            <span class="exp-date">Mar 2025 - Apr 2025</span>
            <span class="exp-role-name">Trainer LKS DIY</span>
            <span class="exp-company-name">SMK N 1 Sedayu</span>
        </button>
        <button class="exp-btn-item" onclick="showExpDetail('exp4', this)">
            <span class="exp-date">Nov 2023 - Jan 2024</span>
            <span class="exp-role-name">Teacher Assistant ISS-MBKM</span>
            <span class="exp-company-name">SMK Muhammadiyah 2 Wates</span>
        </button>
        <button class="exp-btn-item" onclick="showExpDetail('exp5', this)">
            <span class="exp-date">Aug 2023 - Sep 2023</span>
            <span class="exp-role-name">Trainer & Narasumber</span>
            <span class="exp-company-name">SMK Muhammadiyah 1 Bantul</span>
        </button>
        <button class="exp-btn-item" onclick="showExpDetail('exp6', this)">
            <span class="exp-date">Mar 2021 - Sep 2021</span>
            <span class="exp-role-name">Staff Marketing Sales</span>
            <span class="exp-company-name">Nusantara Sakti Group</span>
        </button>
        <button class="exp-btn-item" onclick="showExpDetail('exp7', this)">
            <span class="exp-date">Aug 2020 - Mar 2021</span>
            <span class="exp-role-name">Magang Operator</span>
            <span class="exp-company-name">PT YPTI</span>
        </button>
        <button class="exp-btn-item" onclick="showExpDetail('exp8', this)">
            <span class="exp-date">Sep 2019</span>
            <span class="exp-role-name">Diklat</span>
            <span class="exp-company-name">BLPT Yogyakarta</span>
        </button>
    </div>
    
    <div class="exp-details-pane">
        <div id="exp1" class="exp-detail-content active">
            <h3>PIC & Supervisor</h3>
            <h4>PT Margo Mutiasa Susanto</h4>
            <p>Memimpin operasional proyek kontraktor bangunan, MEP, dan dapur MBG. Mengelola tim, sumber daya, dan K3, serta menyusun rencana arsitektur dan MEP.</p>
            <div class="exp-badge-container">
                <span class="exp-badge-item">Management</span>
                <span class="exp-badge-item">MEP</span>
            </div>
        </div>
        
        <div id="exp2" class="exp-detail-content">
            <h3>Project Manager & Mech. Engineer</h3>
            <h4>PT Stechoq Robotika</h4>
            <p>Mengelola project pembuatan "Lembaga Pelatihan Kompetensi" (LMS). Merancang mesin pencacah plastik dan membuat ±20 modul pelatihan berbasis kompetensi.</p>
            <div class="exp-badge-container">
                <span class="exp-badge-item">Project Management</span>
                <span class="exp-badge-item">Mechanical Design</span>
            </div>
        </div>

        <div id="exp3" class="exp-detail-content">
            <h3>Trainer LKS DIY</h3>
            <h4>SMK N 1 Sedayu</h4>
            <p>Menjadi trainer untuk peserta Lomba Kompetensi Siswa (LKS) DIY 2025 di bidang Prototype Modeling menggunakan CAD 3D Fusion 360.</p>
            <div class="exp-badge-container">
                <span class="exp-badge-item">Training</span>
                <span class="exp-badge-item">CAD 3D</span>
            </div>
        </div>

        <div id="exp4" class="exp-detail-content">
            <h3>Teacher Assistant ISS-MBKM</h3>
            <h4>SMK Muhammadiyah 2 Wates</h4>
            <p>Membuat modul ajar pengelasan dan CAD 3D. Sukses menciptakan proyek inovasi <em>Standing Las Universal All Position</em>.</p>
            <div class="exp-badge-container">
                <span class="exp-badge-item">Education</span>
                <span class="exp-badge-item">Innovation</span>
            </div>
        </div>

        <div id="exp5" class="exp-detail-content">
            <h3>Trainer & Narasumber</h3>
            <h4>SMK Muhammadiyah 1 Bantul</h4>
            <p>Trainer & Narasumber workshop 3D Printing untuk mold making Pengecoran Logam.</p>
            <div class="exp-badge-container">
                <span class="exp-badge-item">3D Printing</span>
                <span class="exp-badge-item">Mold Making</span>
            </div>
        </div>

        <div id="exp6" class="exp-detail-content">
            <h3>Staff Marketing Sales</h3>
            <h4>Nusantara Sakti Group</h4>
            <p>Memonitoring dan melakukan pengecekan data. Melakukan kegiatan pemasaran melalui digital marketing.</p>
            <div class="exp-badge-container">
                <span class="exp-badge-item">Marketing</span>
            </div>
        </div>

        <div id="exp7" class="exp-detail-content">
            <h3>Magang Operator</h3>
            <h4>PT YPTI</h4>
            <p>Operator Machining Mesin Hartford 3210 dan Mesin EDM. Terlibat dalam Project Jig & Fixture Mobil Toyota dan Mold Making.</p>
            <div class="exp-badge-container">
                <span class="exp-badge-item">CNC Machining</span>
                <span class="exp-badge-item">Jig & Fixture</span>
            </div>
        </div>

        <div id="exp8" class="exp-detail-content">
            <h3>Diklat</h3>
            <h4>BLPT Yogyakarta</h4>
            <p>Mendapatkan keahlian khusus dalam Pattern Making.</p>
            <div class="exp-badge-container">
                <span class="exp-badge-item">Training</span>
            </div>
        </div>
    </div>
</div>

<script>
function showExpDetail(id, btnElement) {
    const container = btnElement.closest('.exp-interactive-container');
    container.querySelectorAll('.exp-detail-content').forEach(el => el.classList.remove('active'));
    container.querySelectorAll('.exp-btn-item').forEach(el => el.classList.remove('active'));
    
    container.querySelector('#' + id).classList.add('active');
    btnElement.classList.add('active');
}
</script>
"""

# The timeline-container div spans multiple lines up to its matching </div>.
# Pattern matches <div class="timeline-container"> to the matching </div> 
# We'll use a regex that matches `<div class="timeline-container">` and everything inside it up to `</div>\n</div>\n</section>` 
# Wait, the closing tags are:
# </div>
# </div>
# </section>

pattern = re.compile(r'<div class="timeline-container">.*?</div>\s*</div>\s*</section>', re.DOTALL)
replacement = new_html + "\n</div>\n</section>"

new_content = pattern.sub(replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Timeline replaced successfully!")
