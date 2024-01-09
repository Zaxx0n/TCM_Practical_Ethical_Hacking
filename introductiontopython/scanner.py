#!/bin/python3

import sys
import socket
from datetime import datetime

dt = datetime.now

# Define our Target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

# Add a Pretty Banner
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Could not connect to the server.")
	sys.exit()
