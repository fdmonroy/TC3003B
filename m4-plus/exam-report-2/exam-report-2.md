---
title: "CCNA Practice Final 2"
subtitle: "Implementación de redes de área amplia y servicios distribuidos (TC3003B.570)"
author: "Fernando Daniel Monroy Sánchez (A01750536)"
date: "22 de octubre de 2026"
lang: es-MX
---

**Profesor:** Juan Manuel Campos Sandoval

---

1. Three devices are on three different subnets. Match the network address and the broadcast address with each subnet where these devices are located. Device 1: IP address 192.168.10.77/28 on subnet 1. Device 2: IP address 192.168.10.17/30 on subnet 2. Device 3: IP address 192.168.10.35/29 on subnet 3.
    - **Respuesta: Subnet 1 network number -> 192.168.10.64; Subnet 2 broadcast address -> 192.168.10.19; Subnet 3 network number -> 192.168.10.32; Subnet 1 broadcast address -> 192.168.10.79; Subnet 2 network number -> 192.168.10.16; Subnet 3 broadcast address -> 192.168.10.39**
    - La tabla de división en subredes muestra que tomar bits prestados en el cuarto octeto duplica las subredes y reduce la cantidad de direcciones de host: `/28` crea bloques de 16 direcciones, `/29` bloques de 8 direcciones y `/30` bloques de 4 direcciones.
    - Para la subred 1 (`/28`), la dirección `.77` se ubica en el intervalo `.64` a `.79`, por lo que la dirección de red es `192.168.10.64` y la de difusión es `192.168.10.79`.
    - Para la subred 2 (`/30`), la dirección `.17` se ubica en el intervalo `.16` a `.19`, con dirección de red `192.168.10.16` y difusión en `192.168.10.19`.
    - Para la subred 3 (`/29`), la dirección `.35` se ubica en el intervalo `.32` a `.39`, con dirección de red `192.168.10.32` y difusión en `192.168.10.39`.

2. Given network 172.18.109.0, which subnet mask would be used if 6 host bits were available?
    - **Respuesta: 255.255.255.192**
    - La tabla oficial de subredes de una red `/24` indica que la fila `/26` reserva exactamente 6 bits para la porción de host en el cuarto octeto.
    - En notación binaria, el cuarto octeto con 2 bits de red y 6 bits de host (`11000000`) equivale en formato decimal punteado a `255.255.255.192`.
    - Esta máscara `/26` genera 4 subredes utilizables y permite albergar 62 direcciones de host por subred.

3. Refer to the exhibit. A user issues the command netstat -r on a workstation. Which IPv6 address is one of the link-local addresses of the workstation?
    - **Respuesta: fe80::30d0:115:3f57:fe4c/128**
    - El material de Cisco define que las direcciones IPv6 link local residen exclusivamente en el rango reservado `fe80::/10`.
    - Los primeros 10 bits fijos (`1111 1110 10xx xxxx`) restringen el primer hexteto a un valor comprendido entre `fe80` y `febf`.
    - En la salida del comando `netstat -r`, la dirección `fe80::30d0:115:3f57:fe4c/128` contiene el prefijo `fe80` y la longitud `/128` que identifica la interfaz de host local en ese enlace.

4. What type of IPv6 address is represented by ::1/128?
    - **Respuesta: loopback**
    - El diagrama de clasificación de direcciones IPv6 unicast distingue categorías como Global Unicast, Link local, Loopback, Unspecified, Unique Local y Embedded IPv4.
    - Dentro de este esquema formal, la dirección `::1/128` corresponde a la dirección de loopback local.
    - El nodo utiliza `::1/128` para enviar paquetes hacia sí mismo y comprobar que la pila de protocolos TCP/IP funcione correctamente sin enviar tráfico al medio físico.

5. Refer to the exhibit. What does the value of the window size specify?
    - **Respuesta: the amount of data that can be sent before an acknowledgment is required**
    - El texto de control de flujo en TCP determina que el tamaño de ventana define la cantidad de bytes que pueden transmitirse antes de esperar un acuse de recibo.
    - Este valor corresponde al volumen de datos que el equipo receptor puede aceptar y almacenar en su búfer en un instante específico.
    - El tamaño de ventana se negocia durante el establecimiento de la sesión y el receptor lo actualiza de forma continua en cada segmento transmitido.

