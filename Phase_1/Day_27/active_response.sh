#!/bin/bash
ALERT_FILE="$HOME/Autonomous Cyber Defense/Phase_1/Day_26/nids_alerts.log"

if [ ! -f "$ALERT_FILE" ]; then
    ALERT_FILE="$HOME/nids_alerts.log"
fi

# Column 9 ($9) extracts the source IP address (127.0.0.1)
for ip in $(awk '/ALERT/ {print $9}' "$ALERT_FILE" | sort -u); do
    echo "[ACTION] Blocking Attacker IP: $ip" | tee -a "$HOME/active_response_blocks.log"
    sudo iptables -A INPUT -s "$ip" -j DROP
done
