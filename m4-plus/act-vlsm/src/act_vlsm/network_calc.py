"""
Módulo de cálculo y validación de direccionamiento VLSM.
Implementa algoritmos de dimensionamiento de subredes, conversión binaria,
validación de no solapamiento y métricas de aprovechamiento del espacio IP.
"""

from dataclasses import dataclass
import ipaddress
from typing import List, Dict, Tuple, Optional


def ip_to_bin_str(ip: ipaddress.IPv4Address) -> str:
    """Convierte una dirección IPv4 a cadena binaria con puntos separadores."""
    octets = [f"{int(b):08b}" for b in str(ip).split(".")]
    return ".".join(octets)


@dataclass
class SubnetRequirement:
    """Requerimiento de capacidad para un segmento de red."""
    name: str
    required_hosts: int
    category: str
    notes: str = ""

    def calculate_host_bits(self) -> int:
        """Calcula el número mínimo de bits de host requeridos."""
        # Se requieren 2^h - 2 >= required_hosts
        needed = self.required_hosts + 2
        h = 1
        while (1 << h) < needed:
            h += 1
        return h

    def calculate_prefix(self) -> int:
        """Calcula el prefijo CIDR mínimo."""
        return 32 - self.calculate_host_bits()

    def usable_hosts(self) -> int:
        """Calcula los hosts utilizables según la fórmula 2^h - 2."""
        h = self.calculate_host_bits()
        return (1 << h) - 2

    def total_addresses(self) -> int:
        """Calcula el total de direcciones del bloque."""
        h = self.calculate_host_bits()
        return 1 << h


@dataclass
class AllocatedSubnet:
    """Detalle completo de una subred asignada mediante VLSM."""
    index: int
    name: str
    category: str
    required_hosts: int
    network: ipaddress.IPv4Network
    use_case: str = ""

    @property
    def network_address(self) -> ipaddress.IPv4Address:
        return self.network.network_address

    @property
    def broadcast_address(self) -> ipaddress.IPv4Address:
        return self.network.broadcast_address

    @property
    def netmask(self) -> ipaddress.IPv4Address:
        return self.network.netmask

    @property
    def prefix(self) -> int:
        return self.network.prefixlen

    @property
    def first_usable(self) -> ipaddress.IPv4Address:
        return self.network_address + 1

    @property
    def last_usable(self) -> ipaddress.IPv4Address:
        return self.broadcast_address - 1

    @property
    def total_addresses(self) -> int:
        return self.network.num_addresses

    @property
    def usable_hosts(self) -> int:
        return max(0, self.network.num_addresses - 2)

    @property
    def free_hosts(self) -> int:
        return self.usable_hosts - self.required_hosts

    @property
    def efficiency_pct(self) -> float:
        if self.usable_hosts == 0:
            return 0.0
        return (self.required_hosts / self.usable_hosts) * 100.0

    @property
    def network_bin(self) -> str:
        return ip_to_bin_str(self.network_address)

    @property
    def broadcast_bin(self) -> str:
        return ip_to_bin_str(self.broadcast_address)

    @property
    def netmask_bin(self) -> str:
        return ip_to_bin_str(self.netmask)

    @property
    def usable_range_str(self) -> str:
        return f"{self.first_usable} a {self.last_usable}"

    @property
    def cidr_str(self) -> str:
        return f"{self.network_address}/{self.prefix}"

    @property
    def mask_prefix_str(self) -> str:
        return f"{self.netmask} (/{self.prefix})"


def get_tec_requirements() -> List[SubnetRequirement]:
    """Retorna los requerimientos oficiales del escenario Tec de Monterrey."""
    return [
        SubnetRequirement(
            name="LAN Estudiantes de Prepa Tec",
            required_hosts=8000,
            category="LAN",
            notes="Subneteo inicial /19. Ocupa un bloque completo de 8,192 IPs."
        ),
        SubnetRequirement(
            name="LAN Estudiantes de Ingeniería Tec",
            required_hosts=4000,
            category="LAN",
            notes="Prefijo /20. Bloque de 4,096 IPs. Mitad de bloque /19."
        ),
        SubnetRequirement(
            name="LAN Estudiantes de Negocios Tec",
            required_hosts=4000,
            category="LAN",
            notes="Prefijo /20. Bloque de 4,096 IPs. Dimensión idéntica a Ingeniería."
        ),
        SubnetRequirement(
            name="LAN Estudiantes de Estudios Creativos Tec",
            required_hosts=2000,
            category="LAN",
            notes="Prefijo /21. Bloque de 2,048 IPs. Cuarta parte de bloque /19."
        ),
        SubnetRequirement(
            name="LAN Estudiantes de Ciencias Médicas Tec",
            required_hosts=1000,
            category="LAN",
            notes="Prefijo /22. Bloque de 1,024 IPs. Octava parte de bloque /19."
        ),
        SubnetRequirement(
            name="LAN Estudiantes de Humanidades",
            required_hosts=500,
            category="LAN",
            notes="Prefijo /23. Bloque de 512 IPs. Dieciseisava parte de bloque /19."
        ),
        SubnetRequirement(
            name="Enlaces WAN (6)",
            required_hosts=12,
            category="WAN",
            notes="Seis enlaces punto a punto de dos hosts útiles cada uno (/30)."
        ),
    ]


