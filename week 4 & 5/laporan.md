# laporan praktikum jarkom modul 4 & 5

## Nslookup 

Nslookup digunakan untuk mencari informasi DNS (Domain Name System).

![nslookup-1](../assets/image/week%204%20&%205/nslookup-1.png)
![nslookup-3](../assets/image/week%204%20&%205/nslookup-3.png)

Pada perintah "nslookup www.mit.edu" tujuannya adalah mencari tahu alamat IP dari www.mit.edu, yaitu : 23.15.150.186.
Kemudian perintah "nslookup -type=NS mit.edu" bertujuan untuk mencari server mana yang bertanggung jawab mengelola catatan DNS untuk domain tersebut, dan perintah "nslookup www.aiit.or.kr 8.8.8.8" bertujuan untuk mencari tahu alamat IP dari www.aiit.or.kr, yaitu : 104.21.74.8 dan 172.67.152.120.

## Question:

1. Jalankan nslookup untuk mendapatkan alamat IP dari server web di Asia. Berapa alamat IP 
server tersebut? 
![soal-1-nslookup](../assets/image/week%204%20&%205/soal-1-nslookup.png)
alamat IP = 34.36.102.170
2. Jalankan nslookup agar dapat mengetahui server DNS otoritatif untuk universitas di Eropa.
![soal-2-nslookup](../assets/image/week%204%20&%205/soal-2-nslookup.png)
Berdasarkan output di atas, server DNS otoritatif pada universitas di eropa(Oxford) yaitu : dns0.ox.ac.uk, dll.  
3. Jalankan nslookup untuk mencari tahu informasi mengenai server email dari Yahoo! Mail 
melalui salah satu server yang didapatkan di pertanyaan nomor 2. Apa alamat IP-nya?
1[soal-3-nslookup](../assets/image/week%204%20&%205/soal-3-nslookup.png)
Alamat IP tidak dapat ditemukan melalui server dns0.ox.ac.uk , karena server tersebut adalah Authoritative Name Server untuk domain Oxford, bukan Recursive Resolver.

## Ipconfig
Ipconfig adalahperintah pada sistem operasi Windows yang digunakan untuk menampilkan rincian konfigurasi jaringan yang sedang digunakan oleh perangkat saat ini.

![ipconfig-1](../assets/image/week%204%20&%205/ipconfig-1.png)
![ipconfig-1-1](../assets/image/week%204%20&%205/ipconfig-1-1.png)
Gambar di atas menggunakan perintah "ipconfig /all" untuk menampilkan konfigurasi lengkap, termasuk Physical Address (MAC Address), DNS Server, serta status dan masa sewa (lease) DHCP.
![ipconfig-2](../assets/image/week%204%20&%205/ipconfig-2.png)
Gambar di atas menggunakan perintah "ipconfig /displaydns" untuk melihat record yang telah disimpan.
![ipconfig-3](../assets/image/week%204%20&%205/ipconfig-3.png)
Gambar di atas menggunakan perintah "ipconfig /flushdns" untuk mengosongkan catatan DNS/ menghapus.

