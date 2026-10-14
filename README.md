# 🛡️ Autonomous Cyber Defense (ACD)

A hands-on, engineering-focused repository documenting a 120-day journey building production-grade security tools, automated threat responders, SIEM log pipelines, and SOAR daemons from scratch on **Ubuntu Linux (WSL2)** using standard **Bash** and **Python 3**.

## 🚀 Mission & Vision

Modern Security Operations Centers (SOC) require security engineers who understand telemetry at the code level—moving beyond relying solely on third-party tools to writing resilient, custom automation for log parsing, threat intelligence integration, and real-time active response.

This repository tracks my progress from low-level Linux defense scripts to modular, fault-tolerant Python security engines.

## 📊 Progress Dashboard

| Phase | Focus Area | Status | Progress |
| ----- | ----- | ----- | ----- |
| **Phase 1** | Linux Hardening, Networking & Shell Automation | `[COMPLETED]` | 30 / 30 Days |
| **Phase 2** | Python Security Automation | `[IN PROGRESS]` | 8 / 24 Lessons |
| **Phase 3** | SIEM, NIDS & Detection Engineering | `[UPCOMING]` | 0 / 16 Lessons |
| **Phase 4** | Enterprise SOAR & Capstone Portfolio | `[UPCOMING]` | 0 / 16 Lessons |

## 📂 Repository Architecture

```text
.
├── Phase_1
│   ├── Day_01
│   │   └── day_01_networking_and_linux_basics.txt
│   ├── Day_02
│   │   └── day_02_ip_addressing_and_subnetting.txt
│   ├── Day_03
│   │   └── day_03_dns_and_traceroute.txt
│   ├── Day_04
│   │   └── day_04_ufw_firewall_and_port_security.txt
│   ├── Day_05
│   │   └── day_05_system_telemetry_and_process_auditing.txt
│   ├── Day_06
│   │   └── day_06_authentication_logs_and_telemetry.txt
│   ├── Day_07
│   │   └── day_07_network_socket_telemetry.txt
│   ├── Day_08
│   │   └── day_08_kernel_parameter_auditing.txt
│   ├── Day_09
│   │   └── day_09_user_identity_permissions.txt
│   ├── Day_10
│   │   └── day_10_suid_sgid_permission_auditing.txt
│   ├── Day_11
│   │   └── day_11_cron_scheduled_task_auditing.txt
│   ├── Day_12
│   │   └── day_12_pam_authentication_auditing.txt
│   ├── Day_13
│   │   └── day_13_ssh_security_auditing.txt
│   ├── Day_14
│   │   └── day_14_filesystem_mount_auditing.txt
│   ├── Day_15
│   │   └── day_15_service_surface_reduction.txt
│   ├── Day_16
│   │   └── day_16_file_integrity_monitoring.txt
│   ├── Day_17
│   │   └── day_17_kernel_module_auditing.txt
│   ├── Day_18
│   │   └── day_18_auditd_kernel_telemetry.txt
│   ├── Day_19
│   │   └── day_19_logging_architecture.txt
│   ├── Day_20
│   │   └── day_20_network_firewalls.txt
│   ├── Day_21
│   │   └── day_21_network_reconnaissance.txt
│   ├── Day_22
│   │   └── day_22_packet_telemetry_tcpdump.txt
│   ├── Day_23
│   │   └── day_23_deep_packet_inspection.txt
│   ├── Day_24
│   │   └── day_24_network_anomaly_detection.txt
│   ├── Day_25
│   │   └── day_25_network_baselining.txt
│   ├── Day_26
│   │   ├── day_26_nids_signature_rules.txt
│   │   ├── local.rules
│   │   ├── nids_alert.log
│   │   ├── nids_alerts.log
│   │   ├── nids_alerts.log.1.gz
│   │   └── nids_alerts.log.2.gz
│   ├── Day_27
│   │   ├── active_response.sh
│   │   ├── active_response_blocks.log
│   │   ├── active_response_blocks.log.1.gz
│   │   ├── active_response_blocks.log.2.gz
│   │   ├── active_response_blocks.log.3.gz
│   │   └── day_27_automated_active_response.txt
│   ├── Day_28
│   │   └── day_28_firewall_persistence_and_log_rotation.txt
│   ├── Day_29
│   │   └── day_29_acd_active_response_daemon.txt
│   └── Day_30
│       └── day_30_phase_1_integration_and_milestone_audit.txt
├── Phase_2
│   ├── Block_01_Python_Fundamentals
│   │   ├── 01_variables_and_strings.py
│   │   ├── 02_ip_blacklist_checker.py
│   │   ├── 03_file_handling_and_log_loops.py
│   │   ├── 04_functions_and_exception_handling.py
│   │   ├── lesson_01_output.txt
│   │   ├── lesson_02_output.txt
│   │   ├── lesson_03_output.txt
│   │   ├── lesson_04_output.txt
│   │   └── sample_auth.log
│   ├── Block_02_Data_Structures_and_JSON
│   │   ├── 01_python_dictionaries.py
│   │   ├── 02_parsing_json_logs.py
│   │   ├── 03_json_files_and_structured_logging.py
│   │   ├── 04_nested_json_parsing.py
│   │   ├── alerts.json
│   │   ├── events.json
│   │   ├── lesson_01_output.txt
│   │   ├── lesson_02_output.txt
│   │   ├── lesson_03_output.txt
│   │   └── lesson_04_output.txt
│   ├── Block_03_Socket_Programming_and_Auditor
│   ├── Block_04_Packet_Manipulation_Scapy
│   ├── Block_05_Threat_Intel_APIs
│   └── Block_06_Python_SOAR_Daemon
├── Phase_3
│   ├── Block_01_Suricata_NIDS_Setup
│   ├── Block_02_ELK_Stack_SIEM_Ingestion
│   ├── Block_03_Dashboards_and_Alerting
│   └── Block_04_Sigma_Rule_Engineering
├── Phase_4
│   ├── Block_01_Modular_SOAR_Architecture
│   ├── Block_02_Docker_Containerization
│   ├── Block_03_Red_Blue_Attack_Simulations
│   └── Block_04_Capstone_Documentation_and_Portfolio
└── README.md
```

