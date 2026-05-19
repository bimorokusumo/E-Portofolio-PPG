import re

with open('script.js', 'r') as f:
    js = f.read()

# Replace the search and filter logic
# Find everything from "5. Fitur Pencarian Dokumen" to the end of DOMContentLoaded block
js_pattern = r'// 5\. Fitur Pencarian Dokumen.*?\}\);\s*\}\);'
new_js = """// 5. Fitur Pencarian & Filter Terisolasi Per Galeri
    const gallerySections = document.querySelectorAll('.gallery-section');

    gallerySections.forEach(section => {
        const searchInput = section.querySelector('.search-input-gallery');
        const filterBtns = section.querySelectorAll('.filter-btn');
        const galleryCards = section.querySelectorAll('.gallery-card-item');

        // Logic Pencarian (Search)
        if (searchInput && galleryCards.length > 0) {
            searchInput.addEventListener('input', function() {
                const query = this.value.toLowerCase().trim();
                
                // Reset filter buttons for THIS section when typing
                if (query.length > 0) {
                    filterBtns.forEach(b => b.classList.remove('active'));
                    const allBtn = section.querySelector('.filter-btn[data-filter="all"]');
                    if (allBtn) allBtn.classList.add('active');
                }

                galleryCards.forEach(card => {
                    const textContent = card.innerText.toLowerCase();
                    if (textContent.includes(query)) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        }

        // Logic Filter Kategori
        if (filterBtns.length > 0 && galleryCards.length > 0) {
            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Reset search input for THIS section when clicking filter
                    if (searchInput) searchInput.value = '';

                    // Remove active class from all buttons in THIS section
                    filterBtns.forEach(b => b.classList.remove('active'));
                    // Add active class to clicked button
                    btn.classList.add('active');
                    
                    const filterValue = btn.getAttribute('data-filter');
                    
                    // Show/Hide cards based on category in THIS section
                    galleryCards.forEach(card => {
                        const category = card.getAttribute('data-category');
                        if (filterValue === 'all' || category === filterValue) {
                            card.style.display = 'flex';
                        } else {
                            card.style.display = 'none';
                        }
                    });
                });
            });
        }
    });"""

js = re.sub(js_pattern, new_js, js, flags=re.DOTALL)

with open('script.js', 'w') as f:
    f.write(js)

print("Done")
