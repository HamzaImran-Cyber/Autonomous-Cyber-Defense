#!/usr/bin/env python3
"""
Phase 2 - Block 06: Lesson 2
Automated Temporary IP Bans with Asynchronous Unban Timers
"""
import subprocess
import time
from threading import Timer

def block_ip(ip):
    cmd = ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[+] [BAN] Applied temporary DROP rule for: {ip}")

def unblock_ip(ip):
    cmd = ["sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[-] [UNBAN] Expired ban timer. Removed DROP rule for: {ip}")

def temp_ban(ip, duration_seconds=5):
    block_ip(ip)
    # Schedule unblock_ip to run in a background thread after duration_seconds
    timer = Timer(duration_seconds, unblock_ip, args=[ip])
    timer.start()
    print(f"[*] [TIMER] Scheduled automatic unban for {ip} in {duration_seconds}s (Non-blocking)")

print("=== Phase 2 Block 06: Temporary Ban & Auto-Unban Daemon ===\n")
target_ip = "198.51.100.99"

# 1. Trigger a 5-second temporary ban
temp_ban(target_ip, duration_seconds=5)

# 2. Simulate main monitoring loop continuing uninterrupted
print("\n[*] Main thread continues processing without waiting...")
for second in range(1, 7):
    print(f"    [Main Thread Active] Elapsed: {second}s")
    time.sleep(1)

