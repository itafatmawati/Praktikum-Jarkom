# Laporan praktikum jarkom modul 3

## Basic HTTP GET/response interaction 

Saat membuka halaman web dengan HTTP, browser mengirimkan **GET request** ke server dan server membalas dengan **response** berisi halaman (HTML), yang dapat diamati menggunakan Wireshark.

Eksplorasi HTTP dengan mengunduh file HTML yang sangat sederhana:

1. Jalankan wireshark anda
2. Salin link berikut : http://gaia.cs.umass.edu/wireshark-labs/HTTP
wireshark-file1.html , lalu buka web browser anda, dan jalankan link tersebut dengan memastikan bahwa format web yaitu "http". Tampilan web akan seperti gambar di bawah ini:
![web 3.2](../assets/image/week%203/web-3.2.png)
3. Masuk ke wireshark, lalu klik ikon kotak merah pada bagian atas filter untuk stop capture. lalu pada baris filter, cari "http".
4. Temukan baris seperti gambar di bawah ini, lalu klik untuk melihat isi dari baris tersebut :
![ws 3.2](../assets/image/week%203/ws-3.2.png)
pada gambar tersebut, pada bagian paling bawah terdapat suatu kalimat. Apabila kalimat tersebut cocok/ sama dengan kalimat pada halaman web sebelumnya, maka berhasil.

## HTTP CONDITIONAL GET/response interaction 

Saat menggunakan **HTTP Conditional GET**, browser hanya meminta ulang data ke server jika versi terbaru tersedia (berdasarkan cache), dan proses request–response ini dapat diamati melalui Wireshark.

Sebelum melakukan langkah-langkah di bawah ini, pastikan cache browser Anda kosong.

1. Jalankan wireshark anda
2. Salin link berikut : http://gaia.cs.umass.edu/wireshark-labs/HTTP
wireshark-file2.html , lalu buka web browser anda, dan jalankan link tersebut dengan memastikan bahwa format web yaitu "http". Tampilan web akan seperti gambar di bawah ini:
![web 3.2.1](../assets/image/week%203/web-3.2.1.png)
3. Masuk ke wireshark, lalu klik ikon kotak merah pada bagian atas filter untuk stop capture. lalu pada baris filter, cari "http".
4. Temukan baris seperti gambar di bawah ini, lalu klik untuk melihat isi dari baris tersebut :
![ws 3.2](../assets/image/week%203/ws-3.2.1.png)
pada gambar tersebut, pada bagian dengan tanda kotak oranye di paling bawah terdapat suatu kalimat. Apabila kalimat tersebut cocok/ sama dengan kalimat pada halaman web sebelumnya, maka berhasil.
6. ![ws 3.2](../assets/image/week%203/frament-3.2.1.png)

Penjelasan: 

Pada gambar tersebut, bagian kotak berwarna oranye menunjukkan proses TCP Reassembly. File web HTTP-wireshark-file3.html yang dikirim oleh server tidak dikirim dalam satu paket utuh, melainkan dipecah menjadi dua segmen/frame karena ukuran file melebihi batas transmisi maksimum. Hal ini menunjukkan bahwa data yang dikirim melalui protokol TCP dapat dibagi menjadi beberapa segmen agar dapat ditransmisikan melalui jaringan, kemudian akan disusun kembali (reassembly) di sisi penerima sehingga file dapat diterima secara utuh.

## Retrieving Long Documents 

Saat mengambil dokumen berukuran besar, data dikirim dari server ke klien dalam beberapa segmen TCP (fragmentasi) yang kemudian disatukan kembali (reassembly), dan proses ini dapat diamati melalui Wireshark.

Mari kita lihat apa yang terjadi ketika kita mengunduh file HTML yang panjang.

1. Jalankan wireshark anda
2. Salin link berikut : http://gaia.cs.umass.edu/wireshark-labs/HTTP
wireshark-file3.html  , lalu buka web browser anda, dan jalankan link tersebut dengan memastikan bahwa format web yaitu "http". Tampilan web akan seperti gambar di bawah ini:
![web 3.2.1](../assets/image/week%203/web-3.3.png)
3. Masuk ke wireshark, lalu klik ikon kotak merah pada bagian atas filter untuk stop capture. lalu pada baris filter, cari "http".
4. Temukan baris seperti gambar di bawah ini, lalu klik untuk melihat isi dari baris tersebut :
![ws 3.2](../assets/image/week%203/ws-3.3.png)
pada gambar tersebut, pada bagian dengan tanda kotak oranye di paling bawah terdapat suatu kalimat. Apabila kalimat tersebut cocok/ sama dengan kalimat pada halaman web sebelumnya, maka berhasil.
5. Lalu pada baris filter, cari "tcp", lalu pada baris yang ada cari sekumpulan baris perti gambar di bawah ini:
![web 3.3](../assets/image/week%203/rincian3.3%20.png)

Penjelasan :

