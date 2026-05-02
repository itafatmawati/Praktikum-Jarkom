from socket import * #import semua method yang ada di socket module

serverport = 8080

serverSocket = socket(AF_INET, SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = TCP

serverSocket.bind(('', serverport)) #mengikat socket ke alamat dan port yang telah ditentukan

serverSocket.listen(5) #mendengarkan koneksi masuk, 5 = jumlah maksimal koneksi yang dapat diterima dalam satu waktu
print("The server is ready to receive")

serverSocket.settimeout(1) #mengatur timeout untuk socket, 1 detik

try: 
    while True:
        try: 
            connectionSocket, addr = serverSocket.accept() #menerima koneksi masuk, connectionSocket = socket yang digunakan untuk berkomunikasi dengan client, addr = alamat client yang terhubung
            print("[SYSTEM] koneksi diterima dari : ", addr) #menampilkan alamat client yang terhubung

            sentence = connectionSocket.recv(1024).decode() #menerima pesan dari client, 1024 = buffer size, ukuran maksimal data yang bisa diterima dalam satu kali pengiriman
            print("[SYSTEM] pesan telah diterima dari : ", addr) #menampilkan alamat client yang mengirim pesan
            
            modifiedSentence = sentence.upper() #mengubah pesan menjadi huruf kapital
            print("[SYSTEM] mengirim kembali pesan :", modifiedSentence)
            connectionSocket.send(modifiedSentence.encode()) #mengirim pesan ke client, encode merubah menjadi biner

            connectionSocket.close() #menutup koneksi dengan client
        except timeout:
            continue #jika terjadi timeout, lanjutkan ke iterasi berikutnya untuk menerima koneksi baru

except KeyboardInterrupt:
    print("\n[SYSTEM] Server dihentikan oleh user.")
    
finally:
    serverSocket.close() #menutup socket server jika terjadi error atau interupsi
    print("[SYSTEM] Server telah dihentikan.")