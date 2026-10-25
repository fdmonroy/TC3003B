# CCNA Practice Final - Guía Parte 1

| Reactivo | Pregunta | Respuesta | Tema en Cisco ITN |
| :---: | :--- | :--- | :--- |
| 1 | What characteristic describes spyware? | software that is installed on a user device and collects information about the user | `- 1.8.1 Security Threats` |
| 2 | Which statement describes network security? | It ensures sensitive corporate data is available for authorized users. | `- 1.6.5 Network Security` |
| 3 | Which two devices would be described as intermediary devices? (Choose two.) | IPS; wireless LAN controller | `- 1.2.4 Intermediary Devices` |
| 4 | What is a user trying to determine when issuing a ping 10.1.1.1 command on a PC? | if there is connectivity with the destination device | `- 13.2.1 Ping - Test Connectivity` |
| 5 | Refer to the exhibit. An administrator is trying to configure the switch but receives the error message that is displayed in the exhibit. What is the problem? | The administrator must first enter privileged EXEC mode before issuing the command. | `- 2.2.4 Navigate Between IOS Modes` |
| 6 | What is a characteristic of a switch virtual interface (SVI)? | An SVI is created in software and requires a configured IP address and a subnet mask in order to provide remote access to the switch. | `- 2.7.4 Switch Virtual Interface Configuration` |
| 7 | Match the descriptions to the terms. | users interact with the operating system by typing commands -> CLI; enables the user to interact with the operating system by pointing and clicking -> GUI; the part of the OS that interacts directly with the device hardware -> kernel; the part of the operating system that interfaces with applications and the user -> shell | `- 2.1.1 Operating Systems` |
| 8 | Which two OSI model layers have the same functionality as two layers of the TCP/IP model? (Choose two.) | transport; network | `- 3.5.4 OSI and TCP/IP Model Comparison` |
| 9 | Which PDU is processed when a host computer is de-encapsulating a message at the transport layer of the TCP/IP model? | segment | `- 3.6.3 Protocol Data Units` |
| 10 | Which three layers of the OSI model are comparable in function to the application layer of the TCP/IP model? (Choose three.) | session; application; presentation | `- 3.5.4 OSI and TCP/IP Model Comparison` |
| 11 | Refer to the exhibit. What is the maximum possible throughput between the PC and the server? | 128 kb/s | `- 4.2.6 Bandwidth Terminology` |
| 12 | Which two statements describe the characteristics of fiber-optic cabling? (Choose two.) | Fiber-optic cabling does not conduct electricity.; Fiber-optic cabling is primarily used as backbone cabling. | `- 4.5.1 Properties of Fiber-Optic Cabling` |
| 13 | Match the description with the media. | STP -> This type of copper media is used in industrial or similar environments where there is a lot of interference.; coaxial -> Traditionally used for television but can now be used in a network to connect the customer location to the wiring of the customer premises.; optical fiber -> This type of media is used for high transmission speed and can also transfer data over long distances.; wireless -> This type of media provides the most mobility options. | `- 1.2.5 Network Media` |
| 14 | What OSI physical layer term describes the measure of the transfer of bits across a medium over a given period of time? | throughput | `- 4.2.6 Bandwidth Terminology` |
| 15 | Although CSMA/CD is still a feature of Ethernet, why is it no longer necessary? | the use of full-duplex capable Layer 2 switches | `- 6.2.7 Contention-Based Access - CSMA/CD` |
| 16 | Which two acronyms represent the data link sublayers that Ethernet relies upon to operate? (Choose two.) | MAC; LLC | `- 7.1.2 Data Link Sublayers` |
| 17 | A network team is comparing topologies for connecting on a shared media. Which physical topology is an example of a hybrid topology for a LAN? | extended star | `- 6.2.4 LAN Topologies` |
| 18 | What does a router do when it receives a Layer 2 frame over the network medium? | de-encapsulates the frame | `- 6.1.3 Providing Access to Media` |
| 19 | If the default gateway is configured incorrectly on the host, what is the impact on communications? | The host can communicate with other hosts on the local network, but is unable to communicate with hosts on remote networks. | `- 8.4.2 Default Gateway` |
| 20 | Why is NAT not needed in IPv6? | Any host or user can get a public IPv6 network address because the number of available IPv6 addresses is extremely large. | `- 8.3.2 IPv6 Overview` |
| 21 | What routing table entry has a next hop address associated with a destination network? | remote routes | `- 8.5.2 IP Router Routing Table` |
| 22 | Which term describes a field in the IPv4 packet header that contains a unicast, multicast, or broadcast address? | destination IPv4 address | `- 8.2.2 IPv4 Packet Header Fields` |
| 23 | Refer to the exhibit. PC1 issues an ARP request because it needs to send a packet to PC3. In this scenario, what will happen next? | RT1 will send an ARP reply with its own Fa0/0 MAC address. | `- 9.2.2 ARP Functions` |
| 24 | Which destination address is used in an ARP request frame? | FFFF.FFFF.FFFF | `- 9.2.2 ARP Functions` |
| 25 | Refer to the exhibit. The exhibit shows a small switched network and the contents of the MAC address table of the switch. PC1 has sent a frame addressed to PC3. What will the switch do with the frame? | The switch will forward the frame to all ports except port 4. | `- 7.3.2 Switch Learning and Forwarding` |
| 26 | Match the command with the device mode at which the command is entered. | service password-encryption -> R1(config)#; enable -> R1>; copy running-config startup-config -> R1#; login -> R1(config-line)#; ip address 192.168.4.4 255.255.255.0 -> R1(config-if)# | `- 2.2.2 Configuration Mode and Subconfiguration Modes` |
| 27 | A router boots and enters setup mode. What is the reason for this? | The configuration file is missing from NVRAM. | `- 2.5.1 Configuration Files` |
| 28 | Refer to the exhibit. A network administrator is connecting a new host to the Registrar LAN. The host needs to communicate with remote networks. What IP address would be configured as the default gateway on the new host? | 192.168.235.234 | `- 10.3.1 Default Gateway on a Host` |

