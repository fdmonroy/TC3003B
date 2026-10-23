---
title: "CCNA Practice Final 1"
subtitle: "Implementación de redes de área amplia y servicios distribuidos (TC3003B.570)"
author: "Fernando Daniel Monroy Sánchez (A01750536)"
date: "22 de octubre de 2026"
lang: es-MX
---

**Profesor:** Juan Manuel Campos Sandoval

---

1. Although CSMA/CD is still a feature of Ethernet, why is it no longer necessary?
    - **Respuesta: the use of full-duplex capable Layer 2 switches**
    - Las redes Ethernet antiguas con concentradores (hubs) operan en modo semidúplex, donde solo 1 dispositivo puede enviar o recibir a la vez en el medio compartido.
    - Si 2 dispositivos transmiten al mismo tiempo en un medio compartido ocurre una colisión, por lo que las redes en semidúplex requieren CSMA/CD para detectar colisiones.
    - Los switches Ethernet de Capa 2 y las tarjetas NIC actuales usan comunicación en dúplex completo, donde los 2 extremos envían y reciben simultáneamente sin colisiones.

2. A network team is comparing topologies for connecting on a shared media. Which physical topology is an example of a hybrid topology for a LAN?
    - **Respuesta: extended star**
    - En las redes LAN de acceso múltiple, los dispositivos finales se conectan a un dispositivo intermedio central como un switch Ethernet para formar una topología en estrella.
    - Una topología en estrella extendida amplía la topología en estrella porque interconecta múltiples switches Ethernet en un diseño físico híbrido.
    - Las topologías de bus encadenan los sistemas finales entre sí en 1 cable, y las topologías de anillo conectan cada sistema con su vecino formando un anillo.

3. What does a router do when it receives a Layer 2 frame over the network medium?
    - **Respuesta: de-encapsulates the frame**
    - Cuando un router acepta una trama desde un medio físico, de inmediato desencapsula el encabezado y el tráiler de Capa 2 para extraer la PDU de Capa 3.
    - Después, el router examina la dirección IP de destino del paquete y busca en su tabla de enrutamiento la entrada con la mejor coincidencia.
    - Por último, el router reencapsula el paquete dentro de una nueva trama y reenvía esa trama hacia el siguiente segmento de la red física.

4. What routing table entry has a next hop address associated with a destination network?
    - **Respuesta: remote routes**
    - La tabla de enrutamiento de un router almacena 3 tipos de entradas de ruta: redes conectadas directamente, redes remotas y una ruta predeterminada.
    - Las entradas de redes conectadas directamente representan interfaces activas del propio router local, por lo que no requieren una dirección de router de siguiente salto.
    - Las entradas de redes remotas representan redes de destino conectadas a otros routers, por lo que el router reenvía los paquetes a la dirección IP del siguiente salto.

5. Which term describes a field in the IPv4 packet header that contains a unicast, multicast, or broadcast address?
    - **Respuesta: destination IPv4 address**
    - El encabezado del paquete IPv4 de 20 bytes contiene campos binarios que el proceso de Capa 3 examina para entregar el paquete al dispositivo final de destino.
    - El campo de dirección IPv4 de destino contiene un valor binario de 32 bits que representa la dirección unicast, multicast o broadcast del receptor.
    - En cambio, el campo de dirección IPv4 de origen identifica siempre a 1 host emisor, mientras que TTL, Protocolo y Suma de comprobación almacenan valores de control.

6. Refer to the exhibit. PC1 issues an ARP request because it needs to send a packet to PC3. In this scenario, what will happen next?
    - **Respuesta: RT1 will send an ARP reply with its own Fa0/0 MAC address.**
    - Cuando la dirección IPv4 de destino (PC3) pertenece a una red distinta a la de origen (PC1), PC1 debe enviar la trama a su puerta de enlace predeterminada (RT1).
    - Si la entrada de la puerta de enlace predeterminada no figura en la tabla ARP, PC1 envía una solicitud ARP para obtener la dirección MAC de la puerta de enlace.
    - Solo el dispositivo con la dirección IPv4 solicitada responde, por lo que el router RT1 envía una respuesta ARP unicast con su propia dirección MAC de la interfaz Fa0/0.

7. Refer to the exhibit. The exhibit shows a small switched network and the contents of the MAC address table of the switch. PC1 has sent a frame addressed to PC3. What will the switch do with the frame?
    - **Respuesta: The switch will forward the frame to all ports except port 4.**
    - Un switch Ethernet de Capa 2 reenvía tramas buscando una coincidencia entre la dirección MAC de destino de la trama y una entrada en su tabla de direcciones MAC.
    - Si la dirección MAC unicast de destino no está en la tabla, el switch reenvía la trama por todos los puertos excepto por el puerto de entrada.
    - Como la tabla MAC no contiene la dirección MAC de PC3, el switch inunda esta trama unicast desconocida por todos los puertos excepto el puerto 4 de entrada.

8. Refer to the exhibit. A network administrator is connecting a new host to the Registrar LAN. The host needs to communicate with remote networks. What IP address would be configured as the default gateway on the new host?
    - **Respuesta: 192.168.235.234**
    - Un host necesita una dirección de puerta de enlace predeterminada para alcanzar redes remotas, y esa dirección corresponde a la interfaz del router conectada a la red local.
    - En un router Cisco, el comando `description` identifica la red conectada y el comando `ip address` asigna la dirección IPv4 y máscara a esa interfaz.
    - La interfaz `gi0/1` tiene la descripción `Connects to the Registrar LAN` y la dirección IPv4 `192.168.235.234`, por lo que los hosts en esa LAN deben usar `192.168.235.234`.

---

**Anexo: Capturas del material de Cisco Introduction to Networks**

![](<../cisco-course/assets/Screenshot 2026-10-22 at 21.28.37.JPG>){ width=48% } ![](<../cisco-course/assets/Screenshot 2026-10-22 at 21.29.06.JPG>){ width=48% }

![](<../cisco-course/assets/Screenshot 2026-10-22 at 21.29.52.JPG>){ width=48% } ![](<../cisco-course/assets/Screenshot 2026-10-22 at 21.31.37.JPG>){ width=48% }

![](<../cisco-course/assets/Screenshot 2026-10-22 at 21.32.27.JPG>){ width=48% } ![](<../cisco-course/assets/Screenshot 2026-10-22 at 21.33.04.JPG>){ width=48% }

![](<../cisco-course/assets/Screenshot 2026-10-22 at 21.37.30.JPG>){ width=48% } ![](<../cisco-course/assets/Screenshot 2026-10-22 at 21.37.47.JPG>){ width=48% }

