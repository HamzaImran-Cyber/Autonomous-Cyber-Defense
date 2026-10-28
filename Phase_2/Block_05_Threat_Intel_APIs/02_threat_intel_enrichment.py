#!/usr/bin/env python3
"""
Phase 2 - Block 05: Lesson 2
Threat Intelligence API Ingestion & IP Reputation Scoring
"""
import os
import json
flagged_ips = ["203.0.113.45", "198.51.100.14", "192.168.1.50"]


def query_threat_intel(ip):
    mock_api_database = {
        "203.0.113.45": '{"ip": "203.0.113.45", "abuseScore": 88, "country": "US", "isp": "BadActor Hosting", "isTor": true}',
        "198.51.100.14": '{"ip": "198.51.100.14", "abuseScore": 20, "country": "DE", "isp": "CleanCloud GmbH", "isTor": false}',
        "192.168.1.50": '{"ip": "192.168.1.50", "abuseScore": 0, "country": "LOCAL", "isp": "Private LAN", "isTor": false}'
    }
    json_str = mock_api_database.get(
        ip, '{"ip": "' + ip + '", "abuseScore": 0, "country": "UNKNOWN", "isp": "Unknown", "isTor": false}'
    )
    return json.loads(json_str)
print("=== Phase 2 Block 05: Threat Intelligence IP Enrichment ===\n")

for ip in flagged_ips:
    intel = query_threat_intel(ip)
    
    score = intel["abuseScore"]
    country = intel["country"]
    isp = intel["isp"]
    tor_status = "YES" if intel["isTor"] else "NO"
    
    if score >= 75:
        verdict = "CRITICAL (Auto-Block)"
    elif score >= 30:
        verdict = "WARNING (Flagged)"
    else:
        verdict = "CLEAN (Allow)"
        
    print(f"IP: {ip:<15} | Score: {score:>3}% | Country: {country:<3} | TOR: {tor_status:<3} | Action: {verdict}")
