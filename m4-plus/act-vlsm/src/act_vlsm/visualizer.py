"""
Módulo de visualización gráfica para la actividad VLSM.
Genera diagramas vectoriales y de alta resolución de:
1. Topología lógica y física de la red nacional Tec de Monterrey.
2. Mapa horizontal de asignación de bloques del espacio 172.16.0.0/16.
3. Árbol de subdivisión binaria jerárquica VLSM.
"""

from pathlib import Path
from typing import Optional
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def ensure_assets_dir() -> Path:
    """Garantiza la existencia del directorio assets."""
    assets_dir = Path("assets")
    assets_dir.mkdir(parents=True, exist_ok=True)
    return assets_dir


def plot_address_space_blocks(output_path: Optional[Path] = None) -> Path:
    """
    Genera un diagrama de bloques horizontales que reproduce y extiende
    la vista general del espacio 172.16.0.0/16 en ocho bloques /19.
    """
    if output_path is None:
        output_path = ensure_assets_dir() / "espacio_direcciones_bloques.png"

    fig, ax = plt.subplots(figsize=(12, 4.8), dpi=300)
    plt.subplots_adjust(left=0.04, right=0.96, top=0.82, bottom=0.18)

    blocks = [
        {"num": 1, "title": "Bloque 1: Prepa Tec", "sub": "172.16.0.0/19 (8,192 IPs)\n8,000 requeridos (100% bloque)", "color": "#2563EB", "text_color": "white"},
        {"num": 2, "title": "Bloque 2: Ingeniería", "sub": "172.16.32.0/20 (4,096 IPs)\n4,000 req | 4,096 libre", "color": "#059669", "text_color": "white"},
        {"num": 3, "title": "Bloque 3: Negocios", "sub": "172.16.64.0/20 (4,096 IPs)\n4,000 req | 4,096 libre", "color": "#D97706", "text_color": "white"},
        {"num": 4, "title": "Bloque 4: Creativos", "sub": "172.16.96.0/21 (2,048 IPs)\n2,000 req | 6,144 libre", "color": "#7C3AED", "text_color": "white"},
        {"num": 5, "title": "Bloque 5: Médicas", "sub": "172.16.128.0/22 (1,024 IPs)\n1,000 req | 7,168 libre", "color": "#DB2777", "text_color": "white"},
        {"num": 6, "title": "Bloque 6: Humanidades", "sub": "172.16.160.0/23 (512 IPs)\n500 req | 7,680 libre", "color": "#0891B2", "text_color": "white"},
        {"num": 7, "title": "Bloque 7: Reserva", "sub": "172.16.192.0/19 (8,192 IPs)\nReserva institucional 100%", "color": "#EA580C", "text_color": "white"},
        {"num": 8, "title": "Bloque 8: WANs Core", "sub": "172.16.224.0/19 (8,192 IPs)\n8,168 libre | 24 IPs WAN /30", "color": "#475569", "text_color": "white"},
    ]

    total_width = 8.0
    block_width = 1.0
    bar_y = 0.35
    bar_h = 0.40

    for i, b in enumerate(blocks):
        x = i * block_width
        rect = patches.FancyBboxPatch(
            (x + 0.015, bar_y),
            block_width - 0.03,
            bar_h,
            boxstyle="round,pad=0.01,rounding_size=0.02",
            edgecolor="#1E293B",
            facecolor=b["color"],
            linewidth=1.2
        )
        ax.add_patch(rect)

        # Encabezado del bloque
        ax.text(
            x + block_width / 2.0,
            bar_y + bar_h - 0.08,
            b["title"],
            ha="center",
            va="center",
            fontsize=8.5,
            fontweight="bold",
            color=b["text_color"]
        )

        # Detalle de direccionamiento
        ax.text(
            x + block_width / 2.0,
            bar_y + 0.12,
            b["sub"],
            ha="center",
            va="center",
            fontsize=6.8,
            color=b["text_color"]
        )

    # Limites y flecha superior de primer subneteo
    ax.annotate(
        "",
        xy=(8.0, 0.88),
        xytext=(0.0, 0.88),
        arrowprops=dict(arrowstyle="<->", color="#0F172A", lw=1.5)
    )
    ax.text(
        4.0,
        0.92,
        "Primer subneteo: ocho bloques iguales a partir de 172.16.0.0/16 (cada bloque contiene 8,192 direcciones /19)",
        ha="center",
        va="bottom",
        fontsize=9.5,
        fontweight="bold",
        color="#0F172A"
    )

    # Etiquetas de bordes de la red
    ax.text(0.0, 0.22, "172.16.0.0\n(Inicio red)", ha="left", va="top", fontsize=8.5, fontweight="bold", color="#1E293B")
    ax.text(8.0, 0.22, "172.16.255.255\n(Broadcast global)", ha="right", va="top", fontsize=8.5, fontweight="bold", color="#1E293B")

    ax.set_xlim(-0.1, 8.1)
    ax.set_ylim(0.0, 1.05)
    ax.axis("off")

    fig.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return output_path


