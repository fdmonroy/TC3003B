# Actividad VLSM: Diseño de Direccionamiento de una Red Nacional

Proyecto de ingeniería de redes para el diseño, dimensionamiento, asignación y validación de direccionamiento IPv4 sin clase utilizando VLSM sobre el bloque institucional `172.16.0.0/16` del Tecnológico de Monterrey.

## Estructura del Repositorio

* [notebooks/01_vlsm_tec_nacional.ipynb](file:///home/ubuntu/workspace/TC3003B/m4-plus/act%20vlsm/notebooks/01_vlsm_tec_nacional.ipynb): Cuaderno de Jupyter interactivo con salidas y tablas de Great Tables renderizadas.
* [notebooks/01_vlsm_tec_nacional.py](file:///home/ubuntu/workspace/TC3003B/m4-plus/act%20vlsm/notebooks/01_vlsm_tec_nacional.py): Script maestro en formato percent sincronizado con Jupytext.
* [src/act_vlsm/](file:///home/ubuntu/workspace/TC3003B/m4-plus/act%20vlsm/src/act_vlsm/): Paquete modular en Python para cálculo de subredes, renderizado de tablas, configuraciones Cisco IOS y visualizaciones.
* [assets/](file:///home/ubuntu/workspace/TC3003B/m4-plus/act%20vlsm/assets/): Diagramas vectoriales de alta resolución de topología y asignación de bloques.
* [export/Actividad_VLSM_A01750536.pdf](file:///home/ubuntu/workspace/TC3003B/m4-plus/act%20vlsm/export/Actividad_VLSM_A01750536.pdf): Reporte ejecutivo final compilado en formato PDF de 14 páginas cumpliendo estándares de publicación.
* [act_vlsm_solucion.md](file:///home/ubuntu/workspace/TC3003B/m4-plus/act%20vlsm/act_vlsm_solucion.md): Documento Markdown autónomo con la solución analítica completa.

## Flujo de Ejecución y Compilación

Para sincronizar, ejecutar desatendidamente y generar el reporte final en PDF:

```bash
# 1. Sincronizar el script de Python con el cuaderno de Jupyter
./.venv/bin/jupytext --sync notebooks/01_vlsm_tec_nacional.py

# 2. Ejecutar todas las celdas y capturar salidas
./.venv/bin/jupyter nbconvert --execute --to notebook --inplace notebooks/01_vlsm_tec_nacional.ipynb

# 3. Compilar el reporte en PDF con Pandoc y Tectonic
pandoc -f ipynb+raw_attribute notebooks/01_vlsm_tec_nacional.ipynb \
  -o export/Actividad_VLSM_A01750536.pdf \
  --lua-filter=scripts/hide_code_cells.lua \
  -H scripts/preamble.tex \
  --pdf-engine=tectonic \
  -V geometry:margin=2.2cm \
  -V colorlinks=true \
  -V linkcolor=blue \
  --resource-path=.:assets:notebooks
```