## 💡 Real-World Applications & Professional Capability

The scripts and configurations developed across **Phase 1** and **Phase 2** directly map to everyday SOC Engineering, SecOps, and Security Software tasks:

### 1. Host Hardening & System Auditing (Phase 1)
* **Skill:** Auditing PAM modules, SSH daemon policies, kernel parameters (`sysctl`), and SUID/SGID permissions.
* **Real-World Impact:** Enforcing CIS Benchmarks and hardening enterprise Linux servers against privilege escalation and unauthorized access.

### 2. Network Telemetry & Active Response (Phase 1)
* **Skill:** Writing custom NIDS rules (`local.rules`) and automated active response scripts (`active_response.sh`) triggered by log events.
* **Real-World Impact:** Automatically isolating attacker IPs at the host firewall level (`iptables`/`ufw`) during active brute-force or port-scan attempts.

### 3. Log Ingestion & SIEM Parsing (Phase 2)
* **Skill:** Extracting telemetry from both unstructured log files (`sample_auth.log`) and structured JSON outputs (`events.json`, nested EDR logs).
* **Real-World Impact:** Building custom ingestion pipelines for non-standard or legacy security sensors that lack pre-built SIEM plugins.

### 4. Log Enrichment & Threat Intelligence Matching (Phase 2)
* **Skill:** Modifying JSON dictionaries in memory to append metadata tags (`"action": "BLOCK"`, `"rule_triggered": "BLACKLIST_MATCH"`).
* **Real-World Impact:** Automating SOC triage by dynamically enriching raw telemetry against threat intelligence lists before pushing data to security dashboards.

### 5. Fault-Tolerant Daemon Engineering (Phase 2)
* **Skill:** Wrapping parsing logic into reusable functions (`def`) backed by `try/except` blocks handling `IndexError`, `FileNotFoundError`, and `JSONDecodeError`.
* **Real-World Impact:** Building 24/7 background security automation services (SOAR daemons) that remain operational when reading corrupted payloads or missing fields.

## 🛠️ Quickstart & Local Verification

To run and verify any lesson script locally on Linux/WSL2:

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/Autonomous-Cyber-Defense.git
cd "Autonomous-Cyber-Defense"

# 2. Navigate to a target Block (e.g., Phase 2 Block 02)
cd Phase_2/Block_02_Data_Structures_and_JSON

# 3. Execute a lesson script
python3 04_nested_json_parsing.py
```

## 📈 Roadmap Overview

* **Phase 1: Linux System Hardening & Active Defense:** System telemetry, kernel parameters, PAM, SSH security, custom NIDS signatures, automated active response scripts.
* **Phase 2: Python Security Automation:** Log parsers, key-value lookup engines, socket scanners, network packet manipulation (`Scapy`), threat intel API integration, background SOAR daemons.
* **Phase 3: Detection Engineering & SIEM:** Suricata NIDS rule creation, ELK stack log ingestion pipelines, custom dashboards, Sigma rules.
* **Phase 4: Enterprise SOAR & Capstone:** Modular Python engines, Docker containerization, Red vs. Blue attack simulations, capstone portfolio.

*Created and maintained as part of the Autonomous Cyber Defense engineering track.*
