# py-port-scanner
A simple TCP port scanner in Python that scan all 65 535 TCP ports on a given host, categorize results as open/closed/unresponsive, and display a concise summary.


## 🚀 Features

- **Full TCP port scan** (0–65535)  
- **Port state classification**: open, closed, unresponsive  
- **Lightweight & no external dependencies**  
- **IPv4 support**  

---

## 🛠️ Installation

1. Clone the repository:

```
$ git clone https://github.com/your-username/py-port-scanner.git
$ cd py-port-scanner
```
---

## Usage
```
$ python3 port_scanner.py -i <TARGET_IP>
```
---

## Example
```
$ python3 port_scanner.py -i 127.0.0.1
[+] Port 53 is open.
[+] Port 42225 is open.
Total open ports: 2
Total closed ports: 65533
Total unresponsive ports: 0
Scanned 65535 TCP ports in 1.20 seconds.
```

