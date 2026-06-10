# Panduan Pengguna: Translate Advanced untuk NVDA

<h2 id="index">Index</h2>

- [1 - Pendahuluan](#pengantar)
- [1.1 - Persyaratan](#persyaratan)
- [1.2 - Batasan dan peringatan](#batasan-dan-peringatan)
- [1.3 - Informasi penulis](#informasi-penulis)
- [2 - Deskripsi dan konfigurasi](#deskripsi-konfigurasi)
- [2.1 - Deskripsi modul](#deskripsi-modul)
    - [Google](#google)
    - [DeepL](#deepl)
    - [LibreTranslate](#libretranslate)
    - [Microsoft Translate](#microsoft-translate)
- [2.2 - Konfigurasi](#konfigurasi)
    - [Addon Menu](#addon-menu)
    - [Addon Hotkeys](#addon-hotkeys)
- [3 - Pemecahan Masalah](#pemecahan masalah)
- [Masalah-Umum dan Solusinya](#masalah-dan-solusi-umum)
- [Cara Mengkonsultasikan Log NVDA](#cara-mengkonsultasikan-log-nvda)
- [4 - Ucapan Terima Kasih](#ucapan terima kasih)
- [Penerjemah](#penerjemah)
- [5 - Log Perubahan Versi](#log perubahan versi)
- [Versi 1.0](#versi-1-0)
- [Versi 2024.06.16](#versi-2024-06-16)
- [Versi 23-06-2024](#versi-23-06-2024)
- [Versi 2024.09.07](#versi-09-2024-07)

<h2 id="introduction">1 - Introduction</h2>

**Translate Advanced untuk NVDA** adalah add-on yang memungkinkan Anda menerjemahkan teks menggunakan berbagai layanan terjemahan online, seperti Google Translate, DeepL, LibreTranslate, dan Microsoft Translator. Addon ini menawarkan fitur-fitur canggih seperti terjemahan waktu nyata, riwayat terjemahan, terjemahan teks yang dipilih, dukungan untuk berbagai bahasa, dan banyak lagi.

[Kembali ke indeks](#index)

<h3 id="requirements">1.1 - Requirements</h3>

- NVDA (Akses Desktop NonVisual) 2024.1 atau lebih tinggi
- Koneksi internet

[Kembali ke indeks](#index)

<h3 id="limitations-and-warnings">1.2 - Limitations and warnings</h3>

Addon mengirimkan informasi melalui Internet ke setiap layanan untuk melakukan terjemahan waktu nyata. Penting untuk dicatat bahwa informasi yang diterjemahkan mungkin mencakup data rahasia dan sensitif. Penggunaan plugin adalah tanggung jawab pengguna, yang harus mengevaluasi sifat informasi yang dikirim. Pengembang plugin tidak bertanggung jawab atas data yang dikirim ke layanan yang digunakan plugin.

Sebagai pengembang, saya menolak semua tanggung jawab atas segala kemungkinan yang mungkin timbul akibat penggunaan plugin. Tanggung jawab penuh terletak pada pengguna.

Selain itu, plugin memerlukan koneksi Internet agar dapat berfungsi. Kecepatan respon plugin bergantung pada beberapa faktor, seperti:
- Kualitas koneksi Internet Anda.
- Kemungkinan penundaan (lag) dari layanan terjemahan yang digunakan.
- Faktor yang berhubungan dengan infrastruktur jaringan pengguna.

Disarankan agar pengguna menyadari aspek-aspek ini dan melakukan pengujian yang diperlukan untuk memastikan bahwa plugin memenuhi harapan dan persyaratan keamanan mereka.[Kembali ke indeks](#index)

<h3 id="author-information">1.3 - Author information</h3>

**Informasi Teknis dan Tindakan Keamanan Addon untuk NVDA**

Saya telah bekerja keras untuk membuat plugin sekuat mungkin, memperhitungkan dan menangani potensi bug. Semua kesalahan ditangkap dan dicatat dalam log NVDA, sehingga memudahkan pelacakan dan penyelesaian masalah dengan cepat.

**Masalah dengan Sertifikat Windows**

Baru-baru ini, saya memperhatikan bahwa penginstalan baru Windows dapat mengalami masalah dengan sertifikat, yang dapat membuat frustasi. Untuk alasan ini, saya telah melakukan pemeriksaan saat addon dimulai. Jika kegagalan terkait sertifikat terdeteksi, addon akan secara otomatis membuat ulang sertifikat tersebut, memastikan pengoperasian Windows dan addon itu sendiri dengan benar.

**Langkah-langkah keamanan**

Addon ini mencakup beberapa langkah keamanan:
- Tidak diperbolehkan berjalan di layar aman.
- Itu tidak dimulai jika koneksi Internet tidak terdeteksi.

Terkadang NVDA dapat memulai lebih cepat daripada koneksi jaringan wi-fi. Dalam kasus seperti ini, NVDA perlu di-restart setelah koneksi dibuat agar dapat menggunakan add-on dengan benar.

**Manajemen Kunci API**

Addon ini menghasilkan file JSON yang menyimpan kunci API yang diperlukan untuk layanan yang memerlukannya. File ini, bernama `apis.json`, terletak di folder pengguna Windows.

**Pertimbangan File Utama**

Telah diputuskan untuk menyimpan file ini di luar folder addon, karena berisi informasi sensitif.  Hal ini untuk mencegah informasi ini dibagikan secara tidak sengaja dengan salinan portabel NVDA atau dalam situasi lainnya. Jika pengguna memutuskan untuk berhenti menggunakan addon, mereka harus menghapus file ini secara manual.

Langkah-langkah ini memastikan pengelolaan dan keamanan add-on yang lebih baik, memfasilitasi penggunaan dan pemeliharaannya.

[Kembali ke indeks](#index)

<h2 id="description-configuration">2 - Description and configuration</h2>

<h3 id="description-modules">2.1 - Description of modules</h3>

Pada versi pertamanya, plugin ini menawarkan 7 modul terjemahan:

<h4 id="google">Google</h4>

**4 Google Modul**

- **2 Modul Pengikisan Web:** Setiap modul menjalankan fungsi yang sama, namun dengan cara yang berbeda, memastikan bahwa selalu ada alternatif yang tersedia jika salah satu modul gagal.
- **2 Modul melalui API:** Modul ini juga tidak terbatas dan gratis, namun penyalahgunaannya dapat mengakibatkan larangan IP sementara selama beberapa jam, setelah itu modul akan tersedia kembali.
- Semua modul Google ini tidak memerlukan kunci API dan tidak terbatas serta gratis.

<h4 id="deepl">DeepL</h4>

**2 Modul DeepL**

- **API Gratis:** Opsi ini memerlukan perolehan kunci API Gratis dari halaman DeepL, yang menawarkan 500.000 karakter per bulan.
- **Pro API:** Opsi ini juga memerlukan kunci API yang diperoleh dari situs web DeepL. Penggunaannya bergantung pada saldo dan paket kontrak akun DeepL pengguna.
- Ketentuan penggunaan DeepL API dapat ditemukan di [situs web] (https://www.deepl.com/en/pro/change-plan#developer), dan addon dibatasi oleh ketentuan ini.

<h4 id="libretranslate">LibreTranslate</h4>

**1 Modul LibreTranslate**

- Layanan ini terus ditingkatkan berkat pembelajaran saraf yang berkelanjutan. Meskipun saat ini tidak mencapai kualitas Google, namun dapat digunakan dengan sempurna.
- Berdasarkan teknologi Argos Translate.
- Untuk menggunakan modul ini diperlukan kunci API, yang dapat diperoleh dengan memberikan donasi ke komunitas [NVDA.es](https://nvda.es/donaciones/).
- Setelah berdonasi, Anda dapat meminta kunci API menggunakan formulir di [halaman] berikut(https://nvda.es/contacto/), dengan menunjukkan subjek "solicitud de clave API" dan memberikan referensi PayPal, transfer, dll.
- Selain itu, dimungkinkan untuk mengonfigurasi layanan LibreTranslate lainnya dengan menambahkan kunci API dan mengubah URL layanan di bagian konfigurasi addon.

<h4 id="microsoft-translate">Microsoft Translate</h4>

**1 Modul Terjemahan Microsoft**

- Modul ini memiliki batasan bahwa penggunaan terus menerus dapat mengakibatkan larangan IP sementara selama beberapa menit.
- Larangan ini hanya terjadi pada penggunaan yang sangat intensif dan pada terjemahan teks yang panjang.
- Layanan berfungsi dengan sangat baik, namun disarankan untuk tidak menggunakannya terus menerus untuk menghindari gangguan.

Opsi ini memungkinkan pengguna untuk memilih di antara berbagai modul terjemahan, memastikan ketersediaan dan fleksibilitas add-on berdasarkan kebutuhan dan preferensi individu.

Saat addon menerima pembaruan, layanan dapat ditambahkan atau dihapus. Perubahan akan dilaporkan di bagian pembaruan.

[Kembali ke indeks](#index)

<h3 id="configuration">2.2 - Configuration</h3>

**Pengaturan Tambahan**

Bagian ini merinci cara mengonfigurasi setiap modul yang tersedia di addon, termasuk cara menambahkan kunci API, mengubah URL layanan, dan pengaturan lain yang diperlukan untuk menyesuaikan penggunaan addon dengan kebutuhan pengguna.

<h4 id="plugin-menu">Addon menu</h4>

Di NVDA > Preferences > Advanced Translator terdapat menu yang berisi hal berikut:

- **Konfigurasi Translate Advanced**

Jika Anda mengklik opsi ini, jendela konfigurasi addon akan terbuka. Jendela ini memiliki 2 bagian:

- **Umum**

    In this tab, the general options of the addon are shown. Currently there is only one checkbox to turn the addon cache on or off.

    The addon can save a cache of the translations for each application, which will make the translation easier and faster for future translations. In addition, it now creates a cache for each language, and there may be more than one application that has a cache for different languages.

- **Modul terjemahan**

    In this tab you can choose the service you want to use to translate. For those services that require an API key, the API key manager will also be shown.

    You can have more than one API key for the same service; For example, in LibreTranslate you can have different keys and URLs to connect. You can add, edit, delete and set the default API key that you want for the current service.

    The API key management section changes depending on the service you have selected. You can give each API key an identifying name to quickly know which API you are referring to. When you have more than one API key for a service, the item that has an asterisk in the list will be the default one. This can be changed with the "Default" button, making the key defined for the service the key you have focused on at that moment.

    If the translation service you choose does not require an API key, the API manager will not be displayed.

    Then you have the "OK" and "Cancel" buttons. All options have a shortcut key that NVDA will inform you about.

- **Dokumentasi Tambahan**

Jika Anda mengklik "Dokumentasi Plugin", dokumentasi ini akan terbuka.

- **Sumbangkan kopi jika Anda menyukai pekerjaan saya**

Jika Anda menekan opsi ini, halaman PayPal akan terbuka di mana terdapat link bertuliskan "Kirim". Jika Anda mengklik link ini, Anda akan diminta untuk masuk ke akun Anda dan meninggalkan Anda di halaman donasi.

Saya hanya akan mengatakan bahwa saya minum banyak kopi saat membuat addon ini.

[Kembali ke indeks](#index)

<h4 id="addon-hotkeys">Addon-hotkeys</h4>

Di NVDA > Preferences > Input Gestures... > Advanced Translator terdapat tombol berikut yang dapat Anda konfigurasi.

Kunci default tidak ditetapkan sehingga pengguna dapat memilih tata letak terbaik untuknya. Mereka adalah sebagai berikut:

- **Membuka konfigurasi addon**

Ini akan dengan cepat membuka konfigurasi plugin.

- **Mengaktifkan atau menonaktifkan cache terjemahan**

Ini akan mengaktifkan atau menonaktifkan cache tanpa harus masuk ke konfigurasi.

- **Aktifkan atau nonaktifkan terjemahan online waktu nyata**

Ini mengaktifkan atau menonaktifkan terjemahan waktu nyata. Ini adalah fungsi utama yang akan mulai diterjemahkan saat Anda menggerakkan panah kursor. Jika semuanya benar, Anda akan mendengar terjemahannya; Jika Anda mendengar teks aslinya, Anda harus melihat log NVDA dan melihat apa yang terjadi.

- **Ubah modul terjemahan**

Ini akan membuka jendela dengan semua modul terjemahan yang tersedia. Anda dapat berpindah dengan panah dan memilih dengan "Enter". Modul yang Anda pilih akan menjadi modul yang Anda miliki secara default.

- **Ubah bahasa target**

Ini akan membuka jendela dengan bahasa target yang tersedia dalam modul yang telah kita pilih. Setiap layanan memiliki bahasa yang berbeda, dan, misalnya, jika Anda menerjemahkan teks dalam bahasa Rusia dan ingin mendengarnya dalam bahasa Inggris, dalam dialog ini Anda harus memilih Bahasa Inggris. Anda menelusuri dialog dengan panah kursor dan "Enter" untuk memilih bahasa yang Anda inginkan.

- **Ubah bahasa sumber**

Mirip dengan fungsi sebelumnya, namun dialog ini hanya tersedia untuk penerjemah Microsoft. Layanan Microsoft tidak mengizinkan Anda menyetel bahasa sumber sebagai otomatis sehingga dapat mendeteksi bahasa mana yang dikirimkan kepada Anda, jadi Anda harus memilihnya sendiri.

Layanan lainnya tidak akan dapat menggunakan dialog ini karena opsi defaultnya adalah mendeteksi bahasa yang dikirim.

- **Salin teks yang terakhir diterjemahkan ke papan klip**

Ini akan menyalin teks terakhir yang telah diterjemahkan ke clipboard.

- **Hapus cache terjemahan untuk aplikasi yang saat ini difokuskan**

Jika kita menekannya sekali, ini akan memberi kita informasi; Jika kita menekannya dua kali dengan cepat, itu akan menghapus cache untuk aplikasi yang saat ini fokus dan akan memberi tahu kita hasilnya.

- **Hapus semua terjemahan cache untuk semua aplikasi**

Jika ini ditekan sekali, ini akan memberi kita informasi; Ditekan dua kali dengan cepat, ini akan menghapus seluruh cache plugin, juga menawarkan informasi.

- **Menampilkan riwayat terjemahan**

Ini akan menampilkan dialog dengan 500 terjemahan terakhir dalam daftar. Anda dapat mencari dan meninjau teks sumber dan teks terjemahan dalam kotak baca-saja. Dialog ini memungkinkan Anda mencari seluruh riwayat, menyalin teks sumber dan teks terjemahan ke clipboard, atau keduanya.

Ini juga memungkinkan Anda untuk beralih antara teks sumber dan teks terjemahan dan bekerja dengan cara apa pun. Selain itu, Anda dapat menghapus semua riwayat untuk memulai dari awal.

Perhatikan bahwa riwayat dihapus setiap kali NVDA dimulai ulang.

- **Terjemahkan teks yang dipilih**

Tindakan ini akan menerjemahkan teks yang telah Anda pilih dan fokuskan. Jika teksnya besar, dialog akan terbuka dengan persentase terjemahan. Dialog tersebut dapat dibatalkan, yang juga akan membatalkan terjemahannya.

Setelah terjemahan selesai, teks akan ditampilkan dalam dialog sehingga Anda dapat menjelajahinya.

Opsi ini menggunakan layanan Google Terjemahan dan layanan ini tidak dapat diubah, dipilih secara internal karena layanan ini memberikan hasil terbaik untuk teks panjang.

[Kembali ke indeks](#index)

<h2 id="troubleshooting">3 - Troubleshooting</h2>

<h3 id="common-problems-and-solutions">Common Problems and Solutions</h3>

**koneksi internet**
- Periksa apakah koneksi Internet Anda aktif dan berfungsi dengan baik.
- Mulai ulang router atau modem Anda jika perlu.

**Kesalahan Sertifikat**
- Jika Anda mengalami kesalahan sertifikat, pastikan tanggal dan waktu sistem Anda sudah benar.
- Verifikasi bahwa sertifikat yang diperlukan telah diinstal dan diperbarui.

**Masalah Kinerja**
- Pastikan komputer Anda memenuhi persyaratan sistem minimum.
- Tutup aplikasi lain yang mungkin menghabiskan banyak sumber daya.

[Kembali ke indeks](#index)

<h3 id="how-to-consult-the-nvda-log">How to Consult the NVDA Log</h3>

1. Buka NVDA.
2. Buka `NVDA > Alat > Lihat Log`.
3. Di jendela log, cari kesalahan atau pesan apa pun yang terkait dengan Translate Advanced.

[Kembali ke indeks](#index)

<h2 id="acknowledgments">4 - Acknowledgments</h2>

Terima kasih kepada semua programmer NVDA atas kerja luar biasa mereka.

Dan saya tidak ingin gagal untuk mengatakan bahwa awal mula plugin ini berasal dari plugin Yannick PLASSIARD (TRANSLATE), dari mana saya telah mempelajari dan menggunakan beberapa fungsi.

Terima kasih juga kepada Alexy Sadovoy alias Lex, ruslan, beqa, Mesar Hameed, Alberto Buffolino, dan kontributor NVDA lainnya untuk plugin Terjemahan Instan yang merupakan salah satu metode untuk Google diperoleh dan dimodifikasi untuk diterapkan di Translate Advanced.

Plugin ini merupakan hasil kerja beberapa tahun dalam merilis versi tidak resmi dan studi penggunaan terjemahan offline.

Addon ini merupakan hasil pembelajaran ini, mengingat kedepannya akan menghadirkan fitur-fitur baru yang mengejutkan.

[Kembali ke indeks](#index)
<h3 id="translators">Translators</h3>

- **Portugis:** Ângelo Abrantes.
- **Turki:** Umut Korkmaz.
- **Bahasa Rusia:** Valentin Kupriyanov.
- **Bahasa Inggris:** Samuel Proulx.
- **Orang Ukraina:** Heorhii Halas dan Volodymyr Pyrih.

[Kembali ke indeks](#index)

<h2 id="version-changelog">5 - changelog</h2>

Di bagian ini akan ditambahkan changelog, di mana fitur-fitur baru dari setiap versi akan diposting.

Panduan ini didasarkan pada versi pertama sehingga tidak akan diperbarui sebagai dasar.

Berita akan ditambahkan di bagian ini.

[Kembali ke indeks](#index)

<h3 id="version-2026-06-10">Version 2026.06.10</h3>

- Improved support for NVDA version 2026.1 with Python 64-bit architecture
- Fixed all detected bugs from the previous version
- Added Indonesian (id) translation

<h3 id="version-1-0">Version 2024.06.06</h3>

- Rilis awal plugin.
- Dukungan untuk 7 layanan terjemahan.
- Fungsi dasar terjemahan waktu nyata dan manajemen kunci API.

<h3 id="version-2024-06-16">Version 2024.06.16</h3>

- **Tambahkan kemampuan untuk menyalin terjemahan teks yang dipilih ke clipboard alih-alih menampilkannya dalam dialog:**

Opsi telah ditambahkan untuk secara otomatis menyalin teks terjemahan ke clipboard ketika fungsi ini dipilih, sehingga tidak perlu menampilkan kotak dialog tambahan.

Opsi ini ditambahkan dalam dialog konfigurasi plugin secara Umum.

Jika opsi ini dicentang, dialog tidak akan lagi ditampilkan saat Anda menerjemahkan teks yang dipilih, melainkan akan langsung menyalinnya ke clipboard.

- **Terjemahkan apa pun yang ada di clipboard:**

Sekarang dimungkinkan untuk langsung menerjemahkan konten yang terletak di clipboard, menyediakan cara yang cepat dan efisien untuk menerjemahkan teks yang disalin.

Jika tidak ada yang diterjemahkan, ia akan memberi tahu Anda apa yang ada di papan klip atau jika tidak ada apa pun di papan klip, ia akan memberi tahu Anda melalui pesan.

- **Terjemahkan hal terakhir yang diucapkan oleh synthesizer:**

Sebuah fungsi telah ditambahkan yang memungkinkan Anda menerjemahkan frasa atau teks terakhir yang diucapkan oleh penyintesis suara, meningkatkan aksesibilitas dan kegunaan addon.

Jika hal terakhir yang diucapkan tidak dapat diterjemahkan, ini akan memberi tahu Anda hal terakhir yang diucapkan dalam bahasa sumber.

- **Tampilkan terjemahan dalam Braille:**

Versi baru ini mencakup dukungan untuk menampilkan terjemahan pada perangkat tampilan Braille, sehingga terjemahan lebih mudah diakses.

Ini hanya akan berfungsi pada perangkat yang memiliki tampilan Braille yang dikonfigurasi.

Fungsi ini sedang dalam tahap pengujian.

- **Pembaru bahasa plugin:**

Pembaru telah diterapkan untuk menjaga bahasa plugin selalu terbarui, memastikan ketersediaan bahasa terbaru dan akurat.

Sekarang di menu NVDA > Preferensi > Translate Advanced

Anda akan memiliki item baru bernama Perbarui bahasa plugin (Tidak ada pembaruan).

Item ini akan memberi tahu Anda jika ada pembaruan, misalnya:

Perbarui bahasa plugin (tersedia 3 pembaruan)

Jika Anda menekannya, dialog akan muncul dengan bahasa baru, dengan pembaruan bahasa yang ada, atau dengan keduanya.

Anda dapat menginstal atau melewati.

Jika Anda mengklik instal, bahasa akan diunduh dan diinstal dan NVDA akan dimulai ulang.

Item menu diperbarui setiap 30 menit untuk memeriksa pembaruan atau setiap restart.

Biaya data untuk pengecekan ini kecil karena untuk tempat-tempat yang bermasalah datanya kurang dari 1kb yang harus dicek.

Pembaru ini akan mempermudah berbagi pembaruan bahasa untuk addon dengan pengguna secepat mereka tiba dan tanpa perlu merilis versi baru dengan bahasa baru.

Setiap versi baru dari add-on akan hadir dengan semua bahasa baru dan terbaru yang telah hadir.

- **Bug membaca berkelanjutan diperbaiki:**

Memperbaiki masalah yang menyebabkan kesalahan pembacaan terus-menerus, meningkatkan stabilitas dan kinerja addon selama penggunaan jangka panjang.

- **Catatan Penulis:**

Semua fungsi baru seperti menerjemahkan clipboard, menerjemahkan kata-kata terakhir yang diucapkan oleh synthesizer, atau memeriksa pembaruan bahasa, dapat ditetapkan dengan isyarat.

Saya menyarankan jika Anda tidak akan menggunakan opsi apa pun, Anda tidak menambahkan isyarat masukan sehingga Anda bisa mendapatkannya gratis untuk add-on lainnya. Hanya tambahkan yang berguna bagi Anda.

Saat fitur ditambahkan, lebih banyak isyarat akan diperlukan dan suatu fitur mungkin tidak berfungsi untuk satu orang atau mungkin berfungsi dengan baik untuk orang lain, jadi tetapkan hanya isyarat yang akan Anda gunakan.

[Kembali ke indeks](#index)

<h3 id="version-2024-06-23">Version 2024.06.23</h3>

* Menambahkan modul DeepL Translator baru (Gratis)

Modul baru ini tidak memerlukan kunci API dan digunakan untuk terjemahan waktu nyata

* Koreksi kesalahan

[Kembali ke indeks](#index)

<h3 id="version-2024-09-07">Version 2024.09.07</h3>

#### Antarmuka Terjemahan

**Antarmuka Terjemahan** adalah komponen utama dari addon **Translate Advanced** untuk NVDA. Antarmuka ini memungkinkan pengguna untuk menerjemahkan teks antara berbagai bahasa secara efisien, menampilkan teks asli dan terjemahan, dan menyediakan berbagai opsi penyesuaian.

Untuk menjalankannya, Anda harus menetapkan kombinasi tombol dalam gerakan input atau dari menu virtual (dijelaskan di bawah).

##### Fitur utama:

1. **Entri teks sumber**: Memungkinkan pengguna menulis atau menempelkan teks yang ingin mereka terjemahkan. Itu dapat diakses dengan cepat dengan kombinasi tombol `Alt+1`.
   
2. **Teks ​​target (hasil)**: Area di mana teks terjemahan ditampilkan. Bidang ini bersifat baca-saja dan dapat difokuskan dengan `Alt+2`.

3. **Pemilihan bahasa sumber**: Memungkinkan Anda memilih bahasa teks sumber. Bahasa default adalah opsi "Deteksi Otomatis", yang memungkinkan sistem mendeteksi bahasa teks secara otomatis. Itu diakses dengan `Alt+3`.

4. **Pemilihan bahasa target**: Memungkinkan Anda memilih bahasa yang ingin Anda terjemahkan teksnya. Itu dapat difokuskan dengan `Alt+4`.

5. **Penghitung Karakter**: Menampilkan jumlah karakter di kolom teks sumber. Berguna untuk mengetahui jumlah teks yang akan diterjemahkan. Itu diakses dengan `Alt+5`.

6. **Tombol Tindakan**:
- **Terjemahkan**: Memulai terjemahan teks yang dimasukkan.
- **Dengarkan**: Mendapatkan audio terjemahan dan memungkinkannya diputar melalui pemutar terintegrasi (lihat bagian di bawah).
- **Tukar**: Menukar bahasa sumber dengan bahasa target, berguna jika Anda ingin membalikkan bahasa terjemahan.
- **Hapus**: Menghapus kolom teks sumber dan tujuan.
- **Tempel ke Fokus**: Menempelkan teks terjemahan ke jendela aktif atau kolom teks di belakang antarmuka. Itu juga dapat diaktifkan dengan `F3`.
- **Tutup**: Menutup jendela terjemahan.

##### Pintasan keyboard:

- `Alt+1`: Memfokuskan kotak teks sumber.
- `Alt+2`: Memfokuskan kotak teks target.
- `Alt+3`: Pilih bahasa sumber.
- `Alt+4`: Pilih bahasa target.
- `Alt+5`: Memfokuskan penghitung karakter.
- `F3`: Tempelkan teks terjemahan ke jendela aktif.
- `Esc`: Menutup dialog terjemahan.

##### Perilaku jika terjadi kesalahan:

- Jika tidak ada koneksi Internet, sistem akan menampilkan pesan yang menginformasikan kurangnya koneksi.
- Jika kotak teks sumber kosong, pengguna akan menerima peringatan yang meminta untuk memasukkan teks sebelum melakukan terjemahan.
- Jika bahasa sumber dan bahasa sasaran sama, akan muncul peringatan yang menunjukkan bahwa teks tidak perlu diterjemahkan ke dalam bahasa yang sama.

##### Fitur Tambahan:

- **Deteksi otomatis bahasa**: Jika "Deteksi Otomatis" dipilih dalam bahasa sumber,Plugin akan mencoba mengidentifikasi secara otomatis bahasa teks yang akan diterjemahkan.
- **Pertukaran Bahasa**: Fungsi ini berguna saat Anda ingin menerjemahkan teks kembali ke bahasa aslinya.

#### Pemutar Audio

Saat pengguna menggunakan opsi **Dengarkan** setelah melakukan terjemahan, plugin akan mengubah teks terjemahan menjadi file audio dan memutarnya melalui pemutar terintegrasi. Pemutar ini mencakup kontrol dasar dan lanjutan untuk mengelola pemutaran audio.

##### Fitur Pemain:

1. **Tombol kontrol**:
- **Mundur (F1)**: Memutar mundur pemutaran sesuai waktu yang dipilih. Pengguna dapat mengkonfigurasi kali ini.
- **Putar/Jeda (F2)**: Memulai atau menjeda pemutaran file audio.
- **Fast forward (F3)**: Mempercepat pemutaran sesuai dengan waktu yang ditentukan oleh pengguna.
- **Stop (F4)**: Menghentikan pemutaran sepenuhnya.

2. **Volume dan kecepatan**:
- **Volume (F5/F6)**: Sesuaikan volume pemutaran menggunakan penggeser.
- **Kecepatan (F7/F8)**: Mengubah kecepatan pemutaran, dengan opsi dari 0,50x hingga 2,0x kecepatan normal.

3. **Teks ​​terkait**: Menampilkan teks terjemahan dalam kotak baca-saja, sehingga pengguna dapat melihat apa yang sedang diputar.

4. **Simpan**: Memungkinkan Anda menyimpan file audio yang dihasilkan dalam format WAV di sistem Anda.

5. **Tutup**: Menutup pemutar dan melepaskan sumber daya terkait.

##### Pintasan keyboard:

- `F1`: Memundurkan pemutaran.
- `F2`: Memutar atau menjeda audio.
- `F3`: Pemutaran maju cepat.
- `F4`: Menghentikan pemutaran.
- `F5/F6`: Menyesuaikan volume.
- `F7/F8`: Mengubah kecepatan pemutaran.
- `F9`: Informasi waktu pemutaran.
- `Shift+F10/Applications`: akan menampilkan menu kontekstual untuk memilih interval waktu tombol mundur dan maju cepat.

##### Fitur Tambahan:

- **Simpan Audio**: Pengguna dapat memilih untuk menyimpan file audio ke perangkat mereka dalam format WAV untuk digunakan nanti.
- **Menu opsi lanjutan**: Pemutar memungkinkan Anda memilih waktu yang tepat untuk memundurkan atau memajukan pemutaran melalui menu kontekstual (diakses dengan tombol `Shift+F10`) atau tombol aplikasi.

#### Menu maya

Menu virtual telah ditambahkan yang berisi semua opsi addon.

Anda dapat menjalankan semua opsi dari menu virtual yang dapat Anda tetapkan dalam gerakan input. Dengan cara ini, semua fitur addon dapat digunakan tanpa harus menetapkan kunci lagi ke addon tersebut.

Ini terserah pengguna.

Untuk menjalankan menu virtual, Anda harus menetapkan kunci pada menu tersebut dengan gerakan input.

Menggunakan menu virtual itu sederhana, setelah dipanggil Anda harus menekan tombol yang sesuai untuk tindakan yang ingin Anda lakukan. Setelah ditekan, tindakan akan dilakukan dan Anda akan selalu diberitahu tentang apa yang telah dilakukan. Jika Anda menekan tombol yang tidak ditetapkan, menu virtual akan ditutup dan Anda juga dapat menutupnya dengan escape.

##### Pintasan Keyboard Menu Virtual

Menu virtual Translate Advanced memungkinkan Anda mengakses fungsi plugin yang paling berguna dengan cepat. Berikut adalah pintasan yang dapat Anda gunakan untuk melakukan berbagai tindakan:

- **`P`**: **Buka konfigurasi**
Buka pengaturan Translate Advanced di mana Anda dapat menyesuaikan bahasa dan layanan terjemahan.

- **`U`**: **Periksa pembaruan bahasa**
Periksa dan unduh pembaruan yang tersedia untuk bahasa plugin.

- **`O`**: **Ubah bahasa sumber**
Ubah bahasa teks yang ingin Anda terjemahkan (bahasa sumber).

- **`D`**: **Ubah bahasa target**
Ubah bahasa yang Anda inginkan untuk menerjemahkan teks (bahasa target).

- **`C`**: **Ubah layanan terjemahan**
Memungkinkan Anda beralih di antara layanan terjemahan yang tersedia, seperti Google, DeepL, Microsoft, dan lainnya.

- **`A`**: **Hapus semua cache terjemahan**
Menghapus semua terjemahan yang di-cache.

- **`X`**: **Hapus cache terjemahan aplikasi saat ini**
Hapus terjemahan yang di-cache hanya untuk aplikasi yang Anda buka.

- **`G`**: **Aktifkan/Nonaktifkan cache terjemahan**
Mengaktifkan atau menonaktifkan fitur cache yang menyimpan terjemahan sementara.

- **`L`**: **Salin terjemahan terakhir ke papan klip**
Salin terjemahan terakhir yang dibuat ke papan klip sehingga Anda dapat menempelkannya di mana pun Anda memerlukannya.

- **`B`**: **Terjemahkan teks papan klip**
Menerjemahkan isi clipboard saat ini.

- **`V`**: **Terjemahkan teks yang terakhir diucapkan**
Menerjemahkan teks terakhir yang dibacakan NVDA.

- **`T`**: **Aktifkan/Nonaktifkan terjemahan waktu nyata**
Mengaktifkan atau menonaktifkan terjemahan otomatis saat menelusuri teks.

- **`S`**: **Terjemahkan teks yang dipilih**
Terjemahkan teks yang Anda pilih dalam aplikasi.

- **`Z`**: **Terjemahkan teks dari objek browser**
Menerjemahkan teks objek tertentu dalam browser, seperti tombol atau kotak teks.

- **`W`**: **Buka antarmuka terjemahan**
Membuka jendela grafis tempat Anda dapat memasukkan teks yang ingin Anda terjemahkan secara manual.

- **`I`**: **Deteksi bahasa yang dipilih**
Secara otomatis mendeteksi bahasa teks yang dipilih.

- **`J`**: **Aktifkan/Nonaktifkan pertukaran bahasa otomatis**
Mengaktifkan atau menonaktifkan peralihan otomatis jika bahasa sumber yang terdeteksi cocok dengan bahasa target.

- **`K`**: **Tukar bahasa utama dan bahasa alternatif**
Tukar bahasa utama dengan bahasa alternatif di pengaturan penerjemah.

- **`H`**: **Tampilkan riwayat terjemahan**
Menampilkan riwayat terjemahan terkini yang dilakukan.

- **`F1`**:**Tampilkan daftar perintah**
Menampilkan daftar dialog perintah satu tombol untuk Translate Advanced.

#### Deteksi bahasa

Opsi ini memungkinkan Anda mendeteksi secara otomatis bahasa teks yang Anda pilih di aplikasi apa pun. Untuk menggunakan fitur ini:
1. Pilih teks yang ingin Anda ketahui bahasanya.
2. Gunakan pintasan keyboard yang dikonfigurasi dalam gerakan input (atau menu virtual) untuk mengaktifkan deteksi bahasa.
3. Sistem akan mendeteksi dan memberi tahu Anda tentang bahasa penulisan teks yang dipilih.
Fitur ini berguna ketika Anda tidak yakin dengan bahasa suatu teks dan perlu mengetahuinya sebelum menerjemahkannya atau mengambil tindakan lainnya.

#### Pertukaran Bahasa Otomatis di NVDA Advanced Translator

1. Aktifkan pertukaran otomatis dengan menekan pintasan keyboard yang sesuai atau mengaksesnya dari menu virtual.
2. Jika teks yang Anda pilih memiliki bahasa yang sama dengan bahasa target, sistem akan secara otomatis mengalihkan bahasa target ke bahasa alternatif untuk menghindari terjemahan yang tidak perlu.
3. Anda dapat menonaktifkan opsi ini kapan saja menggunakan pintasan yang sama.

##### Pengaturan Bahasa di Addon

- Anda dapat mengonfigurasi **bahasa target** dan **bahasa alternatif** dengan mengakses **Pengaturan Addon** di bagian **Umum**. Dari sana Anda dapat memilih bahasa yang akan digunakan untuk pertukaran otomatis.

Fitur ini berguna untuk menghindari kebingungan saat menerjemahkan teks yang bahasa sumbernya sama dengan bahasa target, secara otomatis beralih ke bahasa alternatif yang dikonfigurasi.

#### Bantuan dalam Dialog Addon

Menambahkan fungsionalitas untuk menampilkan bantuan kontekstual dalam dialog addon. Menekan kombinasi tombol `Ctrl+H` akan menampilkan penjelasan kecil tentang fungsi widget yang sedang fokus.

Di mana saja dalam dialog addon, jika Anda memerlukan informasi tentang fungsi tombol, kotak teks, penggeser, atau kontrol lainnya, Anda cukup menekan `Ctrl+H`. Ini akan menampilkan penjelasan singkat tentang widget yang difokuskan, memberikan panduan singkat tentang penggunaannya.

#### Terjemahkan teks dari objek browser

Fungsionalitas ini memungkinkan Anda menerjemahkan teks objek tertentu dalam browser atau aplikasi lain yang digunakan NVDA. Ini dapat diaktifkan melalui menu virtual atau melalui kombinasi tombol yang ditetapkan dalam gerakan input addon.

1. Tempatkan kursor pada objek yang ingin Anda terjemahkan (bisa berupa tombol, kotak teks, dll.).
2. Aktifkan fungsionalitas dengan menekan kombinasi tombol yang ditetapkan atau melalui menu virtual.
3. Addon akan menerjemahkan teks yang terdapat dalam objek tersebut dan menampilkan atau mengucapkannya, tergantung pada konfigurasinya.

- Terjemahkan teks apa pun yang terdapat dalam objek yang dipilih dalam halaman web, aplikasi, atau antarmuka lain tempat NVDA berinteraksi.
- Berguna untuk menerjemahkan potongan kecil teks yang bukan merupakan bagian utama halaman atau aplikasi, seperti menu, tombol, atau label.
- Jika objek tidak berisi teks atau tidak dapat diakses, plugin akan menampilkan pesan yang menginformasikan bahwa tidak ada teks untuk diterjemahkan.

- Anda dapat mengakses fungsi ini baik dari menu virtual addon dan dengan mengatur hotkey di "Input Gestures" NVDA.

#### OpenAI module

Modul baru telah ditambahkan untuk menerjemahkan dengan OpenAI dengan model chatGPT-4º-mini, yang termurah dan tercepat.

Modul ini sedang dalam tahap pengujian, terkadang mengalami sedikit lag, namun akan diperbaiki pada versi mendatang.

Modul ini memerlukan kunci API untuk ditetapkan dalam konfigurasi/modul.

OpenAI berbayar sehingga pengguna bebas memeriksa pengeluarannya.

Pada link berikut ini Anda dapat melihat pengeluaran yang telah Anda gunakan:

[https://platform.openai.com/usage](https://platform.openai.com/usage)

#### Peningkatan pada modul Microsoft

Modul penerjemah Microsoft telah ditulis ulang dari awal untuk meningkatkan kecepatan, stabilitas, dan memberikan lebih banyak waktu terjemahan hingga mereka memblokir Anda karena penggunaan dan Anda harus menunggu beberapa menit untuk menerjemahkan lagi.

Sekarang dalam pengujian saya yang dilakukan dengan menerjemahkan banyak teks secara bersamaan, bahkan lebih dari penggunaan normal, saya tidak mengalami batasan apa pun.

Jadi saat ini sudah berfungsi dan sudah ditingkatkan dibandingkan modul sebelumnya.

#### Yang lain

* Memperbaiki masalah verbalisasi beberapa pesan.
* Mengubah cara untuk memeriksa apakah ada internet.
* Perbaikan bug
* Secara resmi menambahkan bahasa Perancis.

[Kembali ke indeks](#index)
