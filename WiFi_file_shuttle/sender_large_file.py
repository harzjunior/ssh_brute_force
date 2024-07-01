import socket
import threading
import time
from network_utils import get_local_ip

# Get local IP address
SENDER_IP = get_local_ip()
PORT = 12344
BROADCAST_PORT = 12346
BROADCAST_INTERVAL = 5  # seconds

def broadcast_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        while True:
            message = f"SENDER_IP:{SENDER_IP}".encode('utf-8')
            s.sendto(message, ('<broadcast>', BROADCAST_PORT))
            time.sleep(BROADCAST_INTERVAL)

# Start the broadcasting thread
threading.Thread(target=broadcast_ip, daemon=True).start()

print(f"Using IP: {SENDER_IP}")

# File to Send
filename = 'file_to_send_large.txt'

# Create a socket for file transfer
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind to IP and Port
    s.bind((SENDER_IP, PORT))
    
    # Listen for incoming connections
    s.listen()
    
    print(f"Sender listening on {SENDER_IP}:{PORT}")
    
    # Accept connection
    conn, addr = s.accept()
    with conn:
        print(f"Connected to {addr}")
        
        # Open file and send data
        with open(filename, 'rb') as f:
            total_sent = 0
            while True:
                data = f.read(1024)
                if not data:
                    break
                conn.sendall(data)
                total_sent += len(data)
                print(f"Sent {len(data)} bytes, total {total_sent} bytes.")
            
        print(f"Sent {filename} successfully, total {total_sent} bytes.")
