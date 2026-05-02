from socket import *

#mmembuat socket untuk server
serverport = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET = IPv4, SOCK_DGRAM = UDP

#menghubungkan 
serverSocket.bind(
    #tuple
    ('',serverport)
)

print("[SYSTEM] server siap menerima pesan")

running = True
while running:
    message, clientAddress = serverSocket.recvfrom(2048) #2048 = buffer size, ukuran maksimal data yang bisa diterima dalam satu kali pengiriman

    decodeMessage = message.decode() #decode merubah menjadi string

    if decodeMessage.lower() == "exit":
        print("[SYSTEM] keluar dari program")#encode merubah menjadi biner
        running = False
        continue

    ModifiedMessage = decodeMessage.upper() #mengubah pesan menjadi huruf besar
    print("[SYSTEM] diterima dari ", clientAddress, "message: ", decodeMessage ) #menampilkan alamat client yang mengirim pesan

    #mengirim pesan ke client
    serverSocket.sendto(
        ModifiedMessage.encode(), #encode merubah menjadi biner
        
        #x,y
        clientAddress
    )

serverSocket.close()
print("[SYSTEM] socket telah ditutup")