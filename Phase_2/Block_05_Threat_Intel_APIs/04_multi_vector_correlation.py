#!/usr/bin/env python3

ssh_fails = {"203.0.113.45": 2}
web_attacks = {"203.0.113.45": 1}
threat_intel = {"203.0.113.45": 85}

all_ips = set(ssh_fails) | set(web_attacks) | set(threat_intel)
print("=== Multi-Vector Risk Report ===\n")
for ip in all_ips:
    score = (ssh_fails.get(ip, 0) * 20) + (web_attacks.get(ip, 0) * 30) + (threat_intel.get(ip, 0))
    action = "CRITICAL (Auto-Block)" if score >= 100 else "ALLOW"
    print(f"IP: {ip:<15} | Risk Score: {score:>3} | Action: {action}")
