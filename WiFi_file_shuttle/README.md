# WiFi File Shuttle

WiFi File Shuttle is a Python-based tool that allows you to transfer files between devices on the same WiFi network using IP protocol. It features dynamic IP discovery and efficient data transfer using TCP sockets.

⚠️ **Security Notice**: This tool is designed for use on trusted local networks. Please consider the following security implications:

## Security Considerations

- **Local Network Usage**: Ensure that you use WiFi File Shuttle only on trusted WiFi networks where you control the devices.
- **IP Address Exposure**: Broadcasting and discovering IP addresses can expose device information within the local network.
- **Encryption**: Files transferred using this tool are not encrypted. Avoid transferring sensitive information unless the network is secure.
- **Authentication**: Implement additional authentication mechanisms if transferring sensitive files.

## Features

- **Dynamic IP Discovery**: Automatically discovers the sender's IP address.
- **File Transfer**: Transfers files in chunks to handle large files efficiently.
- **Broadcasting**: Uses UDP broadcasting to announce the sender's IP address.

## Requirements

- Python 3.x
- NetworkUtils module for obtaining local IP addresses and checking IP availability

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/harzjunior/WiFi_file_shuttle.git
    cd WiFi_file_shuttle
    ```

2. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure the `network_utils.py` file is present in the same directory**.

## Usage

### Sender

1. **Prepare the file to send**:
    - Place the file you want to send in the same directory and name it `file_to_send_large.txt` (or update the filename in the script).

2. **Run the sender script**:
    ```bash
    python sender_large_file.py
    ```

3. **Output**:
    - The sender will start broadcasting its IP address and listen for connections.
    - Example output:
      ```
      Using IP: 192.168.43.128
      Sender listening on 192.168.43.128:12344
      Connected to ('192.168.43.129', 12345)
      Sent 1024 bytes, total 2048 bytes.
      ...
      Sent file_to_send_large.txt successfully, total 1048576 bytes.
      ```

### Receiver

1. **Run the receiver script**:
    ```bash
    python receiver_larger_file.py
    ```

2. **Output**:
    - The receiver will listen for the sender's IP address and connect to it.
    - Example output:
      ```
      Listening for sender IP address...
      Discovered sender IP: 192.168.43.128
      Received 1024 bytes, total 2048 bytes.
      ...
      Received 1048576 bytes successfully.
      ```

3. **Received File**:
    - The received file will be saved as `received_file.txt` in the same directory.

## File Structure

```
WiFi_file_shuttle/
├── network_utils.py
├── sender.py
├── sender_large_file.py
├── receiver_larger_file.py
├── receiver.py
├── file_to_send.txt
├── file_to_send_large.txt
├── received_file.txt
├── received_file_large.txt
└── README.md
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## Credits

- **Concept and Guidance**: ChatGPT (OpenAI)
- **Implementation and Customization**: [@harzjunior](https://github.com/harzjunior)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.