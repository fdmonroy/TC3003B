"""
Módulo de renderizado y formateo de tablas para la actividad VLSM.
Genera estructuras tabulares limpias y compatibles con Great Tables y LaTeX booktabs.
"""

from typing import List, Dict, Any, Optional
import pandas as pd
from great_tables import GT

from act_vlsm.network_calc import (
    SubnetRequirement,
    AllocatedSubnet,
    build_primary_subnets_8_blocks,
    get_free_blocks_scheme_a,
    get_free_blocks_scheme_b,
)


def create_requirements_df(reqs: List[SubnetRequirement]) -> pd.DataFrame:
    """Crea el DataFrame de requerimientos de hosts sin columna de notas."""
    data = []
    short_names = [
        "Prepa Tec",
        "Ingeniería Tec",
        "Negocios Tec",
        "Estudios Creativos",
        "Ciencias Médicas",
        "Humanidades",
        "Enlaces WAN (6)",
    ]
    for i, r in enumerate(reqs):
        if r.category == "WAN" or "WAN" in r.name:
            h = 2
            mask_str = "255.255.255.252 (/30)"
            req_str = "2 c/u (6 enlaces)"
            usable_str = "2 c/u"
        else:
            h = r.calculate_host_bits()
            prefix = r.calculate_prefix()
            usable = r.usable_hosts()
            usable_str = f"{usable:,}"
            req_str = f"{r.required_hosts:,}"
            if prefix <= 24:
                third = 256 - (1 << (24 - prefix))
                fourth = 0
            else:
                third = 255
                fourth = 256 - (1 << (32 - prefix))
            mask_str = f"255.255.{third}.{fourth} (/{prefix})"
        data.append({
            "Área Académica": short_names[i],
            "Hosts Req.": req_str,
            "Bits h": h,
            "Hosts Útiles": usable_str,
            "Máscara / Prefijo": mask_str,
        })
    return pd.DataFrame(data)


def create_subnets_summary_df(subnets: List[AllocatedSubnet]) -> pd.DataFrame:
    """Crea el DataFrame de resumen operacional de subredes LAN."""
    short_names = [
        "Prepa Tec",
        "Ingeniería Tec",
        "Negocios Tec",
        "Estudios Creativos",
        "Ciencias Médicas",
        "Humanidades",
    ]
    data = []
    for i, s in enumerate(subnets):
        data.append({
            "Área Académica": short_names[i],
            "IP de red": str(s.network_address),
            "Rango Útil": f"{s.first_usable} a {s.last_usable}",
            "Broadcast": str(s.broadcast_address),
            "Máscara": f"{s.netmask} (/{s.prefix})",
            "Req.": f"{s.required_hosts:,}",
            "Útiles": f"{s.usable_hosts:,}",
            "Libres": f"{s.free_hosts:,}",
        })
    return pd.DataFrame(data)


def create_subnets_binary_df(subnets: List[AllocatedSubnet]) -> pd.DataFrame:
    """Crea el DataFrame de justificación binaria para subredes LAN."""
    short_names = [
        "Prepa Tec",
        "Ingeniería Tec",
        "Negocios Tec",
        "Estudios Creativos",
        "Ciencias Médicas",
        "Humanidades",
    ]
    data = []
    for i, s in enumerate(subnets):
        data.append({
            "#": s.index,
            "Área Académica": short_names[i],
            "Red (Dec)": s.cidr_str,
            "Red (Binario)": s.network_bin,
            "Broadcast (Dec)": str(s.broadcast_address),
            "Broadcast (Binario)": s.broadcast_bin,
        })
    return pd.DataFrame(data)


