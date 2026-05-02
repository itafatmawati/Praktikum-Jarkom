## Laporan Praktikum Modul 7

## Program Socket dengan UDP 
 Pada UDP, sebelum data dikirim, proses pengirim harus menyertakan alamat tujuan yang terdiri dari alamat IP dan nomor port agar paket dapat dirutekan oleh jaringan ke soket yang tepat pada host tujuan. Setelah paket sampai, proses penerima mengambil data dari soket dan memprosesnya sesuai kebutuhan. Karena satu host dapat menjalankan banyak aplikasi sekaligus, nomor port digunakan untuk membedakan tiap soket. Selain alamat tujuan, paket juga memiliki alamat sumber (IP dan port pengirim) yang biasanya ditambahkan secara otomatis oleh sistem operasi tanpa perlu diatur langsung oleh aplikasi.

# UDPClient.py 
Contoh Kode dan Penjelasan:
![UDP CLIENT](../assets/image/week%207/UDP-CLIENT.png)

# UDPServer.py
Contoh Kode dan Penjelasan:
![UDP SERVER](../assets/image/week%207/UDP-SERVER.png)

# Output keduanya
![OUTPUT UDP](../assets/image/week%207/OUTPUT-UDP.png)

## Program Socket dengan TCP
TCP merupakan protokol berorientasi koneksi, yang berarti sebelum proses client dan server dapat bertukar data, keduanya harus melakukan proses handshake untuk membangun koneksi terlebih dahulu. Koneksi ini menghubungkan soket client dan soket server menggunakan alamat IP dan nomor port masing-masing. Berbeda dengan UDP, pada TCP data dapat langsung dikirim melalui koneksi tanpa perlu melampirkan alamat tujuan setiap kali mengirim. Server harus aktif terlebih dahulu dan menyediakan soket khusus sebagai “pintu penyambutan” untuk menerima koneksi dari client. Setelah koneksi terbentuk melalui proses three-way handshake (yang terjadi secara otomatis di layer transport), server akan membuat soket baru yang didedikasikan untuk setiap client. TCP menjamin pengiriman data secara andal, berurutan, dan tanpa kehilangan, sehingga komunikasi antara client dan server menjadi lebih stabil.

# TCPClient.py
Contoh Kode dan Penjelasan:
![TCP CLIENT](../assets/image/week%207/TCP-CLIENT.png)

# TCPServer.py
Contoh KOde dan Penjelasan:
![TCP SERVER](../assets/image/week%207/TCP-SERVER.png)

# Output keduanya 
![OUTPUT TCP](../assets/image/week%207/OUTPUT-TCP.png)

## Kesimpulan 
Pemrograman soket pada aplikasi jaringan client-server dapat dilakukan menggunakan dua protokol utama, yaitu UDP dan TCP, yang memiliki karakteristik berbeda. UDP bersifat connectionless sehingga pengiriman data dilakukan tanpa membangun koneksi terlebih dahulu, dengan setiap paket harus menyertakan alamat tujuan secara eksplisit. Sebaliknya, TCP bersifat connection-oriented yang mengharuskan adanya proses handshake sebelum komunikasi dimulai, sehingga memungkinkan pengiriman data yang lebih andal, terurut, dan tanpa kehilangan. Dalam implementasinya, TCP menggunakan soket tambahan di sisi server untuk menangani setiap koneksi client secara khusus, sedangkan UDP tidak. Oleh karena itu, pemilihan antara UDP dan TCP bergantung pada kebutuhan aplikasi, apakah lebih mengutamakan kecepatan dan kesederhanaan (UDP) atau keandalan dan konsistensi data (TCP).

