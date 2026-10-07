#!/usr/bin/env python3
"""
Phase 2 - Block 01: Lesson 2
Conditional Logic (if/else) & IP Blacklist Filtering
"""

blacklist = ["192.168.1.50", "10.0.0.99", "172.16.0.4"]
raw_log = "2026-10-06 14:32:10 [ALERT] Failed password for root from 192.168.1.50 port 22"
attacker_ip = raw_log.split()[8]
print("==========================================")
print("     ACD BLACKLIST EVALUATION ENGINE      ")
print("==========================================")
print(f"Evaluated IP : {attacker_ip}")

if attacker_ip in blacklist:
    print(f"Match Status : [FOUND IN BLACKLIST]")
    print(f"Decision     : TRIGGERING FIREWALL BLOCK")
else:
    print(f"Match Status : [CLEAN]")
    print(f"Decision     : ALLOW TRAFFIC")
print("==========================================")
