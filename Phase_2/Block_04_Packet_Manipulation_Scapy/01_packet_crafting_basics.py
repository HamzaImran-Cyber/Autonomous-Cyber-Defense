#!/usr/bin/env python3
"""
Phase 2 - Block 04: Lesson 1
Introduction to Scapy & Packet Crafting
"""
from scapy.all import IP, TCP, sr1
target_ip = "127.0.0.1"
target_port = 80
packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")
print("===== Crafted Packet Details ====")
packet.show()
print("\nSending SYN packet ....")
response = sr1(packet, timeout=2, verbose=0)
if response:
    print(f"[+] Received response from: {response.src}")
    if response.haslayer(TCP):
        print(f"[+] TCP Response Flags: {response[TCP].flags}")
else:
    print("[-] No response received (Port closed or filtered)")
