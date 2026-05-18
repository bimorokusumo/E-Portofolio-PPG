// Portfolio Chooser Logic
window.selectPortfolio = function(id) {
    document.getElementById('portfolioChooser').style.opacity = '0';
    setTimeout(() => {
        document.getElementById('portfolioChooser').style.display = 'none';
        document.getElementById('mainNav').classList.remove('hidden-section');
        
        if (id === 1) {
            document.getElementById('portfolio1').classList.remove('hidden-section');
            document.getElementById('portfolio2').classList.add('hidden-section');
            document.getElementById('nav-ep1').classList.remove('hidden-section');
            document.getElementById('nav-ep2').classList.add('hidden-section');
        } else {
            document.getElementById('portfolio1').classList.add('hidden-section');
            document.getElementById('portfolio2').classList.remove('hidden-section');
            document.getElementById('nav-ep1').classList.add('hidden-section');
            document.getElementById('nav-ep2').classList.remove('hidden-section');
        }
    }, 500);
};

window.showChooser = function() {
    document.getElementById('portfolioChooser').style.display = 'flex';
    setTimeout(() => {
        document.getElementById('portfolioChooser').style.opacity = '1';
    }, 10);
    
    document.getElementById('mainNav').classList.add('hidden-section');
    document.getElementById('portfolio1').classList.add('hidden-section');
    document.getElementById('portfolio2').classList.add('hidden-section');
    window.scrollTo(0,0);
};

document.addEventListener('DOMContentLoaded', () => {
    // 1. Smooth Scrolling for Navigation Links
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                // Adjust for sticky header height (approx 80px)
                const headerOffset = 80;
                const elementPosition = targetSection.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.scrollY - headerOffset;
  
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
  
    // 2. Sticky Navbar Effect & Active State update
    const nav = document.querySelector('nav');
    const sections = document.querySelectorAll('section');
    
    window.addEventListener('scroll', () => {
        // Add shadow to nav on scroll
        if (window.scrollY > 50) {
            nav.style.boxShadow = '0 4px 6px -1px rgb(0 0 0 / 0.1)';
            nav.style.background = 'rgba(255, 255, 255, 0.95)';
        } else {
            nav.style.boxShadow = '0 1px 2px 0 rgb(0 0 0 / 0.05)';
            nav.style.background = 'rgba(255, 255, 255, 0.85)';
        }
  
        // Update active link
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            // Adjust offset to trigger earlier
            if (window.scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });
  
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
  
    // 3. Scroll Animation (Intersection Observer)
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };
    
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: Stop observing once animated
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    animateElements.forEach(el => {
        observer.observe(el);
    });

    // 4. Modal Popup Logic
    const popupLinks = document.querySelectorAll('.popup-link');
    const modalOverlay = document.getElementById('artefakModal');
    const modalIframe = document.getElementById('modalIframe');
    const modalTitle = document.getElementById('modalTitle');
    const closeModal = document.getElementById('closeModal');

    const openModal = (targetUrl, title) => {
        if (!modalOverlay) return;
        modalIframe.src = targetUrl;
        modalTitle.textContent = title;
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    };

    if (modalOverlay) {
        popupLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                openModal(this.getAttribute('href'), this.getAttribute('data-title'));
            });
        });

        const closePopup = () => {
            modalOverlay.classList.remove('active');
            document.body.style.overflow = '';
            // Delay clearing iframe src to allow animation to finish
            setTimeout(() => {
                modalIframe.src = '';
            }, 300);
        };

        closeModal.addEventListener('click', closePopup);

        // Close when clicking outside content
        modalOverlay.addEventListener('click', function(e) {
            if (e.target === modalOverlay) {
                closePopup();
            }
        });
        
        // Close on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
                closePopup();
            }
        });
    }

    // 5. Fitur Pencarian & Filter Terisolasi Per Galeri
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
    });
});

// Carousel Auto Slide
document.addEventListener("DOMContentLoaded", function() {
    const track = document.querySelector(".carousel-track");
    if (!track) return;
    
    let currentIndex = 0;
    
    function moveToSlide(index) {
        const currentSlides = Array.from(track.children);
        if (currentSlides.length === 0) return;
        track.style.transform = `translateX(-${index * 100}%)`;
    }
    
    function autoSlide() {
        const currentSlides = Array.from(track.children);
        if (currentSlides.length <= 1) return;
        currentIndex++;
        if (currentIndex >= currentSlides.length) {
            currentIndex = 0;
        }
        moveToSlide(currentIndex);
    }
    
    // Auto slide every 2 seconds
    setInterval(autoSlide, 2000);
});
