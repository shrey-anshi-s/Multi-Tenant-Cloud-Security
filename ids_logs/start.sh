#!/bin/bash
mkdir -p /var/log/snort
echo "[*] Starting Snort in background..."
snort -A fast -c /etc/snort/snort.conf -i eth0 -l /var/log/snort &

echo "[*] Starting Fail2Ban..."
service fail2ban restart

echo "[*] Setup complete. Showing Snort alerts..."
tail -f /var/log/snort/alert

