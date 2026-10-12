#!/usr/bin/env python3
"""
Phase 2 - Block 02: Lesson 2
Parsing Native JSON Logs
"""
import json

# Raw JSON telemetry string from a security sensor
raw_json_log = '{"timestamp": "2026-10-12T14:30:00Z", "src_ip": "10.0.0.99", "event_type": "AUTHENTICATION_FAILURE", "severity": "HIGH"}'
threat_blacklist = {"192.168.1.55","10.0.0.99"}

try:
    event = json.loads(raw_json_log)
    ip = event.get("src_ip", "0.0.0.0")
    event_type = event.get("event_type", "UNKNOWN")
    severity = event.get("severity", "LOW")
    print("==========================================")
    print(f"JSON Parsed Event : {event_type} [{severity}]")
    print(f"Source IP         : {ip}")
    if ip in threat_blacklist:
        print(f"Decision          : [ALERT] {ip} is Blacklisted")
    else:
        print(f"Decision          : [SAFE] {ip} is Safe/Permitted")
    print("==========================================")
except json.JSONDecodeError:
    print("[ERROR] Failed to parse: Malformed JSON string!")
