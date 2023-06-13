#!/usr/bin/env bash
# This script renews certbot ssl certificate

# Renew the certificate
sudo certbot renew --force-renewal --tls-sni-01-port=8080

# concatenate new cert files, with less output (avoiding to use tee and its output to stdout)
sudo bash -c "cat /etc/letsencrypt/live/thelevites.tech/fullchain.pem /etc/letsencrypt/live/thelevites.tech/privkey.pem > /etc/ssl/thelevites.tech/thelevites.tech.pem"

# Reload HAProxy
sudo service haproxy reload
