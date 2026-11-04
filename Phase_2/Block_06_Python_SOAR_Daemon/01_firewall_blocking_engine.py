#!/usr/bin/env python3
import subprocess

def is_ip_blocked(ip):
    cmd = ["sudo", "iptables", "-C", "INPUT", "-s", ip, "-j", "DROP"]
    res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return res.returncode == 0

def block_ip(ip):
    if is_ip_blocked(ip):
        print(f"[!] IP {ip} is already blocked in iptables.")
        return False
    
    cmd = ["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[+] [ACTION] Successfully added DROP rule for IP: {ip}")
        return True
    else:
        print(f"[-] [ERROR] Failed to block {ip}: {res.stderr.strip()}")
        return False

print("=== Phase 2 Block 06: Active Firewall Response Engine ===\n")
target_ip = "203.0.113.45"

# 1. First execution: Applies the block rule
block_ip(target_ip)

# 2. Second execution: Tests idempotency check
block_ip(target_ip)
