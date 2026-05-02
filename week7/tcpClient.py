from socket import * #import semua method yang ada di socket module

#server port

serverName = 'localhost'
serverPort = 8080


#client socket
clientSocket = socket(AF_INET, SOCK_STREAM) # AF_INET = IPv4, SOCK_STREAM = TCP

#connect ke server
clientSocket.connect((serverName, serverPort)) #menghubungkan client ke server dengan alamat dan port yang telah ditentukan

#send message to server
sentence = input('input lowercase sentence: ') #input dari user
clientSocket.send(sentence.encode()) #mengirim pesan ke server, encode merubah menjadi biner

#receive message from server
modifiedSentence = clientSocket.recv(1024) #menerima pesan dari server, 1024 = buffer size, ukuran maksimal data yang bisa diterima dalam satu kali pengiriman
print('From Server: ', modifiedSentence.decode()) #menampilkan pesan yang diterima dari server, decode merubah menjadi string

clientSocket.close() #menutup socke