6. To which TCP port group does the port 414 belong?
    - **Respuesta: well-known**
    - La IANA divide el espacio de puertos de 16 bits (0 a 65535) en 3 rangos: puertos conocidos de 0 a 1023, puertos registrados de 1024 a 49151 y puertos privados o dinámicos de 49152 a 65535.
    - Los puertos conocidos se reservan para servicios y aplicaciones universales como servidores web, transferencia de archivos y acceso remoto.
    - Dado que el número 414 se ubica dentro del rango de 0 a 1023, queda clasificado como un puerto conocido.

7. Which statement describes the characteristics of packet-filtering and stateful firewalls as they relate to the OSI model?
    - **Respuesta: A packet-filtering firewall typically can filter up to the transport layer, whereas a stateful firewall can filter up to the session layer.**
    - El material de Cisco explica que los firewalls de filtrado de paquetes inspeccionan direcciones IP y puertos analizando tráfico hasta la capa de transporte (Capa 4).
    - Los firewalls con inspección de estado monitorean las conexiones activas y verifican que el tráfico entrante corresponda a respuestas legítimas hasta la capa de sesión (Capa 5).
    - Al conservar el estado de cada flujo, el firewall stateful bloquea paquetes entrantes no solicitados y mitiga ataques directos a la red.

8. Only employees connected to IPv6 interfaces are having difficulty connecting to remote networks. The analyst wants to verify that IPv6 routing has been enabled. What is the best command to use to accomplish the task?
    - **Respuesta: show running-config**
    - Para que un router Cisco encamine paquetes entre subredes IPv6 es obligatorio habilitar el comando de configuración global `ipv6 unicast-routing`.
    - La forma directa de confirmar que esta instrucción global forma parte de la configuración activa del router consiste en consultar el archivo con `show running-config`.
    - Otros comandos informan el estado operativo de interfaces individuales pero no validan si el motor de enrutamiento global IPv6 está activo en el dispositivo.

9. What happens when a switch receives a frame and the calculated CRC value is different than the value that is in the FCS field?
    - **Respuesta: The switch drops the frame.**
    - El campo de secuencia de verificación de trama (FCS) de 4 bytes permite detectar si ocurrieron errores de bits durante el trayecto físico.
    - El switch receptor recalcula el código de redundancia cíclica (CRC) y lo compara contra el valor registrado en el campo FCS al final de la trama.
    - Si ambos valores no coinciden, el switch determina que la trama contiene señales no deseadas o datos dañados y descarta la trama de inmediato.

10. Which two issues can cause both runts and giants in Ethernet networks? (Choose two.)
    - **Respuesta: a malfunctioning NIC; half-duplex operations**
    - El estándar Ethernet establece que cualquier trama menor a 64 bytes se cataloga como fragmento de colisión o trama enana, producto habitual de colisiones en enlaces semidúplex.
    - Las tramas que sobrepasan el tamaño máximo esperado de 1518 bytes se consideran tramas gigantes y suelen generarse por una tarjeta de red (NIC) defectuosa que transmite señales corruptas.
    - Por lo tanto, operar en modo semidúplex con colisiones frecuentes y una tarjeta de red con mal funcionamiento son las 2 causas de tramas enanas y gigantes.

11. Which two functions are performed at the LLC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)
    - **Respuesta: places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame; adds Ethernet control information to network protocol data**
    - La subcapa de control de enlace lógico (LLC, IEEE 802.2) enlaza el software de red de los niveles superiores con los componentes de hardware de los niveles inferiores.
    - La subcapa LLC inserta información en la trama que especifica cuál protocolo de Capa 3 (como IPv4 o IPv6) viaja encapsulado dentro del paquete de datos.
    - Además, la subcapa LLC agrega información de control de enlace a los datos del protocolo de red antes de transferirlos a la subcapa MAC.

---

**Anexo: Capturas del material de Cisco Introduction to Networks**

![](<assets/11-5-2-subnet-within-an-octet-boundary.jpg>){ width=48% } ![](<assets/12-3-7-ipv6-lla.jpg>){ width=48% }

![](<assets/12-3-3-types-of-ipv6-unicast-addresses.jpg>){ width=48% } ![](<assets/14-6-5-tcp-flow-control-window-size-and-acknowledgments.jpg>){ width=48% }

![](<assets/14-4-3-port-number-groups.jpg>){ width=48% } ![](<assets/16-3-6-types-of-firewalls.jpg>){ width=48% }

![](<assets/12-4-1-static-gua-configuration-on-a-router.jpg>){ width=48% } ![](<assets/7-1-4-ethernet-frame-fields.jpg>){ width=48% }

![](<assets/7-1-2-data-link-sublayers.jpg>){ width=48% }
