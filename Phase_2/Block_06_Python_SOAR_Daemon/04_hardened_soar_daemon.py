#!/usr/bin/env python3
import os
import re
import time
import ipaddress
import subprocess
from collections import defaultdict
from threading import Timer

LOG_FILE = "/home/hamzaimran/Autonomous Cyber Defense/Phase_2/Block_06_Python_SOAR_Daemon/live_auth.log"
BAN_THRESHOLD = 3
COOLDOWN_SECONDS = 30

WHITELIST_SUBNETS = [
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("10.0.0.0/8"),
]

FAILED_LOG_REGEX = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\w+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)

failed_counts = defaultdict(int)

def is_whitelisted(ip_str):
    try:
        target = ipaddress.ip_address(ip_str)
        return any(target in subnet for subnet in WHITELIST_SUBNETS)
    except ValueError:
        return True

def block_ip(ip):
    check = subprocess.run(
        ["iptables", "-C", "INPUT", "-s", ip, "-j", "DROP"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    if check.returncode != 0:
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
        print(f"[!] [SOAR BLOCK] Dropped traffic from {ip} for {COOLDOWN_SECONDS}s")
        Timer(COOLDOWN_SECONDS, unblock_ip, args=[ip]).start()

def unblock_ip(ip):
    subprocess.run(
        ["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    failed_counts[ip] = 0
    print(f"[*] [SOAR UNBAN] Cooldown expired for {ip}")

def watch_logs():
    print(f"[*] Hardened SOAR Daemon started. Watching {LOG_FILE}...")
    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            match = FAILED_LOG_REGEX.search(line)
            if match:
                ip = match.group("ip")
                if is_whitelisted(ip):
                    print(f"[SAFE] Ignored whitelisted IP: {ip}")
                    continue

                failed_counts[ip] += 1
                print(f"[+] Failed SSH from {ip} ({failed_counts[ip]}/{BAN_THRESHOLD})")
                if failed_counts[ip] >= BAN_THRESHOLD:
                    block_ip(ip)

if __name__ == "__main__":
    watch_logs()