---

## Guía rápida de estudio

1. What characteristic describes spyware?
    - Answer: software that is installed on a user device and collects information about the user
    - Cisco ITN: - 1.8.1 Security Threats
2. Which statement describes network security?
    - Answer: It ensures sensitive corporate data is available for authorized users.
    - Cisco ITN: - 1.6.5 Network Security
3. Which two devices would be described as intermediary devices? (Choose two.)
    - Answer: IPS; wireless LAN controller
    - Cisco ITN: - 1.2.4 Intermediary Devices
4. What is a user trying to determine when issuing a ping 10.1.1.1 command on a PC?
    - Answer: if there is connectivity with the destination device
    - Cisco ITN: - 13.2.1 Ping - Test Connectivity
5. Refer to the exhibit. An administrator is trying to configure the switch but receives the error message that is displayed in the exhibit. What is the problem?
    - Answer: The administrator must first enter privileged EXEC mode before issuing the command.
    - Cisco ITN: - 2.2.4 Navigate Between IOS Modes
6. What is a characteristic of a switch virtual interface (SVI)?
    - Answer: An SVI is created in software and requires a configured IP address and a subnet mask in order to provide remote access to the switch.
    - Cisco ITN: - 2.7.4 Switch Virtual Interface Configuration
7. Match the descriptions to the terms.
    - Answer: users interact with the operating system by typing commands -> CLI; enables the user to interact with the operating system by pointing and clicking -> GUI; the part of the OS that interacts directly with the device hardware -> kernel; the part of the operating system that interfaces with applications and the user -> shell
    - Cisco ITN: - 2.1.1 Operating Systems
8. Which two OSI model layers have the same functionality as two layers of the TCP/IP model? (Choose two.)
    - Answer: transport; network
    - Cisco ITN: - 3.5.4 OSI and TCP/IP Model Comparison
9. Which PDU is processed when a host computer is de-encapsulating a message at the transport layer of the TCP/IP model?
    - Answer: segment
    - Cisco ITN: - 3.6.3 Protocol Data Units
10. Which three layers of the OSI model are comparable in function to the application layer of the TCP/IP model? (Choose three.)
    - Answer: session; application; presentation
    - Cisco ITN: - 3.5.4 OSI and TCP/IP Model Comparison
11. Refer to the exhibit. What is the maximum possible throughput between the PC and the server?
    - Answer: 128 kb/s
    - Cisco ITN: - 4.2.6 Bandwidth Terminology
