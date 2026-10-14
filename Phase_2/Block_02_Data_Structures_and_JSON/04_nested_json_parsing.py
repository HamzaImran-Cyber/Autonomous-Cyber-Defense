#!/usr/bin/env python3
"""
Phase 2 - Block 02: Lesson 4
Nested JSON Parsing
"""
import json

raw_log = '{"event": "ALERT", "network": {"src_ip": "10.0.0.99", "port": 22}}'
blacklist = ["10.0.0.9", "192.168.1.50"]
log = json.loads(raw_log)
network_info = log.get("network", {})
ip = network_info.get("src_ip", "0.0.0.0")

print("==================================")
print(f"Extracted Nested IP : {ip}")
if ip in blacklist:
    print(f"Decision            :[ALERT] {ip} is Blacklisted")
else:
    print(f"Decision            :[ALERT] {ip} is Safe")
print("==================================")
