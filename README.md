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

* Python 3.x installed on your system.
* No additional 3rd-party modules or `pip` installations required (uses standard library modules: `socket`, `time`).

### Installation

Clone the repository to your local system:

```bash
git clone [https://github.com/nihalhyder/port-scanner.git](https://github.com/nihalhyder/port-scanner.git)
cd port-scanner
