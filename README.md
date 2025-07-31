# py-port-scanner
An asynchronous TCP port scanner in Python that scan all 65 535 TCP ports on a given host, categorize results and display a concise summary.


## 🚀 Features

- **Full TCP port scan** (0–65535)  
- **Port state classification**: open, closed, unresponsive  
- **Lightweight & no external dependencies**  
- **IPv4 support**  

---

## 🛠️ Installation

1. Clone the repository:

```
$ git clone https://github.com/luiiss117/py-port-scanner.git
$ cd py-port-scanner
```
---

## ⚡️ Usage
```
$ python3 port_scanner.py -i <TARGET_IP>
```
---

## 💡 Example
```
python3 port_scanner.py -i 127.0.0.1 -t 500 --timeout 3
Running 500 tasks at once
[+] Port: 53 is open
[+] Port: 45815 is open
[+] Port: 55788 is open
Total open ports: 3
Total closed ports: 65532
Total unresponsive ports: 0
Total error ports: 0
Scanned 65535 TCP ports in 19.48 seconds.
```

