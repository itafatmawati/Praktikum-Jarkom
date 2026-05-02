# Laporan Praktikum Jarkom week 6 

## TCP
## Menangkap Tansfer TCP dalam Jumlah Besar dari Komputer Pribadi ke Remote Server 

Pertama, dilakukan pengaksesan halaman web TCP-wireshark-file1.html. Pada Wireshark, terlihat paket dengan protokol HTTP menggunakan metode GET. Ini menandakan komputer klien (sumber) sedang meminta data tampilan form unggah dari server gaia.cs.umass.edu:
![alice-1](../assets/image/week%206/alice-1.png)
Setelah file alice.txt dipilih, dilakukan proses unggah menggunakan metode HTTP POST. Pada tahap ini, terjadi transfer data dalam jumlah besar (sekitar 150 KB) dari komputer pribadi ke remote server. Data tersebut dipecah menjadi beberapa segmen TCP untuk menjamin pengiriman yang andal (reliable transfer) sesuai dengan prinsip protokol TCP:
![alice-2](../assets/image/week%206/alice-2.png)
Setelah seluruh data terkirim, server memberikan respon berupa status HTTP/1.1 200 OK seperti gamabar di atas yang menunjukkan bahwa transfer berhasil. dan berikut tampilan pada browser yang menandakan bahwa trace paket TCP sudah lengkap:
![alice-3](../assets/image/week%206/alice-3.png)

## Tampilan Awal pada Captured Trace 

## Question 

1. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien (sumber) untuk 
mentransfer file ke gaia.cs.umass.edu? Cara paling mudah menjawab pertanyaan ini adalah 
dengan memilih sebuah pesan HTTP dan meneliti detail paket TCP yang digunakan untuk 
membawa pesan HTTP tersebut. 

![6-3.1](../assets/image/week%206/6-3.1.png)
![6-3.1-1](../assets/image/week%206/6-3.1-1.png)
Berdasarkan kedua gambar di atas, didapatkan Alamat IP klien = 10.218.13.38, dan nomor port TCP = 52789.

2. Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima 
segmen TCP untuk koneksi ini? 

![6-3.2](../assets/image/week%206/6-3.2.png)
![6-3.2-2](../assets/image/week%206/6-3.2-2.png)
Berdasarkan kedua gambar di atas, didapatkan Alamat IP Server: 128.119.245.12, dan pada nomor port = 443 ia mengirim an menerima segmen TCP untuk koneksi ini

## Dasar TCP

## Question

1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara 
komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga 
teridentifikasi sebagai segmen SYN? 

![soal-1](../assets/image/week%206/soal-1.png)
Nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP adalah 0 dan pada bagian Flags terdapat SYN : Set, berarti fungsi tersebut sedang Aktif atau sedang digunakan, sehingga segmen tersebut teridentifikasi sebagai SYN.

2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien 
sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? 
Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen  
sehingga teridentifikasi sebagai segmen SYNACK? 

![soal-2](../assets/image/week%206/soal-2.png)
Berdasarkan gambar diatas, nomor urut adalah 0 dan ACK number adalah 1 , hal ini diperoleh dari menambhakan sequence number dengan 1 sehingga 0 + 1 = 1.
Kemudian yang dimiliki segemen tersebut yaitu nilai Flags =  0x012 (SYN, ACK). Ini adalah hasil penggabungan bit ACK (0x010) dan bit SYN (0x002), yang membuktikan bahwa segmen ini berfungsi ganda sebagai sinkronisasi sekaligus konfirmasi penerimaan paket sebelumnya.

3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST? Perhatikan bahwa untuk 
menemukan perintah POST, Anda harus menelusuri content field milik paket di bagian 
bawah jendela Wireshark, kemudian cari segmen yang berisi "POST" di bagian field DATA
nya. 
![soal-3](../assets/image/week%206/soal-3.png)
Nomor urut segmen yang berisi perintah HTTP POST = 1

4.  Anggap segmen TCP yang berisi HTTP POST sebagai segmen pertama dalam koneksi TCP. 
Berapa nomor urut dari enam segmen pertama dalam TCP (termasuk segmen yang berisi 
HTTP POST)? Pada jam berapa setiap segmen dikirim? Kapan ACK untuk setiap segmen 
diterima? Dengan adanya perbedaan antara kapan setiap segmen TCP dikirim dan kapan 
acknowledgement-nya diterima, berapakah nilai RTT untuk keenam segmen tersebut? 
Berapa nilai EstimatedRTT setelah penerimaan setiap ACK? (Catatan: Wireshark memiliki 
fitur yang memungkinkan Anda untuk memplot RTT untuk setiap segmen TCP yang dikirim. 
Pilih segmen TCP yang dikirim dari klien ke server gaia.cs.umass.edu pada jendela "daftar paket yang ditangkap". Kemudian pilih: Statistics->TCP Stream Graph- >Round Trip Time 
Graph). 
![soal 4-1](../assets/image/week%206/soal%204-1.png)
![soal 4-1.1](../assets/image/week%206/soal%204-1.1.png)

![soal-4-2](../assets/image/week%206/soal%204-2.png)
![soal-4-2.1](../assets/image/week%206/soal%204-2.1.png)

