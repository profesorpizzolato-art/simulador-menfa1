import streamlit as st

from modulos.panel_perforador import panel_perforador
from modulos.panel_cabina import panel_cabina
from modulos.torque_drag import torque_drag
from modulos.bombas_lodo import bombas_lodo
from modulos.geonavegacion import geonavegacion

from evaluacion.examen import examen


st.set_page_config(
    page_title="Simulador MENFA",
    layout="wide",
    page_icon="assets/logo_menfa.png"
)


st.title("SIMULADOR OPERATIVO DE PERFORACIÓN MENFA")

menu = st.sidebar.selectbox(

    "Seleccionar módulo",

    [
        "Panel del Perforador",
        "Cabina de perforación",
        "Torque y Drag",
        "Bombas de Lodo",
        "Geonavegación",
        "Evaluación"
    ]

)


if menu == "Panel del Perforador":
    panel_perforador()

elif menu == "Cabina de perforación":
    panel_cabina()

elif menu == "Torque y Drag":
    torque_drag()

elif menu == "Bombas de Lodo":
    bombas_lodo()

elif menu == "Geonavegación":
    geonavegacion()

elif menu == "Evaluación":
    examen()
