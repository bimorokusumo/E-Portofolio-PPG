import sys
from bs4 import BeautifulSoup
import re
import copy

def main():
    html_file = 'index.html'
    
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # 1. Update navigation for portfolio 3
    nav_ep1 = soup.find('ul', id='nav-ep1')
    if not nav_ep1:
        print("Cannot find nav-ep1")
        return
        
    nav_ep3 = copy.copy(nav_ep1)
    nav_ep3['id'] = 'nav-ep3'
    nav_ep3['class'] = ['nav-links', 'hidden-section']
    
    # Update hrefs in nav-ep3
    for a in nav_ep3.find_all('a'):
        href = a['href']
        if href.startswith('#'):
            a['href'] = '#ep3-' + href[1:]
            
    # insert nav_ep3 after nav_ep2
    nav_ep2 = soup.find('ul', id='nav-ep2')
    nav_ep2.insert_after(nav_ep3)
    nav_ep2.insert_after("\n")
    
    # 2. Duplicate portfolio1 to portfolio3
    p1 = soup.find('div', id='portfolio1')
    if not p1:
        print("Cannot find portfolio1")
        return
        
    p3 = copy.copy(p1)
    p3['id'] = 'portfolio3'
    p3['class'] = ['hidden-section']
    
    # Update section ids
    sections_to_rename = ['home', 'profil', 'pengalaman', 'pendidikan', 'keahlian', 'sertifikat', 'galeri', 'artefak', 'analisis-produk', 'penilaian', 'model-guru']
    for section in p3.find_all('section'):
        if section.get('id') in sections_to_rename:
            section['id'] = 'ep3-' + section['id']
            
    # Update artefak section
    artefak = p3.find('section', id='ep3-artefak')
    if artefak:
        tab_nav = artefak.find('div', class_='tab-nav')
        if tab_nav:
            tab_nav.decompose()
            
        siklus2 = artefak.find('div', id='siklus-2')
        if siklus2: siklus2.decompose()
        siklus3 = artefak.find('div', id='siklus-3')
        if siklus3: siklus3.decompose()
        
        siklus1 = artefak.find('div', id='siklus-1')
        if siklus1:
            siklus1['id'] = 'ep3-siklus-1'
            siklus1['class'] = ['tab-content', 'active']
            
            # The gallery section inside siklus1
            gallery_section = siklus1.find('div', class_='gallery-section')
            if gallery_section:
                # We need 5 copies with new titles
                subjects = [
                    "Pengetahuan Bahan",
                    "Wawasan Bidang Teknik",
                    "Kecakapan Kerja Dasar (Basic Job Skills)",
                    "K3",
                    "Budaya Kerja"
                ]
                
                # Create a list to hold the new sections
                new_sections = []
                for subj in subjects:
                    new_sec = copy.copy(gallery_section)
                    h3 = new_sec.find('h3')
                    if h3:
                        h3.string = f"📂 {subj}"
                    new_sections.append(new_sec)
                
                # Clear existing contents of siklus1 (which contains the original gallery_section)
                # wait, siklus1 might have other things? Let's just replace gallery_section with our 5 new ones.
                
                parent = gallery_section.parent
                gallery_section.extract()
                
                for ns in new_sections:
                    parent.append(ns)
                    
    # Insert p3 after p2
    p2 = soup.find('div', id='portfolio2')
    p2.insert_after(p3)
    p2.insert_after("\n")
    
    # Save the HTML
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print("index.html updated successfully")
    
if __name__ == '__main__':
    main()
