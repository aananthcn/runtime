#! /bin/sh

echo "Running applications from startup.sh!"
sysctl -w net.inet.ip.forwarding=1
route -n add 224.224.224.245 192.168.10.255
