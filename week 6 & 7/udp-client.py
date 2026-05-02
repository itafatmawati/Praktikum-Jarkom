from socket import * #import semua method yang ada di socket module

serverName = 'localhost'
serverPort = 12000 

clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET = IPv4, SOCK_DGRAM = UDP

running = True
while running:
    message = input("> ") #input dari user

    #Exit, EXIT, Exit, eXit, exiT, exIt, ExiT, EXIt, eXIT
    if message.lower() == "exit":
        clientSocket.sendto(message.encode(), 
                            (serverName, serverPort)
                            ) #mengirim pesan ke server bahwa client ingin keluar
        print("[SYSTEM] keluar dari program")#encode merubah menjadi biner
        running = False
        continue

        #mengirim pesan 
    clientSocket.sendto(
        message.encode(), 
        
        #x,y
        (serverName, serverPort)
    )
        
    #menerima pesan
    clientSocket.recvfrom(2048) #2048 = buffer size, ukuran maksimal data yang bisa diterima dalam satu kali pengiriman
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) #menerima pesan dari server, modifiedMessage = pesan yang diterima, serverAddress = alamat server yang mengirim pesan

    print("[system] pesan telah diterima dari : ", serverAddress) #menampilkan alamat server yang mengirim pesan
    print(modifiedMessage.decode()) #decode merubah menjadi string

clientSocket.close()
print("[SYSTEM] socket telah ditutup")