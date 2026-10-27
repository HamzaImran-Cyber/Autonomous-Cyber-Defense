#!/usr/bin/env python3
"""
Phase 2 - Block 05: Lesson 1
Automated Auth Log Parser & SSH Brute-Force Detection
"""
import re
from collections import defaultdict

SAMPLE_LOG_DATA = """
Oct 25 14:10:01 server sshd[1001]: Accepted password for hamza from 192.168.1.50 port 51112 ssh2
Oct 25 14:11:02 server sshd[1005]: Failed password for invalid user admin from 203.0.113.45 port 41200 ssh2
Oct 25 14:11:05 server sshd[1007]: Failed password for root from 203.0.113.45 port 41202 ssh2
Oct 25 14:11:08 server sshd[1009]: Failed password for root from 203.0.113.45 port 41206 ssh2
Oct 25 14:11:12 server sshd[1012]: Failed password for root from 203.0.113.45 port 41210 ssh2
Oct 25 14:12:00 server sshd[1015]: Failed password for user test from 198.51.100.12 port 33100 ssh2
"""

log_file = "auth_sample.log"
with open(log_file, "w") as f:
    f.write(SAMPLE_LOG_DATA.strip())

FAILED_IP_REGEX = r"Failed password for (?:invalid user )?(\w+) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

failed_counts = defaultdict(int)
THRESHOLD = 3

print(f"=== Processing {log_file} for SSH Brute-Force Activity ===")
with open(log_file, "r") as f:
    for line in f:
        match = re.search(FAILED_IP_REGEX, line)
        if match:
            ip = match.group(2)
            failed_counts[ip]+=1
print("\n--- Failed Attempt Summary ---")
for ip, count in failed_counts.items():
    print(f"IP: {ip:<15} | Failures: {count}")
    if count >= THRESHOLD:
        print(f"  [ALERT] BRUTE-FORCE DETECTED: {ip} exceeds threshold ({count}/{THRESHOLD})!")

