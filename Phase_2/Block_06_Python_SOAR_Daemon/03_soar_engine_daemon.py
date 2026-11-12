#!/usr/bin/env python3
"""
Phase 2 - Block 06: Lesson 3
End-to-End SOAR Engine Integration
"""
import re
import time
import subprocess
from collections import defaultdict
from threading import Timer

# 1. Simulated Authentication Log Stream
raw_logs = [
    "Nov 10 12:00:01 server sshd[2001]: Failed password for invalid user admin from 198.51.100.45 port 51110 ssh2",
    "Nov 10 12:00:03 server sshd[2001]: Failed password for invalid user admin from 198.51.100.45 port 51112 ssh2",
    "Nov 10 12:00:05 server sshd[2001]: Failed password for invalid user admin from 198.51.100.45 port 51114 ssh2",
    "Nov 10 12:00:08 server sshd[2005]: Accepted password for hamza from 192.168.1.10 port 52000 ssh2"
]

# 2. Pre-compiled Regex Pattern
FAILED_LOG_REGEX = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\w+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)

failed_counts = defaultdict(int)
BAN_THRESHOLD = 3
COOLDOWN_SECONDS = 5

def block_ip(ip):
    cmd = ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[!] [SOAR ACTION] Applied kernel iptables DROP rule for {ip}")

def unblock_ip(ip):
    cmd = ["sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[*] [SOAR ACTION] Cooldown expired. Removed iptables DROP rule for {ip}")

def trigger_playbook(ip):
    block_ip(ip)
    # Asynchronous non-blocking timer
    timer = Timer(COOLDOWN_SECONDS, unblock_ip, args=[ip])
    timer.start()
    print(f"[*] [PLAYBOOK] Scheduled automated unban for {ip} in {COOLDOWN_SECONDS}s")

print("=== Phase 2 Block 06: End-to-End SOAR Engine Pipeline ===\n")

for line in raw_logs:
    match = FAILED_LOG_REGEX.search(line)
    if match:
        ip = match.group("ip")
        user = match.group("user")
        failed_counts[ip] += 1
        print(f"[+] [LOG DETECTED] Failed SSH login | User: {user} | IP: {ip} (Count: {failed_counts[ip]})")
        
        if failed_counts[ip] == BAN_THRESHOLD:
            print(f"    [ALERT] Threshold crossed! Executing Automated Response Playbook...")
            trigger_playbook(ip)

# Sleep to observe background timer unban complete cleanly before script exit
time.sleep(6)
