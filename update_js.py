with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

new_js = """
// =========================================================================
// REDESIGN LOGIC: PARTICLES, CHART, ANIMATIONS, TYPEWRITER
// =========================================================================

document.addEventListener('DOMContentLoaded', function() {
    // 1. Typewriter Effect
    const text = "Guru Teknik Pemesinan | PPG Prajabatan 2026 | SMK N 2 Depok";
    let i = 0;
    const speed = 50;
    const typewriterElem = document.getElementById('typewriter');
    
    function typeWriter() {
        if (i < text.length && typewriterElem) {
            typewriterElem.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
        }
    }
    // Delay start
    setTimeout(typeWriter, 1000);

    // 2. Initialize particles.js
    if (typeof particlesJS !== 'undefined') {
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 60, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#f59e0b" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.5, "random": true },
                "size": { "value": 3, "random": true },
                "line_linked": { "enable": true, "distance": 150, "color": "#1e40af", "opacity": 0.4, "width": 1 },
                "move": { "enable": true, "speed": 2, "direction": "top-right", "random": true, "out_mode": "out" }
            },
            "interactivity": {
                "events": { "onhover": { "enable": true, "mode": "grab" }, "onclick": { "enable": true, "mode": "push" } },
                "modes": { "grab": { "distance": 140, "line_linked": { "opacity": 1 } } }
            },
            "retina_detect": true
        });
    }

    // 3. Radar Chart (Chart.js)
    const ctx = document.getElementById('skillRadar');
    if (ctx && typeof Chart !== 'undefined') {
        new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Desain CAD', 'CNC Programming', 'Fabrikasi Logam', 'Pedagogik', 'Manajemen Kelas', 'Teknologi Pendidikan'],
                datasets: [{
                    label: 'Kompetensi Profesional vs Pedagogis',
                    data: [90, 85, 88, 85, 80, 92],
                    backgroundColor: 'rgba(30, 64, 175, 0.2)',
                    borderColor: '#1e40af',
                    pointBackgroundColor: '#f59e0b',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: '#f59e0b'
                }]
            },
            options: {
                elements: { line: { borderWidth: 2 } },
                scales: { 
                    r: { 
                        angleLines: { color: 'rgba(0,0,0,0.1)' },
                        grid: { color: 'rgba(0,0,0,0.1)' },
                        pointLabels: { font: { family: 'Inter', size: 12, weight: 'bold' } },
                        ticks: { display: false, min: 0, max: 100 }
                    } 
                },
                plugins: { legend: { display: false } }
            }
        });
    }

    // 4. Animated Counters & Skill Bars via IntersectionObserver
    const counters = document.querySelectorAll('.counter');
    const skillBars = document.querySelectorAll('.skill-progress-fill');
    
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Animate Counters
                if (entry.target.classList.contains('counter')) {
                    const target = parseFloat(entry.target.getAttribute('data-target'));
                    const duration = 2000;
                    const increment = target / (duration / 16);
                    let current = 0;
                    
                    const updateCounter = () => {
                        current += increment;
                        if (current < target) {
                            entry.target.innerText = (target % 1 === 0) ? Math.ceil(current) : current.toFixed(2);
                            requestAnimationFrame(updateCounter);
                        } else {
                            entry.target.innerText = target;
                        }
                    };
                    updateCounter();
                    observer.unobserve(entry.target);
                }
                
                // Animate Skill Bars
                if (entry.target.classList.contains('skill-progress-fill')) {
                    const width = entry.target.getAttribute('data-width');
                    entry.target.style.width = width;
                    observer.unobserve(entry.target);
                }
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => observer.observe(counter));
    skillBars.forEach(bar => observer.observe(bar));
});

// 5. Section Interaction Logic
window.showExperience = function(id) {
    // Hide all details
    document.querySelectorAll('.experience-detail-card').forEach(el => el.classList.remove('active'));
    // Show selected
    document.getElementById('exp-' + id).classList.add('active');
    
    // Update timeline active state
    document.querySelectorAll('.timeline-item').forEach(el => el.classList.remove('active'));
    event.currentTarget.classList.add('active');
};

window.switchPenilaian = function(id) {
    const title = document.getElementById('penilaian-title');
    if (id === 'lamp7') {
        title.innerHTML = '<span>Preview Lampiran 7 (PDF)</span><span style="font-size: 0.8rem; background-color: #f59e0b; color: white; padding: 0.2rem 0.6rem; border-radius: 4px;">File Menyusul</span>';
    } else {
        title.innerHTML = '<span>Preview Lampiran 8 (PDF)</span><span style="font-size: 0.8rem; background-color: #f59e0b; color: white; padding: 0.2rem 0.6rem; border-radius: 4px;">File Menyusul</span>';
    }
};

window.showLightbox = function(index) {
    const img = document.getElementById('lightbox-main-img');
    img.src = 'assets/dokumentasi/' + index + '.jpg';
};

// Update Sertifikat List UI
document.addEventListener('DOMContentLoaded', () => {
    const certItems = document.querySelectorAll('.cert-list li');
    certItems.forEach(item => {
        item.addEventListener('click', function() {
            certItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active');
        });
    });
});
"""

with open('script.js', 'a', encoding='utf-8') as f:
    f.write(new_js)

print("script.js updated.")
