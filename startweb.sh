#!/bin/bash
# Launch uwsgi running on port 5000
# Caddy redirects connections on port 443 (and 80) to 5000, via reverse proxy
# Check caddy status with systemctl status caddy
# Start (and stop) Caddy with systemctl start caddy (and systemctl stop caddy)
# The Caddyfile is located at /etc/caddy

echo ""
if [ ! "$(screen -ls | grep -i web)" ]; then
	echo "Starting website..."
	screen -d -m -S "web" uwsgi --http 127.0.0.1:5000 --module website:app
else 
	echo "Website already runnning on a screen!"
fi
