import re

with open('index.html', 'r') as f:
    html = f.read()

# We want to insert the new cards right after the RPP TFLM 1 card in the gallery-tflm section.
# Let's find the closing div of the RPP card in the TFLM section.
# The RPP TFLM card ends with:
#                         </details>
#                         <a href="..." target="_blank" class="doc-btn">Lihat Dokumen</a>
#                     </div>
#                 </div>

new_cards = """
                <!-- Media TFLM -->
                <div class="doc-card gallery-card-item" data-category="media">
                    <div class="doc-card-thumb">
                        <span class="doc-badge">Media</span>
                        <img src="https://drive.google.com/thumbnail?id=1r731nhtZtBrNWqnU5yFxrolUtw7V1MFj&sz=w600" alt="Media SMAW" class="doc-thumb-img">
                        <a href="https://drive.google.com/file/d/1r731nhtZtBrNWqnU5yFxrolUtw7V1MFj/view?usp=sharing" target="_blank" class="doc-overlay-btn">📄 Buka PDF di Drive</a>
                    </div>
                    <div class="doc-card-content">
                        <h4>Media Pembelajaran tentang Pengelasan Dasar SMAW</h4>
                        <p>Dokumen presentasi atau media pendukung materi pengelasan dasar SMAW.</p>
                        
                        <details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                            <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                            <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                                <div><strong>Kendala proses penyusunan perangkat:</strong> <br><span style="color: var(--text-light);">Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).</span></div>
                                <div><strong>Teori konsep pedagogi:</strong> <br><span style="color: var(--text-light);">Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).</span></div>
                                <div><strong>Faktor keberhasilan:</strong> <br><span style="color: var(--text-light);">Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.</span></div>
                                <div><strong>Perubahan komponen penunjang kelas:</strong> <br><span style="color: var(--text-light);">Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.</span></div>
                            </div>
                        </details>
                        <a href="https://drive.google.com/file/d/1r731nhtZtBrNWqnU5yFxrolUtw7V1MFj/view?usp=sharing" target="_blank" class="doc-btn">Lihat Dokumen</a>
                    </div>
                </div>

                <!-- Bahan Ajar TFLM -->
                <div class="doc-card gallery-card-item" data-category="bahan-ajar">
                    <div class="doc-card-thumb">
                        <span class="doc-badge">Bahan Ajar</span>
                        <img src="https://drive.google.com/thumbnail?id=1uAAiLfUJuPvRXwSSajwhgBctBgL5lhM_&sz=w600" alt="Bahan Ajar SMAW" class="doc-thumb-img">
                        <a href="https://docs.google.com/document/d/1uAAiLfUJuPvRXwSSajwhgBctBgL5lhM_/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-overlay-btn">📄 Buka Dokumen</a>
                    </div>
                    <div class="doc-card-content">
                        <h4>Bahan Ajar tentang Pengelasan Dasar SMAW</h4>
                        <p>Materi pembelajaran komprehensif untuk pengelasan dasar SMAW.</p>
                        
                        <details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                            <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                            <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                                <div><strong>Kendala proses penyusunan perangkat:</strong> <br><span style="color: var(--text-light);">Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).</span></div>
                                <div><strong>Teori konsep pedagogi:</strong> <br><span style="color: var(--text-light);">Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).</span></div>
                                <div><strong>Faktor keberhasilan:</strong> <br><span style="color: var(--text-light);">Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.</span></div>
                                <div><strong>Perubahan komponen penunjang kelas:</strong> <br><span style="color: var(--text-light);">Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.</span></div>
                            </div>
                        </details>
                        <a href="https://docs.google.com/document/d/1uAAiLfUJuPvRXwSSajwhgBctBgL5lhM_/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-btn">Lihat Dokumen</a>
                    </div>
                </div>

                <!-- LKS 1 TFLM -->
                <div class="doc-card gallery-card-item" data-category="lks">
                    <div class="doc-card-thumb">
                        <span class="doc-badge">LKS & Asesmen</span>
                        <img src="https://drive.google.com/thumbnail?id=1gEA5b2XoDz2c5A4Uey9pucKQDNVs7TZH&sz=w600" alt="LKS 1" class="doc-thumb-img">
                        <a href="https://docs.google.com/document/d/1gEA5b2XoDz2c5A4Uey9pucKQDNVs7TZH/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-overlay-btn">📄 Buka Dokumen</a>
                    </div>
                    <div class="doc-card-content">
                        <h4>Spesifikasi Mesin Las SMAW</h4>
                        <p>Lembar Kerja Siswa dan Asesmen mengenai identifikasi dan spesifikasi mesin las SMAW.</p>
                        
                        <details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                            <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                            <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                                <div><strong>Kendala proses penyusunan perangkat:</strong> <br><span style="color: var(--text-light);">Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).</span></div>
                                <div><strong>Teori konsep pedagogi:</strong> <br><span style="color: var(--text-light);">Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).</span></div>
                                <div><strong>Faktor keberhasilan:</strong> <br><span style="color: var(--text-light);">Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.</span></div>
                                <div><strong>Perubahan komponen penunjang kelas:</strong> <br><span style="color: var(--text-light);">Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.</span></div>
                            </div>
                        </details>
                        <a href="https://docs.google.com/document/d/1gEA5b2XoDz2c5A4Uey9pucKQDNVs7TZH/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-btn">Lihat Dokumen</a>
                    </div>
                </div>

                <!-- LKS 2 TFLM -->
                <div class="doc-card gallery-card-item" data-category="lks">
                    <div class="doc-card-thumb">
                        <span class="doc-badge">LKS & Asesmen</span>
                        <img src="https://drive.google.com/thumbnail?id=1G3xuiTzwjI3eXhgHU2V2avBdMjrOMWQY&sz=w600" alt="LKS 2" class="doc-thumb-img">
                        <a href="https://docs.google.com/document/d/1G3xuiTzwjI3eXhgHU2V2avBdMjrOMWQY/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-overlay-btn">📄 Buka Dokumen</a>
                    </div>
                    <div class="doc-card-content">
                        <h4>Penyiapan Mesin dan Bahan Pengelasan SMAW</h4>
                        <p>Langkah-langkah persiapan sebelum melakukan praktik pengelasan SMAW.</p>
                        
                        <details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                            <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                            <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                                <div><strong>Kendala proses penyusunan perangkat:</strong> <br><span style="color: var(--text-light);">Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).</span></div>
                                <div><strong>Teori konsep pedagogi:</strong> <br><span style="color: var(--text-light);">Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).</span></div>
                                <div><strong>Faktor keberhasilan:</strong> <br><span style="color: var(--text-light);">Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.</span></div>
                                <div><strong>Perubahan komponen penunjang kelas:</strong> <br><span style="color: var(--text-light);">Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.</span></div>
                            </div>
                        </details>
                        <a href="https://docs.google.com/document/d/1G3xuiTzwjI3eXhgHU2V2avBdMjrOMWQY/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-btn">Lihat Dokumen</a>
                    </div>
                </div>

                <!-- LKS 3 TFLM -->
                <div class="doc-card gallery-card-item" data-category="lks">
                    <div class="doc-card-thumb">
                        <span class="doc-badge">LKS & Asesmen</span>
                        <img src="https://drive.google.com/thumbnail?id=15zqoi3EkXyvWifbOys-01TyFhbKItFl-&sz=w600" alt="LKS 3" class="doc-thumb-img">
                        <a href="https://docs.google.com/document/d/15zqoi3EkXyvWifbOys-01TyFhbKItFl-/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-overlay-btn">📄 Buka Dokumen</a>
                    </div>
                    <div class="doc-card-content">
                        <h4>Identifikasi Elektroda</h4>
                        <p>Pengenalan jenis, fungsi, dan klasifikasi elektroda pada pengelasan.</p>
                        
                        <details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                            <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                            <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                                <div><strong>Kendala proses penyusunan perangkat:</strong> <br><span style="color: var(--text-light);">Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).</span></div>
                                <div><strong>Teori konsep pedagogi:</strong> <br><span style="color: var(--text-light);">Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).</span></div>
                                <div><strong>Faktor keberhasilan:</strong> <br><span style="color: var(--text-light);">Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.</span></div>
                                <div><strong>Perubahan komponen penunjang kelas:</strong> <br><span style="color: var(--text-light);">Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.</span></div>
                            </div>
                        </details>
                        <a href="https://docs.google.com/document/d/15zqoi3EkXyvWifbOys-01TyFhbKItFl-/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-btn">Lihat Dokumen</a>
                    </div>
                </div>

                <!-- LKS 4 TFLM -->
                <div class="doc-card gallery-card-item" data-category="lks">
                    <div class="doc-card-thumb">
                        <span class="doc-badge">LKS & Asesmen</span>
                        <img src="https://drive.google.com/thumbnail?id=1WgeMX1TaJ7yi2cVbqCiQWJLQVLP9uISU&sz=w600" alt="LKS 4" class="doc-thumb-img">
                        <a href="https://docs.google.com/document/d/1WgeMX1TaJ7yi2cVbqCiQWJLQVLP9uISU/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-overlay-btn">📄 Buka Dokumen</a>
                    </div>
                    <div class="doc-card-content">
                        <h4>Posisi Pengelasan</h4>
                        <p>Pemahaman mengenai berbagai posisi standar dalam pengelasan SMAW.</p>
                        
                        <details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                            <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                            <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                                <div><strong>Kendala proses penyusunan perangkat:</strong> <br><span style="color: var(--text-light);">Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).</span></div>
                                <div><strong>Teori konsep pedagogi:</strong> <br><span style="color: var(--text-light);">Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).</span></div>
                                <div><strong>Faktor keberhasilan:</strong> <br><span style="color: var(--text-light);">Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.</span></div>
                                <div><strong>Perubahan komponen penunjang kelas:</strong> <br><span style="color: var(--text-light);">Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.</span></div>
                            </div>
                        </details>
                        <a href="https://docs.google.com/document/d/1WgeMX1TaJ7yi2cVbqCiQWJLQVLP9uISU/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-btn">Lihat Dokumen</a>
                    </div>
                </div>

                <!-- LKS 5 TFLM -->
                <div class="doc-card gallery-card-item" data-category="lks">
                    <div class="doc-card-thumb">
                        <span class="doc-badge">LKS & Asesmen</span>
                        <img src="https://drive.google.com/thumbnail?id=16FR7AYhJ0bw_Ngl5NctYlEHZReAA-PfL&sz=w600" alt="LKS 5" class="doc-thumb-img">
                        <a href="https://docs.google.com/document/d/16FR7AYhJ0bw_Ngl5NctYlEHZReAA-PfL/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-overlay-btn">📄 Buka Dokumen</a>
                    </div>
                    <div class="doc-card-content">
                        <h4>Pemeriksaan Hasil Las (Visual)</h4>
                        <p>Prosedur asesmen untuk mengevaluasi kualitas jalur dan cacat las secara visual.</p>
                        
                        <details style="margin: 1rem 0; font-size: 0.9rem; text-align: left; background: var(--bg-white); border: 1px solid var(--border-color); padding: 0.8rem; border-radius: 8px;">
                            <summary style="cursor: pointer; font-weight: 600; color: var(--kemendikbud-blue); outline: none;">📝 Analisis Artefak</summary>
                            <div style="padding-top: 0.8rem; display: flex; flex-direction: column; gap: 0.5rem; color: var(--text-dark);">
                                <div><strong>Kendala proses penyusunan perangkat:</strong> <br><span style="color: var(--text-light);">Tantangan utama yang dihadapi dalam proses penyusunan perangkat pembelajaran ini adalah menyelaraskan tingkat kesulitan materi vokasi yang diajarkan dengan heterogenitas kemampuan kognitif dan psikomotorik awal peserta didik. Selain itu, terdapat keterbatasan waktu yang signifikan dalam merancang instrumen asesmen dan lembar kerja yang benar-benar autentik, komprehensif, serta mampu secara presisi mengukur ketercapaian kompetensi riil yang sepenuhnya relevan dengan tuntutan dan standar operasional di dunia kerja industri (DUDI).</span></div>
                                <div><strong>Teori konsep pedagogi:</strong> <br><span style="color: var(--text-light);">Pengembangan perangkat pembelajaran ini secara konsisten mengintegrasikan pendekatan Understanding by Design (UbD) yang berfokus pada hasil akhir pembelajaran. Pendekatan ini dikombinasikan dengan sintaks dari model Inquiry Learning yang membuat siswa lebih difasilitasi dengan guru menjadi pamong. Kolaborasi konsep pedagogi ini bertujuan untuk membangun scaffolding yang kuat, membimbing siswa secara sistematis dari tahap pemahaman konsep dasar menuju tahap eksperimen dan praktik bengkel yang terstruktur, bermakna, serta mampu mengasah kemampuan berpikir tingkat tinggi (HOTS).</span></div>
                                <div><strong>Faktor keberhasilan:</strong> <br><span style="color: var(--text-light);">Faktor kunci yang berkontribusi terhadap keberhasilan proses pembelajaran ini adalah tingginya tingkat antusiasme dan partisipasi aktif peserta didik, khususnya ketika mereka dihadapkan pada media pembelajaran visual interaktif dan demonstrasi praktik secara langsung. Dukungan ketersediaan alat, bahan, dan fasilitas bengkel mekanik yang memadai juga sangat menentukan kelancaran simulasi, memungkinkan peserta didik mempraktikkan teori yang didapat secara langsung dalam kondisi yang aman, kondusif, dan merepresentasikan lingkungan kerja nyata.</span></div>
                                <div><strong>Perubahan komponen penunjang kelas:</strong> <br><span style="color: var(--text-light);">Berdasarkan evaluasi formatif selama siklus pembelajaran, dilakukan beberapa penyesuaian esensial pada komponen penunjang. Perubahan utama mencakup penyempurnaan rancangan Lembar Kerja Peserta Didik (LKPD) agar instruksi langkah kerjanya menjadi lebih sistematis, rinci, dan sesuai dengan Standar Operasional Prosedur (SOP). Selain itu, dilakukan pengayaan variasi media pembelajaran, seperti penggunaan video demonstrasi praktik alat perkakas dan materi keselamatan kerja, yang secara khusus ditujukan untuk memperkuat fondasi pemahaman siswa pada mata pelajaran Dasar-Dasar Kejuruan (DDK) serta mengakomodasi gaya belajar yang beragam.</span></div>
                            </div>
                        </details>
                        <a href="https://docs.google.com/document/d/16FR7AYhJ0bw_Ngl5NctYlEHZReAA-PfL/edit?usp=sharing&ouid=114957738313413873346&rtpof=true&sd=true" target="_blank" class="doc-btn">Lihat Dokumen</a>
                    </div>
                </div>"""

# Find the insertion point:
# End of RPP card in TFLM gallery:
target = r"""                        <a href="https://drive.google.com/file/d/1xBHUuzC9I2kDbD7liKjG90Gk7j5e967G/view\?usp=sharing" target="_blank" class="doc-btn">Lihat Dokumen</a>
                    </div>
                </div>"""

# Append the new cards right after the target.
html = re.sub(target, target.replace("\\?", "?") + "\n" + new_cards, html, count=1)

with open('index.html', 'w') as f:
    f.write(html)

