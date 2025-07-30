import socket
import time
from collections import defaultdict
import argparse

# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--ip", help = "IPv4 address of the target host")
parser.parse_args()
args = parser.parse_args()

host_ip = args.ip

results = defaultdict(list)

# Initialize timer
start = time.time()

# Port scan function that scans all 65535 TCP ports
def scan():
   for port in range(1, 65536):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(0.5)
      try:
         result = s.connect_ex((host_ip, port))
         if result == 0:
            print(f"[+] Port {port} is open.")
            results["open"].append(port)
         else:
            results["closed"].append(port)
      except socket.timeout:
         print("Connection timed out")
         results["unresponsive"].append(port)
      finally:
         s.close()

# Calling the scan function
scan()

# End timer
end = time.time()
duration = end - start

# Calculate the total length of the lists
def calculate_list_length(x):
   list_length = len(results[x])
   return list_length

# Adds the length of all lists
all_ports = len(results["open"]) + len(results["closed"]) + len(results["unresponsive"])

print(f"Total open ports: {calculate_list_length('open')}")
print(f"Total closed ports: {calculate_list_length('closed')}")
print(f"Total unresponsive ports: {calculate_list_length('unresponsive')}")
print(f"Scanned {all_ports} TCP ports in {duration:.2f} seconds.")
exit(0)
