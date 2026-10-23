#!/usr/bin/env python3
"""
Phase 2 - Block 04: Lesson 4
Packet Sniffing & PCAP Logging with Scapy
"""
import os
from scapy.all import IP, TCP, sniff, wrpcap, rdpcap

# 1. Generate absolute path so sudo reads/writes from the exact script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
pcap_file = os.path.join(script_dir, "captured_traffic.pcap")

print("==== Sniffing 5 Packets on 'lo' ====")

# 2. Sniff 5 TCP packets on loopback
packets = sniff(iface="lo", filter="tcp", count=5)
print(f"[+] Captured {len(packets)} packets in memory.")

# 3. Call wrpcap() as a FUNCTION (not assignment)
wrpcap(pcap_file, packets)
print(f"[+] Saved raw packets to disk: {pcap_file}")

print("\n=== Reading PCAP File back into Scapy ===")

# 4. Read the file back from disk
offline_pkts = rdpcap(pcap_file)
print(f"[+] Loaded {len(offline_pkts)} packets from {pcap_file}:\n")

for idx, pkt in enumerate(offline_pkts, 1):
    if pkt.haslayer(TCP):
        src = pkt[IP].src
        dst = pkt[IP].dst
        port = pkt[TCP].dport
        flags = pkt[TCP].flags
        print(f"  [{idx}] {src} -> {dst}:{port} | Flags: {flags}")
