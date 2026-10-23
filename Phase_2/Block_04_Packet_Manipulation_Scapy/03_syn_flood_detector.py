#!/usr/bin/env python3
"""
Phase 2 - Block 04: Lesson 3
Defensive Traffic Monitoring & SYN Flood Detection
"""
from scapy.all import IP, TCP, sniff
from collections import defaultdict

pending_syns = defaultdict(int)
THRESHOLD = 3

def analyze_packet(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        src_ip = pkt[IP].src
        flags =  pkt[TCP].flags
        
        if flags == "S":
            pending_syns[src_ip] += 1
            print(f"[+] SYN from {src_ip} | Pending: {pending_syns[src_ip]}")
            if pending_syns[src_ip] >= THRESHOLD:
                print(f"[ALERT] POTENTIAL SYN FLOOD DETECTED FROM {src_ip}!")
        elif "A" in flags and src_ip in pending_syns:
            if pending_syns[src_ip] > 0:
                pending_syns[src_ip] -= 1
                print(f"[-] Handshake completed for {src_ip} | Pending reset to: {pending_syns[src_ip]}")

print("=== Stateful SYN Flood Detector Active (Listening on 'lo' interface) ===")

sniff(iface="lo", filter="tcp and host 127.0.0.1", prn=analyze_packet, count=6)

