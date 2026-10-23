---
title: "Trabajo sobre CCNA Practice Final 1"
subtitle: "Implementación de redes de área amplia y servicios distribuidos (TC3003B.570)"
author: "Fernando Daniel Monroy Sánchez (A01750536)"
date: "22 de octubre de 2026"
lang: en-US
---

**Profesor:** Juan Manuel Campos Sandoval

---

1. Although CSMA/CD is still a feature of Ethernet, why is it no longer necessary?
   * **Answer: the use of full-duplex capable Layer 2 switches**
   * Legacy Ethernet LANs with hubs operate in half duplex mode, where only 1 device can send or receive at a time on the shared medium.
   * If 2 devices transmit at the same time on a shared medium, a collision will occur, so half duplex networks require CSMA/CD to detect collisions.
   * Modern Layer 2 Ethernet switches and NICs use full duplex communication, where the 2 ends of the connection can send and receive simultaneously without collisions.

2. A network team is comparing topologies for connecting on a shared media. Which physical topology is an example of a hybrid topology for a LAN?
   * **Answer: extended star**
   * In multiaccess LANs, end devices connect to a central intermediary device such as an Ethernet switch to form a star topology.
   * An extended star topology extends the star topology because it interconnects multiple Ethernet switches into a hybrid physical layout.
   * Bus topologies chain end systems to each other on 1 cable, and ring topologies connect each end system to its neighbor to form a ring.

3. What does a router do when it receives a Layer 2 frame over the network medium?
   * **Answer: de-encapsulates the frame**
   * When a router accepts a frame from a medium, it immediately deencapsulates the Layer 2 header and trailer to extract the Layer 3 PDU.
   * Next, the router examines the destination IP address of the packet and searches its routing table for the best matching route entry.
   * Last, the router reencapsulates the packet into a new frame and forwards the frame to the next segment of the physical network.

4. What routing table entry has a next hop address associated with a destination network?
   * **Answer: remote routes**
   * The routing table of a router stores 3 types of route entries: directly connected networks, remote networks, and a default route.
   * Directly connected network entries represent active interfaces on the local router, so they do not require a next hop router address.
   * Remote network entries represent destination networks connected to other routers, so the router forwards matching packets to the IP address of the next hop router.

5. Which term describes a field in the IPv4 packet header that contains a unicast, multicast, or broadcast address?
   * **Answer: destination IPv4 address**
   * The 20 byte IPv4 packet header contains binary fields that the Layer 3 process examines to deliver the packet to its destination end device.
   * The Destination IP Address field contains a 32 bit binary value that represents the unicast, multicast, or broadcast address of the target host group.
   * In contrast, the Source IP Address field always identifies 1 sending host, while Time to Live, Protocol, and Header Checksum store control values.

6. Refer to the exhibit. PC1 issues an ARP request because it needs to send a packet to PC3. In this scenario, what will happen next?
   * **Answer: RT1 will send an ARP reply with its own Fa0/0 MAC address.**
   * When the destination IPv4 address (PC3) is on a different network than the source (PC1), PC1 must send the frame to its default gateway (RT1).
   * If the default gateway entry is not in the ARP table, PC1 sends an ARP request to determine the MAC address of the default gateway.
   * Only the device with the target IPv4 address responds, so router RT1 sends a unicast ARP reply with its own Fa0/0 MAC address.

7. Refer to the exhibit. The exhibit shows a small switched network and the contents of the MAC address table of the switch. PC1 has sent a frame addressed to PC3. What will the switch do with the frame?
   * **Answer: The switch will forward the frame to all ports except port 4.**
   * A Layer 2 switch forwards frames when it searches for a match between the destination MAC address in the frame and its MAC address table.
   * If the destination unicast MAC address is not in the table, the switch forwards the frame out all ports except the incoming port.
   * The MAC address table lacks an entry for PC3, so the switch floods this unknown unicast frame out all ports except incoming port 4.

8. Refer to the exhibit. A network administrator is connecting a new host to the Registrar LAN. The host needs to communicate with remote networks. What IP address would be configured as the default gateway on the new host?
   * **Answer: 192.168.235.234**
   * A host requires a default gateway address to reach remote networks, and this address is the router interface address attached to the local network.
   * On a Cisco router, the `description` command identifies the connected network, and the `ip address` command assigns the IPv4 address to that interface.
   * Interface `gi0/1` has the description `Connects to the Registrar LAN` and the IPv4 address `192.168.235.234`, so hosts on that LAN must use `192.168.235.234`.
