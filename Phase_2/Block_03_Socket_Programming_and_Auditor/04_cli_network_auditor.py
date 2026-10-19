#!/usr/bin/env python3
"""
Phase 2 - Block 03: Lesson 4
Building a CLI Network Auditor Tool
"""
import socket
import json
import sys

if len(sys.argv) < 2:
    print("Error: Missing target IP!")
    print("Usage: python3 04_cli_network_auditor.py <target_ip>")
    sys.exit(1)

target_host = sys.argv[1]
target_ports = [21, 22, 80, 443, 8080]
audit_report = []

print("==========================================")
print(f"CLI Network Auditor -> Target: {target_host}")
print("==========================================")

for port in target_ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.5)
    
    code = s.connect_ex((target_host, port))
    
    if code == 0:
        status = "OPEN"
        banner = "No banner"
        try:
            s.send(b"HEAD / HTTP/1.1\r\nHost: " + target_host.encode() + b"\r\n\r\n")
            raw_data = s.recv(1024)
            if raw_data:
                banner = raw_data.decode("utf-8", errors="ignore").split("\r\n")[0].strip()
        except Exception:
            banner = "Open (No banner response)"
    else:
        status = "CLOSED"
        banner = "N/A"

    print(f"[{status:<6}] Port {port:<5} | Banner: {banner}")

    audit_report.append({
        "target": target_host,
        "port": port,
        "status": status,
        "banner": banner
    })
    s.close()

with open("audit_report.json", "w") as outfile:
    json.dump(audit_report, outfile, indent=4)

print("==========================================")
print("Audit Complete! Report saved to audit_report.json")
print("==========================================")
