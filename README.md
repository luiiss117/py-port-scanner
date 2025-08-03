# py-port-scanner
An asynchronous TCP port scanner in Python that scan all 65 535 TCP ports on a given host, categorize results and display a concise summary.


## 🚀 Features

- **Full TCP port scan** (1–65535)  
- **Port state classification**: open, closed, unresponsive  
- **Lightweight & no external dependencies**  
- **IPv4 support**
- **Timeout configuration**
- **Top ports scan (10 or 100 most common) with --top-ports 10|100| (scan 1000 ports by default)**
- **Number of maximum tasks to run simultaneously**  

---

## 🛠️ Installation

1. Clone the repository and it is ready to run:

```
git clone https://github.com/luiiss117/py-port-scanner.git
cd py-port-scanner
python3 port_scanner.py
```
---

## ⚡️ Usage
```
python3 port_scanner.py -i <TARGET_IP>
```
---

## 💡 Example
```
port_scanner.py -i 127.0.0.1 --top 100 -t 50 --timeout 2 
Running 50 tasks simultaneously
Scanning 100 ports...
[+] Port: 80 is open
[+] Port: 135 is open
[+] Port: 443 is open
[+] Port: 445 is open
[+] Port: 5357 is open
Total open ports: 5
Total closed ports: 0
Total unresponsive ports: 95
Total error ports: 0
Scanned 100 TCP ports in 4.04 seconds.
```

