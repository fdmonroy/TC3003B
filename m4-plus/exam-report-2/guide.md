# CCNA Practice Final - Guía Parte 2

| Reactivo | Pregunta | Respuesta | Tema en Cisco ITN |
| :---: | :--- | :--- | :--- |
| 29 | Three devices are on three different subnets. Match the network address and the broadcast address with each subnet where these devices are located. Device 1: IP address 192.168.10.77/28 on subnet 1. Device 2: IP address 192.168.10.17/30 on subnet 2. Device 3: IP address 192.168.10.35/29 on subnet 3. | Subnet 1 network number -> 192.168.10.64; Subnet 2 broadcast address -> 192.168.10.19; Subnet 3 network number -> 192.168.10.32; Subnet 1 broadcast address -> 192.168.10.79; Subnet 2 network number -> 192.168.10.16; Subnet 3 broadcast address -> 192.168.10.39 | `- 11.5.2 Subnet within an Octet Boundary` |
| 30 | What does the IP address 192.168.1.15/29 represent? | broadcast address | `- 11.1.6 Network, Host, and Broadcast Addresses` |
| 31 | What type of address is 198.133.219.162? | public | `- 11.3.1 Public and Private IPv4 Addresses` |
| 32 | Given network 172.18.109.0, which subnet mask would be used if 6 host bits were available? | 255.255.255.192 | `- 11.5.2 Subnet within an Octet Boundary` |
| 33 | Refer to the exhibit. A user issues the command netstat -r on a workstation. Which IPv6 address is one of the link-local addresses of the workstation? | fe80::30d0:115:3f57:fe4c/128 | `- 12.3.7 IPv6 LLA` |
| 34 | Which is the compressed format of the IPv6 address fe80:0000:0000:0000:0220:0b3f:f0e0:0029? | fe80::220:b3f:f0e0:29 | `- 12.2.1 IPv6 Addressing Formats` |
| 35 | What type of IPv6 address is represented by ::1/128? | loopback | `- 12.3.3 Types of IPv6 Unicast Addresses` |
| 36 | A network technician types the command ping 127.0.0.1 at the command prompt on a computer. What is the technician trying to accomplish? | testing the integrity of the TCP/IP stack on the local machine | `- 13.2.2 Ping the Loopback` |
| 37 | Which two ICMP messages are used by both IPv4 and IPv6 protocols? (Choose two.) | protocol unreachable; route redirection | `- 13.1.1 ICMPv4 and ICMPv6 Messages` |
| 38 | Network information: • local router LAN interface: 172.19.29.254 / fe80:65ab:dec1::10 • local router WAN interface: 198.133.219.33 / 2001:db8:FACE:39::10 • remote server: 192.135.250.103. What task might a user be trying to accomplish by using the ping 2001:db8:FACE:39::10 command? | verifying that there is connectivity to the Internet | `- 13.2.4 Ping a Remote Host` |
| 39 | Refer to the exhibit. What does the value of the window size specify? | the amount of data that can be sent before an acknowledgment is required | `- 14.6.5 TCP Flow Control - Window Size and Acknowledgments` |
| 40 | A client packet is received by a server. The packet has a destination port number of 22. What service is the client requesting? | SSH | `- 14.4.3 Port Number Groups` |
| 41 | To which TCP port group does the port 414 belong? | well-known | `- 14.4.3 Port Number Groups` |
| 42 | Two students are working on a network design project. One student is doing the drawing, while the other student is writing the proposal. The drawing is finished and the student wants to share the folder that contains the drawing so that the other student can access the file and copy it to a USB drive. Which networking model is being used? | peer-to-peer | `- 15.2.2 Peer-to-Peer Networks` |
| 43 | Which command is used to manually query a DNS server to resolve a specific host name? | nslookup | `- 15.4.4 The nslookup Command` |
| 44 | What service is provided by POP3? | Retrieves email from the server by downloading the email to the local mail application of the client. | `- 15.3.4 SMTP, POP, and IMAP` |
| 45 | The employees and residents of Ciscoville cannot access the Internet or any remote web-based services. IT workers quickly determine that the city firewall is being flooded with so much traffic that a breakdown of connectivity to the Internet is occurring. Which type of attack is being launched at Ciscoville? | DoS | `- 16.2.4 Denial of Service Attacks` |
| 46 | A network administrator is issuing the login block-for 180 attempts 2 within 30 command on a router. Which threat is the network administrator trying to prevent? | a user who is trying to guess a password to access the router | `- 16.4.3 Additional Password Security` |
| 47 | Which statement describes the characteristics of packet-filtering and stateful firewalls as they relate to the OSI model? | A packet-filtering firewall typically can filter up to the transport layer, whereas a stateful firewall can filter up to the session layer. | `- 16.3.6 Types of Firewalls` |
| 48 | What are two ways to protect a computer from malware? (Choose two.) | Use antivirus software.; Keep software up to date. | `- 16.3.7 Endpoint Security` |
| 49 | Which two commands could be used to check if DNS name resolution is working properly on a Windows PC? (Choose two.) | ping cisco.com; nslookup cisco.com | `- 15.4.4 The nslookup Command` |
| 50 | A small advertising company has a web server that provides critical business service. The company connects to the Internet through a leased line service to an ISP. Which approach best provides cost effective redundancy for the Internet connection? | Add a connection to the Internet via a DSL line to another ISP. | `- 1.5.3 Businesses Internet Connections` |
| 51 | Only employees connected to IPv6 interfaces are having difficulty connecting to remote networks. The analyst wants to verify that IPv6 routing has been enabled. What is the best command to use to accomplish the task? | show running-config | `- 12.4.1 Static GUA Configuration on a Router` |
| 52 | What happens when a switch receives a frame and the calculated CRC value is different than the value that is in the FCS field? | The switch drops the frame. | `- 7.1.4 Ethernet Frame Fields` |
| 53 | Which two issues can cause both runts and giants in Ethernet networks? (Choose two.) | a malfunctioning NIC; half-duplex operations | `- 7.1.4 Ethernet Frame Fields` |
| 54 | Two network engineers are discussing the methods used to forward frames through a switch. What is an important concept related to the cut-through method of switching? | Packets can be relayed with errors when fast-forward switching is used. | `- 7.4.2 Cut-Through Switching` |
| 55 | Which two functions are performed at the LLC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.) | places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame; adds Ethernet control information to network protocol data | `- 7.1.2 Data Link Sublayers` |

