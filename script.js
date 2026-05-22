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

// Data Analisis Produk
const analysisData = {
    '01': {
        title: 'Kendala Penyusunan Produk',
        subtitle: 'Penyusunan produk pembelajaran tidak hanya berhenti pada pembuatan dokumen, tetapi menjadi proses menerjemahkan kebutuhan kelas ke dalam rancangan yang dapat dijalankan secara nyata.',
        diagnosis: 'Kendala paling besar muncul ketika rancangan ideal harus disesuaikan dengan kondisi kelas, kemampuan awal siswa, ketersediaan waktu, dan kesiapan media. Produk pembelajaran harus tetap sistematis, tetapi tidak boleh terlalu kaku karena situasi kelas dapat berubah ketika pembelajaran berlangsung.',
        implikasi: 'Implikasinya, produk pembelajaran harus dirancang sebagai perangkat yang hidup: jelas secara alur, kuat secara pedagogis, tetapi tetap fleksibel ketika menghadapi dinamika kelas. Produk yang baik bukan hanya lengkap, melainkan mampu membantu guru mengambil keputusan saat pembelajaran berlangsung.',
        mendalam: 'Pada tahap awal penyusunan, tantangan utama terletak pada penyelarasan antara tujuan pembelajaran, materi, kegiatan, LKM, media, dan asesmen. Jika salah satu komponen tidak saling terhubung, produk pembelajaran berisiko hanya menjadi dokumen administratif, bukan alat bantu yang benar-benar mengarahkan pembelajaran. Kendala berikutnya adalah menentukan tingkat kedalaman materi. Materi perlu cukup kuat secara konsep, tetapi tetap dapat dipahami oleh peserta didik dengan latar kemampuan yang beragam. Hal ini menuntut guru untuk memilih contoh, urutan penjelasan, dan bentuk latihan yang bertahap. Kendala teknis juga muncul pada pengaturan waktu. Dalam pembelajaran kejuruan, waktu tidak hanya digunakan untuk menjelaskan materi, tetapi juga untuk demonstrasi, latihan, pendampingan, koreksi, dan refleksi. Produk pembelajaran yang terlalu padat dapat membuat guru tergesa-gesa dan siswa kehilangan kesempatan memperbaiki pemahamannya.',
        theme: 'cyan'
    },
    '02': {
        title: 'Konsep Pedagogis yang Diadopsi',
        subtitle: 'Pemilihan kerangka pedagogis bertujuan untuk memastikan bahwa produk pembelajaran yang dihasilkan berpusat pada siswa dan memfasilitasi pemahaman tingkat tinggi.',
        diagnosis: 'Pemilihan metode pengajaran (seperti Understanding by Design dan Inquiry Learning) seringkali dihadapkan pada realita siswa yang terbiasa dengan metode konvensional. Dibutuhkan adaptasi agar konsep ini dapat diterapkan efektif tanpa menimbulkan kebingungan pada siswa.',
        implikasi: 'Guru bertindak lebih sebagai fasilitator (pamong) daripada pusat informasi. Hal ini menuntut produk pembelajaran seperti modul dan media memiliki instruksi yang sangat jelas dan scaffolding yang bertahap agar siswa dapat membangun pengetahuannya sendiri secara mandiri.',
        mendalam: 'Penerapan Understanding by Design (UbD) memaksa saya sebagai penyusun untuk mulai dari tujuan akhir (kompetensi yang diharapkan) sebelum menyusun langkah-langkah pembelajaran. Pendekatan ini memastikan bahwa setiap media, LKS, dan asesmen yang dibuat memiliki relevansi langsung dengan tujuan akhir tersebut. Sementara itu, sintaks Inquiry Learning diintegrasikan untuk mendorong rasa ingin tahu dan kemampuan problem-solving siswa, khususnya dalam konteks permesinan dan manufaktur. Kolaborasi kedua konsep ini melahirkan produk pembelajaran yang sistematis, menantang, dan bermakna. Siswa tidak hanya menghafal prosedur, tetapi memahami "mengapa" dan "bagaimana" suatu proses produksi dilakukan. Tantangannya adalah menyeimbangkan antara kebebasan eksplorasi (Inquiry) dengan standar keselamatan dan presisi teknis yang ketat di area bengkel manufaktur.',
        theme: 'purple'
    },
    '03': {
        title: 'Faktor Keberhasilan Penerapan',
        subtitle: 'Efektivitas produk pembelajaran diukur dari sejauh mana rancangan tersebut berhasil diterapkan, dipahami, dan meningkatkan kompetensi siswa di dalam kelas.',
        diagnosis: 'Tingkat keberhasilan berbanding lurus dengan kejelasan instruksi pada Lembar Kerja (LKM/LKS) serta kesesuaian media visual (video/presentasi) dalam menjembatani kesenjangan antara teori abstrak dengan praktik nyata di bengkel.',
        implikasi: 'Produk pembelajaran yang sukses adalah produk yang adaptif. Saat fasilitas mendukung dan siswa merespons positif terhadap media interaktif, tingkat ketercapaian kompetensi meningkat tajam, yang dibuktikan dengan hasil asesmen sumatif dan produk kerja praktik siswa.',
        mendalam: 'Faktor penentu utama keberhasilan penerapan produk ini adalah kombinasi antara materi yang terstruktur (melalui modul/RPP) dan media pembelajaran yang representatif. Penggunaan media visual seperti animasi 3D CAD atau video demonstrasi las SMAW terbukti sangat krusial dalam membantu siswa memvisualisasikan konsep abstrak sebelum mereka mengeksekusinya di mesin nyata. Selain itu, Lembar Kerja Siswa (LKS) yang dirancang dengan format step-by-step (SOP) memberikan panduan yang aman dan terukur selama praktikum. Keberhasilan juga didukung oleh pengelolaan kelas yang baik, di mana alokasi waktu untuk briefing K3, eksekusi praktik, dan evaluasi hasil kerja telah terdistribusi secara proporsional. Antusiasme siswa melonjak signifikan ketika mereka diberikan proyek nyata (Project-Based Learning) yang hasil akhirnya dapat mereka lihat dan gunakan, sehingga produk pembelajaran benar-benar dirasakan manfaat dan relevansinya.',
        theme: 'green'
    },
    '04': {
        title: 'Penyesuaian untuk Kelas Berbeda',
        subtitle: 'Tidak ada satu rancangan pembelajaran yang sempurna untuk semua kondisi; produk pembelajaran harus selalu diuji dan disesuaikan secara berkesinambungan.',
        diagnosis: 'Setiap kelas memiliki dinamika unik: ada kelas dengan mayoritas pembelajar visual, ada yang lebih kinestetik, dan ada yang membutuhkan pendampingan ekstra (scaffolding) pada materi dasar pemesinan.',
        implikasi: 'Asesmen awal (diagnostik) menjadi kunci. Produk pembelajaran tidak dirancang secara statis, melainkan menyediakan opsi diferensiasi, baik dari segi konten (tingkat kesulitan latihan), proses (kelompok vs individu), maupun produk akhir yang diharapkan.',
        mendalam: 'Dalam implementasinya, saya menyadari bahwa satu modul ajar yang sama bisa memberikan hasil yang berbeda pada dua rombongan belajar (rombel) yang berbeda. Oleh karena itu, penyesuaian (diferensiasi) adalah sebuah keharusan. Pada kelas yang kemampuan teknis awalnya rendah, produk pembelajaran disesuaikan dengan memperbanyak porsi demonstrasi langsung (modeling) dan memperkecil rasio kesulitan pada LKS awal. Sebaliknya, pada kelas yang lebih cekatan, penyesuaian dilakukan dengan memberikan studi kasus (troubleshooting) atau proyek fabrikasi dengan tingkat presisi yang lebih menantang. Fleksibilitas ini juga tercermin pada media pembelajaran; saya menyiapkan alternatif simulasi digital (CAD/CAM) bagi siswa yang menunggu giliran menggunakan mesin fisik. Proses adaptasi berkelanjutan ini membuktikan bahwa produk pembelajaran yang baik harus berfungsi sebagai kompas, bukan rel kereta api, yang memungkinkan guru untuk mengambil jalur alternatif demi mencapai tujuan kompetensi akhir yang sama.',
        theme: 'orange'
    }
};

