#!/usr/bin/env python3
"""
Phase 2 - Block 04: Lesson 2
Building a TCP SYN Scanner with Scapy
"""
from scapy.all import IP, TCP, sr1
target_host = "127.0.0.1"
target_port = [21, 22, 80, 443,8080]
print(f"=== TCP SYN Scan Target: {target_host} ===")
for port in target_port:
    pkt = IP(dst=target_host)/TCP(dport=port, flags="S")
    resp = sr1(pkt, timeout=1, verbose=0)
    if resp and resp.haslayer(TCP):
        flags = resp[TCP].flags
        if flags == "SA":
            status = "OPENED (SYN-ACK)"
        elif flags == "RA":
            status = "CLOSED (RST-ACK)"
        else:
            status = f"RESPONSE ({flags})"
    else:
        status = f"Filtered / No Reponse ({flags})"
    print(f"Port {port:<5} | Status: {status}")

