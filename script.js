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

    if (modalOverlay) {
        popupLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetUrl = this.getAttribute('href');
                const title = this.getAttribute('data-title');
                
                modalIframe.src = targetUrl;
                modalTitle.textContent = title;
                
                modalOverlay.classList.add('active');
                document.body.style.overflow = 'hidden'; // Prevent background scrolling
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
});