1. Baris dengan centang merah pada gambar tersebut, merupakan baris yang menandakan HTTP GET request. Tanda panah (->) di ujung sebelah kiri menunjukkan paket keluar dari sisi klien.
2. Baris dengan centang oren, menandakan server merespon permintaan klien dengan memberikan konfirmasi atau "ACC" bahwa koneksi telah diterima dan server siap untuk mengirimkan data yang diminta.
3. Baris dengan centang ungu, menandakan server melakukan TCP Segmentation, di mana file dipecah menjadi beberapa potongan (segmen). Pada baris ini, terlihat keterangan [TCP PDU reassembled], yang berarti paket tersebut adalah salah satu bagian dari potongan data besar yang sedang dikirim.
4. Baris dengan cetang hitam, menandakan bahwa semua potongan (fragmen) data tadi telah diterima sepenuhnya oleh klien dan telah disatukan kembali secara otomatis oleh Wireshark (Reassembled). Tanda panah (<-) di ujung kiri menandakan data sedang masuk ke komputer dari server.

## HTML Documents dengan Embedded Objects

Saat halaman HTML memiliki embedded objects (seperti gambar), browser akan mengirim beberapa HTTP GET request ke server yang berbeda untuk mengambil setiap objek (PNG, JPG, dll), dan proses ini dapat diamati melalui Wireshark.

Mari kita lihat apa yang terjadi ketika browser mengunduh file dengan objek yang disematkan, yaitu file yang menyertakan objek lain (dalam contoh di bawah, file gambar ) yang disimpan di server lain. 

1. Jalankan wireshark anda
2. Salin link berikut : http://gaia.cs.umass.edu/wireshark-labs/HTTP
wireshark-file4.html, lalu buka web browser anda, dan jalankan link tersebut dengan memastikan bahwa format web yaitu "http". Tampilan web akan seperti gambar di bawah ini :
![web 3.4](../assets/image/week%203/web3.4.png)

Lalu, lakukan inspect untuk mengetahui detail dari gambar pada web tersebut :
![web 3.4 inspect](../assets/image/week%203/web-3.4inspect.png)
pada gambar tersebut, bagian dengan garis merah di bawah link menandakan bahwa halaman web ini mengambil objek (gambar) dari lokasi atau server yang berbeda-beda.
3. Masuk ke wireshark, lalu klik ikon kotak merah pada bagian atas filter untuk stop capture. lalu pada baris filter, cari "http".
4. Temukan baris seperti gambar di bawah ini, lalu klik untuk melihat isi dari baris tersebut :
![ws 3.4](../assets/image/week%203/ws-3.4.png)

Penjelasan :

Pada gambar di atas, indikasi keberhasilan dapat dilihat pada baris yang ditunjukkan oleh panah merah, serta pada baris yang menampilkan format PNG dan JPG. Hal ini menunjukkan bahwa konten web yang diminta berhasil diterima, karena halaman web tersebut berisi beberapa jenis data seperti gambar berformat PNG, JPG, dan juga teks.

## HTTP Authentication

Saat menggunakan HTTP Authentication, username dan password dikirim dalam bentuk plaintext (tidak terenkripsi) sehingga dapat terlihat melalui Wireshark, yang menunjukkan bahwa HTTP kurang aman.

Mari kita coba mengunjungi situs web yang dilindungi kata sandi dan memeriksa urutan pesan HTTP yang dipertukarkan untuk situs tersebut

1. Jalankan wireshark anda
2. Salin link berikut : http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html, lalu buka web browser anda, dan jalankan link tersebut dengan memastikan bahwa format web yaitu "http". Tampilan web akan seperti gambar di bawah ini:
![masuk 3.5](../assets/image/week%203/masuk-3.5.png)
3. Masukkan username : "wireshark-students" dan password "network" tanpa tanda kutip. 
![web 3.5](../assets/image/week%203/web-3.5.png)
4. Masuk ke wireshark, lalu klik ikon kotak merah pada bagian atas filter untuk stop capture. lalu pada baris filter, cari "http".
5. Temukan baris seperti gambar di bawah ini, lalu klik untuk melihat isi dari baris tersebut :
![ws 3.5](../assets/image/week%203/ws-3.5.png)
6. ![isi ws 3.5](../assets/image/week%203/isiws-3.5.png)

Penjelasan:

Pada gambar tersebut terlihat username dan password yang sebelumnya telah dimasukkan oleh pengguna. Hal ini menunjukkan bahwa data yang dikirim melalui protokol HTTP dapat terlihat secara langsung dalam bentuk teks biasa (plaintext). Oleh karena itu, HTTP dianggap kurang aman karena tidak menggunakan proses enkripsi untuk melindungi data yang dikirimkan melalui jaringan.

## Kesimpulan
Secara umum, proses dimulai dari HTTP GET request yang dikirim browser dan direspons server dengan HTTP response berisi data halaman web (HTML). Pada Conditional GET, browser memanfaatkan cache sehingga hanya meminta data baru jika terjadi perubahan. Saat mengunduh dokumen berukuran besar, data dikirim dalam beberapa segmen TCP (fragmentasi) yang kemudian disusun kembali (reassembly) di sisi klien.

Selain itu, halaman HTML yang memiliki embedded objects (seperti gambar) akan memicu beberapa request tambahan ke server berbeda untuk mengambil setiap objek. Terakhir, pada HTTP Authentication, terlihat bahwa username dan password dikirim dalam bentuk plaintext, sehingga membuktikan bahwa HTTP tidak aman karena tidak menggunakan enkripsi.

Sehingga, praktikum ini membantu memahami cara kerja HTTP, pengiriman data dalam jaringan, serta keterbatasan keamanan pada protokol HTTP.