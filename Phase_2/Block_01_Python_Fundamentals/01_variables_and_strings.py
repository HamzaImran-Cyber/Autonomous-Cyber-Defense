#!/usr/bin/env python3
"""
Phase 2 - Block 01: Lesson 1
Python Variables & Security String Parsing
"""

raw_log = "2026-10-06 14:32:10 [ALERT] Failed password for root from 192.168.1.50 port 22"
words = raw_log.split()

target_user = words[6]
attacker_ip = words[8]

print("==========================================")
print("       ACD TELEMETRY PARSER LOG           ")
print("==========================================")
print(f"Target User : {target_user}")
print(f"Attacker IP : {attacker_ip}")
print("==========================================")
