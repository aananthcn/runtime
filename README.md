# Runtime Build System
Prototype of runtime build system

## usage
```
$ source rbs/env-rbs.sh
$ rbs config/rbs.json
```


## Routing configuration for inter-domain communication

### QNX
```
$ su root
$ sysctl -w net.inet.ip.forwarding=1
$ route -n add 224.0.0.0/24 192.168.162.255
$ netstat -r

$ route delete <destination> <gateway>
```

### Linux
```
$ echo 1 > /proc/sys/net/ipv4/ip_forward
$ sudo route add -net 224.0.0.0/4 dev <network_if>
$ netstat -r (or) route -n

$ sudo route del -net 0.0.0.0 gw 192.168.178.1 netmask 0.0.0.0 dev eth0
```