![soal-4-3](../assets/image/week%206/soal%204-3.png)
![soal-4-3.1](../assets/image/week%206/soal%204-3.1.png)

![soal-4-4](../assets/image/week%206/soal-4-4.1.png)
![soal-4-4.1](../assets/image/week%206/soal%204-4.png)

![soal-4-5](../assets/image/week%206/soal%204-5.png)
![soal-4-5.1](../assets/image/week%206/soal-4-5.1.png)

![soal-4-6](../assets/image/week%206/soal%204-6.png)
![soal-4-6.1](../assets/image/week%206/soal%204-6.1.png)
Sehingga, didapatkan :
![soal-4-time](../assets/image/week%206/soal-4-time.png)

5. Berapa panjang setiap enam segmen TCP pertama? 
![soal-5](../assets/image/week%206/soal-5.png)
6. Berapa jumlah minimum ruang buffer tersedia yang disarankan kepada penerima dan 
diterima untuk seluruh trace? Apakah kurangnya ruang buffer penerima pernah 
menghambat pengiriman? 
![soal-6](../assets/image/week%206/soal-6.png)
Berdasarkan gambar di atas, ruang buffer minimum yang disarankan/disediakan oleh penerima adalah 5840 bytes. Serta Tidak, kurangnya ruang buffer penerima tidak pernah menghambat pengiriman data dalam trace ini.

7. Apakah ada segmen yang ditransmisikan ulang dalam file trace? Apa yang anda periksa (di 
dalam file trace) untuk menjawab pertanyaan ini? 

![soal-7](../assets/image/week%206/soal-7.png)
Tidak ada.

8. Berapa banyak data yang biasanya diakui oleh penerima dalam ACK? Dapatkah anda 
mengidentifikasi kasus-kasus di mana penerima melakukan ACK untuk setiap segmen yang 
diterima?
![soal-8](../assets/image/week%206/soal-8.png)
kesimpulan: Penerima biasanya mengakui 2920 bytes data sekaligus (2 paket dibalas 1 ACK), tapi ada pengecekan per segmen (1 paket dibalas 1 ACK) pada Paket No. 6 yang hanya mengakui Paket No. 4.

9. Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP? 
Jelaskan bagaimana Anda menghitung nilai ini. 
![soal-9](../assets/image/week%206/soal-9.png)
Throughput untuk sambungan TCP ini adalah sekitar 250 kbps (atau sekitar 31 kB/s). Nilai throughput dihitung dengan menjumlahkan seluruh byte data aplikasi yang dikirim (164 kB) dibagi dengan durasi waktu transmisi (± 5.3 detik). Berdasarkan grafik Wireshark, rata-rata throughput stabil pada angka 250 kbps setelah melewati fase slow start di satu detik pertama.

## Congestion Control pada TCP 

## Question
1. Gunakan alat plotting Time-Sequence-Graph (Stevens) untuk melihat grafik nomor urut 
berbanding waktu dari segmen yang dikirim oleh klien ke server gaia.cs.umass.edu. 
Dapatkah Anda mengidentifikasi di mana fase “slow start” TCP dimulai dan berakhir, dan 
pada bagian mana algoritma ”congestion avoidance” mengambil alih? 
![soal-1](../assets/image/week%206/soal-1%206.5.png)
Berdasarkan garfik di atas, fase slow start dimulai dari awal transmisi (sekitar 0 detik) dan berlangsung hingga sekitar 0.8–1 detik, yang ditandai dengan kenaikan eksponensial pada grafik. Setelah itu, grafik berubah menjadi linear, menandakan bahwa fase congestion avoidance mulai mengambil alih hingga akhir transmisi. Kemudian, terdapat beberapa perbedaan antara perilaku TCP ideal dan data hasil pengukuran. Secara teori, fase slow start seharusnya menunjukkan peningkatan eksponensial yang jelas, namun pada grafik hanya terlihat sedikit kenaikan di awal karena fase ini berlangsung sangat singkat. Selain itu, transisi dari slow start ke congestion avoidance terlihat lebih halus. Grafik juga tidak menunjukkan adanya penurunan drastis yang menandakan packet loss, sehingga dapat disimpulkan bahwa kondisi jaringan relatif stabil. Bentuk grafik yang menyerupai tangga juga menunjukkan bahwa data dikirim dalam burst per RTT.

## Kesimpulan
Pemanfaatan Wireshark dalam analisis TCP memungkinkan kita memahami secara langsung bagaimana proses komunikasi data berlangsung antara client dan server, mulai dari pembentukan koneksi melalui three-way handshake hingga pengiriman data menggunakan nomor urut dan acknowledgement untuk menjamin keandalan. Selain itu, mekanisme penting seperti flow control dan congestion control dapat diamati melalui trace paket, termasuk fase slow start dan congestion avoidance yang mengatur laju pengiriman data agar tidak terjadi kemacetan jaringan. Dengan menganalisis parameter seperti RTT, throughput, ukuran segmen, serta kemungkinan retransmisi, kita dapat mengevaluasi performa koneksi TCP secara lebih mendalam dan memahami bagaimana TCP menjaga efisiensi serta keandalan dalam transfer data skala besar.