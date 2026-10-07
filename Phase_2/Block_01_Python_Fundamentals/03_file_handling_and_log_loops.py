#!/usr/bin/env python3
"""
Phase 2 - Block 01: Lesson 3
File Handling & Log Reading Loops
"""

blacklist = ["192.168.1.50", "10.0.0.99"]
log_path = "sample_auth.log"

print("==========================================")
print("     ACD AUTOMATED LOG STREAM PARSER      ")
print("==========================================")

with open(log_path, "r") as log_file:
    # 3. Iterate line-by-line
    for line in log_file:
        clean_line = line.strip()
        if not clean_line:
            continue
            
        words = clean_line.split()
        attacker_ip = words[8]
        if attacker_ip in blacklist:
            print(f"Status: [MATCH] | Threat IP: {attacker_ip} | Line: {clean_line}")
        else:
            print(f"Status: [CLEAN] | Normal IP: {attacker_ip}")

print("==========================================")