def build_primary_subnets_8_blocks() -> List[Dict[str, any]]:
    """
    Construye la división inicial de 172.16.0.0/16 en ocho bloques de tamaño /19.
    Cada bloque contiene 8,192 direcciones.
    """
    root_net = ipaddress.IPv4Network("172.16.0.0/16")
    blocks_19 = list(root_net.subnets(new_prefix=19))
    result = []
    
    descriptions = [
        "Bloque 1: Asignado a Prepa Tec (8,000 hosts requeridos)",
        "Bloque 2: Asignado a Ingeniería Tec (4,000 hosts requeridos)",
        "Bloque 3: Asignado a Negocios Tec (4,000 hosts requeridos)",
        "Bloque 4: Asignado a Estudios Creativos Tec (2,000 hosts requeridos)",
        "Bloque 5: Asignado a Ciencias Médicas Tec (1,000 hosts requeridos)",
        "Bloque 6: Asignado a Humanidades (500 hosts requeridos)",
        "Bloque 7: Bloque completo libre para reserva estratégica institucional",
        "Bloque 8: Último bloque para enlaces WAN /30 y expansión futura",
    ]
    
    colors = [
        "#3B82F6",  # Blue (Prepa)
        "#10B981",  # Green (Ingeniería)
        "#F59E0B",  # Yellow/Amber (Negocios)
        "#8B5CF6",  # Purple (Estudios Creativos)
        "#EC4899",  # Pink (Ciencias Médicas)
        "#06B6D4",  # Cyan (Humanidades)
        "#F97316",  # Light Orange (Reserva)
        "#64748B",  # Slate/Grey (WANs)
    ]
    
    for i, net in enumerate(blocks_19, start=1):
        result.append({
            "block_num": i,
            "network": str(net),
            "network_address": str(net.network_address),
            "broadcast_address": str(net.broadcast_address),
            "first_usable": str(net.network_address + 1),
            "last_usable": str(net.broadcast_address - 1),
            "prefix": net.prefixlen,
            "netmask": str(net.netmask),
            "total_ips": net.num_addresses,
            "description": descriptions[i - 1],
            "color": colors[i - 1],
        })
    return result


