import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Define the HTML blocks
siklus1_card = """
<div class="doc-card gallery-card-item" data-category="hasil-kerja">
<div class="doc-card-thumb">
<span class="doc-badge">Hasil Kerja</span>
<img alt="Hasil Kerja Siklus 1" class="doc-thumb-img" src="assets/hasil-kerja/siklus-1/IMG_9657.jpg" style="object-fit: cover; aspect-ratio: 16/9;" />
<a class="doc-overlay-btn" href="assets/hasil-kerja/siklus-1/IMG_9657.jpg" target="_blank">🔍 Perbesar</a>
</div>
<div class="doc-card-content">
<h4>Hasil Kerja Praktik Siklus 1</h4>
<p>Dokumentasi produk dan hasil kerja siswa selama pembelajaran Siklus 1.</p>
<a class="doc-btn" href="assets/hasil-kerja/siklus-1/IMG_9657.jpg" target="_blank">Lihat Foto</a>
</div>
</div>
"""

siklus2_card = """
<div class="doc-card gallery-card-item" data-category="hasil-kerja">
<div class="doc-card-thumb">
<span class="doc-badge">Hasil Kerja</span>
<img alt="Hasil Kerja Siklus 2" class="doc-thumb-img" src="assets/hasil-kerja/siklus-2/IMG_9287.jpg" style="object-fit: cover; aspect-ratio: 16/9;" />
<a class="doc-overlay-btn" href="assets/hasil-kerja/siklus-2/IMG_9287.jpg" target="_blank">🔍 Perbesar</a>
</div>
<div class="doc-card-content">
<h4>Hasil Kerja Praktik Siklus 2</h4>
<p>Dokumentasi produk dan hasil kerja siswa selama pembelajaran Siklus 2.</p>
<a class="doc-btn" href="assets/hasil-kerja/siklus-2/IMG_9287.jpg" target="_blank">Lihat Foto</a>
</div>
</div>
"""

siklus3_card = """
<div class="doc-card gallery-card-item" data-category="hasil-kerja">
<div class="doc-card-thumb">
<span class="doc-badge">Hasil Kerja</span>
<img alt="Hasil Kerja Siklus 3" class="doc-thumb-img" src="assets/hasil-kerja/siklus-3/IMG_9521.jpg" style="object-fit: cover; aspect-ratio: 16/9;" />
<a class="doc-overlay-btn" href="assets/hasil-kerja/siklus-3/IMG_9521.jpg" target="_blank">🔍 Perbesar</a>
</div>
<div class="doc-card-content">
<h4>Hasil Kerja Praktik Siklus 3</h4>
<p>Dokumentasi produk dan hasil kerja siswa selama pembelajaran Siklus 3.</p>
<a class="doc-btn" href="assets/hasil-kerja/siklus-3/IMG_9521.jpg" target="_blank">Lihat Foto</a>
</div>
</div>
"""

# Find the end of doc-grid gallery-grid for siklus-1
s1_start = html.find('id="siklus-1"')
s2_start = html.find('id="siklus-2"')
s3_start = html.find('id="siklus-3"')
s_end = html.find('id="penilaian"')

# Insert Siklus 1 card
# We want to put it before the closing </div> of the .doc-grid for siklus-1
# The grid for siklus-1 ends just before s2_start
grid1_end = html.rfind('</div>', s1_start, s2_start) 
grid1_end2 = html.rfind('</div>', s1_start, grid1_end-1) 
# Wait, let's use regex or split on specific markers
# Let's just find "<!-- Tab Contents -->" and inject inside the grids
pass
