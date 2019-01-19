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


## Test Applications
1. **hello-node**  
This application a very simple hello-world application, it is meant to check if the cross compilation and installation are working properly.  

2. **hello-someip**  
This application sends a raw SOME-IP request from Linux and the QNX client provide a response. This is meant to check if SOME-IP libs are built correctly and routing configurations are done as per the section above.  

3. **hello-system**  
This application is based on Common API. It reads 2 numbers from Linux client and sends them to QNX client. QNX client computes the average of these 2 number and sends it back to Linux client. Linux client prints it. This application is meant to test the Common API & vSomeIP functions across nodes.  



## Lessons Learned

1. Ubuntu network configuration: If you are using Ubuntu, use network manager to configure fixed IP address.
2. On QNX, ensure that sshd is in /sbin and sh is in /bin/sh. If we don't specify the path of these binaries in build script of QNX, it places them in /boot/proc and reason for failures will be a hard thing to find, because files like /etc/passwd may point to /bin/sh path.
3. Default QNX compiler configuration: Use ```qcc -V5.4.0,gcc_ntoarmv7le_gpp -set-default```. Though this can be given as -V option to qcc, but sometimes in some packages like vsomeip, it chooses the default binary (assembler). This will give a good head-ache if not configured correctly.
4. The current code generators for Common API & vSomeIP depends on OpenJDK-8 (JRE). On Ubuntu 18.04, the default JRE is version 11, so you need to change this to OpenJDK-8.
5. Strictly follow the routing instructions as above.
