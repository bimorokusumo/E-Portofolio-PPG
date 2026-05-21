# Append CSS for EP2 Modals and Interactive Accordion
css_content = """
/* EP2 Interactive & Glassmorphism UI */
.ep2-card {
  position: relative;
  background: var(--bg-white);
  border-radius: var(--radius-lg);
  padding: 2rem;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  overflow: hidden;
  z-index: 1;
}
.ep2-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 4px;
  background: linear-gradient(90deg, var(--kemendikbud-cyan), var(--kemendikbud-blue));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s ease;
  z-index: 0;
}
.ep2-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 45, 98, 0.08);
  border-color: rgba(0, 168, 204, 0.3);
}
.ep2-card:hover::before {
  transform: scaleX(1);
}

.ep2-card-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: inline-block;
  color: var(--kemendikbud-blue);
}

.ep2-card-title {
  font-size: 1.25rem;
  color: var(--kemendikbud-blue-dark);
  margin-bottom: 1rem;
  font-weight: 700;
  position: relative;
  z-index: 2;
}

.ep2-card-summary {
  color: var(--text-light);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  position: relative;
  z-index: 2;
}

.btn-ep2-readmore {
  background: transparent;
  color: var(--kemendikbud-blue);
  border: 2px solid var(--kemendikbud-blue);
  padding: 0.5rem 1.2rem;
  border-radius: 50px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  position: relative;
  z-index: 2;
}
.btn-ep2-readmore:hover {
  background: var(--kemendikbud-blue);
  color: white;
  transform: translateX(5px);
}

/* Glassmorphism Modal EP2 */
.ep2-modal-overlay {
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}
.ep2-modal-overlay.active {
  opacity: 1;
  visibility: visible;
}
.ep2-modal-content {
  background: white;
  width: 90%;
  max-width: 700px;
  max-height: 85vh;
  border-radius: 20px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  transform: translateY(30px) scale(0.95);
  opacity: 0;
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
}
.ep2-modal-overlay.active .ep2-modal-content {
  transform: translateY(0) scale(1);
  opacity: 1;
}

.ep2-modal-header {
  padding: 1.5rem 2rem;
  background: linear-gradient(135deg, var(--kemendikbud-blue-dark), var(--kemendikbud-blue));
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.ep2-modal-title {
  margin: 0;
  font-size: 1.4rem;
  font-weight: 600;
  color: white;
  display: flex;
  align-items: center;
  gap: 10px;
}
.ep2-modal-close {
  background: rgba(255,255,255,0.2);
  border: none;
  color: white;
  width: 36px; height: 36px;
  border-radius: 50%;
  font-size: 1.5rem;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.2s ease;
}
.ep2-modal-close:hover {
  background: rgba(255,255,255,0.4);
  transform: rotate(90deg);
}

.ep2-modal-body {
  padding: 2.5rem 2rem;
  overflow-y: auto;
  color: var(--text-dark);
  font-size: 1.05rem;
  line-height: 1.7;
}

/* Interactive Accordion for Filosofi Mengajar */
.ep2-accordion {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.ep2-accordion-item {
  background: white;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all 0.3s ease;
  box-shadow: 0 2px 5px rgba(0,0,0,0.02);
}
.ep2-accordion-item.active {
  border-color: var(--kemendikbud-cyan);
  box-shadow: 0 10px 25px rgba(0, 168, 204, 0.1);
}
.ep2-accordion-header {
  padding: 1.5rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  background: white;
  transition: all 0.3s ease;
}
.ep2-accordion-header:hover {
  background: var(--bg-light-gray);
}
.ep2-accordion-title {
  font-weight: 700;
  font-size: 1.15rem;
  color: var(--kemendikbud-blue-dark);
  display: flex;
  align-items: center;
  gap: 15px;
  margin: 0;
}
.ep2-accordion-icon {
  font-size: 1.5rem;
  color: var(--kemendikbud-cyan);
  transition: transform 0.3s ease;
}
.ep2-accordion-item.active .ep2-accordion-icon {
  transform: rotate(180deg);
  color: var(--kemendikbud-blue);
}
.ep2-accordion-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease-in-out;
  background: #fafafa;
}
.ep2-accordion-content {
  padding: 0 2rem 2rem 2rem;
  color: var(--text-dark);
  line-height: 1.7;
  font-size: 1.05rem;
  text-align: justify;
}
"""
with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)