def build_scheme_a() -> Tuple[List[AllocatedSubnet], List[AllocatedSubnet]]:
    """
    Construye el Esquema A: Diseño Modular por Bloques Departamentales.
    Asigna cada área académica al inicio de su bloque /19 correspondiente (Bloques 1 al 6),
    mantiene el Bloque 7 como reserva completa, y ubica las seis subredes WAN /30
    en las últimas direcciones del Bloque 8 (172.16.255.232/30 a 172.16.255.252/30).
    """
    lan_subnets = [
        AllocatedSubnet(
            index=1,
            name="LAN Estudiantes de Prepa Tec",
            category="LAN",
            required_hosts=8000,
            network=ipaddress.IPv4Network("172.16.0.0/19"),
            use_case="Campus Prepa Tec Nacional"
        ),
        AllocatedSubnet(
            index=2,
            name="LAN Estudiantes de Ingeniería Tec",
            category="LAN",
            required_hosts=4000,
            network=ipaddress.IPv4Network("172.16.32.0/20"),
            use_case="Escuela de Ingeniería y Ciencias"
        ),
        AllocatedSubnet(
            index=3,
            name="LAN Estudiantes de Negocios Tec",
            category="LAN",
            required_hosts=4000,
            network=ipaddress.IPv4Network("172.16.64.0/20"),
            use_case="Escuela de Negocios EGADE y Pregrado"
        ),
        AllocatedSubnet(
            index=4,
            name="LAN Estudiantes de Estudios Creativos Tec",
            category="LAN",
            required_hosts=2000,
            network=ipaddress.IPv4Network("172.16.96.0/21"),
            use_case="Escuela de Arquitectura, Arte y Diseño"
        ),
        AllocatedSubnet(
            index=5,
            name="LAN Estudiantes de Ciencias Médicas Tec",
            category="LAN",
            required_hosts=1000,
            network=ipaddress.IPv4Network("172.16.128.0/22"),
            use_case="Escuela de Medicina y Ciencias de la Salud"
        ),
        AllocatedSubnet(
            index=6,
            name="LAN Estudiantes de Humanidades",
            category="LAN",
            required_hosts=500,
            network=ipaddress.IPv4Network("172.16.160.0/23"),
            use_case="Escuela de Humanidades y Educación"
        ),
    ]

    wan_uses = [
        "Enlace WAN Core Nacional a Sede Prepa Tec",
        "Enlace WAN Core Nacional a Sede Ingeniería Tec",
        "Enlace WAN Core Nacional a Sede Negocios Tec",
        "Enlace WAN Core Nacional a Sede Estudios Creativos Tec",
        "Enlace WAN Core Nacional a Sede Ciencias Médicas Tec",
        "Enlace WAN Core Nacional a Sede Humanidades",
    ]

    # Últimas direcciones del bloque 8 (172.16.224.0/19 -> termina en 172.16.255.255)
    wan_subnets = []
    base_fourth_octet = 232
    for i in range(6):
        net_str = f"172.16.255.{base_fourth_octet + (i * 4)}/30"
        wan_subnets.append(
            AllocatedSubnet(
                index=i + 1,
                name=f"WAN {i + 1}",
                category="WAN",
                required_hosts=2,
                network=ipaddress.IPv4Network(net_str),
                use_case=wan_uses[i]
            )
        )

    return lan_subnets, wan_subnets


def build_scheme_b() -> Tuple[List[AllocatedSubnet], List[AllocatedSubnet]]:
    """
    Construye el Esquema B: Empaquetamiento Contiguo Jerárquico VLSM.
    Asigna todas las subredes de manera estrictamente contigua sin espacios intermedios.
    """
    lan_subnets = [
        AllocatedSubnet(
            index=1,
            name="LAN Estudiantes de Prepa Tec",
            category="LAN",
            required_hosts=8000,
            network=ipaddress.IPv4Network("172.16.0.0/19"),
            use_case="Campus Prepa Tec Nacional"
        ),
        AllocatedSubnet(
            index=2,
            name="LAN Estudiantes de Ingeniería Tec",
            category="LAN",
            required_hosts=4000,
            network=ipaddress.IPv4Network("172.16.32.0/20"),
            use_case="Escuela de Ingeniería y Ciencias"
        ),
        AllocatedSubnet(
            index=3,
            name="LAN Estudiantes de Negocios Tec",
            category="LAN",
            required_hosts=4000,
            network=ipaddress.IPv4Network("172.16.48.0/20"),
            use_case="Escuela de Negocios EGADE y Pregrado"
        ),
        AllocatedSubnet(
            index=4,
            name="LAN Estudiantes de Estudios Creativos Tec",
            category="LAN",
            required_hosts=2000,
            network=ipaddress.IPv4Network("172.16.64.0/21"),
            use_case="Escuela de Arquitectura, Arte y Diseño"
        ),
        AllocatedSubnet(
            index=5,
            name="LAN Estudiantes de Ciencias Médicas Tec",
            category="LAN",
            required_hosts=1000,
            network=ipaddress.IPv4Network("172.16.72.0/22"),
            use_case="Escuela de Medicina y Ciencias de la Salud"
        ),
        AllocatedSubnet(
            index=6,
            name="LAN Estudiantes de Humanidades",
            category="LAN",
            required_hosts=500,
            network=ipaddress.IPv4Network("172.16.76.0/23"),
            use_case="Escuela de Humanidades y Educación"
        ),
    ]

    wan_uses = [
        "Enlace WAN Core Nacional a Sede Prepa Tec",
        "Enlace WAN Core Nacional a Sede Ingeniería Tec",
        "Enlace WAN Core Nacional a Sede Negocios Tec",
        "Enlace WAN Core Nacional a Sede Estudios Creativos Tec",
        "Enlace WAN Core Nacional a Sede Ciencias Médicas Tec",
        "Enlace WAN Core Nacional a Sede Humanidades",
    ]

    wan_subnets = []
    base_fourth_octet = 232
    for i in range(6):
        net_str = f"172.16.255.{base_fourth_octet + (i * 4)}/30"
        wan_subnets.append(
            AllocatedSubnet(
                index=i + 1,
                name=f"WAN {i + 1}",
                category="WAN",
                required_hosts=2,
                network=ipaddress.IPv4Network(net_str),
                use_case=wan_uses[i]
            )
        )

    return lan_subnets, wan_subnets