const themeColors = {
    'cyan': '#22d3ee',
    'purple': '#c084fc',
    'green': '#34d399',
    'orange': '#fbbf24'
};

function openAnalysisModal(id) {
    const data = analysisData[id];
    if (!data) return;

    // Set texts
    document.getElementById('modalNumber').textContent = id;
    document.getElementById('modalTitle').textContent = data.title;
    document.getElementById('modalSubtitle').textContent = data.subtitle;
    document.getElementById('modalDiagnosis').textContent = data.diagnosis;
    document.getElementById('modalImplikasi').textContent = data.implikasi;
    document.getElementById('modalMendalam').textContent = data.mendalam;

    // Set theme colors
    const color = themeColors[data.theme];
    
    // Update number bg class
    const numEl = document.getElementById('modalNumber');
    numEl.className = `modal-number ${data.theme}-bg`;
    
    // Update category text color
    document.querySelector('.modal-kategori').style.color = color;
    
    // Update borders and text colors of boxes
    const boxDiagnosis = document.getElementById('boxDiagnosis');
    const boxImplikasi = document.getElementById('boxImplikasi');
    const labelDiagnosis = document.getElementById('labelDiagnosis');
    const labelImplikasi = document.getElementById('labelImplikasi');
    const boxFull = document.querySelector('.box-full');
    const labelFull = boxFull.querySelector('h4');

    // Convert hex to rgba for border
    let r = parseInt(color.slice(1, 3), 16),
        g = parseInt(color.slice(3, 5), 16),
        b = parseInt(color.slice(5, 7), 16);
    
    const borderColor = `rgba(${r}, ${g}, ${b}, 0.2)`;

    boxDiagnosis.style.borderColor = borderColor;
    boxImplikasi.style.borderColor = borderColor;
    boxFull.style.borderColor = borderColor;
    
    labelDiagnosis.style.color = color;
    labelImplikasi.style.color = color;
    labelFull.style.color = color;

    // Show modal
    const overlay = document.getElementById('analysisModalOverlay');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
}

function closeAnalysisModal() {
    const overlay = document.getElementById('analysisModalOverlay');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
}

// Close when clicking outside modal content
document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.getElementById('analysisModalOverlay');
    if(overlay) {
        overlay.addEventListener('click', function(e) {
            if (e.target === this) {
                closeAnalysisModal();
            }
        });
    }
});

// Tab Switching Logic
window.switchTab = function(tabId) {
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    document.getElementById(tabId).classList.add('active');
    document.querySelector(`.tab-btn[onclick="switchTab('${tabId}')"]`).classList.add('active');
};