js_content = """
// EP2 Modal Logic
window.ep2ModalData = {
    's1-1': { title: 'Apa yang Telah Saya Pelajari?', icon: '📚', content: 'Pada Siklus 1, saya belajar esensi mengkondisikan siswa dari budaya SMP menuju budaya industri SMK (orientasi manufaktur). Saya menyusun produk pembelajaran awal yang menitikberatkan pada pengenalan proses produksi, mesin-mesin konvensional, serta menanamkan urgensi K3 (Kesehatan dan Keselamatan Kerja) sebelum mereka benar-benar bekerja di bengkel.' },
    's1-2': { title: 'Pengalaman Menantang & Solusi', icon: '⛰️', content: 'Tantangan utama adalah siswa masih belum terbiasa dengan kedisiplinan dan SOP bengkel, sehingga pengawasan harus ekstra ketat.<br><br>Solusi yang saya rancang dalam produk pembelajaran (LKM) adalah membuat <i>checklist</i> wajib K3 dan menerapkan metode tutor sebaya (<i>peer-tutoring</i>) pada kelompok kecil untuk memastikan setiap siswa saling mengingatkan terkait prosedur aman berpraktik.' },
    's1-3': { title: 'Umpan Balik & Saran Konstruktif', icon: '💡', content: 'Guru Pamong memberikan masukan bahwa alokasi waktu transisi dari penyampaian teori di kelas menuju bengkel masih kurang efisien.<br><br>Sebagai perbaikan, saya disarankan menyertakan materi <i>micro-learning</i> atau apersepsi visual (media animasi) yang singkat agar siswa lebih cepat menangkap instruksi dan sisa waktu praktik menjadi lebih maksimal.' },
    's2-1': { title: 'Apa yang Telah Saya Pelajari?', icon: '⚙️', content: 'Siklus 2 mengajarkan saya cara menerjemahkan konsep fisika abstrak (seperti gaya, torsi, dan rasio roda gigi) menjadi modul ajar yang aplikatif.<br><br>Saya belajar pentingnya <i>scaffolding</i> yang terstruktur agar siswa tidak merasa terintimidasi oleh perhitungan matematis yang krusial bagi seorang teknisi.' },
    's2-2': { title: 'Pengalaman Menantang & Solusi', icon: '🚧', content: 'Tantangannya adalah disparitas kemampuan berhitung siswa yang cukup lebar, membuat sebagian siswa tertinggal dalam analisis rasio transmisi.<br><br>Solusi yang saya lakukan adalah mendiferensiasi instrumen asesmen dan memanfaatkan alat peraga benda nyata (seperti transmisi sepeda motor bekas) di LKM, sehingga perhitungan terasa nyata, tidak hanya di atas kertas.' },
    's2-3': { title: 'Umpan Balik & Saran Konstruktif', icon: '💬', content: 'DPL menyarankan agar produk media pembelajaran tidak hanya berfokus pada presentasi <i>slide</i>, melainkan harus lebih banyak menggunakan instrumen sentuh (<i>hands-on</i>).<br><br>Masukan ini menyadarkan saya bahwa pembelajaran kinestetik adalah inti dari pendidikan kejuruan, dan perbaikan ini akan saya terapkan pada desain LKM Siklus 3 dan PPL Mandiri.' },
    's3-1': { title: 'Apa yang Telah Saya Pelajari?', icon: '🔥', content: 'Pada materi pengelasan SMAW yang berisiko tinggi, saya memelajari krusialnya integrasi antara demonstrasi guru (<i>modeling</i>) dan rubrik penilaian yang sangat detail.<br><br>Perangkat ajar yang saya susun harus mampu memfasilitasi <i>Zone of Proximal Development</i> (ZPD) secara fisik, yaitu membimbing postur tangan siswa agar terbiasa mengendalikan busur las.' },
    's3-2': { title: 'Pengalaman Menantang & Solusi', icon: '🛡️', content: 'Ketakutan psikologis siswa terhadap panas dan percikan api las menghambat mereka memegang elektroda dengan rileks.<br><br>Sebagai solusi, saya merombak strategi RPP dengan menambahkan sesi <i>dry run</i> (mengayunkan elektroda tanpa arus) sebelum mesin dinyalakan, serta memberikan pendampingan <i>hand-over-hand</i> (memandu gerakan tangan siswa secara langsung) saat pertama kali memantik busur.' },
    's3-3': { title: 'Umpan Balik & Saran Konstruktif', icon: '🎯', content: 'Diskusi bersama praktisi dan pamong menekankan pentingnya umpan balik instan.<br><br>Saya disarankan untuk mengevaluasi hasil las siswa setiap satu jalur (<i>bead</i>) selesai, jangan menunggu benda kerja penuh. Umpan balik langsung ini bertujuan agar siswa tidak mengulangi kesalahan gerakan berulang kali. Ini menjadi catatan emas untuk fase mandiri berikutnya.' }
};

window.openEP2Modal = function(id) {
    const data = window.ep2ModalData[id];
    if(!data) return;
    
    document.getElementById('ep2ModalIcon').textContent = data.icon;
    document.getElementById('ep2ModalTitleText').textContent = data.title;
    document.getElementById('ep2ModalBody').innerHTML = data.content;
    
    const overlay = document.getElementById('ep2ModalOverlay');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
};

window.closeEP2Modal = function() {
    const overlay = document.getElementById('ep2ModalOverlay');
    if(overlay) {
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // Modal Overlay click listener
    const overlay = document.getElementById('ep2ModalOverlay');
    if(overlay) {
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) {
                closeEP2Modal();
            }
        });
    }
    
    // Accordion Logic
    const accordionHeaders = document.querySelectorAll('.ep2-accordion-header');
    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const item = this.parentElement;
            const isActive = item.classList.contains('active');
            
            // Close all
            document.querySelectorAll('.ep2-accordion-item').forEach(acc => {
                acc.classList.remove('active');
                acc.querySelector('.ep2-accordion-body').style.maxHeight = null;
            });
            
            // Open clicked if it wasn't active
            if (!isActive) {
                item.classList.add('active');
                const body = item.querySelector('.ep2-accordion-body');
                body.style.maxHeight = body.scrollHeight + "px";
            }
        });
    });
});
"""
with open('script.js', 'a', encoding='utf-8') as f:
    f.write(js_content)
print("CSS and JS appended successfully")
