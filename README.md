# Runtime Build System
Prototype of runtime build system

## usage
```
$ source rbs/env-rbs.sh
$ rbs config/rbs.json
```


## Routing configuration for inter-domain communication

Multicast IP: 224.244.224.245
Multicast Port: 30490

### QNX
```
$ su root
$ sysctl -w net.inet.ip.forwarding=1
$ route -n add 224.224.224.245 192.168.10.255
$ netstat -r

$ route delete <destination> <gateway>
```

### Linux
```
$ echo 1 > /proc/sys/net/ipv4/ip_forward
$ sudo route add -nv 224.224.224.245 dev <network_if> (from 10mins...)
$ sudo netstat -r (or) route -n

$ sudo route del -net 0.0.0.0 gw 192.168.10.1 netmask 0.0.0.0 dev eth0
```

TBD - QNX BSP
1. sockstat  /sbin

