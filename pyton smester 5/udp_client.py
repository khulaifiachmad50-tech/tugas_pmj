import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Ketik pesan ke server (atau ketik 'exit' untuk keluar)\n")

while True:
    message = input("Pesan: ")
    if message.lower() == "exit":
        print("Menutup koneksi client...")
        break

    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    # Terima balasan dari server
    data, _ = client_socket.recvfrom(1024)
    print("Server:", data.decode())

client_socket.close()