def plot_network_topology(output_path: Optional[Path] = None) -> Path:
    """
    Genera el diagrama formal de la topología lógica y física de la red nacional Tec,
    detallando enrutadores, interfaces GigE y Seriales, subredes e IPs asignadas.
    """
    if output_path is None:
        output_path = ensure_assets_dir() / "topologia_red_nacional.png"

    fig, ax = plt.subplots(figsize=(13, 9.2), dpi=300)
    plt.subplots_adjust(left=0.03, right=0.97, top=0.95, bottom=0.05)

    # Coordenadas de los nodos
    core_pos = np.array([6.5, 4.8])

    campus_nodes = [
        {
            "id": "PREPA",
            "name": "Router Sede Prepa Tec",
            "pos": np.array([2.0, 8.0]),
            "lan_net": "172.16.0.0/19",
            "lan_gw": "172.16.0.1 (Gi0/0)",
            "hosts_req": "8,000 hosts",
            "wan_core_ip": "172.16.255.233 (Se0/1/0)",
            "wan_sede_ip": "172.16.255.234 (Se0/1/0)",
            "wan_net": "WAN 1: 172.16.255.232/30",
            "color": "#2563EB",
        },
        {
            "id": "ING",
            "name": "Router Sede Ingeniería",
            "pos": np.array([6.5, 8.5]),
            "lan_net": "172.16.32.0/20",
            "lan_gw": "172.16.32.1 (Gi0/0)",
            "hosts_req": "4,000 hosts",
            "wan_core_ip": "172.16.255.237 (Se0/1/1)",
            "wan_sede_ip": "172.16.255.238 (Se0/1/0)",
            "wan_net": "WAN 2: 172.16.255.236/30",
            "color": "#059669",
        },
        {
            "id": "NEG",
            "name": "Router Sede Negocios",
            "pos": np.array([11.0, 8.0]),
            "lan_net": "172.16.64.0/20",
            "lan_gw": "172.16.64.1 (Gi0/0)",
            "hosts_req": "4,000 hosts",
            "wan_core_ip": "172.16.255.241 (Se0/1/2)",
            "wan_sede_ip": "172.16.255.242 (Se0/1/0)",
            "wan_net": "WAN 3: 172.16.255.240/30",
            "color": "#D97706",
        },
        {
            "id": "CREA",
            "name": "Router Sede Creativos",
            "pos": np.array([11.0, 1.8]),
            "lan_net": "172.16.96.0/21",
            "lan_gw": "172.16.96.1 (Gi0/0)",
            "hosts_req": "2,000 hosts",
            "wan_core_ip": "172.16.255.245 (Se0/1/3)",
            "wan_sede_ip": "172.16.255.246 (Se0/1/0)",
            "wan_net": "WAN 4: 172.16.255.244/30",
            "color": "#7C3AED",
        },
        {
            "id": "MED",
            "name": "Router Sede Médicas",
            "pos": np.array([6.5, 1.2]),
            "lan_net": "172.16.128.0/22",
            "lan_gw": "172.16.128.1 (Gi0/0)",
            "hosts_req": "1,000 hosts",
            "wan_core_ip": "172.16.255.249 (Se0/1/4)",
            "wan_sede_ip": "172.16.255.250 (Se0/1/0)",
            "wan_net": "WAN 5: 172.16.255.248/30",
            "color": "#DB2777",
        },
        {
            "id": "HUM",
            "name": "Router Sede Humanidades",
            "pos": np.array([2.0, 1.8]),
            "lan_net": "172.16.160.0/23",
            "lan_gw": "172.16.160.1 (Gi0/0)",
            "hosts_req": "500 hosts",
            "wan_core_ip": "172.16.255.253 (Se0/1/5)",
            "wan_sede_ip": "172.16.255.254 (Se0/1/0)",
            "wan_net": "WAN 6: 172.16.255.252/30",
            "color": "#0891B2",
        },
    ]

    # Dibujar enlaces WAN (líneas punteadas de alta visibilidad)
    for c in campus_nodes:
        p1 = core_pos
        p2 = c["pos"]

        # Línea del enlace
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="#475569", lw=2.2, linestyle="--", zorder=1)

        # Punto medio para etiqueta de la red WAN
        mid = (p1 + p2) / 2.0
        offset = np.array([-(p2[1] - p1[1]), p2[0] - p1[0]])
        norm = np.linalg.norm(offset)
        if norm > 0:
            offset = (offset / norm) * 0.38
        label_pos = mid + offset

        bbox_props = dict(boxstyle="round,pad=0.25", facecolor="#F8FAFC", edgecolor="#64748B", lw=0.8)
        ax.text(
            label_pos[0],
            label_pos[1],
            f"{c['wan_net']}",
            ha="center",
            va="center",
            fontsize=7.2,
            fontweight="bold",
            color="#0F172A",
            bbox=bbox_props,
            zorder=3
        )

        # Etiquetas de interfaces en extremos
        core_int_pos = p1 + (p2 - p1) * 0.22
        sede_int_pos = p2 + (p1 - p2) * 0.20

        ax.text(
            core_int_pos[0],
            core_int_pos[1],
            c["wan_core_ip"],
            fontsize=6.2,
            ha="center",
            va="center",
            color="#1E293B",
            bbox=dict(boxstyle="square,pad=0.15", facecolor="#E2E8F0", edgecolor="none", alpha=0.9),
            zorder=3
        )

        ax.text(
            sede_int_pos[0],
            sede_int_pos[1],
            c["wan_sede_ip"],
            fontsize=6.2,
            ha="center",
            va="center",
            color="#1E293B",
            bbox=dict(boxstyle="square,pad=0.15", facecolor="#E2E8F0", edgecolor="none", alpha=0.9),
            zorder=3
        )

    # Dibujar Nodo Central Core Nacional
    core_box = patches.FancyBboxPatch(
        (core_pos[0] - 1.35, core_pos[1] - 0.75),
        2.7,
        1.5,
        boxstyle="round,pad=0.08,rounding_size=0.15",
        facecolor="#1E293B",
        edgecolor="#0F172A",
        lw=2.0,
        zorder=4
    )
    ax.add_patch(core_box)

    ax.text(
        core_pos[0],
        core_pos[1] + 0.35,
        "NACIONAL (Core)",
        ha="center",
        va="center",
        fontsize=11.5,
        fontweight="bold",
        color="#F8FAFC",
        zorder=5
    )
    ax.text(
        core_pos[0],
        core_pos[1] - 0.05,
        "Cisco ISR 4451 Core Router\nLoopback0: 172.16.255.1/32\nSeis Interfaces Seriales WAN",
        ha="center",
        va="center",
        fontsize=7.5,
        color="#CBD5E1",
        zorder=5
    )

    # Dibujar Nodos Campus y Nubes LAN
    for c in campus_nodes:
        pos = c["pos"]
        r_box = patches.FancyBboxPatch(
            (pos[0] - 1.25, pos[1] - 0.65),
            2.5,
            1.3,
            boxstyle="round,pad=0.06,rounding_size=0.12",
            facecolor="#FFFFFF",
            edgecolor=c["color"],
            lw=2.2,
            zorder=4
        )
        ax.add_patch(r_box)

        ax.text(
            pos[0],
            pos[1] + 0.32,
            c["name"],
            ha="center",
            va="center",
            fontsize=9.0,
            fontweight="bold",
            color=c["color"],
            zorder=5
        )
        ax.text(
            pos[0],
            pos[1] - 0.12,
            f"LAN: {c['lan_net']}\nGateway: {c['lan_gw']}\nCapacidad: {c['hosts_req']}",
            ha="center",
            va="center",
            fontsize=7.2,
            color="#334155",
            zorder=5
        )

    # Título y Metadatos
    ax.text(
        6.5,
        9.65,
        "Topología Nacional de Red con Direccionamiento VLSM | Tecnológico de Monterrey",
        ha="center",
        va="center",
        fontsize=13.0,
        fontweight="bold",
        color="#0F172A"
    )
    ax.text(
        6.5,
        9.35,
        "Red Base Institucional: 172.16.0.0/16 | Seis Sedes Académicas y Seis Enlaces WAN Punto a Punto",
        ha="center",
        va="center",
        fontsize=8.5,
        color="#475569"
    )

    ax.set_xlim(0.0, 13.0)
    ax.set_ylim(0.0, 10.0)
    ax.axis("off")

    fig.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return output_path
