#!/bin/bash
# Autonomous Cyber Defense - Continuous Active Response Daemon
ALERT_FILE="/home/hamzaimran/Autonomous Cyber Defense/Phase_1/Day_26/nids_alerts.log"
BLOCK_LOG="/home/hamzaimran/Autonomous Cyber Defense/Phase_1/Day_27/active_response_blocks.log"

if [ ! -f "$ALERT_FILE" ]; then
    ALERT_FILE="/home/hamzaimran/nids_alerts.log"
fi

echo "[ACD DAEMON] Engine started at $(date)" >> "$BLOCK_LOG"

while true; do
    if [ -f "$ALERT_FILE" ]; then
        for ip in $(awk '/ALERT/ {print $9}' "$ALERT_FILE" 2>/dev/null | sort -u); do
            if [ -n "$ip" ] && [ "$ip" != "Probe" ]; then
                if ! iptables -C INPUT -s "$ip" -j DROP 2>/dev/null; then
                    echo "[DAEMON ACTION] Applying firewall block for IP: $ip at $(date +%T)" >> "$BLOCK_LOG"
                    iptables -A INPUT -s "$ip" -j DROP
                fi
            fi
        done
    fi
    sleep 5
done
