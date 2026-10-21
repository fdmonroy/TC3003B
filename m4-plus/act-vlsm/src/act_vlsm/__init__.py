"""
Paquete act_vlsm para solucion integral de direccionamiento VLSM institucional.
"""

from act_vlsm.network_calc import (
    SubnetRequirement,
    AllocatedSubnet,
    get_tec_requirements,
    build_primary_subnets_8_blocks,
    build_scheme_a,
    build_scheme_b,
    validate_no_overlap,
    get_free_blocks_scheme_a,
    get_free_blocks_scheme_b,
    ip_to_bin_str,
)

from act_vlsm.visualizer import (
    plot_address_space_blocks,
    plot_network_topology,
)

from act_vlsm.ios_config import (
    generate_core_router_config,
    generate_campus_router_configs,
)

from act_vlsm.table_renderer import (
    create_requirements_df,
    create_subnets_summary_df,
    create_subnets_binary_df,
    create_wan_summary_df,
    create_wan_binary_df,
    create_primary_blocks_df,
    create_free_blocks_df,
    build_gt_table,
)

__all__ = [
    "SubnetRequirement",
    "AllocatedSubnet",
    "get_tec_requirements",
    "build_primary_subnets_8_blocks",
    "build_scheme_a",
    "build_scheme_b",
    "validate_no_overlap",
    "get_free_blocks_scheme_a",
    "get_free_blocks_scheme_b",
    "ip_to_bin_str",
    "plot_address_space_blocks",
    "plot_network_topology",
    "generate_core_router_config",
    "generate_campus_router_configs",
    "create_requirements_df",
    "create_subnets_summary_df",
    "create_subnets_binary_df",
    "create_wan_summary_df",
    "create_wan_binary_df",
    "create_primary_blocks_df",
    "create_free_blocks_df",
    "build_gt_table",
]
