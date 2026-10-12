#!/usr/bin/env python3
"""
Phase 2 - Block 02: Lesson 1
Python Dictionaries & Key-Value Security Lookup
"""
# Key Value Entry
event_data = {"timestamp": "2026-10-12 14:00:00", "source_ip": "192.168.1.50", "user": "root", "status": "FAILED"}
blacklist = {"192.168.1.50", "10.0.0.99"}
# Field Value Extraction
ip = event_data.get("source_ip", "0.0.0.0")
user = event_data.get("user", "UNKNOWN")
status = event_data.get("status", "UNKNOWN")
print("==========================================")
print(f"Parsed event: {status} login for '{user}' from {ip}")
# Threat Evaluation
if ip in blacklist:
    print(f"Decision : [ALERT] {ip} matched threat blacklist!")
else:
    print(f"Decision : [CLEAN] {ip} permitted.")
print("==========================================")
