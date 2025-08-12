FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    snort \
    fail2ban \
    iptables \
    nano \
    curl \
    net-tools \
    iproute2

COPY rules/local.rules /etc/snort/rules/local.rules
COPY fail2ban/jail.local /etc/fail2ban/jail.local
COPY fail2ban/filter.d/snort-icmp.conf /etc/fail2ban/filter.d/snort-icmp.conf
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
