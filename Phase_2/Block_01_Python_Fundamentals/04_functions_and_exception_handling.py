#!/usr/bin/env python3
"""
Phase 2 - Block 01: Lesson 4
Functions & Exception Handling (try/except)
"""
def ip_extract_safely(log_line):
    """
    Parses a log line and extracts the IP address at index 8.
    Catches IndexError on malformed/short lines without crashing.
    """
    try:
        words = log_line.strip().split()
        return words[8]
    except IndexError:
        return None
def analyze_log_file(file_path, blacklist):
    """
    Opens a log file safely and checks extracted IPs against a threat blacklist.
    Catches FileNotFoundError if the path is invalid.
    """
    try:
       print(f"Reading telemetry from: {file_path}")
       print("=========================================")
       with open(file_path, "r") as file:
           for line_num, line in enumerate(file, 1):
               clean_line = line.strip()
               if not clean_line:
                   continue

               ip = ip_extract_safely(clean_line)

               if ip is None:
                   print(f"Line {line_num}: [WARNING] Malformed log entry detected & skipped!")
               elif ip in blacklist:
                   print(f"Line {line_num}: [ALERT] Blacklisted IP detected -> {ip}")
               else:
                   print(f"Line {line_num}: [INFO] Safe IP -> {ip}")
       print("=========================================")
    except FileNotFoundError:
        print(f"[CRITICAL ERROR] Target file '{file_path}' not found on filesystem.")
        print("==========================================")
if __name__ == "__main__":
    threat_blacklist = ["192.168.1.50", "10.0.0.99"]
    analyze_log_file("sample_auth.log", threat_blacklist)
    analyze_log_file("non_existent_syslog.log", threat_blacklist)
