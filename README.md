# SSH Brute-Force Script

This Python script demonstrates a simple SSH brute-force attack using multi-threading. It attempts to log into an SSH server with various password combinations.

## Requirements

- Python 3.x
- Paramiko library (`pip install paramiko`)

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/ssh_brute_force.git
   cd ssh_brute_force
   ```

2. **Install Dependencies:**

   Install the required Python libraries using pip:

   ```bash
   pip install paramiko
   ```

3. **Configure the Script:**

   Edit `ssh_brute_multi_thread.py` to specify:
   - `target_ip`: IP address of the SSH server.
   - `username`: SSH username.
   - `max_password_length`: Maximum length of passwords to attempt.

4. **Run the Script:**

   Execute the script using Python:

   ```bash
   python ssh_brute_multi_thread.py
   ```

5. **Monitor Output:**

   The script will attempt to brute-force the SSH server with various password combinations. Monitor the console output for success or failure messages.

## Notes

- **Legal Considerations:** Use this script responsibly and only on systems you own or have explicit permission to test. Unauthorized access attempts are illegal.
  
- **Performance:** Actual cracking times may vary based on network latency, SSH server response times, and system performance.

## Warning

- **Ethical Use:** This script is for educational purposes only. Unauthorized access to computer systems is illegal and unethical. Use responsibly and at your own risk.

## Credits

- Original script concept and guidance: ChatGPT (OpenAI)
- Scope, requirements, and implementation: Your Name (harzjunior@gmail.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.