## Tracing DNS dengan Wireshark 
## Soal 1
1. Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP 
atau TCP? 
![4-4.1](../assets/image/week%204%20&%205/4-4.1.png)
Berdasarkan hasil tangkapan paket (packet capture) pada Wireshark, pesan permintaan (DNS Query) dan balasan (DNS Response) dikirimkan melalui protokol UDP (User Datagram Protocol).
2. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya? 
![4-4.1](../assets/image/week%204%20&%205/4-4.1.png)
Berdasarkan hasil tangkapan paket (packet capture) pada Wireshark, Port tujuan (Destination Port) = 53. sedangkan, Port sumber (Source Port) = 58773
3. Pada pesan permintaan DNS, apa alamat IP tujuannya? Apa alamat IP server DNS lokal anda 
(gunakan ipconfig untuk mencari tahu)? Apakah kedua alamat IP tersebut sama? 
alamat IP tujuan permintaan DNS:
![4-4.3.1](../assets/image/week%204%20&%205/4-4.3.1.png)
alamat IP server DNS lokal:
![4-4.3](../assets/image/week%204%20&%205/4-4.3.png)
Kedua gambar di atas menunjukkan bahwa alamat IP tujuan permintaan DNS maupun alamat IP server DNS lokal saya memiliki alamat IP yang sama yaitu 1.1.1.1
4. Periksa pesan permintaan DNS. Apa “jenis” atau ”type” dari pesan tersebut? Apakah pesan 
permintaan tersebut mengandung ”jawaban” atau ”answers”? 
![4-4.4](../assets/image/week%204%20&%205/4-4.4.png)
![4-4.4-1](../assets/image/week%204%20&%205/4-4.1.png)
Kedua gambar diatas menunjukkan Jenis atau Type dari pesan tersebut adalah 'A', kemudian pada bagian detail Domain Name System (query), terlihat nilai Answer RRs: 0, yang membuktikan bahwa paket tersebut murni hanya berisi pertanyaan (Questions: 1) dan belum memiliki informasi jawaban dari server.
5. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau ”answers” yang terdapat di 
dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut? 
![4-4.5](../assets/image/week%204%20&%205/4-4.5.png)
Berdasarkan gambar di atas, Terdapat 4 jawaban (answers), yang terdiri dari 3 record CNAME (www.mit.edu, www.mit.edu.edgekey.net, e9566.dscb.akamaiedge.net) dan 1 record Type A dengan alamat IP 23.15.150.186.
6. Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP 
pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS?
![4-4-6.1](../assets/image/week%204%20&%205/4-4.6.1.png)
![4-4-6.2](../assets/image/week%204%20&%205/4-4.6.2.png) 
Berdasarkan gambar di atas, alamat IP tujuan pada paket TCP SYN sinkron dengan hasil yang diberikan oleh DNS server sebelumnya.
7. Halaman web yang sebelumnya anda akses (http://www.ietf.org) memuat beberapa 
gambar. Apakah host Anda perlu mengirimkan pesan permintaan DNS baru setiap kali ingin 
mengakses suatu gambar? 
Tidak perlu, karena setelah queri DNS pertama selesai, alamat IP server akan disimpan dalam DNS cache lokal sehingga permintaan gambar selanjutnya pada domain yang sama dapat langsung menggunakan IP tersebut tanpa perlu bertanya kembali ke server DNS.

## Soal 2
1. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasan DNS? 
![trace-2.1.1](../assets/image/week%204%20&%205/trace-2.1.1.png)
![trace-2.1.2](../assets/image/week%204%20&%205/trace-2.1.2.png)
Port tujuan permintaan = 53
Port sumber balasan = 53
2. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda? 
![trace-2.2](../assets/image/week%204%20&%205/trace-2.2.png)
Berdasarkan gambar tersebut, pesan permintaan DNS dikirimkan ke alamat IP 128.238.29.22. dan ya, alamat tersebut merupakan default alamat IP server DNS lokal pada rekaman paket tersebut (trace file). Hal ini dibuktikan karena host pengirim langsung mengarahkan kueri DNS-nya ke IP tersebut untuk melakukan resolusi nama domain
3. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” atau ”answers”? 
1[trace-2.3](../assets/image/week%204%20&%205/trace-2.3.png)
Berdasarkan gambar di atas, pesan DNS tersebut memiliki jenis atau Type A (Host Address). Kemudian, pesan tersebut tidak mengandung jawaban (Answers).
4. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di 
dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut? 
![trace-2.4](../assets/image/week%204%20&%205/trace-2.4.png)
Berdasarkan analisis pada pesan balasan (Packet No. 20), terdapat 1 jawaban (Answer) utama yang memberikan informasi alamat IP dari host yang dicari. Isi yang terkandung dalam jawaban tersebut, yaitu Name: www.mit.edu, Type: A (Host Address), Address: 18.7.22.83.
5. Sertakan hasil tangkapan layar. 

## Soal 3
1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda? 
![manual.1](../assets/image/week%204%20&%205/manual.1.png)
![manual.1.1](../assets/image/week%204%20&%205/manual.1.1.png)
Berdasarkan kolom Destination pada paket nomor 119, pesan permintaan DNS dikirimkan ke alamat IP 8.8.8.8. serta alamat tersebut bukan alamat IP server DNS lokal saya, karena berdasarkan percobaan nslookup sebelumnya di terminal, alamat IP default server DNS lokal saya adalah 2404:c0:b200::3:1. Saya menggunakan 8.8.8.8 (DNS Google) secara manual agar permintaan tidak mengalami timeout
2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” atau ”answers”? 
![manual.2](../assets/image/week%204%20&%205/manual-2.png)
Berdasarkan gambar diatas, jenis pesan tersebut adalah NS dan tidak mengandung jawaban.
3. Periksa pesan balasan DNS. Apa nama server MIT yang diberikan oleh pesan balasan? 
Apakah pesan balasan ini juga memberikan alamat IP untuk server MIT tersebut? 
![manual.3](../assets/image/week%204%20&%205/manual-3.png)
Berdasarkan gambar tersebut, beberapa nama server MIT yang diberikan antara lain: ns1-173.akam.net, ns1-37.akam.net, usw2.akam.net, eur5.akam.net, dan asia1.akam.net. Kemudian, dalam pesan balasan tersebut, alamat IP untuk server-server tersebut tidak disertakan secara langsung dalam bagian Answer.
4. Sertakan hasil tangkapan layar.

## Soal 4
1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut 
merupakan default alamat IP server DNS lokal Anda?
![manual-2.1.1](../assets/image/week%204%20&%205/manual-2.1.1.png)
![manual-2.1.2](../assets/image/week%204%20&%205/manual-2.1.png) 
Berdasarkna gambar di atas, pesan permintaan DNS (Query) dikirimkan ke alamat IP 8.8.8.8, serta alamat tersebut bukan alamat IP server DNS lokal saya, karena berdasarkan percobaan nslookup sebelumnya di terminal, alamat IP default server DNS lokal saya adalah 2404:c0:b200::3:1. Saya menggunakan 8.8.8.8 (DNS Google) secara manual agar permintaan tidak mengalami timeout.
2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan 
tersebut mengandung ”jawaban” atau ”answers”? 
![manual-2.2](../assets/image/week%204%20&%205/manual-2.2.png)
Pesan tersebut adalah tipe A (Host Address), dan tidak mengandung jawaban.
3. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di 
dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut? 
![manual-2.3](../assets/image/week%204%20&%205/manual-2.3.png)
Terdapat 2 jawaban (answers) dalam pesan balasan, isi jawaban : www.aiit.or.kr: type A, class IN, addr 172.67.152.120 dan www.aiit.or.kr: type A, class IN, addr 104.21.74.8.
4. Sertakan hasil tangkapan layar.


## UDP
1. Pilih satu paket UDP yang terdapat pada trace Anda. Dari paket tersebut, berapa banyak 
“field” yang terdapat pada header UDP? Sebutkan nama-nama field yang Anda temukan! 
![5-1](../assets/image/week%204%20&%205/5.1.png)
Berdasarkan analisis pada paket UDP nomor 1 (get-request SNMP) dalam trace Wireshark, terdapat 4 field utama pada header UDP. Nama-nama field tersebut adalah:
Source Port,Destination Port,Length,Checksum.
2. Perhatikan informasi “content field” pada paket yang Anda pilih di pertanyaan 1. Berapa 
panjang (dalam satuan byte) masing-masing “field” yang terdapat pada header UDP? 
![5-2.1](../assets/image/week%204%20&%205/5.2.1.png)
![5.2.2](../assets/image/week%204%20&%205/5.2.2.png)
![5.2.3](../assets/image/week%204%20&%205/5.2.3.png)
![5.2.4](../assets/image/week%204%20&%205/5-2.4.png)
Berdasarkan pengamatan pada Packet Bytes untuk paket UDP nomor 1,
Source Port: Terdiri dari 2 byte (dalam gambar terlihat 10 ee). Nilai desimalnya adalah 4334, Destination Port: Terdiri dari 2 byte. Dalam gambar, ini adalah dua angka setelah kotak merah lo (00 a1). Nilai desimalnya adalah 161, Length: Terdiri dari 2 byte (setelah Destination Port). Di detail tertulis 58, maka di heksadesimalnya adalah 00 3a, Checksum: Terdiri dari 2 byte. Di gambar tertulis 65 f8.
3. Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui 
paket UDP pada trace. 
![5.3](../assets/image/week%204%20&%205/5.3.png)
Berdasarkan gambaar di atas, bagain kotak merah kedua, menunjukkan UDP payload (50 bytes), kemudian berdasarkan soal no.2 diperoleh total panjang header UDP adalah 8 byte. Sehingga verifikasi = 8 byte (Header) + 50 byte (Payload) = 58 byte.
Jadi, nilai "Length" adalah total ukuran header UDP ditambah datanya.
4. Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP? (Petunjuk: 
jawaban untuk pertanyaan ini dapat ditentukan dari jawaban Anda untuk pertanyaan 2)
Jumlah maksimum byte yang dapat disertakan dalam payload UDP adalah 65.527 byte. Karena field Length berukuran 16 bit, nilai maksimum totalnya adalah 2^16 - 1 = 65.535 byte. Karena header UDP memakan 8 byte, maka sisa untuk data adalah 65.535 - 8 = 65.527 byte.
5. Berapa nomor port terbesar yang dapat menjadi port sumber? (Petunjuk: lihat petunjuk 
pada pertanyaan 4) 
Berdasarkan petunjuk pada pertanyaan nomor 4, nomor port terbesar yang dapat menjadi port sumber (Source Port) adalah 65.535. karena Field Source Port pada header UDP memiliki panjang 2 byte atau 16 bit, dan Nilai maksimum yang dapat ditampung oleh 16 bit adalah 2^16 - 1 = 65.536.
6. Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan 
desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada 
datagram IP yang mengandung segmen UDP. 
![5.6](../assets/image/week%204%20&%205/5.6.png)
Notasi Desimal: 17, Notasi Heksadesimal: 0x11
7. Periksa pasangan paket UDP di mana host Anda mengirimkan paket UDP pertama dan paket 
UDP kedua merupakan balasan dari paket UDP yang pertama. (Petunjuk: agar paket kedua merupakan balasan dari paket pertama, pengirim paket pertama harus menjadi tujuan dari paket kedua). Jelaskan hubungan antara nomor port pada kedua paket tersebut! 
![5.7.1](../assets/image/week%204%20&%205/5.7.1.png)
![5.7.2](../assets/image/week%204%20&%205/5.7.2.png)
Pada paket pertama, port sumber (Source Port) adalah port dinamis dari host pengirim dan port tujuan (Destination Port) adalah port layanan server. Kemudian, pada paket kedua, port sumber pada paket balasan berubah menjadi 161 (dari server), dan port tujuannya kembali ke 4334 (ke host pengirim). jadi kesimpulannya adalah agar paket balasan sampai ke aplikasi yang tepat di host pengirim, server harus menukar posisi nomor port sumber dan tujuan dari paket permintaan yang diterimanya.