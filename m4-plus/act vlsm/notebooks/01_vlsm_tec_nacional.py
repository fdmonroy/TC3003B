# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: Python (act-vlsm)
#     language: python
#     name: act-vlsm
# ---

# %% [markdown]
# # Actividad: VLSM
#
# **Institución:** Tecnológico de Monterrey  
# **Materia:** Implementación de redes de área amplia y servicios distribuidos (TC3003B)  
# **Profesor:** Juan Manuel Campos Sandoval  
# **Alumno:** Fernando Daniel Monroy Sánchez (A01750536)  
# **Fecha:** 15 de octubre de 2026  
#
# ---
#
# En subneteo de longitud fija (FLSM), todas las subredes adoptan el tamaño del segmento mayor, lo que ocasiona desperdicio de direcciones IP. La técnica de máscara de subred de longitud variable (VLSM) optimiza el espacio asignando bloques en potencias de 2 mediante la condición $2^h - 2 \ge N_{\text{hosts}}$, donde $h$ representa los bits de host y el prefijo CIDR resultante es $32 - h$.
#
# ## Requerimientos
#
# La red base asignada es 172.16.0.0/16.

# %%
from pathlib import Path
import re
import sys

# Agregar ruta al módulo fuente
sys.path.insert(0, str(Path("../src").resolve()))
sys.path.insert(0, str(Path("src").resolve()))

from IPython.display import display
from great_tables import GT

# Ajustar representación LaTeX de Great Tables
def _gt_to_latex(self):
    latex_str = self.as_latex()
    latex_str = re.sub(
        r"\\begin\{table\}(\[[^\]]*\])?",
        r"\\begin{table}[H]\n\\centering",
        latex_str
    )
    cols = len(self._tbl_data.columns) if hasattr(self, "_tbl_data") else 5
    if cols <= 5:
        latex_str = re.sub(
            r"\\fontsize\{[^}]+\}\{[^}]+\}\\selectfont",
            r"\\fontsize{8pt}{9.2pt}\\selectfont",
            latex_str
        )
    else:
        latex_str = re.sub(
            r"\\fontsize\{[^}]+\}\{[^}]+\}\\selectfont",
            r"\\fontsize{7.5pt}{8.8pt}\\selectfont",
            latex_str
        )
    return latex_str

GT._repr_latex_ = _gt_to_latex

from act_vlsm.network_calc import (
    get_tec_requirements,
    build_scheme_a,
    validate_no_overlap,
)
from act_vlsm.table_renderer import (
    create_requirements_df,
    create_subnets_summary_df,
    create_wan_summary_df,
)

reqs = get_tec_requirements()
df_reqs = create_requirements_df(reqs)
gt_reqs = GT(df_reqs)
display(gt_reqs)

# %% [markdown]
# ## Subredes
#
# Asignación modular de subredes para las 6 áreas académicas dentro de los bloques iniciales /19:

# %%
lan_subnets, wan_subnets = build_scheme_a()
validate_no_overlap(lan_subnets + wan_subnets)

df_lan = create_subnets_summary_df(lan_subnets)
gt_lan = GT(df_lan)
display(gt_lan)

# %% [markdown]
# ## Enlaces
#
# Asignación de 6 enlaces punto a punto en el extremo superior del bloque 172.16.224.0/19:

# %%
df_wan = create_wan_summary_df(wan_subnets)
gt_wan = GT(df_wan)
display(gt_wan)
