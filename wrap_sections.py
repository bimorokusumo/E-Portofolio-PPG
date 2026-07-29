with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<section id="home">' in line:
        start_idx = i
    if '<section class="one-screen" id="keahlian"' in line:
        end_idx = i

if end_idx != -1:
    for i in range(end_idx, len(lines)):
        if '</section>' in lines[i]:
            end_idx = i
            break

if start_idx != -1 and end_idx != -1:
    lines.insert(end_idx + 1, '</div>\n')
    lines.insert(start_idx, '<div id="landing-sections">\n')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Successfully wrapped sections.")
else:
    print("Failed to find sections.")