12. Which two statements describe the characteristics of fiber-optic cabling? (Choose two.)
    - Answer: Fiber-optic cabling does not conduct electricity.; Fiber-optic cabling is primarily used as backbone cabling.
    - Cisco ITN: - 4.5.1 Properties of Fiber-Optic Cabling
13. Match the description with the media.
    - Answer: STP -> This type of copper media is used in industrial or similar environments where there is a lot of interference.; coaxial -> Traditionally used for television but can now be used in a network to connect the customer location to the wiring of the customer premises.; optical fiber -> This type of media is used for high transmission speed and can also transfer data over long distances.; wireless -> This type of media provides the most mobility options.
    - Cisco ITN: - 1.2.5 Network Media
14. What OSI physical layer term describes the measure of the transfer of bits across a medium over a given period of time?
    - Answer: throughput
    - Cisco ITN: - 4.2.6 Bandwidth Terminology
15. Although CSMA/CD is still a feature of Ethernet, why is it no longer necessary?
    - Answer: the use of full-duplex capable Layer 2 switches
    - Cisco ITN: - 6.2.7 Contention-Based Access - CSMA/CD
16. Which two acronyms represent the data link sublayers that Ethernet relies upon to operate? (Choose two.)
    - Answer: MAC; LLC
    - Cisco ITN: - 7.1.2 Data Link Sublayers
17. A network team is comparing topologies for connecting on a shared media. Which physical topology is an example of a hybrid topology for a LAN?
    - Answer: extended star
    - Cisco ITN: - 6.2.4 LAN Topologies
18. What does a router do when it receives a Layer 2 frame over the network medium?
    - Answer: de-encapsulates the frame
    - Cisco ITN: - 6.1.3 Providing Access to Media
19. If the default gateway is configured incorrectly on the host, what is the impact on communications?
    - Answer: The host can communicate with other hosts on the local network, but is unable to communicate with hosts on remote networks.
    - Cisco ITN: - 8.4.2 Default Gateway
20. Why is NAT not needed in IPv6?
    - Answer: Any host or user can get a public IPv6 network address because the number of available IPv6 addresses is extremely large.
    - Cisco ITN: - 8.3.2 IPv6 Overview
21. What routing table entry has a next hop address associated with a destination network?
    - Answer: remote routes
    - Cisco ITN: - 8.5.2 IP Router Routing Table
22. Which term describes a field in the IPv4 packet header that contains a unicast, multicast, or broadcast address?
    - Answer: destination IPv4 address
    - Cisco ITN: - 8.2.2 IPv4 Packet Header Fields
23. Refer to the exhibit. PC1 issues an ARP request because it needs to send a packet to PC3. In this scenario, what will happen next?
    - Answer: RT1 will send an ARP reply with its own Fa0/0 MAC address.
    - Cisco ITN: - 9.2.2 ARP Functions
24. Which destination address is used in an ARP request frame?
    - Answer: FFFF.FFFF.FFFF
    - Cisco ITN: - 9.2.2 ARP Functions
25. Refer to the exhibit. The exhibit shows a small switched network and the contents of the MAC address table of the switch. PC1 has sent a frame addressed to PC3. What will the switch do with the frame?
    - Answer: The switch will forward the frame to all ports except port 4.
    - Cisco ITN: - 7.3.2 Switch Learning and Forwarding
26. Match the command with the device mode at which the command is entered.
    - Answer: service password-encryption -> R1(config)#; enable -> R1>; copy running-config startup-config -> R1#; login -> R1(config-line)#; ip address 192.168.4.4 255.255.255.0 -> R1(config-if)#
    - Cisco ITN: - 2.2.2 Configuration Mode and Subconfiguration Modes
27. A router boots and enters setup mode. What is the reason for this?
    - Answer: The configuration file is missing from NVRAM.
    - Cisco ITN: - 2.5.1 Configuration Files
28. Refer to the exhibit. A network administrator is connecting a new host to the Registrar LAN. The host needs to communicate with remote networks. What IP address would be configured as the default gateway on the new host?
    - Answer: 192.168.235.234
    - Cisco ITN: - 10.3.1 Default Gateway on a Host
