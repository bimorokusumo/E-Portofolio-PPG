// =============================================================
// Performance: Smart Lazy Loading for Iframes (Zero-Lag Startup)
// =============================================================
window.initLazyIframes = function(container) {
    const root = container || document;
    const lazyIframes = root.querySelectorAll('iframe[data-src]');
    if (!lazyIframes.length) return;

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const iframe = entry.target;
                    if (iframe.dataset.src) {
                        iframe.src = iframe.dataset.src;
                        iframe.removeAttribute('data-src');
                    }
                    obs.unobserve(iframe);
                }
            });
        }, { rootMargin: '350px 0px 350px 0px' });

        lazyIframes.forEach(iframe => observer.observe(iframe));
    } else {
        lazyIframes.forEach(iframe => {
            if (iframe.dataset.src) {
                iframe.src = iframe.dataset.src;
                iframe.removeAttribute('data-src');
            }
        });
    }
};

// Portfolio Chooser Logic
window.selectPortfolio = function(id) {
    document.getElementById('portfolioChooser').style.opacity = '0';
    setTimeout(() => {
        document.getElementById('portfolioChooser').style.display = 'none';
        
        // Hide landing sections (Beranda - Keahlian)
        const landingSections = document.getElementById('landing-sections');
        if (landingSections) landingSections.classList.add('hidden-section');

        // Hide default landing nav
        const mainNavLinks = document.getElementById('nav-main');
        if (mainNavLinks) mainNavLinks.classList.add('hidden-section');
        
        // Hide all portfolios and navs
        for (let i = 1; i <= 5; i++) {
            const p = document.getElementById('portfolio' + i);
            if (p) p.classList.add('hidden-section');
            const n = document.getElementById('nav-ep' + i);
            if (n) n.classList.add('hidden-section');
        }

        // Show the selected one and initialize its iframes on-demand
        const targetP = document.getElementById('portfolio' + id);
        if (targetP) {
            targetP.classList.remove('hidden-section');
            window.initLazyIframes(targetP);
        }
        const targetN = document.getElementById('nav-ep' + id);
        if (targetN) targetN.classList.remove('hidden-section');

        // Update nav badge & floating bar dynamically
        const badgeMap = {
            1: 'UTS Sem 1',
            2: 'UAS Sem 1',
            3: 'E-Portofolio Sem 2',
            4: 'UTS & UAS Sem 2',
            5: 'Seminar PPG'
        };
        const nameMap = {
            1: 'Semester 1: E-Portfolio 1 (UTS)',
            2: 'Semester 1: E-Portfolio 2 (UAS)',
            3: 'Semester 2: E-Portofolio Mandiri',
            4: 'Semester 2: E-Portofolio 2 (UTS & UAS)',
            5: 'Seminar PPG'
        };

        const badge = document.querySelector('#mainNav .nav-top span[style*="background: #e0f2fe"], #nav-badge');
        if (badge && badgeMap[id]) {
            badge.innerText = badgeMap[id];
        }

        const floatName = document.getElementById('floatingPortfolioName');
        if (floatName && nameMap[id]) {
            floatName.innerText = nameMap[id];
        }

        // Update floating dock active pill
        document.querySelectorAll('.floating-pill-btn').forEach(btn => {
            if (btn.dataset.p == id) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });

        const floatBar = document.getElementById('floatingActionBar');
        if (floatBar) floatBar.classList.add('visible');

        window.scrollTo({ top: 0, behavior: 'smooth' });
        if (window.showToast && nameMap[id]) {
            window.showToast('Membuka ' + nameMap[id]);
        }
    }, 500);
};

// Portfolio Chooser Filter Logic
window.filterChooser = function(category, btn) {
    document.querySelectorAll('.chooser-filter-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');

    const sem1Heading = document.getElementById('chooser-heading-sem1');
    const sem2Heading = document.getElementById('chooser-heading-sem2');
    const sem1Cards = document.getElementById('chooser-cards-sem1');
    const sem2Cards = document.getElementById('chooser-cards-sem2');

    if (category === 'sem1') {
        if (sem1Heading) sem1Heading.style.display = 'block';
        if (sem1Cards) sem1Cards.style.display = 'grid';
        if (sem2Heading) sem2Heading.style.display = 'none';
        if (sem2Cards) sem2Cards.style.display = 'none';
    } else if (category === 'sem2') {
        if (sem1Heading) sem1Heading.style.display = 'none';
        if (sem1Cards) sem1Cards.style.display = 'none';
        if (sem2Heading) sem2Heading.style.display = 'block';
        if (sem2Cards) sem2Cards.style.display = 'grid';
    } else {
        if (sem1Heading) sem1Heading.style.display = 'block';
        if (sem1Cards) sem1Cards.style.display = 'grid';
        if (sem2Heading) sem2Heading.style.display = 'block';
        if (sem2Cards) sem2Cards.style.display = 'grid';
    }
};

window.showChooser = function() {
    document.getElementById('portfolioChooser').style.display = 'flex';
    setTimeout(() => {
        document.getElementById('portfolioChooser').style.opacity = '1';
    }, 10);
    
    // Show landing sections (Beranda - Keahlian)
    const landingSections = document.getElementById('landing-sections');
    if (landingSections) landingSections.classList.remove('hidden-section');

    // Show default landing nav
    const mainNavLinks = document.getElementById('nav-main');
    if (mainNavLinks) mainNavLinks.classList.remove('hidden-section');

    for (let i = 1; i <= 5; i++) {
        const p = document.getElementById('portfolio' + i);
        if (p) p.classList.add('hidden-section');
        const n = document.getElementById('nav-ep' + i);
        if (n) n.classList.add('hidden-section');
    }
    const badge = document.querySelector('#mainNav .nav-top span[style*="background: #e0f2fe"], #nav-badge');
    if (badge) badge.innerText = 'PPG 2026';
    
    const floatingBar = document.getElementById('floatingActionBar');
    if (floatingBar) floatingBar.classList.remove('visible');

    window.scrollTo({ top: 0, behavior: 'smooth' });
    if (window.showToast) window.showToast('Kembali ke Pusat Portofolio');
};

// Global Experience Detail Switcher
window.showExpDetail = function(id, btnElement) {
    if (!btnElement) return;
    const container = btnElement.closest('.exp-interactive-container');
    if (!container) return;
    container.querySelectorAll('.exp-detail-content').forEach(el => el.classList.remove('active'));
    container.querySelectorAll('.exp-btn-item').forEach(el => el.classList.remove('active'));
    
    const target = container.querySelector('#' + id);
    if (target) target.classList.add('active');
    btnElement.classList.add('active');
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
  
    // 2. Off-Thread Active Nav Link Tracking with IntersectionObserver (Zero Layout Thrashing)
    if ('IntersectionObserver' in window && navLinks.length) {
        const sectionObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    navLinks.forEach(link => {
                        link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
                    });
                }
            });
        }, { rootMargin: '-70px 0px -55% 0px', threshold: 0 });

        sections.forEach(sec => sectionObserver.observe(sec));
    }
  
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
    const target = document.getElementById(tabId);
    if (!target) return;

    if (tabId.startsWith('ep5-')) {
        const ep5Container = document.getElementById('ep5-refleksi');
        if (ep5Container) {
            ep5Container.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            ep5Container.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        }
    } else {
        ['siklus-1', 'siklus-2', 'siklus-3'].forEach(id => {
            const el = document.getElementById(id);
            if (el) el.classList.remove('active');
            const btn = document.querySelector(`.tab-btn[onclick="switchTab('${id}')"]`);
            if (btn) btn.classList.remove('active');
        });
    }

    target.classList.add('active');
    const activeBtn = document.querySelector(`.tab-btn[onclick="switchTab('${tabId}')"]`);
    if (activeBtn) activeBtn.classList.add('active');

    // Instantly load any lazy iframes inside the activated tab
    target.querySelectorAll('iframe[data-src]').forEach(iframe => {
        if (iframe.dataset.src) {
            iframe.src = iframe.dataset.src;
            iframe.removeAttribute('data-src');
        }
    });
};

