#!/usr/bin/env python3
"""
Phase 2 - Block 03: Lesson 2
Multi-Port Scanner & Service Banner Grabbing
"""
import socket

target_host = "127.0.0.1"
target_ports = [21, 22, 80, 443, 8080]

print("==========================================")
print(f"Scanning Host: {target_host}")
print("==========================================")

for port in target_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5)
    
    code = s.connect_ex((target_host, port))
    
    if code == 0:
        banner = "No banner received"
        try:
            # Attempt to read up to 1024 bytes from the service
            raw_data = s.recv(1024)
            if raw_data:
                banner = raw_data.decode("utf-8", errors="ignore").strip()
        except socket.timeout:
            banner = "Connection opened (No auto-banner sent)"
        
        print(f"[OPEN]   Port {port:<5} | Banner: {banner}")
    else:
        print(f"[CLOSED] Port {port:<5}")
        
    s.close()

print("==========================================")
