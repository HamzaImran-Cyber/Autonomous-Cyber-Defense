#!/usr/bin/env python3
"""
Phase 2 - Block 02: Lesson 3
Reading JSON Files & Writing Structured Logs
"""
import json
blacklist = ["10.0.0.99", "192.168.1.50"]
alerts = []
try:
    with open("events.json", "r") as infile:
        events = json.load(infile)
    print("==========================================")
    print(f"Loaded {len(events)} events from events.json")
    for entry in events:
        ip = entry.get("src_ip", "0.0.0.0")
        if ip in blacklist:
            entry["action"] = "BLOCK"
            entry["rule_triggered"] = "BLACKLIST_MATCH"
            alerts.append(entry)
            print(f"[ALERT] Flagged IP {ip} -> Added to alert queue")
    with open("alerts.json", "w") as outfile:
        json.dump(alerts, outfile, indent=4)
    print(f"Successfully generated alerts.json with {len(alerts)} alerts.")
    print("==========================================")
except FileNotFoundError:
    print("[ERROR] Input file 'events.json' not found.")
except json.JSONDecodeError:
    print("[ERROR] Failed to decode JSON file.")
