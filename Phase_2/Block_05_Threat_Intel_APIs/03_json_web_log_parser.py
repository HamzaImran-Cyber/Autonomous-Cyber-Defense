#!/usr/bin/env python3
"""
Phase 2 - Block 05: Lesson 3
JSON Web Access Log Parser
"""
import json
import re

web_logs = [
    '{"ip": "192.168.1.10", "method": "GET", "uri": "/index.php", "status": 200}',
    '{"ip": "10.0.0.5", "method": "GET", "uri": "/etc/passwd", "status": 404}',
    '{"ip": "10.0.0.5", "method": "GET", "uri": "/login.php?user=\' OR 1=1 --", "status": 200}',
    '{"ip": "172.16.0.2", "method": "POST", "uri": "/comment", "status": 200}'
]

ATTACK_PATTERNS = {
    "Path Traversal": re.compile(r"(/etc/passwd|\.\./)"),
    "SQL Injection": re.compile(r"('|\bOR\b|1=1|UNION|SELECT)", re.IGNORECASE)
}
print("=== Phase 2 Block 05: JSON Web Access Log Parser ===\n")
for entry in web_logs:
    data = json.loads(entry)
    ip = data.get("ip","0.0.0.0")
    uri = data.get("uri", "")
    
    for attack_type, pattern in ATTACK_PATTERNS.items():
        if pattern.search(uri):
            print(f"[ALERT] {attack_type} detected | IP: {ip:<10} | URI: {uri}")