def create_wan_summary_df(wan_subnets: List[AllocatedSubnet]) -> pd.DataFrame:
    """Crea el DataFrame de enlaces WAN con columnas idénticas a subredes LAN."""
    short_names = [
        "WAN 1 (Prepa)",
        "WAN 2 (Ingeniería)",
        "WAN 3 (Negocios)",
        "WAN 4 (Creativos)",
        "WAN 5 (Médicas)",
        "WAN 6 (Humanidades)",
    ]
    data = []
    for i, w in enumerate(wan_subnets):
        data.append({
            "Enlace WAN": short_names[i],
            "IP de red": str(w.network_address),
            "Rango Útil": f"{w.first_usable} a {w.last_usable}",
            "Broadcast": str(w.broadcast_address),
            "Máscara": f"{w.netmask} (/{w.prefix})",
            "Req.": f"{w.required_hosts:,}",
            "Útiles": f"{w.usable_hosts:,}",
            "Libres": f"{w.free_hosts:,}",
        })
    return pd.DataFrame(data)


def create_wan_binary_df(wan_subnets: List[AllocatedSubnet]) -> pd.DataFrame:
    """Crea el DataFrame de justificación binaria de enlaces WAN."""
    data = []
    for w in wan_subnets:
        data.append({
            "WAN": w.name,
            "Red (Dec)": w.cidr_str,
            "Red (Binario)": w.network_bin,
            "Broadcast (Dec)": str(w.broadcast_address),
            "Broadcast (Binario)": w.broadcast_bin,
        })
    return pd.DataFrame(data)


def create_primary_blocks_df() -> pd.DataFrame:
    """Crea el DataFrame de los ocho bloques iguales /19 del primer subneteo."""
    blocks = build_primary_subnets_8_blocks()
    short_descriptions = [
        "Prepa Tec (8,000 req)",
        "Ingeniería Tec (4,000 req)",
        "Negocios Tec (4,000 req)",
        "Estudios Creativos (2,000 req)",
        "Ciencias Médicas (1,000 req)",
        "Humanidades (500 req)",
        "Reserva institucional libre",
        "Enlaces WAN /30 y núcleo",
    ]
    data = []
    for i, b in enumerate(blocks):
        data.append({
            "Bloque": b["block_num"],
            "Red CIDR": b["network"],
            "Rango de direcciones": f"{b['network_address']} a {b['broadcast_address']}",
            "IPs totales": f"{b['total_ips']:,}",
            "Máscara": b["netmask"],
            "Asignación sugerida": short_descriptions[i],
        })
    return pd.DataFrame(data)


def create_free_blocks_df(scheme: str = "A") -> pd.DataFrame:
    """Crea el DataFrame de identificación de franjas libres."""
    if scheme == "A":
        raw = get_free_blocks_scheme_a()
        short_locations = [
            "Bloque 2 (Ingeniería)",
            "Bloque 3 (Negocios)",
            "Bloque 4 (Creativos)",
            "Bloque 5 (Médicas)",
            "Bloque 6 (Humanidades)",
            "Bloque 7 (Completo)",
            "Bloque 8 (Núcleo)",
        ]
        short_purposes = [
            "Expansión Ingeniería",
            "Expansión Negocios",
            "Expansión Creativos",
            "Hospitales y Salud",
            "Posgrado y Extensión",
            "Reserva institucional",
            "Datacenter y WANs",
        ]
    else:
        raw = get_free_blocks_scheme_b()
        short_locations = [
            "Bloque 3 (Remanente)",
            "Bloques 4 a 7 (Contiguos)",
            "Bloque 8 (Núcleo)",
        ]
        short_purposes = [
            "Remanente bloque 3",
            "Mitad espacio /16 libre",
            "Datacenter y servicios",
        ]

    data = []
    for i, r in enumerate(raw):
        data.append({
            "Ubicación": short_locations[i],
            "Rango": r["range"],
            "Dirección inicial": r["first_ip"],
            "Dirección final": r["last_ip"],
            "IPs libres": f"{r['total_ips']:,}",
            "Propósito sugerido": short_purposes[i],
        })
    return pd.DataFrame(data)


def build_gt_table(
    df: pd.DataFrame,
    title: str,
    subtitle: str = "",
    column_alignments: Optional[Dict[str, str]] = None
) -> GT:
    """Construye un objeto Great Table estandarizado con formato booktabs."""
    gt = GT(df)
    if title:
        gt = gt.tab_header(
            title=title,
            subtitle=subtitle if subtitle else None
        )
    return gt
