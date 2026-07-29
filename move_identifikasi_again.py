with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Extract Identifikasi Diri
ident_start = -1
ident_end = -1
for i, line in enumerate(lines):
    if '<!-- Identifikasi Diri (Interactive) -->' in line:
        ident_start = i
    if '<section class="one-screen" id="ep5-identifikasi"' in line:
        pass

if ident_start != -1:
    for i in range(ident_start, len(lines)):
        if '</section>' in lines[i]:
            ident_end = i
            break

if ident_start != -1 and ident_end != -1:
    ident_block = lines[ident_start:ident_end+1]
    del lines[ident_start:ident_end+1]
    
    # 2. Find insertion point for Identifikasi Diri (above ep5-refleksi)
    refleksi_idx = -1
    for i, line in enumerate(lines):
        if '<section id="ep5-refleksi"' in line:
            # We want to insert just before this section, maybe there's a comment above it?
            if '<!-- Refleksi Mata Kuliah -->' in lines[i-1] or '<!-- ' in lines[i-1]:
                refleksi_idx = i - 1
            else:
                refleksi_idx = i
            break
            
    if refleksi_idx != -1:
        for line in reversed(ident_block):
            lines.insert(refleksi_idx, line)
            
        print("Successfully moved Identifikasi Diri.")
    else:
        print("Failed to find ep5-refleksi.")
        
    # 3. Add placeholders for Keseluruhan and Inovasi
    # We will add them just before the closing </div> of portfolio5.
    modal_idx = -1
    for i, line in enumerate(lines):
        if '<!-- EP5 Modal Pop-up Overlay -->' in line:
            modal_idx = i
            break
            
    if modal_idx != -1:
        insert_idx = -1
        for j in range(modal_idx-1, -1, -1):
            if '</div>' in lines[j]:
                insert_idx = j
                break
                
        if insert_idx != -1:
            placeholders = """
<!-- Refleksi Keseluruhan -->
<section class="one-screen" id="ep5-keseluruhan" style="padding: 5rem 2rem; background: var(--bg-light-gray); text-align: center;">
    <h2 style="color: var(--kemendikbud-blue); font-size: 2.5rem; margin-bottom: 1rem;"><span style="font-size: 2.5rem; vertical-align: middle; margin-right: 10px;">🌟</span> Refleksi Keseluruhan Program</h2>
    <div style="background: white; max-width: 800px; margin: 2rem auto; padding: 4rem 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px dashed var(--border-color);">
        <div style="font-size: 4rem; opacity: 0.5; margin-bottom: 1rem;">⏳</div>
        <h3 style="color: var(--text-dark); margin-bottom: 1rem;">Konten Segera Hadir</h3>
        <p style="color: var(--text-light); font-size: 1.1rem; line-height: 1.6;">Bagian ini sedang dalam tahap penyusunan dan akan segera diperbarui dengan refleksi komprehensif mengenai keseluruhan program PPG.</p>
    </div>
</section>

<!-- Inovasi Terbaru -->
<section class="one-screen" id="ep5-inovasi" style="padding: 5rem 2rem; background: var(--bg-white); text-align: center;">
    <h2 style="color: var(--kemendikbud-blue); font-size: 2.5rem; margin-bottom: 1rem;"><span style="font-size: 2.5rem; vertical-align: middle; margin-right: 10px;">💡</span> Inovasi Terbaru</h2>
    <div style="background: white; max-width: 800px; margin: 2rem auto; padding: 4rem 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px dashed var(--border-color);">
        <div style="font-size: 4rem; opacity: 0.5; margin-bottom: 1rem;">🚀</div>
        <h3 style="color: var(--text-dark); margin-bottom: 1rem;">Konten Segera Hadir</h3>
        <p style="color: var(--text-light); font-size: 1.1rem; line-height: 1.6;">Bagian ini akan menampilkan inovasi-inovasi terbaru dalam praktik pembelajaran yang sedang dikembangkan.</p>
    </div>
</section>
"""
            lines.insert(insert_idx, placeholders)
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print("Successfully added placeholders.")
else:
    print("Failed to find identifikasi block.")