def validate_no_overlap(subnets: List[AllocatedSubnet]) -> bool:
    """Verifica formalmente que ninguna subred se solape con otra."""
    for i in range(len(subnets)):
        for j in range(i + 1, len(subnets)):
            net_a = subnets[i].network
            net_b = subnets[j].network
            if net_a.overlaps(net_b):
                msg = f"Solapamiento detectado entre {net_a} y {net_b}"
                raise ValueError(msg)
    return True


def get_free_blocks_scheme_a() -> List[Dict[str, any]]:
    """Identifica las franjas de direcciones libres en el Esquema A."""
    free_ranges = [
        {
            "location": "Bloque 2 (Ingeniería)",
            "range": "172.16.48.0/20",
            "first_ip": "172.16.48.0",
            "last_ip": "172.16.63.255",
            "total_ips": 4096,
            "purpose": "Reserva de expansión para Escuela de Ingeniería"
        },
        {
            "location": "Bloque 3 (Negocios)",
            "range": "172.16.80.0/20",
            "first_ip": "172.16.80.0",
            "last_ip": "172.16.95.255",
            "total_ips": 4096,
            "purpose": "Reserva de expansión para Escuela de Negocios"
        },
        {
            "location": "Bloque 4 (Estudios Creativos)",
            "range": "172.16.104.0/21 y 172.16.112.0/20",
            "first_ip": "172.16.104.0",
            "last_ip": "172.16.127.255",
            "total_ips": 6144,
            "purpose": "Reserva para Estudios Creativos y Nuevas Carreras"
        },
        {
            "location": "Bloque 5 (Ciencias Médicas)",
            "range": "172.16.132.0/22, /21, /20",
            "first_ip": "172.16.132.0",
            "last_ip": "172.16.159.255",
            "total_ips": 7168,
            "purpose": "Reserva para Hospitales TecSalud y Laboratorios"
        },
        {
            "location": "Bloque 6 (Humanidades)",
            "range": "172.16.162.0/23, /22, /21, /20",
            "first_ip": "172.16.162.0",
            "last_ip": "172.16.191.255",
            "total_ips": 7680,
            "purpose": "Reserva para Posgrado y Extensión Cultural"
        },
        {
            "location": "Bloque 7 (Completo)",
            "range": "172.16.192.0/19",
            "first_ip": "172.16.192.0",
            "last_ip": "172.16.223.255",
            "total_ips": 8192,
            "purpose": "Reserva institucional completa para nuevos campus"
        },
        {
            "location": "Bloque 8 (Previo a WANs)",
            "range": "172.16.224.0 a 172.16.255.231",
            "first_ip": "172.16.224.0",
            "last_ip": "172.16.255.231",
            "total_ips": 8168,
            "purpose": "Reserva para centros de datos y enlaces WAN adicionales"
        },
    ]
    return free_ranges


def get_free_blocks_scheme_b() -> List[Dict[str, any]]:
    """Identifica las franjas de direcciones libres en el Esquema B."""
    free_ranges = [
        {
            "location": "Bloque 3 (Remanente)",
            "range": "172.16.78.0/23 a 172.16.95.255",
            "first_ip": "172.16.78.0",
            "last_ip": "172.16.95.255",
            "total_ips": 4608,
            "purpose": "Espacio contiguo remanente en bloque 3"
        },
        {
            "location": "Bloques 4 al 7 (Contiguos)",
            "range": "172.16.96.0 a 172.16.223.255",
            "first_ip": "172.16.96.0",
            "last_ip": "172.16.223.255",
            "total_ips": 32768,
            "purpose": "Mitad exacta del espacio total /16 contigua y libre"
        },
        {
            "location": "Bloque 8 (Previo a WANs)",
            "range": "172.16.224.0 a 172.16.255.231",
            "first_ip": "172.16.224.0",
            "last_ip": "172.16.255.231",
            "total_ips": 8168,
            "purpose": "Reserva de infraestructura central y servicios futuros"
        },
    ]
    return free_ranges
