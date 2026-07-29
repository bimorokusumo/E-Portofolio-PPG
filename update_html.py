import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
insert_idx = -1

for i, line in enumerate(lines):
    if '<!-- Portfolio Chooser Screen -->' in line:
        insert_idx = i
    if '<!-- 1. Halaman Beranda (Hero) -->' in line:
        start_idx = i
    if '<!-- Sertifikat -->' in line:
        end_idx = i

if start_idx != -1 and end_idx != -1 and insert_idx != -1:
    extracted_lines = lines[start_idx:end_idx]
    
    # Remove the extracted lines from original place
    del lines[start_idx:end_idx]
    
    # We need to find the new insert index since deleting changed indices? 
    # Actually, start_idx > insert_idx, so deleting them doesn't affect insert_idx.
    
    lines = lines[:insert_idx] + extracted_lines + lines[insert_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Successfully moved sections.")
else:
    print(f"Failed to find markers. start_idx={start_idx}, end_idx={end_idx}, insert_idx={insert_idx}")

