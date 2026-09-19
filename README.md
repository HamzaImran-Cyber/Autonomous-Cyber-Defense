# Autonomous Cyber Defense (120-Day Engineering Initiative)

A hands-on systems security initiative focused on Linux operating system hardening, system call auditing, network threat telemetry, and automated threat mitigation. This repository tracks a daily, open-source engineering progression from low-level host hardening to building an autonomous background defense daemon on Ubuntu Linux (WSL2).

---

## System Environment & Infrastructure Specs

- **Host OS:** Windows 11 / WSL2 Subsystem
- **Guest OS Environment:** Ubuntu Linux
- **Kernel Version:** `6.x-microsoft-standard-WSL2`
- **Primary Shell:** GNU Bash (`/bin/bash`)
- **Version Control & Logging:** Git, standard structured plain-text daily telemetry logs (`.txt`)

---

## 120-Day Master Roadmap

### Phase 1: OS Hardening, Access Controls & Telemetry (Days 01–30) — *IN PROGRESS*
- **Week 1 (Telemetry & Network Isolation):** OS architecture baselining, networking fundamentals, IP addressing/subnetting, DNS/traceroute inspection, UFW firewall surface reduction, process/system telemetry, authentication logs, and network socket/port analysis (`ss`, `lsof`).
- **Week 2 (Kernel, Identity & Mount Security):** `sysctl` kernel parameter tuning, user identity database auditing (`/etc/passwd`, `/etc/shadow`), SUID/SGID permission checks, `cron` scheduled tasks, PAM authentication hardening (`yescrypt`, `faillock.conf`), SSH security auditing (`sshd -T`), and filesystem mount security (`nosuid`, `nodev`, `noexec`).
- **Week 3 (Service Surface Reduction & File Integrity):** Minimizing background services, file integrity monitoring (FIM), immutable file attribute locks (`chattr +i`), and security baselining.
- **Week 4 (Audit Framework & Log Infrastructure):** Linux kernel audit subsystem (`auditd`), system call rules, centralized logging, and log rotation policies.

### Phase 2: Network Traffic Inspection & Threat Telemetry (Days 31–60)
- Deep packet analysis (`tcpdump`, `tshark`), Intrusion Detection System (IDS) deployment using Suricata/Snort, custom signature rule creation, and MITRE ATT&CK event correlation.

### Phase 3: Security Automation & Threat Scripting (Days 61–90)
- Automated compliance auditing via Bash scripts, high-speed log parsing and string analysis via Python, real-time file monitoring daemons, and Threat Intelligence API integration (VirusTotal, AbuseIPDB).

### Phase 4: Autonomous Defense Daemon & Active Response (Days 91–120)
- Engineering a lightweight Python background daemon integrated with `systemd`, automated threat mitigation (dynamic IP blocking via UFW/iptables, account isolation), brute-force emulation testing, and final system benchmarking.

---

## Phase 1 Execution Index (Days 01–14)

| Day | Security Audit & Telemetry Focus | Log File Path | Status |
| :---: | :--- | :--- | :---: |
| **01** | Networking & Linux Basics | `Phase_1/Day_01/day_01_networking_and_linux_basics.txt` | `[COMPLETED]` |
| **02** | IP Addressing & Subnetting | `Phase_1/Day_02/day_02_ip_addressing_and_subnetting.txt` | `[COMPLETED]` |
| **03** | DNS & Traceroute Inspection | `Phase_1/Day_03/day_03_dns_and_traceroute.txt` | `[COMPLETED]` |
| **04** | UFW Firewall & Port Security | `Phase_1/Day_04/day_04_ufw_firewall_and_port_security.txt` | `[COMPLETED]` |
| **05** | System Telemetry & Process Auditing | `Phase_1/Day_05/day_05_system_telemetry_and_process_auditing.txt` | `[COMPLETED]` |
| **06** | Authentication Logs & Telemetry | `Phase_1/Day_06/day_06_authentication_logs_and_telemetry.txt` | `[COMPLETED]` |
| **07** | Network Socket Telemetry | `Phase_1/Day_07/day_07_network_socket_telemetry.txt` | `[COMPLETED]` |
| **08** | Kernel Parameter Auditing | `Phase_1/Day_08/day_08_kernel_parameter_auditing.txt` | `[COMPLETED]` |
| **09** | User Identity & Permissions | `Phase_1/Day_09/day_09_user_identity_permissions.txt` | `[COMPLETED]` |
| **10** | SUID/SGID Permission Auditing | `Phase_1/Day_10/day_10_suid_sgid_permission_auditing.txt` | `[COMPLETED]` |
| **11** | Cron Scheduled Task Auditing | `Phase_1/Day_11/day_11_cron_scheduled_task_auditing.txt` | `[COMPLETED]` |
| **12** | PAM Authentication Auditing | `Phase_1/Day_12/day_12_pam_authentication_auditing.txt` | `[COMPLETED]` |
| **13** | SSH Security Auditing | `Phase_1/Day_13/day_13_ssh_security_auditing.txt` | `[COMPLETED]` |
| **14** | Filesystem Mount Auditing | `Phase_1/Day_14/day_14_filesystem_mount_auditing.txt` | `[COMPLETED]` |

---

## Repository Directory Structure

```text
Autonomous Cyber Defense/
├── README.md
├── Phase_1/
│   ├── Day_01/
│   │   └── day_01_networking_and_linux_basics.txt
│   ├── Day_02/
│   │   └── day_02_ip_addressing_and_subnetting.txt
│   ├── Day_03/
│   │   └── day_03_dns_and_traceroute.txt
│   ├── Day_04/
│   │   └── day_04_ufw_firewall_and_port_security.txt
│   ├── Day_05/
│   │   └── day_05_system_telemetry_and_process_auditing.txt
│   ├── Day_06/
│   │   └── day_06_authentication_logs_and_telemetry.txt
│   ├── Day_07/
│   │   └── day_07_network_socket_telemetry.txt
│   ├── Day_08/
│   │   └── day_08_kernel_parameter_auditing.txt
│   ├── Day_09/
│   │   └── day_09_user_identity_permissions.txt
│   ├── Day_10/
│   │   └── day_10_suid_sgid_permission_auditing.txt
│   ├── Day_11/
│   │   └── day_11_cron_scheduled_task_auditing.txt
│   ├── Day_12/
│   │   └── day_12_pam_authentication_auditing.txt
│   ├── Day_13/
│   │   └── day_13_ssh_security_auditing.txt
│   └── Day_14/
│       └── day_14_filesystem_mount_auditing.txt
├── Phase_2/                                  <-- Network Inspection & IDS (Days 31–60)
├── Phase_3/                                  <-- Automation & Scripting (Days 61–90)
└── Phase_4/                                  <-- Autonomous Defense Daemon (Days 91–120)
