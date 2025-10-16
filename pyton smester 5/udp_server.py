import socket
from datetime import datetime

# Konfigurasi server
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
LOG_FILE = "server_log.txt"

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"Server UDP berjalan di {SERVER_IP}:{SERVER_PORT}")
print("Menunggu pesan dari client...\n")

# Variabel untuk menghitung jumlah pesan
total_messages = 0

while True:
    # Terima pesan dari client
    data, client_address = server_socket.recvfrom(BUFFER_SIZE)
    message = data.decode().strip()
    total_messages += 1

    # Waktu dan log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Dari {client_address}: {message}\n"

    # Simpan log ke file
    with open(LOG_FILE, "a") as file:
        file.write(log_entry)

    print(log_entry, end="")
    print(f"Total pesan diterima: {total_messages}\n")

    # ==== Logika Balasan ====
    message_lower = message.lower()
    if "halo" in message_lower:
        reply = f"Halo juga! Senang bisa menerima pesanmu ({timestamp})"
    elif "apa kabar" in message_lower:
        reply = "Saya server, selalu siap sedia 24 jam 😄"
    elif "waktu" in message_lower:
        reply = f"Sekarang waktu server adalah {timestamp}"
    elif "terima kasih" in message_lower:
        reply = "Sama-sama! 😊"
    else:
        reply = f"Pesan '{message}' telah diterima pada {timestamp}"

    # Kirim balasan ke client
    server_socket.sendto(reply.encode(), client_address)
