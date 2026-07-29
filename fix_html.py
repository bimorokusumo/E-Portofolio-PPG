with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

ep3_start = -1
ep3_end = -1
for i, line in enumerate(lines):
    if '<!-- 1. Halaman Beranda (Hero) -->' in line and 'ep3-home' in lines[i+1]:
        ep3_start = i
        break

for i in range(ep3_start, len(lines)):
    if '<!-- Portfolio Chooser Screen -->' in lines[i]:
        ep3_end = i
        break

ep3_block = lines[ep3_start:ep3_end]

ep1_start = -1
ep1_end = -1
for i, line in enumerate(lines):
    if '<!-- 1. Halaman Beranda (Hero) -->' in line and '<section id="home">' in lines[i+1]:
        ep1_start = i
        break
for i in range(ep1_start, len(lines)):
    if '<!-- Sertifikat -->' in lines[i]:
        ep1_end = i
        break

ep1_block = lines[ep1_start:ep1_end]

new_lines = []
i = 0
while i < len(lines):
    if i == ep3_start:
        i = ep3_end # Skip EP3 block
        continue
    if i == ep1_start:
        i = ep1_end # Skip EP1 block
        continue
    
    line = lines[i]
    
    if '<!-- Portfolio Chooser Screen -->' in line:
        new_lines.extend(ep1_block)
        new_lines.append(line)
    elif '<div class="hidden-section" id="portfolio3">' in line:
        new_lines.append(line)
        new_lines.extend(ep3_block)
    else:
        new_lines.append(line)
    i += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("Restored!")
