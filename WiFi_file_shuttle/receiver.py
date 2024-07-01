import socket

BROADCAST_PORT = 12346
DISCOVERY_TIMEOUT = 10  # seconds

def listen_for_sender_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind(('', BROADCAST_PORT))
        s.settimeout(DISCOVERY_TIMEOUT)
        try:
            message, address = s.recvfrom(1024)
            if message.startswith(b"SENDER_IP:"):
                return message[len("SENDER_IP:"):].decode('utf-8')
        except socket.timeout:
            return None

# Listen for sender IP address
print("Listening for sender IP address...")
SENDER_IP = listen_for_sender_ip()
if SENDER_IP is None:
    print("Failed to discover sender IP address.")
    exit()

print(f"Discovered sender IP: {SENDER_IP}")
PORT = 12345

# Save received file as
filename = 'received_file.txt'

# Create a socket for file transfer
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # Connect to sender
        s.connect((SENDER_IP, PORT))
        
        # Receive file data
        with open(filename, 'wb') as f:
            total_received = 0
            while True:
                data = s.recv(1024)
                if not data:
                    break
                f.write(data)
                total_received += len(data)
                print(f"Received {len(data)} bytes, total {total_received} bytes.")
                
        print(f"Received {total_received} bytes successfully.")
    except ConnectionRefusedError:
        print("Connection refused. Make sure the sender is running.")
