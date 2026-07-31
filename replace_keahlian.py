import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = """
<style>
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
    gap: 1.2rem;
    margin-top: 1.2rem;
}
.skill-card {
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 16px;
    padding: 1.5rem 1rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    position: relative;
    overflow: hidden;
}
.skill-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,119,255,0.1);
    border-color: var(--kemendikbud-cyan);
}
.skill-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: var(--kemendikbud-cyan);
    opacity: 0;
    transition: opacity 0.3s ease;
}
.skill-card:hover::before {
    opacity: 1;
}
.skill-icon {
    width: 52px;
    height: 52px;
    background: #f0f9ff;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--kemendikbud-blue);
    transition: all 0.3s ease;
}
.skill-card:hover .skill-icon {
    background: var(--kemendikbud-blue);
    color: white;
}
.skill-name {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text-dark);
}
.skill-card.pedagogik .skill-icon {
    background: #fdf4ff;
    color: #c026d3;
}
.skill-card.pedagogik:hover .skill-icon {
    background: #c026d3;
    color: white;
}
.skill-card.pedagogik:hover::before {
    background: #c026d3;
}
.skill-card.pedagogik:hover {
    border-color: #e879f9;
    box-shadow: 0 10px 25px rgba(192,38,211,0.1);
}
</style>

<div class="split-layout align-start" style="position: relative; z-index: 2; width: 100%; align-items: stretch;">
    <div class="split-left" style="flex: 1.2;">
        <h2 style="margin-bottom: 1rem; color: var(--kemendikbud-blue);"> Kompetensi Teknis</h2>
        <div class="skills-grid">
            <div class="skill-card">
                <div class="skill-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                </div>
                <div class="skill-name">CADD</div>
            </div>
            <div class="skill-card">
                <div class="skill-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
                </div>
                <div class="skill-name">Machining</div>
            </div>
            <div class="skill-card">
                <div class="skill-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                </div>
                <div class="skill-name">Programming CNC</div>
            </div>
            <div class="skill-card">
                <div class="skill-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                </div>
                <div class="skill-name">Fabrikasi</div>
            </div>
            <div class="skill-card">
                <div class="skill-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                </div>
                <div class="skill-name">Architecture Design</div>
            </div>
            <div class="skill-card">
                <div class="skill-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
                </div>
                <div class="skill-name">Civil Engineering</div>
            </div>
        </div>
    </div>
    
    <div class="split-right" style="flex: 1;">
        <h2 style="margin-bottom: 1rem; color: var(--kemendikbud-blue);"> Kompetensi Pedagogik</h2>
        <div class="skills-grid">
            <div class="skill-card pedagogik">
                <div class="skill-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                </div>
                <div class="skill-name">Pendidik</div>
            </div>
            <div class="skill-card pedagogik">
                <div class="skill-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                </div>
                <div class="skill-name">Education System</div>
            </div>
            <div class="skill-card pedagogik">
                <div class="skill-icon">
                    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                </div>
                <div class="skill-name">Project Management</div>
            </div>
        </div>
    </div>
</div>
"""

pattern = re.compile(
    r'<div class="split-layout align-start" style="position: relative; z-index: 2;">\s*<div class="split-left">.*?<h2[^>]*>\s*Kompetensi Teknis.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

# We want to replace the whole split layout that contains "Kompetensi Teknis".
matches = pattern.findall(content)
print(f"Found {len(matches)} matches to replace.")

new_content = pattern.sub(new_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Keahlian replaced successfully!")
