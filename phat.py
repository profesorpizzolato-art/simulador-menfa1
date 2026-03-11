tu-repositorio/
├── app.py
├── requirements.txt
└── modulos/
    ├── __init__.py  <-- Asegúrate de que este archivo exista (aunque esté vacío)
    └── panel_perforador.py
import sys
import os

# Añade la raíz del proyecto al path de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ahora intenta la importación
from modulos.panel_perforador import panel_perforador