// EP2 Refleksi Akhir Modal Logic
const ep2RefleksiData = {
    'refleksi1': {
        title: 'Apa yang Telah Dipelajari?',
        icon: '💡',
        text: 'Selama pelaksanaan PPL Terbimbing, saya belajar banyak hal tentang dinamika kelas dan karakter peserta didik yang beragam di sekolah vokasi. Saya menyadari bahwa persiapan mengajar teori Dasar-Dasar Keahlian (DDK) untuk jurusan Teknik Pemesinan (TP) dan Teknik Fabrikasi Logam dan Manufaktur (TFLM) tidak sekadar menyusun perangkat administratif, melainkan bagaimana merancang alur pedagogis yang adaptif. Saya belajar menerapkan pendekatan berdiferensiasi dalam menyampaikan konsep-konsep teknik yang abstrak, serta mengintegrasikan aspek Keselamatan dan Kesehatan Kerja (K3) secara konseptual ke dalam setiap sesi pembelajaran teori, memastikan peserta didik memahami fondasi keilmuan dan memiliki kesadaran profesional yang tinggi sejak dari ruang kelas.'
    },
    'refleksi2': {
        title: 'Pengalaman Menantang & Solusi',
        icon: '⚡',
        text: 'Tantangan terbesar yang saya hadapi adalah menjembatani kesenjangan pemahaman konseptual awal antar siswa serta menganalogikan materi teknik yang abstrak menjadi mudah dipahami. Banyak siswa yang belum memiliki gambaran tentang konsep dasar permesinan dan manufaktur, sehingga diperlukan strategi penyederhanaan yang tepat. Solusi yang saya terapkan adalah dengan mengoptimalkan penggunaan media visual, studi kasus industri, dan pendekatan Inquiry Learning. Pendekatan ini sangat krusial bagi siswa Kelas X (Fase E), di mana mereka sangat membutuhkan stimulan awal—seperti pengamatan fenomena atau pertanyaan pemantik—agar mengetahui gambaran besarnya terlebih dahulu sebelum mampu merancang dan memproses konsep-konsep tersebut secara utuh di dalam pikiran mereka. Saya juga memberikan scaffolding (bimbingan bertahap) yang lebih intensif kepada siswa yang tertinggal, serta menerapkan tutor sebaya.'
    },
    'refleksi3': {
        title: 'Umpan Balik & Saran Konstruktif',
        icon: '📈',
        text: 'Dalam diskusi refleksi akhir, Guru Pamong dan Dosen Pembimbing Lapangan (DPL) memberikan masukan yang sangat berharga. Saya disarankan untuk lebih memperkuat keterampilan manajemen kelas, terutama dalam menjaga fokus dan antusiasme siswa selama sesi teori yang panjang. Selain itu, saya juga mendapat masukan untuk terus mengembangkan apersepsi yang lebih kontekstual—mengaitkan materi DDK secara langsung dengan studi kasus nyata di dunia industri manufaktur—sebagai perbaikan krusial untuk menghadapi PPL Mandiri ke depannya.'
    }
};

window.openEp2Modal = function(id) {
    const data = ep2RefleksiData[id];
    if (!data) return;

    document.getElementById('ep2ModalTitle').innerText = data.title;
    document.getElementById('ep2ModalIcon').innerText = data.icon;
    document.getElementById('ep2ModalText').innerText = data.text;

    const overlay = document.getElementById('ep2ModalOverlay');
    const content = document.getElementById('ep2ModalContent');
    
    if (overlay && content) {
        overlay.style.visibility = 'visible';
        overlay.style.opacity = '1';
        content.style.transform = 'translateY(0)';
        document.body.style.overflow = 'hidden';
    }
};

window.closeEp2Modal = function() {
    const overlay = document.getElementById('ep2ModalOverlay');
    const content = document.getElementById('ep2ModalContent');
    
    if (overlay && content) {
        overlay.style.opacity = '0';
        content.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            overlay.style.visibility = 'hidden';
            document.body.style.overflow = '';
        }, 300);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const ep2Overlay = document.getElementById('ep2ModalOverlay');
    if(ep2Overlay) {
        ep2Overlay.addEventListener('click', function(e) {
            if (e.target === this) {
                window.closeEp2Modal();
            }
        });
    }
});

// EP5 Modal Pop-up Logic
const ep5RefleksiData = {
    'subjek1': {
        title: 'Refleksi Filosofi Pendidikan Nasional',
        icon: '🏛️',
        text: 'Melalui mata kuliah Filosofi Pendidikan dan Nilai, saya menyadari pentingnya pemahaman mendalam tentang nilai-nilai luhur budaya bangsa sebagai landasan filosofis pendidikan. Pendidikan bukan sekadar transfer ilmu, melainkan proses \'menuntun\' kodrat anak sesuai ajaran Ki Hajar Dewantara. Tantangan utamanya adalah menginternalisasi nilai-nilai ini di tengah arus modernisasi. Sebagai calon guru, saya belajar untuk menciptakan ekosistem belajar yang berpihak pada peserta didik, mengutamakan pembentukan karakter budi pekerti, serta menyelaraskan pendidikan dengan konteks sosiokultural daerah.'
    },
    'subjek2': {
        title: 'Refleksi Penerapan Growth Mindset',
        icon: '🧠',
        text: 'Mata kuliah Growth Mindset membuka wawasan saya tentang betapa krusialnya pola pikir berkembang bagi seorang pendidik dan peserta didik. Saya menyadari bahwa kemampuan intelektual dan bakat dapat terus dikembangkan melalui dedikasi dan kerja keras. Dalam refleksi ini, saya belajar mengidentifikasi \'fixed mindset\' yang sering tidak disadari, serta strategi untuk mengubahnya. Ke depannya, saya akan lebih berfokus pada penghargaan terhadap proses belajar dan usaha siswa (process praise) dibandingkan sekadar memuji hasil akhir atau kecerdasan bawaan, demi membangun ketangguhan mental mereka.'
    },
    'subjek3': {
        title: 'Refleksi Pemahaman Karakteristik Peserta Didik',
        icon: '👥',
        text: 'Memahami peserta didik adalah fondasi dari pembelajaran berdiferensiasi. Dalam mata kuliah ini, saya mempelajari berbagai teori perkembangan kognitif, sosial, emosional, dan moral siswa. Saya menyadari bahwa setiap anak unik dan membawa latar belakang sosiokultural yang berbeda ke dalam kelas. Refleksi ini membantu saya menyusun strategi observasi (profiling peserta didik) yang lebih komprehensif, sehingga nantinya rancangan pembelajaran yang saya buat dapat lebih relevan, bermakna, dan mampu memfasilitasi kebutuhan belajar mereka yang beragam secara optimal.'
    },
    'subjek4': {
        title: 'Refleksi Perancangan Pembelajaran dan Asesmen',
        icon: '🎯',
        text: 'Pembelajaran mendalam (deep learning) membutuhkan desain instruksional yang terstruktur dan asesmen yang tepat sasaran. Melalui mata kuliah ini, saya belajar memformulasikan tujuan pembelajaran yang selaras dengan asesmen (alignment). Saya juga berlatih menyusun asesmen formatif yang tidak hanya menilai, tetapi juga membimbing proses belajar siswa (assessment for learning dan as learning). Kendala yang sering saya hadapi adalah merancang rubrik penilaian yang objektif untuk tugas unjuk kerja (performance task), namun melalui pendampingan dan refleksi ini, saya kini lebih siap menyusun perangkat asesmen yang valid dan reliabel.'
    },
    'subjek5': {
        title: 'Refleksi Praktik Pengalaman Lapangan Terbimbing',
        icon: '🏫',
        text: 'PPL Terbimbing di SMK Negeri 2 Depok memberikan pengalaman nyata yang sangat berharga. Saya berkesempatan menerapkan teori pedagogis langsung di kelas riil, menghadapi dinamika siswa kejuruan, dan mempraktikkan keterampilan mengajar. Refleksi terbesar saya adalah pentingnya manajemen kelas (classroom management) dan fleksibilitas dalam mengajar. Ketika rencana awal tidak berjalan mulus karena kendala teknis atau daya tangkap siswa, saya harus sigap melakukan penyesuaian. Umpan balik dari Guru Pamong dan Dosen Pembimbing sangat membantu saya dalam mengevaluasi efektivitas metode pengajaran dan membangun komunikasi yang lebih asertif dengan peserta didik.'
    },
    'subjek6': {
        title: 'Refleksi Inovasi Pembelajaran Berbasis Tamansiswa',
        icon: '🌿',
        text: 'Mata kuliah Inovasi Pembelajaran Berbasis Tamansiswa mengajarkan pentingnya mengintegrasikan nilai-nilai luhur ajaran Ki Hadjar Dewantara, seperti Sistem Among (Ing Ngarso Sung Tulodo, Ing Madyo Mangun Karso, Tut Wuri Handayani) dalam merancang pembelajaran modern. Saya menyadari bahwa inovasi teknologi dan metode pengajaran terkini harus selaras dengan karakter budaya bangsa. Melalui refleksi ini, saya belajar untuk menciptakan ekosistem belajar yang tidak hanya canggih secara teknologi, namun juga humanis, memerdekakan siswa, dan berpusat pada kodrat alam serta kodrat zaman peserta didik.'
    },
    'sem2_pse': {
        title: 'Refleksi Pembelajaran Sosial Emosional (PSE)',
        icon: '💙',
        text: 'Mata kuliah Pembelajaran Sosial Emosional (PSE) memberikan pemahaman mendalam bahwa keberhasilan proses pembelajaran kejuruan tidak hanya ditentukan oleh kecakapan teknis (hard skills), melainkan sangat dipengaruhi oleh kematangan emosional dan sosial (soft skills). Melalui kerangka kerja CASEL, saya mendalami lima kompetensi utama: kesadaran diri (self-awareness), manajemen diri (self-management), kesadaran sosial (social awareness), keterampilan berelasi (relationship skills), dan pengambilan keputusan yang bertanggung jawab (responsible decision-making). Dalam konteks pendidikan vokasi di SMK, peserta didik kerap menghadapi dinamika kerja bengkel dan tuntutan presisi yang tinggi. Refleksi ini mengajarkan saya untuk mengintegrasikan teknik mindfulness (seperti teknik STOP), menciptakan iklim kelas yang aman secara psikologis, serta membimbing siswa mengelola stres dan kolaborasi kerja secara konstruktif demi mewujudkan profil Pelajar Pancasila yang tangguh dan berkarakter mulia.'
    },
    'sem2_pmal': {
        title: 'Refleksi Pembelajaran dan Asesmen Lanjutan (PMAL)',
        icon: '🎯',
        text: 'Mata kuliah Pembelajaran dan Asesmen Lanjutan (PMAL) memperdalam kapasitas saya dalam merancang siklus pembelajaran yang berpusat pada peserta didik melalui diferensiasi lanjutan dan asesmen autentik. Saya mempelajari integrasi pendekatan Teaching at the Right Level (TaRL) dan Culturally Responsive Teaching (CRT) guna merespons keberagaman kesiapan belajar, minat, dan profil belajar siswa kejuruan. Refleksi mendalam pada mata kuliah ini berfokus pada transisi menuju asesmen autentik berbasis unjuk kerja industri. Saya belajar merumuskan asesmen diagnostik awal secara terukur, menyusun rubrik analitik berbasis kriteria capaian standar kompetensi kerja, serta memanfaatkan data asesmen formatif sebagai dasar penyesuaian instruksional (scaffolding) secara real-time guna memastikan setiap peserta didik mencapai kompetensi optimal.'
    },
    'sem2_ppl': {
        title: 'Refleksi Praktik Pengalaman Lapangan (PPL II Mandiri)',
        icon: '🏫',
        text: 'Praktik Pengalaman Lapangan II (PPL Mandiri) di SMK Negeri 2 Depok Sleman merupakan puncak pembuktian kemandirian profesionalisme keguruan saya di ruang kelas nyata dan bengkel pemesinan. Melalui pelaksanaan 5 Siklus Pembelajaran (K3LH, Metrologi Alat Ukur, Teknik Pemesinan Bubut & Las, serta Pengetahuan Bahan Teknik), saya mengintegrasikan model Teaching Factory (TeFa), pembelajaran berdiferensiasi TaRL dan CRT, serta manajemen keselamatan kerja bengkel berstandar 5R. Selain kegiatan mengajar intrakurikuler, saya turut mengemban peran nonmengajar sebagai Pembina Pramuka dan Pendamping LKS Kejuruan. Refleksi ini menegaskan komitmen saya untuk terus menumbuhkan etos kerja industri, kematangan pedagogik, serta keteladanan karakter budi pekerti luhur bagi peserta didik vokasi.'
    },
    'sem2_seminar': {
        title: 'Refleksi Seminar Pendidikan Profesi Guru',
        icon: '🎓',
        text: 'Seminar Pendidikan Profesi Guru merupakan ruang dialektika dan sintesis kritis terhadap seluruh pengalaman belajar pedagogis, akademik, dan praktik lapangan yang telah dijalani selama program PPG. Melalui mata kuliah ini, saya belajar melakukan refleksi kritis berbasis artefak portofolio digital dengan menerapkan model refleksi yang terstruktur (seperti kerangka Gibbs dan ALACT). Proses presentasi artefak, diskusi kolegial, serta umpan balik dari dosen pembimbing dan rekan sejawat melatih kemampuan berpikir metakognitif saya sebagai calon guru profesional. Saya menyadari bahwa guru adalah pembelajar sepanjang hayat (lifelong learner) yang secara terus-menerus mengevaluasi efektivitas tindakannya di ruang kelas demi kemajuan pendidikan vokasi.'
    },
    'sem2_inovasi': {
        title: 'Refleksi Inovasi Pembelajaran Kejuruan',
        icon: '💡',
        text: 'Mata kuliah Inovasi Pembelajaran Kejuruan membekali saya dengan kompetensi untuk menghadirkan terobosan metodologis dan teknologi yang kontekstual dengan perkembangan industri manufaktur modern (Era Industri 4.0). Saya mengeksplorasi perancangan modul ajar berbasis Project-Based Learning (PjBL) yang terintegrasi dengan Teaching Factory (TeFa), serta pemanfaatan media digital interaktif dan virtual simulator manufaktur. Refleksi terbesar saya adalah pentingnya menjembatani kesenjangan (link and match) antara kurikulum sekolah vokasi dan standar kompetensi industri terkini. Melalui perancangan inovasi seperti media simulator alat ukur presisi dan sistem evaluasi digital real-time, saya belajar bahwa teknologi mampu memperkuat pemahaman konseptual dan memitigasi risiko kesalahan fatal saat praktik langsung.'
    },
    'sem2_kepemimpinan': {
        title: 'Refleksi Projek Kepemimpinan',
        icon: '🤝',
        text: 'Mata kuliah Projek Kepemimpinan mengembangkan jiwa kepemimpinan transformasional, kepekaan sosial, serta keterampilan manajerial dalam merancang dan mengeksekusi inisiatif perubahan nyata di lingkungan komunitas dan sekolah. Pada tahap lanjutan ini, saya bersama tim mempraktikkan siklus manajemen proyek secara menyeluruh, mulai dari analisis pemangku kepentingan (stakeholder analysis), perumusan target SMART, manajemen risiko, hingga eksekusi aksi lapangan. Refleksi esensial yang saya peroleh adalah hakikat kepemimpinan pendidikan yang melayani (servant leadership). Menghadapi dinamika koordinasi tim dan keterbatasan sumber daya melatih resiliensi, komunikasi asertif, serta kepemimpinan adaptif saya demi keberlanjutan dampak positif (sustainable impact) bagi kemajuan komunitas belajar.'
    }
};