---

## Guía rápida de estudio

29. Three devices are on three different subnets. Match the network address and the broadcast address with each subnet where these devices are located. Device 1: IP address 192.168.10.77/28 on subnet 1. Device 2: IP address 192.168.10.17/30 on subnet 2. Device 3: IP address 192.168.10.35/29 on subnet 3.
    - Answer: Subnet 1 network number -> 192.168.10.64; Subnet 2 broadcast address -> 192.168.10.19; Subnet 3 network number -> 192.168.10.32; Subnet 1 broadcast address -> 192.168.10.79; Subnet 2 network number -> 192.168.10.16; Subnet 3 broadcast address -> 192.168.10.39
    - Cisco ITN: - 11.5.2 Subnet within an Octet Boundary
30. What does the IP address 192.168.1.15/29 represent?
    - Answer: broadcast address
    - Cisco ITN: - 11.1.6 Network, Host, and Broadcast Addresses
31. What type of address is 198.133.219.162?
    - Answer: public
    - Cisco ITN: - 11.3.1 Public and Private IPv4 Addresses
32. Given network 172.18.109.0, which subnet mask would be used if 6 host bits were available?
    - Answer: 255.255.255.192
    - Cisco ITN: - 11.5.2 Subnet within an Octet Boundary
33. Refer to the exhibit. A user issues the command netstat -r on a workstation. Which IPv6 address is one of the link-local addresses of the workstation?
    - Answer: fe80::30d0:115:3f57:fe4c/128
    - Cisco ITN: - 12.3.7 IPv6 LLA
34. Which is the compressed format of the IPv6 address fe80:0000:0000:0000:0220:0b3f:f0e0:0029?
    - Answer: fe80::220:b3f:f0e0:29
    - Cisco ITN: - 12.2.1 IPv6 Addressing Formats
35. What type of IPv6 address is represented by ::1/128?
    - Answer: loopback
    - Cisco ITN: - 12.3.3 Types of IPv6 Unicast Addresses
36. A network technician types the command ping 127.0.0.1 at the command prompt on a computer. What is the technician trying to accomplish?
    - Answer: testing the integrity of the TCP/IP stack on the local machine
    - Cisco ITN: - 13.2.2 Ping the Loopback
37. Which two ICMP messages are used by both IPv4 and IPv6 protocols? (Choose two.)
    - Answer: protocol unreachable; route redirection
    - Cisco ITN: - 13.1.1 ICMPv4 and ICMPv6 Messages
