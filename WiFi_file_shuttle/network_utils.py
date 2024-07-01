import socket
import platform
import subprocess

def is_ip_available(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    return subprocess.call(command) != 0

def get_local_ip():
    # Use a socket to connect to an external IP to get the local IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to connect to an actual server, just needs to be valid
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()
