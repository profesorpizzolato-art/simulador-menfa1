import streamlit as st

# Importación de módulos
from modulos.panel_perforador import panel_perforador
from modulos.panel_cabina import panel_cabina
from modulos.torque_drag import torque_drag
from modulos.bombas_lodo import bombas_lodo
from modulos.geonavegacion import geonavegacion

from evaluacion.examen import examen


# Configuración de página
st.set_page_config(
    page_title="Simulador MENFA",
    layout="wide",
    page_icon="assets/logo_menfa.png"
)


# Título principal
st.title("SIMULADOR OPERATIVO DE PERFORACIÓN MENFA")


# Diccionario de módulos (más limpio que muchos elif)
modulos = {
    "Panel del Perforador": panel_perforador,
    "Cabina de perforación": panel_cabina,
    "Torque y Drag": torque_drag,
    "Bombas de Lodo": bombas_lodo,
    "Geonavegación": geonavegacion,
    "Evaluación": examen
}


# Menú lateral
menu = st.sidebar.selectbox(
    "Seleccionar módulo",
    list(modulos.keys())
)


# Ejecutar módulo seleccionado
modulos[menu]()
