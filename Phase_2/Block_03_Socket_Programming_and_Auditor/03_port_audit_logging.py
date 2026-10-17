#!/usr/bin/env python3
"""
Phase 2 - Block 03: Lesson 3
Port Audit Logging & JSON Report Generation
"""
import socket
import json

target_host = "127.0.0.1"
target_ports = [21, 22, 80, 443, 8080]
audit_report = []

print("==========================================")
print(f"Starting Network Audit: {target_host}")

for port in target_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5)
    
    code = s.connect_ex((target_host, port))
    
    if code == 0:
        banner = "No banner"
        try:
            raw_data = s.recv(1024)
            if raw_data:
                banner = raw_data.decode("utf-8", errors="ignore").strip()
        except socket.timeout:
            banner = "Connection opened (No auto-banner)"
            
        print(f"[OPEN] Port {port}")
        audit_report.append({
            "target": target_host,
            "port": port,
            "status": "OPEN",
            "banner": banner
        })
    else:
        print(f"[CLOSED] Port {port}")
        
    s.close()

with open("audit_report.json", "w") as outfile:
    json.dump(audit_report, outfile, indent=4)

print("==========================================")
print(f"Audit complete! Generated audit_report.json with {len(audit_report)} open findings.")
print("==========================================")
