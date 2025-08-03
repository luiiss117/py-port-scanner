import asyncio, time, argparse, port_list
from collections import defaultdict

# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", required=True, help = "IPv4 address of the target host")
group = parser.add_mutually_exclusive_group()
parser.add_argument("-t", "--tasks", type=int, default=100, help = "Maximum number of tasks at once.")
parser.add_argument("--timeout", type=int, default=1, help = "Timeout in seconds.")
group.add_argument("--top-ports", type=int, choices=[10, 100], help = "Scan the top 5 ports.")
group.add_argument("-p", "--port", nargs="+",type=int, help = "Specify custom ports to scan, e.g: '-p 22 80")
group.add_argument("-p-", action="store_true", help = "Scan all ports.")
args = parser.parse_args()

results = defaultdict(list)
# Ports options
async def ports(num):
   if args.port:
      ports_to_scan = args.port
      print("Scanning", len(ports_to_scan), "ports...")
   elif args.p_:
      ports_to_scan = range(1, 65536)
      print(f"Scanning", len(ports_to_scan), " ports...")
   elif args.top_ports:
      ports_to_scan = port_list.top_list[num]
      print(f"Scanning {len(port_list.top_list[num])} ports...")
   else:
      ports_to_scan = port_list.top_list[1000]
      print(f"Scanning {len(ports_to_scan[:1000])} ports...")
   return ports_to_scan

# Port scan coroutine
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

# Main coroutine to create tasks
async def main():
   ports_to_scan = await ports(args.top_ports)
   semaphore = asyncio.Semaphore(args.tasks)
   tasks = []
   for p in ports_to_scan:
      tasks.append(scan(semaphore, p))
   await asyncio.gather(*tasks)

# Run timer and main
if __name__ == "__main__":
   try:
      start = time.time()
      print(f"Running {args.tasks} tasks simultaneously")
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

# Add the length of all lists
all_ports = len(results["open"]) + len(results["closed"]) + len(results["unresponsive"]) + len(results["error"])

print(f"Total open ports: {calculate_list_length('open')}")
print(f"Total closed ports: {calculate_list_length('closed')}")
print(f"Total unresponsive ports: {calculate_list_length('unresponsive')}")
print(f"Total error ports: {calculate_list_length('error')}")
print(f"Scanned {all_ports} TCP ports in {duration:.2f} seconds.")