window.openEp5Modal = function(id) {
    const data = ep5RefleksiData[id];
    if (!data) return;

    document.getElementById('ep5ModalTitle').innerText = data.title;
    document.getElementById('ep5ModalIcon').innerText = data.icon;
    document.getElementById('ep5ModalText').innerText = data.text;

    const overlay = document.getElementById('ep5ModalOverlay');
    const content = document.getElementById('ep5ModalContent');
    
    if (overlay && content) {
        overlay.style.visibility = 'visible';
        overlay.style.opacity = '1';
        content.style.transform = 'translateY(0)';
        document.body.style.overflow = 'hidden';
    }
};

window.closeEp5Modal = function() {
    const overlay = document.getElementById('ep5ModalOverlay');
    const content = document.getElementById('ep5ModalContent');
    
    if (overlay && content) {
        overlay.style.opacity = '0';
        content.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            overlay.style.visibility = 'hidden';
            document.body.style.overflow = '';
        }, 300);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const ep5Overlay = document.getElementById('ep5ModalOverlay');
    if(ep5Overlay) {
        ep5Overlay.addEventListener('click', function(e) {
            if (e.target === this) {
                window.closeEp5Modal();
            }
        });
    }
});


// EP3 Modal Logic (Semester 2 E-Portofolio Mandiri)
const ep3ModalData = {
    'penilaian_diagnostik': {
        title: 'Asesmen Diagnostik Kognitif & Non-Kognitif',
        badge: 'ASESMEN AWAL PEMBELAJARAN',
        diagnosis: 'Setiap siswa kelas X masuk ke bengkel pemesinan dengan latar belakang kesiapan yang berbeda-beda; sebagian telah mengenal alat ukur di jenjang sebelumnya, sementara sebagian lainnya belum pernah memegang jangka sorong sama sekali.',
        implikasi: 'Tanpa asesmen diagnostik di awal, instruktur berisiko menetapkan ritme pembelajaran yang terlalu cepat bagi kelompok lambat atau terlalu membosankan bagi kelompok yang sudah menguasai konsep dasar.',
        solusi: 'Merancang instrumen tes diagnostik awal berdurasi singkat yang menguji kemampuan membaca skala alat ukur dasar dan pemetaan gaya belajar (kinestetik/visual). Hasilnya dipetakan ke dalam spreadsheet penilaian untuk mengelompokkan siswa secara adaptif (Teaching at the Right Level - TaRL) dan membagi pasangan kerja mesin secara seimbang (peer tutoring).'
    },
    'penilaian_formatif_kinerja': {
        title: 'Asesmen Formatif Unjuk Kerja & Kepatuhan SOP Bengkel',
        badge: 'ASESMEN FORMATIF PROSES',
        diagnosis: 'Kesalahan fatal pada pekerjaan permesinan sering terjadi di tahapan persiapan awal (seperti pencekaman pahat longgar, posisi tubuh salah, atau pembacaan skala terburu-buru) yang tidak terpantau jika penilaian hanya bertumpu pada hasil akhir produk.',
        implikasi: 'Siswa mengulangi kesalahan teknik berulang kali dan baru menyadari kegagalannya setelah benda kerja cacat (afkir) atau pahat patah.',
        solusi: 'Menerapkan lembar checklist observasi unjuk kerja formatif berkala. Guru mengamati dan memberi skor langsung pada tahapan proses: kepatuhan APD keselamatan kerja, kalibrasi titik nol alat ukur, ketelitian pencekaman benda kerja, serta ketepatan sudut pandang mata saat mengukur. Umpan balik korektif diberikan seketika di samping mesin (on-the-spot feedback).'
    },
    'penilaian_sumatif_produk': {
        title: 'Asesmen Sumatif Produk Presisi & Tes Konsep',
        badge: 'ASESMEN SUMATIF HASIL',
        diagnosis: 'Penilaian produk teknik manufaktur memerlukan objektivitas tinggi dan tolok ukur terkuantifikasi secara presisi agar tidak terjadi bias subjektif instruktur.',
        implikasi: 'Siswa merasa penilaian kurang transparan jika batas toleransi ukuran dimensi, kepresisian sudut, dan tingkat kekasaran permukaan tidak diuraikan secara terbuka sejak awal.',
        solusi: 'Mengembangkan rubrik penilaian sumatif berbasis standar industri: toleransi dimensi diameter (±0.05 mm), kepresisian panjang bertingkat, kesikuan bidang (90° ± 15\'), dan tingkat kehalusan permukaan (N7). Rubrik dibagikan kepada siswa sebelum praktik dimulai agar mereka memahami sasaran mutu yang wajib dicapai.'
    },
    'penilaian_analisis_ketercapaian': {
        title: 'Analisis Data Penilaian, Remedial & Pengayaan',
        badge: 'ANALISIS HASIL BELAJAR',
        diagnosis: 'Data nilai yang hanya disimpan sebagai arsip administratif tanpa dianalisis secara statistik tidak akan memberikan dampak perbaikan pada mutu pembelajaran berikutnya.',
        implikasi: 'Siswa yang belum tuntas dibiarkan tertinggal, sedangkan siswa berkemampuan tinggi tidak mendapatkan stimulasi pengayaan yang memadai.',
        solusi: 'Mengintegrasikan seluruh hasil asesmen ke dalam Google Sheets data penilaian terpusat. Dilakukan analisis ketuntasan klasikal (tercapai 89.2%), analisis butir kesulitan, serta menetapkan program tindak lanjut nyata: bimbingan remedial teknis intensif berbantuan simulator digital bagi 4 siswa yang belum tuntas, dan tantangan pembubutan bentuk kompleks/suaian presisi sebagai program pengayaan bagi siswa yang tuntas sempurna.'
    },

    'video_apersepsi_alat_ukur': {
        title: 'Apersepsi Kontekstual: Urgensi Presisi & Toleransi Alat Ukur',
        badge: 'KETERAMPILAN APERSEPSI',
        diagnosis: 'Siswa sering memandang kegiatan pengukuran sebagai langkah sepele dan kurang menyadari dampak fatal dari selisih ukuran seperseratus milimeter (0.01 mm) pada komponen mesin.',
        implikasi: 'Timbul sikap ceroboh dalam membaca skala alat ukur, menghasilkan benda kerja yang tidak presisi sehingga gagal dirakit (loss of interchangeability) di lini produksi industri.',
        solusi: 'Dalam rekaman video, guru membuka pembelajaran melalui apersepsi kontekstual dengan menampilkan studi kasus komponen poros industri manufaktur yang gagal rakit akibat deviasi mikro. Hal ini menstimulasi rasa ingin tahu dan membangun kesadaran kritis siswa akan nilai presisi.'
    },
    'video_pemodelan_alat_ukur': {
        title: 'Pemodelan Penggunaan Jangka Sorong & Mikrometer Sekrup',
        badge: 'DEMONSTRASI & PEMODELAN',
        diagnosis: 'Siswa pemula sering keliru dalam posisi pencekaman rahang ukur dan memutar rachet thimble secara berlebihan hingga merusak spindel mikrometer presisi.',
        implikasi: 'Sensor ukur mengalami keausan dini, timbul deformasi elastis pada benda ukur tipis, serta terjadi kesalahan pembacaan akibat sudut paralaks penglihatan.',
        solusi: 'Guru mendemonstrasikan secara perlahan (slow-motion modeling) di depan kelas: memegang rangka mikrometer dengan tangan kiri, memutar rachet thimble dengan dua jari hingga terdengar bunyi 2-3 klik, serta memposisikan garis pandang mata tepat tegak lurus 90° terhadap garis skala nonius.'
    },
    'video_scaffolding_alat_ukur': {
        title: 'Bimbingan Mandiri & Scaffolding Pembacaan Skala Nonius',
        badge: 'BIMBINGAN MANDIRI SISWA',
        diagnosis: 'Siswa mengalami keraguan saat menentukan garis nonius mana yang benar-benar berimpit lurus dengan garis skala utama pada ketelitian 0.05 mm dan 0.02 mm.',
        implikasi: 'Siswa menebak hasil pengukuran secara spekulatif tanpa prosedur verifikasi visual yang benar.',
        solusi: 'Guru berkeliling secara aktif (active roaming) memberikan scaffolding terarah: tidak langsung menyebutkan angka ukuran, melainkan mengajukan pertanyaan penuntun: "Perhatikan segmen antara angka 3 dan 4, garis mana yang paling sejajar tanpa pembiasan cahaya?" Guru juga membimbing siswa melakukan kalibrasi titik nol (zero error check) sebelum mencatat ukuran.'
    },
    'video_evaluasi_sop_alat_ukur': {
        title: 'Evaluasi Pengukuran & SOP Perawatan Alat Presisi',
        badge: 'EVALUASI & BUDAYA 5R',
        diagnosis: 'Alat ukur presisi sering diletakkan sembarangan di atas meja besi atau tertumpuk dengan perkakas potong lain yang berminyak dan bertatal tajam.',
        implikasi: 'Permukaan ukur (measuring faces) tergores dan presisi alat ukur menurun drastis dalam jangka pendek.',
        solusi: 'Sesi penutup video menampilkan evaluasi unjuk kerja antar-siswa (peer assessment) menggunakan lembar kerja verifikasi dimensi, disusul pembiasaan SOP perawatan instrumen: mengelap alat dengan kain halus, merenggangkan rahang ukur saat disimpan, dan mengunci kotak kayu/plastik pelindung sesuai budaya 5R bengkel.'
    },

    'media_buku_ajar': {
        title: 'Buku Bahan Ajar: Fondasi Teori & Jobsheet Terstruktur',
        badge: 'MEDIA CETAK & DIGITAL',
        diagnosis: 'Peserta didik sering kali mengalami kebingungan urutan operasional atau keliru membaca dimensi gambar kerja jika hanya mengandalkan ingatan dari penjelasan lisan guru di awal jam pelajaran.',
        implikasi: 'Timbul keraguan saat menyetel mesin, waktu pengerjaan menjadi molor, dan timbul risiko benda kerja cacat (afkir/reject) akibat salah pembacaan ukuran toleransi ISO.',
        solusi: 'Menyusun dan menerapkan Buku Bahan Ajar terstruktur yang dilengkapi gambar kerja detail standar ISO, tabel praktis pemilihan kecepatan potong (cutting speed), serta jobsheet langkah kerja bertahap yang dilaminasi tahan oli dan kotoran bengkel sehingga dapat diletakkan langsung di samping mesin bubut/frais sebagai panduan mandiri siswa.'
    },
    'media_bimo_labs': {
        title: 'Web Labs BIMO Manufacturing: Ekosistem Belajar Interaktif',
        badge: 'PLATFORM LABS DIGITAL',
        diagnosis: 'Keterbatasan durasi penyampaian teori di kelas konvensional membuat konsep keteknikan yang padat sering kali kurang terserap maksimal sebelum siswa melangkah ke bengkel praktikum.',
        implikasi: 'Instruktur terpaksa mengalokasikan banyak waktu di bengkel untuk mengulang kembali teori dasar, sehingga jam praktik mengoperasikan mesin menjadi berkurang drastis.',
        solusi: 'Mengembangkan dan mengimplementasikan Web Labs BIMO Manufacturing sebagai media pembelajaran digital interaktif mandiri. Siswa dapat mengeksplorasi materi kejuruan berbasis animasi 3D, visualisasi mekanisme transmisi mesin, dan panduan belajar terstruktur kapan saja dari gawai mereka sebelum jam praktik (menerapkan model flipped classroom).'
    },
    'media_simulator': {
        title: 'Simulator Manufaktur: Praktik & Eksperimen Virtual Aman',
        badge: 'SIMULATOR PERMESINAN',
        diagnosis: 'Peserta didik kelas X Fase E kerap mengalami ketakutan dan kecemasan tinggi saat pertama kali berhadapan langsung dengan mesin perkakas bertenaga motor tinggi yang berputar kencang.',
        implikasi: 'Rasa takut salah menyebabkan kekakuan motorik, kesalahan pemutaran tuas eretan mesin, pencekaman pahat yang longgar, hingga potensi kecelakaan kerja bengkel.',
        solusi: 'Menyediakan fitur Simulator Manufaktur Virtual pada Web Labs BIMO Manufacturing. Fitur ini memungkinkan siswa melatih gerakan koordinasi tangan, mensimulasikan setting putaran spindle (RPM), serta mengamati simulasi pemotongan logam secara visual tanpa rasa takut dan tanpa risiko bahaya fisik atau kerusakan mesin nyata.'
    },
    'media_bank_soal': {
        title: 'Bank Soal, Kuis Adaptif & Evaluasi Real-Time',
        badge: 'ASESMEN FORMATIF DIGITAL',
        diagnosis: 'Kuis konvensional berbasis kertas memerlukan waktu koreksi manual yang lama, sehingga guru tidak dapat segera mengetahui siswa mana yang belum siap mengoperasikan mesin.',
        implikasi: 'Siswa yang belum menguasai pemahaman dasar K3LH dan rumus kecepatan potong berisiko langsung bekerja di mesin tanpa verifikasi kompetensi awal.',
        solusi: 'Mengintegrasikan fitur Bank Soal dan Kuis Adaptif terintegrasi di Web Labs BIMO Manufacturing yang dilengkapi penilaian otomatis instan (instant feedback). Kuis ini berfungsi sebagai asesmen formatif (pre-test/entry pass) mandiri: siswa wajib lulus kuis kesiapan sebelum diperbolehkan menyalakan tombol daya mesin perkakas.'
    },
    'nonmengajar_pramuka_karakter': {
        title: 'Pramuka: Penanaman Karakter, Kepemimpinan & Etika Vokasi',
        badge: 'KEGIATAN KEPRAMUKAAN',
        diagnosis: 'Peserta didik vokasi sering kali memiliki kecakapan fisik dan keteknikan yang prima, namun masih membutuhkan penguatan dalam hal konsistensi kedisiplinan, etika komunikasi, dan kepatuhan norma sekolah.',
        implikasi: 'Kelemahan pada aspek non-teknis (soft skills) ini menjadi kendala krusial saat siswa memasuki dunia industri yang menuntut disiplin tinggi dan integritas kerja tanpa kompromi.',
        solusi: 'Mengoptimalkan peran pendampingan ekstrakurikuler Gerakan Pramuka di SMK Negeri 2 Depok Sleman untuk menginternalisasikan nilai Dasa Darma dan Tri Satya melalui apel disiplin mingguan, penugasan mandiri berintegritas, serta pembiasaan budaya saling menghormati dan peduli lingkungan.'
    },
    'nonmengajar_pramuka_regu': {
        title: 'Pramuka: Kerja Sama Regu, Komunikasi & Ketahanan Mental',
        badge: 'DINAMIKA REGU & KEPRAMUKAAN',
        diagnosis: 'Kecenderungan bekerja secara individualis dan ego sektoral terkadang muncul di kalangan siswa saat dihadapkan pada tugas bersama yang memerlukan koordinasi cepat.',
        implikasi: 'Terjadi disparitas kontribusi dalam regu, miskomunikasi antarsiswa, dan lemahnya rasa tanggung jawab kolektif terhadap tujuan kelompok.',
        solusi: 'Menerapkan metode kepramukaan berbasis sistem beregu (Patrol System). Melalui kegiatan baris-berbaris (PBB), tali-temali (pioneering), pemecahan sandi, dan simulasi penjelajahan, siswa dilatih berbagi peran, mematuhi komando pemimpin regu, serta membangun resiliensi fisik dan mental secara bersama-sama.'
    },
    'nonmengajar_lks_teknis': {
        title: 'Pendampingan LKS: Pembinaan Teknis & Presisi Tinggi',
        badge: 'PEMBINAAN PRESTASI LKS',
        diagnosis: 'Tuntutan kompetisi LKS (Lomba Kompetensi Siswa) permesinan sangat ekstrem dalam hal toleransi geometris (akurasi hingga ±0.01 mm s.d. ±0.005 mm) dengan batas waktu pengerjaan yang sangat ketat.',
        implikasi: 'Peserta bimbingan berisiko melakukan kesalahan fatal pada urutan langkah kerja, salah penentuan geometri pahat potong, atau aus pahat berlebih jika strategi pemesinan tidak diasah secara matang.',
        solusi: 'Melaksanakan pendampingan teknis intensif: membedah gambar kerja standar kompetisi internasional, mengoptimalkan kalkulasi parameter pemotongan per jenis material benda kerja, melatih penggunaan alat ukur presisi tinggi (micrometer dan bore gauge), serta menyusun strategi urutan pemesinan paling efisien.'
    },
    'nonmengajar_lks_mental': {
        title: 'Ekstrakurikuler Kejuruan: Manajemen Stres & Mental Juara',
        badge: 'PENGUATAN MENTAL KOMPETISI',
        diagnosis: 'Tekanan psikologis yang tinggi selama simulasi lomba atau saat disaksikan penguji dapat memicu ketegangan saraf, tremor pada tangan saat menyetel mesin, dan hilangnya fokus siswa.',
        implikasi: 'Siswa membuat kekeliruan fatal dalam penyetelan titik referensi nol (zero offset) atau pembacaan ukuran dial, yang merusak benda kerja uji.',
        solusi: 'Menerapkan latihan simulasi bertekanan (stress-testing simulation) dalam kegiatan ekstrakurikuler kejuruan: melatih teknik pernapasan untuk kestabilan emosi, menetapkan batas waktu bertahap dengan pengawasan ketat, serta menumbuhkan mentalitas tangguh dan budaya perbaikan berkelanjutan (Kaizen mindset).'
    },

        'rancangan_ctl': {
        title: 'Model Pembelajaran CTL (Contextual Teaching and Learning)',
        badge: 'MODEL PEMBELAJARAN',
        diagnosis: 'Materi dasar kejuruan sering kali dianggap abstrak, membosankan, dan sekadar hafalan teoritis jika diajarkan terlepas dari konteks nyata operasional industri dan kehidupan sehari-hari siswa vokasi.',
        implikasi: 'Siswa mengalami penurunan minat belajar dan kesulitan mengaitkan mengapa prosedur K3LH, alur teknik produksi, dan sifat bahan teknik harus dipahami secara presisi sebelum melakukan pekerjaan permesinan.',
        solusi: 'Menerapkan 7 pilar CTL secara komprehensif: (1) Konstruktivisme dalam memahami karakteristik bahan, (2) Inkuiri dalam menganalisis prosedur permesinan, (3) Bertanya untuk menstimulasi nalar kritis, (4) Masyarakat Belajar lewat diskusi kolaboratif, (5) Pemodelan melalui demonstrasi guru dan studi video industri manufaktur, (6) Refleksi terstruktur di akhir sesi, dan (7) Penilaian Autentik berbasis kinerja nyata di bengkel SMK Negeri 2 Depok Sleman.'
    },
    'rancangan_dup_tarl_crt': {
        title: 'Pendekatan DUP Terintegrasi TaRL & Culturally Responsive Teaching (CRT)',
        badge: 'PENDEKATAN PEMBELAJARAN',
        diagnosis: 'Peserta didik kelas X Fase E memiliki disparitas pemahaman awal (heterogenitas kognitif) yang lebar serta latar belakang sosiokultural beragam dalam menyerap konsep keteknikan.',
        implikasi: 'Instruksi klasikal seragam berisiko membuat siswa berkemampuan awal rendah cemas dan tertinggal, sementara siswa yang lebih cepat memahami materi akan kehilangan motivasi belajar.',
        solusi: 'Mengintegrasikan tiga pilar pendekatan pembelajaran: (1) DUP (Diferensiasi, Understanding, dan Praktik) memastikan pemahaman konseptual yang kokoh mendahului pelaksanaan praktik; (2) TaRL (Teaching at the Right Level) menyajikan materi bergradasi dan bimbingan bertingkat (scaffolding) sesuai fase capaian belajar siswa; (3) CRT (Culturally Responsive Teaching) mengintegrasikan nilai kearifan lokal budaya kerja industri Yogyakarta serta filosofi Tamansiswa (Sistem Among: Ing Ngarso Sung Tulodo, Ing Madyo Mangun Karso, Tut Wuri Handayani) guna menumbuhkan etos kerja, ketelitian, dan kepedulian sosial.'
    },
    'rancangan_ceramah_interaktif': {
        title: 'Metode Pembelajaran Ceramah Interaktif',
        badge: 'METODE PEMBELAJARAN',
        diagnosis: 'Penyampaian materi teoritis yang padat seperti regulasi K3LH, parameter potong mesin, dan klasifikasi material logam melalui metode ceramah konvensional satu arah cenderung memicu kepasifan dan kejenuhan siswa.',
        implikasi: 'Daya retensi materi menurun drastis dan guru tidak dapat mendeteksi miskonsepsi siswa secara langsung di saat sesi pembelajaran sedang berlangsung.',
        solusi: 'Merancang sintaks ceramah interaktif terstruktur berdurasi proporsional (10-15 menit per segmen): diselingi pertanyaan pemantik kontekstual (trigger questions), demonstrasi spesimen benda kerja riil di kelas, media tayangan animasi mekanisme mesin, serta kuis respons cepat antarsiswa (think-pair-share) untuk memverifikasi pemahaman secara langsung (check for understanding).'
    },
    'rancangan_3materi': {
        title: 'Integrasi Tiga Materi Pokok: K3LH, Teknik Dasar Produksi, & Pengetahuan Bahan',
        badge: 'KONTEN MATERI PEMBELAJARAN',
        diagnosis: 'Tiga materi fondasi kejuruan sering kali diajarkan secara terpisah tanpa alur keterkaitan yang jelas, sehingga siswa gagal memahami hubungan sistemik antara sifat material, pemilihan mesin produksi, dan keselamatan kerja.',
        implikasi: 'Peserta didik berisiko salah menentukan parameter pemotongan akibat ketidaktahuan atas kekerasan material (Pengetahuan Bahan), yang dapat merusak pahat/mesin (Teknik Produksi) atau bahkan memicu kecelakaan kerja di bengkel (K3LH).',
        solusi: 'Menyusun rancangan modul ajar terpadu: diawali pemahaman sifat mekanik material (Pengetahuan Bahan), dihubungkan dengan penentuan jenis mesin konvensional dan kalkulasi kecepatan potong (Teknik Dasar Produksi), serta dipagari secara ketat dengan SOP keselamatan, APD standar, dan budaya 5R (K3LH).'
    },
    'materi_struktur': {
        title: 'Struktur & Gradasi Kedalaman Materi Ajar',
        badge: 'MATERI PEMBELAJARAN',
        diagnosis: 'Materi teknik pemesinan memiliki konsep fisik dan kalkulasi matematis yang cukup abstrak apabila disajikan langsung secara teoretis murni tanpa jembatan visual.',
        implikasi: 'Peserta didik mengalami cognitive overload saat menghubungkan rumus kecepatan potong dengan penyetelan tuas gearbox mesin bubut/frais di bengkel.',
        solusi: 'Menyusun materi bergradasi: dimulai dari pengamatan fenomena pemotongan logam, analogi visual pergerakan pahat, tabel kalkulasi cepat, hingga pendalaman rumus teknis analitis.'
    },
    'materi_industri': {
        title: 'Kontekstualisasi Standar Industri Manufaktur (DUDI)',
        badge: 'RELEVANSI INDUSTRI',
        diagnosis: 'Standar kerja di dunia industri manufaktur modern menuntut tingkat kepresisian toleransi dimensi ISO dan mutu rigi las yang sangat ketat.',
        implikasi: 'Peserta didik perlu dibiasakan dengan standar industri sejak di sekolah agar tidak mengalami culture shock saat terjun dalam Praktik Kerja Lapangan (PKL) maupun dunia kerja.',
        solusi: 'Mengadopsi gambar kerja teknik nyata dan kriteria inspeksi kendali mutu (quality control) berstandar industri rekanan SMK Negeri 2 Depok Sleman ke dalam bahan ajar modular.'
    },
    'materi_handout': {
        title: 'Handout Bergambar & Information Sheet Praktis',
        badge: 'BAHAN AJAR',
        diagnosis: 'Buku teks kejuruan sering kali tebal dan kurang efisien untuk dibaca langsung di lingkungan bengkel yang menuntut aksi fisik cepat dan tangkas.',
        implikasi: 'Peserta didik enggan membuka referensi teori saat menghadapi keraguan operasional di meja kerja mesin.',
        solusi: 'Menyusun lembar informasi ringkas (information sheet) 1-2 halaman yang diperkaya dengan ilustrasi teknis berwarna dan diagram alur yang mudah diletakkan di dekat mesin.'
    },
    'materi_miskonsepsi': {
        title: 'Identifikasi & Mitigasi Miskonsepsi Siswa',
        badge: 'PENGUATAN KONSEP',
        diagnosis: 'Siswa kerap beranggapan bahwa semakin tinggi putaran mesin (rpm), maka proses kerja akan semakin cepat selesai tanpa memperhatikan jenis bahan dan diameter benda kerja.',
        implikasi: 'Pahat potong cepat aus atau patah, kualitas kehalusan permukaan benda kerja menurun, dan motor penggerak mesin mengalami beban berlebih.',
        solusi: 'Menghadirkan demonstrasi komparasi keausan pahat pada berbagai putaran spindel serta menyusun tabel cepat pemilihan putaran mesin berdasarkan diameter dan material.'
    },
    'media_animasi': {
        title: 'Animasi 3D & Slide Presentasi Visual Interaktif',
        badge: 'MEDIA PEMBELAJARAN',
        diagnosis: 'Mekanisme transmisi roda gigi (gearbox) dan sudut pemotongan pahat (clearance & rake angle) tertutup dan sulit diamati secara kasat mata pada mesin nyata.',
        implikasi: 'Siswa mengalami kesulitan memahami transmisi putaran dan pengaruh variasi sudut potong terhadap pembentukan tatal logam.',
        solusi: 'Mengembangkan media slide interaktif dan animasi 3D pergerakan pahat serta transmisi daya mesin yang memvisualisasikan fenomena internal mesin secara aman dan jelas.'
    },
    'media_sampel': {
        title: 'Pemanfaatan Benda Kerja Sampel & Reject',
        badge: 'ALAT PERAGA',
        diagnosis: 'Peserta didik sering kali baru menyadari kesalahan teknik pembubutan atau pengelasan setelah benda kerja selesai dan dievaluasi guru.',
        implikasi: 'Siswa tidak memiliki kepekaan sensoris (feeling teknik) untuk mendeteksi potensi cacat kerja selama proses pemesinan sedang berlangsung.',
        solusi: 'Menyediakan spesimen benda kerja standar dan sampel cacat (chatter marks, taper, undercut las) sebagai media stimulasi agar siswa dapat mendeteksi kegagalan kerja sedini mungkin.'
    },
    'media_retensi': {
        title: 'Peningkatan Keterlibatan & Retensi Pemahaman Siswa',
        badge: 'EFEKTIVITAS MEDIA',
        diagnosis: 'Penyampaian teori dengan metode ceramah panjang di awal sesi bengkel membuat perhatian siswa cepat menurun karena antusiasme mereka ingin segera praktik.',
        implikasi: 'Penyerapan instruksi keselamatan dan parameter kerja kunci menjadi tidak optimal.',
        solusi: 'Menggunakan video demonstrasi ringkas berdurasi 3-5 menit yang dinamis, dilanjutkan dengan sesi tanya jawab interaktif yang memicu keaktifan siswa sebelum menuju mesin.'
    },
    'media_kendala': {
        title: 'Kendala Lingkungan Bengkel & Solusi Media Fleksibel',
        badge: 'ADAPTASI MEDIA',
        diagnosis: 'Suasana bengkel yang bising oleh putaran motor mesin dan berdebu tatal menyulitkan penggunaan proyektor konvensional di area praktikum.',
        implikasi: 'Tampilan tayangan sering kurang kontras dan instruksi audio video tidak terdengar dengan jelas oleh seluruh siswa.',
        solusi: 'Mengkombinasikan sesi briefing awal di ruang teori bengkel dengan lembar infografis alur SOP tahan oli dan modul digital yang dapat diakses mandiri melalui perangkat ponsel pintar.'
    },
    'video_apersepsi': {
        title: 'Keterampilan Apersepsi & Motivasi Kontekstual',
        badge: 'KETERAMPILAN MENGAJAR',
        diagnosis: 'Siswa memerlukan jembatan mental yang mengaitkan teori di kelas dengan relevansi langsung komponen mekanik di dunia nyata.',
        implikasi: 'Tanpa apersepsi yang bermakna, siswa memandang pekerjaan praktikum semata-mata sebagai tugas menghabiskan bahan tanpa kebanggaan vokasi.',
        solusi: 'Video mendokumentasikan apersepsi kontekstual melalui studi kasus komponen transmisi otomotif presisi, membangkitkan kebanggaan profesi dan motivasi belajar siswa.'
    },
    'video_k3': {
        title: 'Pengawasan K3 & Mobilitas Posisi Guru di Bengkel',
        badge: 'PENGELOLAAN KELAS',
        diagnosis: 'Mengelola kelas bengkel pemesinan menuntut kewaspadaan tinggi karena mesin berputar dengan kecepatan tinggi dan serpihan tatal panas.',
        implikasi: 'Posisi guru yang pasif di satu meja kerja berpotensi menimbulkan celah keselamatan pada siswa di stasiun kerja lainnya.',
        solusi: 'Rekaman video membuktikan mobilitas aktif guru melintasi area kerja (sweep zone), kontak mata berkala, serta intervensi cepat dan persuasif terhadap kepatuhan kacamata pengaman.'
    },
    'video_scaffolding': {
        title: 'Bimbingan Mandiri & Pertanyaan Penuntun (Scaffolding)',
        badge: 'BIMBINGAN SISWA',
        diagnosis: 'Kecenderungan instruktur untuk langsung mengambil alih kendali mesin saat siswa bingung dapat menghambat pembentukan kemandirian belajar.',
        implikasi: 'Peserta didik menjadi sangat bergantung pada guru dan tidak percaya diri dalam mengambil keputusan operasional.',
        solusi: 'Dalam video, guru memfasilitasi scaffolding dengan melontarkan pertanyaan reflektif: "Menurutmu mengapa permukaannya timbul getaran? Mari periksa pencekaman pahatnya bersama."'
    },
    'video_penutup': {
        title: 'Refleksi Penutup & Budaya Kerja 5R Bengkel',
        badge: 'PENUTUP PEMBELAJARAN',
        diagnosis: 'Alokasi waktu praktikum sering tersedot habis untuk pemotongan logam sehingga penutupan kelas dan pembersihan bengkel dilakukan terburu-buru.',
        implikasi: 'Lingkungan bengkel menjadi kotor oleh tatal logam, peralatan tidak terinventarisasi rapi, dan siswa tidak merefleksikan pencapaian hari itu.',
        solusi: 'Video menunjukkan manajemen waktu yang tertib: 20 menit sebelum usai, mesin dimatikan serentak untuk evaluasi dimensi hasil kerja bersama dan penerapan budaya 5R industri.'
    }
};

