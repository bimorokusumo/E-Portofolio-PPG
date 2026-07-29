with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# We will replace the block from <!-- Interactive Teacher SVG --> up to </svg>
# and the <script> block at the end of the section.

new_svg_block = """<!-- Interactive Teacher Image -->
        <div style="flex: 1; min-width: 300px; max-width: 400px; position: relative; border-radius: 20px; overflow: hidden; border: 5px solid white; box-shadow: 0 15px 35px rgba(0,0,0,0.15);">
            <img src="teacher_illustration.png" alt="Teacher Illustration" style="width: 100%; height: auto; display: block; object-fit: cover;">
            
            <!-- Hover overlay style -->
            <style>
                .ai-interactive-part {
                    position: absolute;
                    left: 50%;
                    transform: translateX(-50%);
                    border-radius: 50%;
                    cursor: pointer;
                    border: 2px dashed rgba(255,255,255,0.4);
                    background: rgba(255,255,255,0.05);
                    transition: all 0.3s ease;
                }
                .ai-interactive-part:hover {
                    background: rgba(255,255,255,0.3);
                    border-color: white;
                    box-shadow: 0 0 20px rgba(255,255,255,0.9);
                    transform: translateX(-50%) scale(1.05);
                }
                .ai-interactive-part.selected {
                    background: rgba(14, 165, 233, 0.4);
                    border: 2px solid #0284c7;
                    box-shadow: 0 0 25px rgba(2, 132, 199, 0.6);
                    animation: pulse-glow 2s infinite;
                }
                @keyframes pulse-glow {
                    0% { box-shadow: 0 0 15px rgba(2, 132, 199, 0.4); }
                    50% { box-shadow: 0 0 30px rgba(2, 132, 199, 0.8); }
                    100% { box-shadow: 0 0 15px rgba(2, 132, 199, 0.4); }
                }
                .ai-label {
                    position: absolute;
                    bottom: -30px;
                    left: 50%;
                    transform: translateX(-50%);
                    background: #0f172a;
                    color: white;
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-size: 0.8rem;
                    font-weight: 700;
                    opacity: 0;
                    transition: opacity 0.3s;
                    pointer-events: none;
                    white-space: nowrap;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
                }
                .ai-interactive-part:hover .ai-label, .ai-interactive-part.selected .ai-label {
                    opacity: 1;
                }
            </style>
            
            <!-- Head Region -->
            <div id="btn-head" class="ai-interactive-part" style="top: 10%; width: 22%; height: 16%;" onclick="showIdentifikasi('head')">
                <div class="ai-label">Visi Guru</div>
            </div>
            
            <!-- Chest Region -->
            <div id="btn-body" class="ai-interactive-part" style="top: 29%; width: 35%; height: 23%; border-radius: 30%;" onclick="showIdentifikasi('body')">
                <div class="ai-label">Visi Pendidikan</div>
            </div>
            
            <!-- Legs Region -->
            <div id="btn-legs" class="ai-interactive-part" style="top: 55%; width: 40%; height: 40%; border-radius: 20px;" onclick="showIdentifikasi('legs')">
                <div class="ai-label" style="bottom: 10px;">Langkah Konkret</div>
            </div>
        </div>"""

new_script = """<script>
        function showIdentifikasi(part) {
            document.querySelectorAll('.identifikasi-card').forEach(el => el.classList.remove('active'));
            const target = document.getElementById('identifikasi-' + part);
            if(target) target.classList.add('active');
            
            document.querySelectorAll('.ai-interactive-part').forEach(el => el.classList.remove('selected'));
            const btn = document.getElementById('btn-' + part);
            if(btn) btn.classList.add('selected');
        }
    </script>"""

# Regex replacements
text = re.sub(r'<!-- Interactive Teacher SVG -->\s*<div.*?<svg.*?</svg>\s*</div>', new_svg_block, text, flags=re.DOTALL)
text = re.sub(r'<script>\s*function showIdentifikasi\(part\).*?</script>', new_script, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("HTML updated with AI image.")
