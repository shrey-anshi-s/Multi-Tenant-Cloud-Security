# Multi-Tenant-Cloud-Security

## Overview
This project domentrates how to secure a **multi-tenant cloud enviroment** using Docker conantiners, network segmentation , intrusion prevention , file integrity verification and centralized monitoring .

Multiple tenants (e.g., departments or clients) share the same cloud infrastructure, but each is **isolated at the network level** with **access control and intrusion detection** in place.

Have created a **Flask-based Security Dashboard** displays access logs, highlights suspicious activities, and provides administrators with a central control panel.

## Problem Statments 
Multi-tenant cloud environments allow multiple customers to share the same infrastructure.  
Without proper security measures, this can lead to:
- **Data Leakage**
- **Unauthorized Access**
- **Lateral Movement by Attackers**
- **Lack of Intrusion Detection**
This project implements **layered security controls** to **isolate tenants, monitor access, and prevent attacks**.

## Features
- **Container-Based Tenant Isolation** – Each tenant runs in a separate Docker container.
- **Network Segmentation** – `iptables` rules prevent cross-tenant communication.
- **Login Security** – Flask authentication with **Fail2Ban** to block brute-force attempts.
- **Suspicious Activity Detection** – Dashboard flags cross-tenant access attempts.
- **Attack Simulation** – Python scripts to test defenses.
- **Central Monitoring** – SQLite3 database stores logs for the dashboard

## Tecnology Stack
1. Contaninerization | Docker
2. Web Framework | Flask
3. Database | SQLite3
4. Security | Fail2Ban ,iptables, Linux firewalls
5. Logging & IDS | python script
6. Integrity | Python encrypt code
7. UI | HTML ,CSS

## Security Implementation
1. **Isolation** – Each tenant runs in a Docker container.
2. **Access Control** – Flask-based login with session management.
3. **Network Segmentation** – Block inter-tenant communication using firewall rules.
4. **Intrusion Prevention** – Fail2Ban bans malicious IPs after failed attempts.
5. **Monitoring** – All access logged to SQLite3.
6. **File Integrity** – Verify with RSA encryption .
7. **Testing** – Simulated attacks to validate defenses.

   