window.openEp3Modal = function(id) {
    const data = ep3ModalData[id];
    if (!data) return;

    const modalTitle = document.getElementById('ep3ModalTitle');
    const modalBadge = document.getElementById('ep3ModalBadge');
    const modalDiag = document.getElementById('ep3ModalDiagnosis');
    const modalImpl = document.getElementById('ep3ModalImplikasi');
    const modalSol = document.getElementById('ep3ModalSolusi');

    if (modalTitle) modalTitle.innerText = data.title;
    if (modalBadge) modalBadge.innerText = data.badge;
    if (modalDiag) modalDiag.innerText = data.diagnosis;
    if (modalImpl) modalImpl.innerText = data.implikasi;
    if (modalSol) modalSol.innerText = data.solusi;

    const overlay = document.getElementById('ep3ModalOverlay');
    const content = document.getElementById('ep3ModalContent');
    
    if (overlay && content) {
        overlay.style.visibility = 'visible';
        overlay.style.opacity = '1';
        content.style.transform = 'translateY(0)';
        document.body.style.overflow = 'hidden';
    }
};

window.closeEp3Modal = function() {
    const overlay = document.getElementById('ep3ModalOverlay');
    const content = document.getElementById('ep3ModalContent');
    
    if (overlay && content) {
        overlay.style.opacity = '0';
        content.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            overlay.style.visibility = 'hidden';
            document.body.style.overflow = '';
        }, 300);
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const ep3Overlay = document.getElementById('ep3ModalOverlay');
    if (ep3Overlay) {
        ep3Overlay.addEventListener('click', function(e) {
            if (e.target === this) {
                window.closeEp3Modal();
            }
        });
    }
});



