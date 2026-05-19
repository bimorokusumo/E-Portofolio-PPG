new_css = """

/* Enhanced Elegant UI Additions */
.analisis-section {
    position: relative;
    overflow: hidden;
    background-color: #fafcff;
}

.analisis-section::before {
    content: '';
    position: absolute;
    top: -20%; left: -10%; width: 50%; height: 60%;
    background: radial-gradient(circle, rgba(34,211,238,0.04) 0%, rgba(255,255,255,0) 70%);
    border-radius: 50%;
    z-index: 0;
    pointer-events: none;
}

.analisis-section::after {
    content: '';
    position: absolute;
    bottom: -20%; right: -10%; width: 50%; height: 60%;
    background: radial-gradient(circle, rgba(168,85,247,0.04) 0%, rgba(255,255,255,0) 70%);
    border-radius: 50%;
    z-index: 0;
    pointer-events: none;
}

.analisis-header, .analisis-grid, .sintesis-container {
    position: relative;
    z-index: 1;
}

.analisis-card {
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 10px 40px -10px rgba(0,0,0,0.05);
    border: 1px solid rgba(0,0,0,0.03);
    overflow: hidden;
}

.analisis-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, #22d3ee, #c084fc, #34d399);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.analisis-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px -10px rgba(0,0,0,0.08);
}

.analisis-card:hover::before {
    opacity: 1;
}

.card-number {
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.analisis-card:hover .card-number {
    transform: scale(1.15) rotate(5deg);
}

.sintesis-container {
    border-radius: 24px;
    padding: 3rem;
    margin-top: 4rem;
    box-shadow: 0 20px 50px -10px rgba(0,0,0,0.05);
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #ffffff 0%, #f4f7fb 100%);
    border: 1px solid rgba(255,255,255,1);
}

.sintesis-container::before {
    content: '';
    position: absolute;
    top: 0; right: 0; bottom: 0; width: 40%;
    background: linear-gradient(135deg, rgba(34,211,238,0.03) 0%, rgba(168,85,247,0.03) 100%);
    border-top-left-radius: 100%;
    border-bottom-left-radius: 100%;
    pointer-events: none;
}

.sintesis-left, .sintesis-right {
    position: relative;
    z-index: 2;
}

.sintesis-box {
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,1);
    border-radius: 16px;
    padding: 1.5rem;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 4px 20px rgba(0,0,0,0.02);
}

.sintesis-box:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 15px 35px rgba(52, 211, 153, 0.1);
    background: #ffffff;
}

/* Make artefak cards also hover nicely */
.doc-card {
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.doc-card:hover {
    transform: translateY(-8px);
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(new_css)

print("CSS animations and elegant design elements appended.")
