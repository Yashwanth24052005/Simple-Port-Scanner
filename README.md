# 🔍 Simple Port Scanner

A lightweight Python tool to scan open ports on a target machine, helping to identify potential vulnerabilities.

## 📌 Features
- Scans a range of ports on a target IP address.
- Uses Python's `socket` module to check open ports.
- Simple and easy-to-use command-line tool.

## 🛠️ Installation
Ensure you have **Python 3** installed on your system.

### Install dependencies (if needed)
```bash
pip install socket
🚀 Usage
Run the script with the following command:

bash
Copy
Edit
python port_scanner.py <target_ip> <start_port> <end_port>
Example:
bash
Copy
Edit
python port_scanner.py 192.168.1.1 20 100
This will scan ports 20 to 100 on the target machine.

⚠️ Disclaimer
This tool is for educational purposes only. Do not use it to scan devices without permission. Unauthorized scanning may violate laws and regulations.

📜 License
This project is open-source under the MIT License.
