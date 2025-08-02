import time
from collections import defaultdict
import argparse
import asyncio

# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help = "IPv4 address of the target host")
parser.add_argument("-t", "--tasks", type=int, default=100, help = "Maximum number of tasks at once.")
parser.add_argument("--timeout", type=int, default=1, help = "Timeout in seconds.")
args = parser.parse_args()



if args.ip == None:
   print("Error, an IP address is necessary")    
   exit(1)

max_tasks = args.tasks
timeout = args.timeout

ports_to_scan =  65536

results = defaultdict(list)

# Port scan coroutine that scans all 65535 TCP ports 
async def scan(semaphore, port):
   async with semaphore:   
      try:
         conn = asyncio.open_connection(args.ip, port)
         reader, writer = await asyncio.wait_for(conn, timeout=args.timeout)
         writer.close()
         await writer.wait_closed()
         print(f"[+] Port: {port} is open")
         results["open"].append(port)
       # Exceptions for errors  
      except ConnectionRefusedError:
         results["closed"].append(port)
      except asyncio.TimeoutError:
         results["unresponsive"].append(port)
      except OSError:
         results["error"].append(port)
# Main coroutine
async def main():
   semaphore = asyncio.Semaphore(args.tasks) 
   tasks = []    
   for p in range(1, ports_to_scan):
      tasks.append(scan(semaphore, p)) 
   await asyncio.gather(*tasks)

# Run timer and main
try:
   start = time.time()
   print(f"Running {max_tasks} tasks at once") 
   asyncio.run(main())
except KeyboardInterrupt:
    print("Stopped")
finally:
   end = time.time()
   duration = end - start


# Calculate the total length of the lists
def calculate_list_length(status_of_port):
   list_length = len(results[status_of_port])
   return list_length

# Adds the length of all lists
all_ports = len(results["open"]) + len(results["closed"]) + len(results["unresponsive"]) + len(results["error"])

print(f"Total open ports: {calculate_list_length('open')}")
print(f"Total closed ports: {calculate_list_length('closed')}")
print(f"Total unresponsive ports: {calculate_list_length('unresponsive')}")
print(f"Total error ports: {calculate_list_length('error')}")
print(f"Scanned {all_ports} TCP ports in {duration:.2f} seconds.")
