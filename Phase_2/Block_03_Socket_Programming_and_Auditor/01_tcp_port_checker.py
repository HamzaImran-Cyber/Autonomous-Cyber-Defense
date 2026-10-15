#!/usr/bin/env python3
"""
Phase 2 - Block 03: Lesson 1
Basic TCP Socket Connection & Port Auditor
"""
import socket
target_host = "127.0.0.1"
port = 22
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2.0)
print("=============================================")
print(f"Auditing Target : {target_host}:{port}")
code = s.connect_ex((target_host, port))
if code == 0:
    print(f"Port Status     : [OPEN] Port {port} is active")
else:
    print(f"Port Status     : [CLOSED] Port {port} is inactive (Code: {code})")
s.close()
print("=============================================")