38. Network information: • local router LAN interface: 172.19.29.254 / fe80:65ab:dec1::10 • local router WAN interface: 198.133.219.33 / 2001:db8:FACE:39::10 • remote server: 192.135.250.103. What task might a user be trying to accomplish by using the ping 2001:db8:FACE:39::10 command?
    - Answer: verifying that there is connectivity to the Internet
    - Cisco ITN: - 13.2.4 Ping a Remote Host
39. Refer to the exhibit. What does the value of the window size specify?
    - Answer: the amount of data that can be sent before an acknowledgment is required
    - Cisco ITN: - 14.6.5 TCP Flow Control - Window Size and Acknowledgments
40. A client packet is received by a server. The packet has a destination port number of 22. What service is the client requesting?
    - Answer: SSH
    - Cisco ITN: - 14.4.3 Port Number Groups
41. To which TCP port group does the port 414 belong?
    - Answer: well-known
    - Cisco ITN: - 14.4.3 Port Number Groups
42. Two students are working on a network design project. One student is doing the drawing, while the other student is writing the proposal. The drawing is finished and the student wants to share the folder that contains the drawing so that the other student can access the file and copy it to a USB drive. Which networking model is being used?
    - Answer: peer-to-peer
    - Cisco ITN: - 15.2.2 Peer-to-Peer Networks
43. Which command is used to manually query a DNS server to resolve a specific host name?
    - Answer: nslookup
    - Cisco ITN: - 15.4.4 The nslookup Command
44. What service is provided by POP3?
    - Answer: Retrieves email from the server by downloading the email to the local mail application of the client.
    - Cisco ITN: - 15.3.4 SMTP, POP, and IMAP
45. The employees and residents of Ciscoville cannot access the Internet or any remote web-based services. IT workers quickly determine that the city firewall is being flooded with so much traffic that a breakdown of connectivity to the Internet is occurring. Which type of attack is being launched at Ciscoville?
    - Answer: DoS
    - Cisco ITN: - 16.2.4 Denial of Service Attacks
46. A network administrator is issuing the login block-for 180 attempts 2 within 30 command on a router. Which threat is the network administrator trying to prevent?
    - Answer: a user who is trying to guess a password to access the router
    - Cisco ITN: - 16.4.3 Additional Password Security
47. Which statement describes the characteristics of packet-filtering and stateful firewalls as they relate to the OSI model?
    - Answer: A packet-filtering firewall typically can filter up to the transport layer, whereas a stateful firewall can filter up to the session layer.
    - Cisco ITN: - 16.3.6 Types of Firewalls
48. What are two ways to protect a computer from malware? (Choose two.)
    - Answer: Use antivirus software.; Keep software up to date.
    - Cisco ITN: - 16.3.7 Endpoint Security
49. Which two commands could be used to check if DNS name resolution is working properly on a Windows PC? (Choose two.)
    - Answer: ping cisco.com; nslookup cisco.com
    - Cisco ITN: - 15.4.4 The nslookup Command
50. A small advertising company has a web server that provides critical business service. The company connects to the Internet through a leased line service to an ISP. Which approach best provides cost effective redundancy for the Internet connection?
    - Answer: Add a connection to the Internet via a DSL line to another ISP.
    - Cisco ITN: - 1.5.3 Businesses Internet Connections
51. Only employees connected to IPv6 interfaces are having difficulty connecting to remote networks. The analyst wants to verify that IPv6 routing has been enabled. What is the best command to use to accomplish the task?
    - Answer: show running-config
    - Cisco ITN: - 12.4.1 Static GUA Configuration on a Router
52. What happens when a switch receives a frame and the calculated CRC value is different than the value that is in the FCS field?
    - Answer: The switch drops the frame.
    - Cisco ITN: - 7.1.4 Ethernet Frame Fields
53. Which two issues can cause both runts and giants in Ethernet networks? (Choose two.)
    - Answer: a malfunctioning NIC; half-duplex operations
    - Cisco ITN: - 7.1.4 Ethernet Frame Fields
54. Two network engineers are discussing the methods used to forward frames through a switch. What is an important concept related to the cut-through method of switching?
    - Answer: Packets can be relayed with errors when fast-forward switching is used.
    - Cisco ITN: - 7.4.2 Cut-Through Switching
55. Which two functions are performed at the LLC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)
    - Answer: places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame; adds Ethernet control information to network protocol data
    - Cisco ITN: - 7.1.2 Data Link Sublayers
