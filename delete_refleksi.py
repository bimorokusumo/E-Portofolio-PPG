with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the section to delete
start_str = '<!-- 3.5 Analisis Artefak Pembelajaran -->'
end_str = '    </section>\n\n    <!-- 4. Lampiran Penilaian -->'

if start_str in content and end_str in content:
    # Find positions
    start_pos = content.find(start_str)
    end_pos = content.find('<!-- 4. Lampiran Penilaian -->')
    
    # Remove the slice
    new_content = content[:start_pos] + content[end_pos:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Old refleksi section deleted successfully.")
else:
    print("Could not find exact strings.")
