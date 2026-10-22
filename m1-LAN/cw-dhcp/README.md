# DHCPv4 LAN Classwork

Documentation for the classwork activity assigned on October 22, 2026 in Advanced Networking LAN.

## Class Activity Summary

- Date: October 22, 2026
- Meeting: Class: Advanced Networking. LAN.
- Topic: DHCPv4 server configuration, excluded address pools, client lease parameters, and DHCP Relay Agent mechanics.
- Objective: Build a functional LAN in Cisco Packet Tracer where a Cisco router serves DHCPv4 parameters to connected clients, reserve static addresses, verify client configuration, and explain the architectural difference when the DHCP server resides in a different subnet.

## Topology and Addressing

- Network: 192.168.10.0/24 (Subnet mask: 255.255.255.0)
- Default Gateway: 192.168.10.1 (Router R1 interface GigabitEthernet0/0)
- Excluded IP Range: 192.168.10.1 through 192.168.10.10
- DNS Server: 192.168.10.53
- Leased Client 1 (PC1): 192.168.10.11 /24
- Leased Client 2 (PC2): 192.168.10.13 /24

## Device Connections

- R1 GigabitEthernet0/0 to S1 GigabitEthernet0/1 via straight copper cable
- S1 FastEthernet0/1 to PC1 FastEthernet0 via straight copper cable
- S1 FastEthernet0/2 to PC2 FastEthernet0 via straight copper cable

## Cisco IOS Configurations

### Router R1 Configuration

```ios
enable
configure terminal
hostname R1
no ip domain-lookup

interface GigabitEthernet0/0
 description LAN Interface
 ip address 192.168.10.1 255.255.255.0
 no shutdown
exit

ip dhcp excluded-address 192.168.10.1 192.168.10.10

ip dhcp pool LAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 192.168.10.53
 domain-name lan10.net
 lease 1
exit

end
write memory
```

### Switch S1 Configuration

```ios
enable
configure terminal
hostname S1
no ip domain-lookup
spanning-tree portfast default

interface GigabitEthernet0/1
 description Uplink to R1
exit

interface FastEthernet0/1
 description Link to PC1
exit

interface FastEthernet0/2
 description Link to PC2
exit

end
write memory
```

## Client Verification

### PC1 Addressing Output

```
C:\>ipconfig /all

FastEthernet0 Connection:(default port)
   Connection-specific DNS Suffix..: lan10.net
   Physical Address................: 000D.BD23.1ED8
   IPv4 Address....................: 192.168.10.11
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 192.168.10.1
   DHCP Servers....................: 192.168.10.1
   DNS Servers.....................: 192.168.10.53
```

### PC2 Addressing Output

```
C:\>ipconfig /all

FastEthernet0 Connection:(default port)
   Connection-specific DNS Suffix..: lan10.net
   Physical Address................: 00D0.BA6D.2648
   IPv4 Address....................: 192.168.10.13
   Subnet Mask.....................: 255.255.255.0
   Default Gateway.................: 192.168.10.1
   DHCP Servers....................: 192.168.10.1
   DNS Servers.....................: 192.168.10.53
```

### Verification Commands on Router R1

```
R1#show ip dhcp binding
IP address       Client-ID/              Lease expiration        Type
                 Hardware address
192.168.10.11    000D.BD23.1ED8           --                     Automatic
192.168.10.13    00D0.BA6D.2648           --                     Automatic

R1#show ip dhcp pool
Pool LAN10 :
 Total addresses                : 254
 Leased addresses               : 2
 Excluded addresses             : 1
```

## Connectivity Testing

- Ping from PC1 to Gateway 192.168.10.1: 4 of 4 packets received, 100% success rate, minimum latency 0 ms.
- Ping from PC1 to PC2 192.168.10.13: 4 of 4 packets received, 100% success rate, round trip latency 0 to 21 ms.

## Question Asked in Class: DHCP Relay Explanation

Question: Que cambiaria si el servidor estuviera en otra subred?

1. Broadcast Domain Limitation:
   DHCP Discover and Request packets are Layer 2 broadcasts (destination MAC FF:FF:FF:FF:FF:FF, destination IP 255.255.255.255). Routers block broadcast frames and do not forward them between subnets by default.

2. Configuration Change on Router:
   The local router interface serving as the default gateway for the clients (GigabitEthernet0/0 on R1) must be configured with the IP helper command:
   ```ios
   interface GigabitEthernet0/0
    ip helper-address <DHCP_SERVER_IP>
   ```

3. Operation of DHCP Relay Agent:
   Upon receiving the incoming DHCP broadcast on port UDP 67, the router converts the broadcast frame into a unicast packet with source IP set to the router incoming interface address (192.168.10.1) and destination IP set to the remote DHCP server address. The router forwards this packet across the routed network.

4. Centralized DHCP Server Configuration:
   The DHCP pool for subnet 192.168.10.0/24 is configured on the centralized external server instead of the local router. The server uses the GIADDR (Gateway IP Address) field populated by the router (192.168.10.1) to determine which pool to select addresses from.

## Artifacts and Files

- Packet Tracer Topology File: [actividad_dhcpv4_oct22.pkt](file:///Users/pez/workspace/Academic/9/TC3003B/m1-LAN/cw-dhcp/actividad_dhcpv4_oct22.pkt)
- Topology Diagram Screenshot: [actividad_dhcpv4_oct22.png](file:///Users/pez/workspace/Academic/9/TC3003B/m1-LAN/cw-dhcp/actividad_dhcpv4_oct22.png)
