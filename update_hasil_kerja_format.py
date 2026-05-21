import bs4

with open('index.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

cards = soup.find_all('div', {'data-category': 'hasil-kerja'})

for card in cards:
    # Get image source
    img = card.find('img')
    if not img:
        continue
    img_src = img.get('src')
    alt_text = img.get('alt', 'Hasil Kerja Siswa')
    
    # Create new anchor tag
    new_card = soup.new_tag('a', href=img_src, target='_blank', **{
        'class': 'gallery-card-item photo-only-card',
        'data-category': 'hasil-kerja',
        'style': 'display: block; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.3s ease; cursor: pointer;'
    })
    
    new_img = soup.new_tag('img', src=img_src, alt=alt_text, **{
        'style': 'width: 100%; height: 100%; object-fit: cover; aspect-ratio: 4/3; display: block; transition: transform 0.5s ease;',
        'onmouseover': "this.style.transform='scale(1.05)'",
        'onmouseout': "this.style.transform='scale(1)'"
    })
    
    new_card.append(new_img)
    
    # Replace old card with new card
    card.replace_with(new_card)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
