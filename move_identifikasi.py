with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

ident_start = -1
ident_end = -1
for i, line in enumerate(lines):
    if '<!-- Identifikasi Diri (Interactive) -->' in line:
        ident_start = i
    if '<section class="one-screen" id="ep5-identifikasi"' in line:
        pass # this is start

if ident_start != -1:
    for i in range(ident_start, len(lines)):
        if '</section>' in lines[i]:
            ident_end = i
            break

print(f"identifikasi block: {ident_start} to {ident_end}")

if ident_start != -1 and ident_end != -1:
    ident_block = lines[ident_start:ident_end+1]
    
    # delete it from original place
    del lines[ident_start:ident_end+1]
    
    # now find portfolio5 end.
    # It was at line 3447 originally. But let's find it dynamically.
    # The structure was:
    # 3446: </section>
    # 3447: </div>
    # 3448: 
    # 3449: <!-- EP5 Modal Pop-up Overlay -->
    # So we look for <!-- EP5 Modal Pop-up Overlay --> and go up to the first </div>
    
    insert_idx = -1
    for i, line in enumerate(lines):
        if '<!-- EP5 Modal Pop-up Overlay -->' in line:
            # The closing div of portfolio5 should be right above this
            for j in range(i-1, -1, -1):
                if '</div>' in lines[j]:
                    insert_idx = j
                    break
            break
            
    print(f"Insert at {insert_idx}")
    
    if insert_idx != -1:
        # Insert ident_block just before insert_idx
        for line in reversed(ident_block):
            lines.insert(insert_idx, line)
            
        with open('index.html', 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print("Successfully moved Identifikasi Diri to be inside portfolio5.")
    else:
        print("Failed to find insertion point.")
else:
    print("Failed to find block.")