// Global Toast Notification
window.showToast = function(msg) {
    const toast = document.getElementById('toast-notification');
    const toastText = document.getElementById('toast-text');
    if (toast && toastText) {
        toastText.innerText = msg;
        toast.classList.add('show');
        clearTimeout(window._toastTimeout);
        window._toastTimeout = setTimeout(() => {
            toast.classList.remove('show');
        }, 2200);
    }
};

// EP4 Interactive Filter (UTS vs UAS)
window.filterEp4 = function(view, btn) {
    document.querySelectorAll('.ep4-filter-tabs .portfolio-chip').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');

    const secMateri = document.getElementById('ep4-materi');
    const secVideoRpp = document.getElementById('ep4-video-rpp');
    const secEvaluasi = document.getElementById('ep4-evaluasi');
    const secTimeline = document.getElementById('ep4-timeline');
    const secKomp = document.getElementById('ep4-komparasi');

    const allSecs = [secMateri, secVideoRpp, secEvaluasi, secTimeline, secKomp];

    if (view === 'materi') {
        allSecs.forEach(s => { if (s) s.style.display = 'none'; });
        if (secMateri) {
            secMateri.style.display = 'block';
            secMateri.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        window.showToast('Menampilkan 3 Pokok Materi Kejuruan Berjejer');
    } else if (view === 'video' || view === 'uts') {
        allSecs.forEach(s => { if (s) s.style.display = 'none'; });
        if (secVideoRpp) {
            secVideoRpp.style.display = 'block';
            secVideoRpp.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        window.showToast('Menampilkan Video Praktik Mengajar & RPP Pendamping');
    } else if (view === 'evaluasi' || view === 'uas') {
        allSecs.forEach(s => { if (s) s.style.display = 'none'; });
        if (secEvaluasi) {
            secEvaluasi.style.display = 'block';
            secEvaluasi.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        window.showToast('Menampilkan Data Penilaian & Evaluasi Asesmen');
    } else if (view === 'timeline') {
        allSecs.forEach(s => { if (s) s.style.display = 'none'; });
        if (secTimeline) {
            secTimeline.style.display = 'block';
            secTimeline.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        window.showToast('Menampilkan Roadmap 5 Siklus PPL II');
    } else if (view === 'komparasi') {
        allSecs.forEach(s => { if (s) s.style.display = 'none'; });
        if (secKomp) {
            secKomp.style.display = 'block';
            secKomp.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        window.showToast('Menampilkan Matriks Evaluasi Komparatif');
    } else {
        allSecs.forEach(s => { if (s) s.style.display = 'block'; });
        if (secMateri) {
            secMateri.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
        window.showToast('Menampilkan Seluruh Bagian Portofolio 5 Siklus');
    }

    if (window.initLazyIframes) {
        window.initLazyIframes(document.getElementById('portfolio4'));
    }
};

// =============================================================
// Unified High-Performance Scroll Listener (60/120 FPS Buttery Smooth)
// =============================================================
let scrollTimer = null;
let isNavScrolled = false;
let isFloatingVisible = false;
let scrollBarTicking = false;

window.addEventListener('scroll', () => {
    // 1. Suppress hover and mouse events during active scrolling
    if (!document.body.classList.contains('is-scrolling')) {
        document.body.classList.add('is-scrolling');
    }
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(() => {
        document.body.classList.remove('is-scrolling');
    }, 120);

    // 2. Offload visual updates to requestAnimationFrame
    if (!scrollBarTicking) {
        window.requestAnimationFrame(() => {
            const scrollY = window.scrollY || document.documentElement.scrollTop;

            // Nav shadow toggle (class-based, zero inline style mutation)
            const nav = document.querySelector('nav');
            const shouldNavScrolled = scrollY > 50;
            if (shouldNavScrolled !== isNavScrolled && nav) {
                isNavScrolled = shouldNavScrolled;
                nav.classList.toggle('nav-scrolled', isNavScrolled);
            }

            // Scroll progress bar
            const progressBar = document.getElementById('scroll-progress');
            if (progressBar) {
                const docHeight = document.documentElement.scrollHeight - window.innerHeight;
                if (docHeight > 0) {
                    progressBar.style.width = ((scrollY / docHeight) * 100) + '%';
                }
            }

            // Floating action bar auto-visibility
            const floatingBar = document.getElementById('floatingActionBar');
            const landing = document.getElementById('landing-sections');
            const isLandingVisible = landing && !landing.classList.contains('hidden-section');
            if (floatingBar) {
                const shouldFloating = !isLandingVisible && scrollY > 150;
                if (shouldFloating !== isFloatingVisible) {
                    isFloatingVisible = shouldFloating;
                    floatingBar.classList.toggle('visible', isFloatingVisible);
                }
            }
            scrollBarTicking = false;
        });
        scrollBarTicking = true;
    }
}, { passive: true });

// Interactive Card Iframe Loader on Demand
window.loadCardIframe = function(boxId, url, title) {
    const box = document.getElementById(boxId);
    if (!box) return;
    box.innerHTML = `
        <div style="background: #0f172a; color: white; padding: 0.45rem 0.8rem; font-size: 0.78rem; font-weight: 600; display: flex; justify-content: space-between; align-items: center;">
            <span>📄 ${title || 'Pratinjau Dokumen'}</span>
            <button type="button" onclick="openDocPreviewModal('${url}', '${title || 'Dokumen'}')" style="background: rgba(255,255,255,0.25); border: none; color: white; padding: 0.2rem 0.5rem; border-radius: 6px; cursor: pointer; font-size: 0.72rem; font-weight: 700;">⛶ Penuh</button>
        </div>
        <iframe src="${url}" title="${title || 'Pratinjau'}" style="width: 100%; height: calc(100% - 32px); border: none; background: white;"></iframe>
    `;
    if (window.showToast) window.showToast('Memuat pratinjau ' + (title || 'dokumen'));
};

// -------------------------------------------------------------
// Direct In-Website Document & Media Preview Logic
// -------------------------------------------------------------
window.openDocPreviewModal = function(url, title) {
    const modalOverlay = document.getElementById('artefakModal');
    const modalIframe = document.getElementById('modalIframe');
    const modalTitle = document.getElementById('modalTitle');
    if (!modalOverlay || !modalIframe) return;

    let previewUrl = url;
    
    // YouTube links (youtu.be/ID or youtube.com/watch?v=ID)
    if (previewUrl.includes('youtu.be/')) {
        const vidId = previewUrl.split('youtu.be/')[1].split(/[?&]/)[0];
        previewUrl = `https://www.youtube.com/embed/${vidId}?autoplay=1`;
    } else if (previewUrl.includes('youtube.com/watch')) {
        const urlParts = previewUrl.split('?');
        const urlParams = new URLSearchParams(urlParts[1] || '');
        const vidId = urlParams.get('v');
        if (vidId) {
            previewUrl = `https://www.youtube.com/embed/${vidId}?autoplay=1`;
        }
    }
    // Google Sheets (convert edit/view to htmlembed)
    else if (previewUrl.includes('docs.google.com/spreadsheets/d/')) {
        const sheetMatch = previewUrl.match(/\/spreadsheets\/d\/([a-zA-Z0-9_-]+)/);
        const gidMatch = previewUrl.match(/gid=([0-9]+)/);
        if (sheetMatch && sheetMatch[1]) {
            const sheetId = sheetMatch[1];
            const gid = gidMatch ? gidMatch[1] : '0';
            previewUrl = `https://docs.google.com/spreadsheets/d/${sheetId}/htmlembed?gid=${gid}&widget=false&chrome=false`;
        }
    }
    // Google Docs (convert edit/view to preview)
    else if (previewUrl.includes('docs.google.com/document/d/') && !previewUrl.includes('/preview')) {
        const docMatch = previewUrl.match(/\/document\/d\/([a-zA-Z0-9_-]+)/);
        if (docMatch && docMatch[1]) {
            previewUrl = `https://docs.google.com/document/d/${docMatch[1]}/preview`;
        }
    }
    // Google Drive File
    else if (previewUrl.includes('drive.google.com/file/d/') && !previewUrl.includes('/preview')) {
        previewUrl = previewUrl.replace(/\/view(\?.*)?$/, '/preview');
    }
    
    modalIframe.src = previewUrl;
    if (modalTitle) modalTitle.textContent = title || 'Preview Dokumen';
    modalOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
};

window.switchUasModul = function(tabName, btn) {
    const iframe = document.getElementById('uasModulIframe');
    const title = document.getElementById('uasModulTitle');
    const fullscreenBtn = document.getElementById('uasModulFullscreenBtn');
    
    document.querySelectorAll('.uas-modul-tab').forEach(b => {
        b.style.background = 'rgba(255,255,255,0.15)';
        b.style.color = '#e2e8f0';
        b.style.fontWeight = '500';
    });
    if (btn) {
        btn.style.background = '#ffffff';
        btn.style.color = '#0f172a';
        btn.style.fontWeight = '700';
    }

    if (tabName === 'k3lh') {
        const url = 'https://drive.google.com/file/d/1Z03qLXSKLj4QveKXVh8s85Tp8hrhOSDg/preview';
        if (iframe) iframe.src = url;
        if (title) title.innerHTML = '🛡️ <strong>Modul Ajar Siklus 1:</strong> Penerapan K3LH & Budaya Kerja 5R Bengkel Mesin';
        if (fullscreenBtn) {
            fullscreenBtn.onclick = function() {
                window.openDocPreviewModal(url, 'Modul Ajar Siklus 1: Penerapan K3LH & Budaya 5R');
            };
        }
    } else if (tabName === 'bahan') {
        const url = 'https://drive.google.com/file/d/1E5vGh3PegvlUHAFJzhNCb4vbTBvDrxSP/preview';
        if (iframe) iframe.src = url;
        if (title) title.innerHTML = '🔬 <strong>Modul Ajar Siklus 4 & 5:</strong> Pengetahuan Bahan Teknik (Sifat Fisik, Kimia, Listrik & Mekanik)';
        if (fullscreenBtn) {
            fullscreenBtn.onclick = function() {
                window.openDocPreviewModal(url, 'Modul Ajar Siklus 4 & 5: Pengetahuan Bahan Teknik');
            };
        }
    } else if (tabName === 'produksi') {
        const url = 'https://drive.google.com/file/d/1ulngK_Fq_GWslrw87j8aES4ksfZbMMNV/preview';
        if (iframe) iframe.src = url;
        if (title) title.innerHTML = '⚙️ <strong>Modul Ajar Siklus 3:</strong> Teknik Dasar Produksi (Mesin Bubut & Las)';
        if (fullscreenBtn) {
            fullscreenBtn.onclick = function() {
                window.openDocPreviewModal(url, 'Modul Ajar Siklus 3: Teknik Dasar Produksi Manufaktur');
            };
        }
    }
};

window.switchUasEvaluasi = function(tabName, btn) {
    const iframe = document.getElementById('uasEvaluasiIframe');
    const title = document.getElementById('uasEvaluasiTitle');
    const fullscreenBtn = document.getElementById('uasEvaluasiFullscreenBtn');

    document.querySelectorAll('.uas-evaluasi-tab').forEach(b => {
        b.style.background = 'rgba(255,255,255,0.15)';
        b.style.color = '#e2e8f0';
        b.style.fontWeight = '500';
    });
    if (btn) {
        btn.style.background = '#ffffff';
        btn.style.color = '#0f172a';
        btn.style.fontWeight = '700';
    }

    if (tabName === 'sheets') {
        const url = 'https://docs.google.com/spreadsheets/d/1-YH8PCzHIUv1B8I1dCj_XmcQ2c-jyAavPQfWGHYCUT4/htmlembed?gid=1196549737&widget=false&chrome=false';
        if (iframe) {
            iframe.src = url;
            iframe.removeAttribute('data-src');
        }
        if (title) title.innerHTML = '📊 <strong>Data Rekapitulasi Penilaian:</strong> Google Sheets Nilai 36 Siswa';
        if (fullscreenBtn) {
            fullscreenBtn.onclick = function() {
                window.openDocPreviewModal('https://docs.google.com/spreadsheets/d/1-YH8PCzHIUv1B8I1dCj_XmcQ2c-jyAavPQfWGHYCUT4/edit?hl=id&gid=1196549737#gid=1196549737', 'Data Rekapitulasi & Analisis Penilaian Siswa');
            };
        }
    } else if (tabName === 'labs') {
        const url = 'https://bimorokusumo.github.io/bimo-manfacturing-labs/';
        if (iframe) {
            iframe.src = url;
            iframe.removeAttribute('data-src');
        }
        if (title) title.innerHTML = '🧪 <strong>Web Labs Interaktif:</strong> Simulator Manufaktur BIMO Manufacturing';
        if (fullscreenBtn) {
            fullscreenBtn.onclick = function() {
                window.openDocPreviewModal(url, 'Web Labs BIMO Manufacturing - Simulator Interaktif');
            };
        }
    }
};

// -------------------------------------------------------------
// Companion RPP Selector Beside Video Logic (3 Materi & Pilihan Video)
// -------------------------------------------------------------
const rppDatabase = {
    produksi: {
        title: 'Teknik Dasar Produksi Manufaktur (Siklus 2 & 3)',
        badge: '⚙️ RPP Siklus 2 & 3',
        url: 'https://drive.google.com/file/d/1ulngK_Fq_GWslrw87j8aES4ksfZbMMNV/preview',
        fullTitle: 'RPP Siklus 2 & 3: Teknik Dasar Produksi Manufaktur (Mesin Bubut Standar, Mesin Bor, & Las SMAW)',
        desc: 'Operasi mesin bubut standar, mesin bor bangku, pengelasan busur manual SMAW, kalkulasi parameter potong (Cutting Speed & RPM), serta aplikasi pengukuran presisi metrologi.',
        relation: 'Keterampilan pengukuran alat ukur presisi pada video di samping merupakan prasyarat teknis langsung (prerequisite) yang diintegrasikan dalam RPP ini untuk memastikan toleransi dimensi benda kerja saat pembubutan.'
    },
    k3lh: {
        title: 'Penerapan K3LH & Budaya Kerja 5R (Siklus 1)',
        badge: '🛡️ RPP Siklus 1',
        url: 'https://drive.google.com/file/d/1Z03qLXSKLj4QveKXVh8s85Tp8hrhOSDg/preview',
        fullTitle: 'RPP Siklus 1: Penerapan K3LH, Bahaya Bengkel, & Budaya Kerja 5R',
        desc: 'Identifikasi bahaya mekanik bengkel mesin, standar APD industri 100%, penanganan darurat APAR, Job Safety Analysis (JSA), dan pembiasaan budaya kerja 5R.',
        relation: 'Menjadi fondasi mutlak keselamatan kerja dan disiplin APD yang tampak diterapkan secara konsisten dalam rekaman video praktik mengajar di bengkel mesin.'
    },
    bahan: {
        title: 'Pengetahuan Bahan Teknik (Siklus 4 & 5)',
        badge: '🔬 RPP Siklus 4 & 5',
        url: 'https://drive.google.com/file/d/1E5vGh3PegvlUHAFJzhNCb4vbTBvDrxSP/preview',
        fullTitle: 'RPP Siklus 4 & 5: Pengetahuan Bahan Teknik (Sifat Fisik, Kimia, Listrik & Mekanik)',
        desc: 'Klasifikasi logam ferro/non-ferro, pengujian sifat fisik, ketahanan korosi kimia, konduktivitas listrik, sifat mekanik (kekerasan, keuletan), serta pemilihan material mesin.',
        relation: 'Menghubungkan karakteristik material yang dibubut dan diukur dalam video dengan analisis sifat mampu mesin (machinability) dan toleransi material teknik.'
    }
};

window.selectRppBesideVideo = function(rppKey, btn) {
    const data = rppDatabase[rppKey];
    if (!data) return;

    const iframe = document.getElementById('companionRppIframe');
    const badge = document.getElementById('companionRppBadge');
    const title = document.getElementById('companionRppTitle');
    const relation = document.getElementById('companionRppRelation');
    const desc = document.getElementById('companionRppDesc');
    const fullscreenBtn = document.getElementById('companionRppFullscreenBtn');
    const bottomModalBtn = document.getElementById('companionRppBottomModalBtn');

    if (iframe) {
        iframe.src = data.url;
        iframe.removeAttribute('data-src');
    }
    if (badge) badge.innerText = data.badge;
    if (title) title.innerText = data.title;
    if (relation) relation.innerText = data.relation;
    if (desc) desc.innerText = data.desc;

    if (fullscreenBtn) {
        fullscreenBtn.onclick = function() {
            window.openDocPreviewModal(data.url, data.fullTitle);
        };
    }
    if (bottomModalBtn) {
        bottomModalBtn.onclick = function() {
            window.openDocPreviewModal(data.url, data.fullTitle);
        };
    }

    // Update tab styling
    document.querySelectorAll('.companion-rpp-tab').forEach(b => {
        b.style.background = 'transparent';
        b.style.color = '#475569';
        b.style.fontWeight = '600';
        b.style.border = '1px solid transparent';
        b.style.boxShadow = 'none';
    });
    const targetBtn = btn || document.querySelector(`.companion-rpp-tab[data-key="${rppKey}"]`);
    if (targetBtn) {
        targetBtn.style.background = '#ffffff';
        targetBtn.style.color = '#0f172a';
        targetBtn.style.fontWeight = '700';
        targetBtn.style.border = '1px solid #10b981';
        targetBtn.style.boxShadow = '0 4px 10px rgba(0,0,0,0.06)';
    }
};

window.scrollAndSelectRpp = function(rppKey) {
    const stage = document.getElementById('ep4-video-rpp');
    if (stage) {
        stage.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    window.selectRppBesideVideo(rppKey);
    if (window.showToast) {
        const names = {
            produksi: 'RPP Teknik Dasar Produksi (Siklus 2 & 3) Dipilih di Samping Video',
            k3lh: 'RPP K3LH & 5R (Siklus 1) Dipilih di Samping Video',
            bahan: 'RPP Pengetahuan Bahan (Siklus 4 & 5) Dipilih di Samping Video'
        };
        window.showToast(names[rppKey] || 'RPP Dipilih');
    }
};
