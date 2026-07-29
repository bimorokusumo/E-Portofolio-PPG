from bs4 import BeautifulSoup

def main():
    html_file = 'index.html'
    
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    siklus = soup.find('div', id='ep3-siklus-1')
    if siklus:
        galleries = siklus.find_all('div', class_='gallery-section', recursive=False)
        if len(galleries) >= 5:
            # Update 3rd gallery
            h3 = galleries[2].find('h3')
            if h3:
                h3.string = "📂 Kecakapan Kerja Dasar (Basic Job Skills), K3, dan Budaya Kerja"
            
            # Delete 4th and 5th gallery
            galleries[3].decompose()
            galleries[4].decompose()
            
            with open('index.html', 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print("Successfully merged K3 and Budaya Kerja into Kecakapan Kerja Dasar")
        else:
            print("Not enough gallery sections found.")
    else:
        print("Could not find ep3-siklus-1")

if __name__ == '__main__':
    main()
