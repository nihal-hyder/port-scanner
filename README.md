# 🔍 Multi-Threaded TCP/UDP Banner Grabbing Port Scanner

A lightweight, multi-protocol command-line network reconnaissance tool written in pure Python. This scanner identifies open TCP and UDP ports, resolves service names, grabs version banners for active services, and supports target batches—all without external dependencies.

---

## 🌟 Key Features

* **Dual Protocol Support:** Performs scanning on both **TCP** (`socket.SOCK_STREAM`) and **UDP** (`socket.SOCK_DGRAM`) protocols.
* **Service Name Resolution:** Maps open ports to standard service names (e.g., HTTP, SSH, FTP) using `socket.getservbyport()`.
* **Proactive Banner Grabbing:** Extracts software and version information from responsive services (such as HTTP response headers, SSH banners, and FTP greetings).
* **Multi-Target Scanning:** Supports scanning multiple IP addresses simultaneously via comma-separated inputs.
* **Execution Profiling:** Uses high-precision timers (`time.perf_counter()`) to calculate accurate runtime performance.
* **Colorized Terminal UI:** Clean, color-coded output highlighting active ports in green and script headers in red.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10.0 installed on your system.
* No additional 3rd-party modules or `pip` installations required (uses standard library modules: `socket`, `time`).

### Installation

Clone the repository to your local system:

```bash
git clone https://github.com/nihal-hyder/port-scanner-python
cd port-scanner

```

---

## 💻 Usage

Run the scanner directly using Python:

```bash
python main.py

```

### Interactive Prompts

When executed, the program will ask for three inputs:

1. **Target IP Address(es):** Enter a single IP or multiple comma-separated IPs (e.g., `192.168.1.1` or `127.0.0.1, 192.168.1.254`).
2. **Port Range Limit:** Enter the maximum port number to scan up to (e.g., `100` scans ports 1 through 100).
3. **Scan Mode:** Specify the protocol (`tcp` or `udp`).

### Sample Output

```text
  ___  ___  ___ _____   ___  ___   _   _  _  _ _____ ___ 
 | _ \/ _ \| _ \_   _| / __|/ __| /_\ | \| || | | __| _ \
 |  _/ (_) |   / | |   \__ \ (__ / _ \| .` || |_| _||   /
 |_|  \___/|_|_\ |_|   |___/\___/_/ \_\_|\_| \___/___|_|_\ 

Made by : Nihal Hyder
My GitHub account : https://github.com/nihal-hyder

Enter IP address(es) (split by comma): 127.0.0.1
Enter max port number to scan (e.g. 100): 100
Enter scan protocol (tcp/udp): tcp
[*] Target count: 1 IP address(es)

[*] Scanning target: 127.0.0.1 (TCP mode)...
[+] 22/TCP OPEN | Service: ssh | Version: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.6
[+] 80/TCP OPEN | Service: http | Version: Apache/2.4.52 (Ubuntu)

total time it tooks to scan the port(s) 1.241503921 seconds

```

---

## 🛠️ How It Works

1. **TCP Scanning:** Attempts socket connections with a 0.5-second connection timeout. If successful, the port is flagged as open, and a banner probe is initiated.
2. **HTTP Probing:** For web ports (`80`, `8080`, `8000`, `443`), the scanner sends a raw `HEAD / HTTP/1.1` request to trigger a `Server:` header response before reading incoming socket bytes.
3. **UDP Probing:** Transmits a datagram payload (`Ping`) to the target port. Received responses or lack of ICMP unreachable errors indicate port availability.

---

## 👤 Author

* **Nihal Hyder**
* GitHub: [@nihalhyder](https://www.google.com/url?sa=E&source=gmail&q=[https://github.com/nihalhyder](https://github.com/nihal-hyder))

---

## ⚠️ Disclaimer

This tool is designed strictly for educational, security research, and network auditing purposes on authorized systems. Unauthorized port scanning against targets without explicit permission may violate applicable local and international laws.
