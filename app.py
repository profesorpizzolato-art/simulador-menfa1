import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="MENFA DRILLING SIMULATOR", layout="wide")

st.title("MENFA DRILLING & WELL CONTROL SIMULATOR")
st.subheader("Centro de Entrenamiento Técnico Petrolero")

# SIDEBAR
st.sidebar.header("Parámetros del Pozo")

profundidad = st.sidebar.slider("Profundidad (ft)",1000,20000,8000)
mud_weight = st.sidebar.slider("Peso de lodo (ppg)",8.0,18.0,10.0)

grad_form = st.sidebar.slider("Gradiente formación (psi/ft)",0.30,1.0,0.65)
grad_frac = st.sidebar.slider("Gradiente fractura (psi/ft)",0.8,1.5,1.1)

escenario = st.sidebar.selectbox(
"Escenario",
[
"Perforación normal",
"Kick de gas",
"Pérdida de circulación",
"Pozo bajo balance"
]
)

# CALCULOS PRINCIPALES

ph = 0.052*mud_weight*profundidad
pf = grad_form*profundidad
pfrac = grad_frac*profundidad

# DASHBOARD PRESIONES

st.header("Panel de Presiones")

c1,c2,c3 = st.columns(3)

c1.metric("Presión Hidrostática",round(ph))
c2.metric("Presión Formación",round(pf))
c3.metric("Presión Fractura",round(pfrac))

# DIAGNOSTICO

st.header("Diagnóstico del Pozo")

if ph < pf:
    st.error("RIESGO DE KICK")

elif ph > pfrac:
    st.warning("RIESGO DE FRACTURA")

else:
    st.success("VENTANA OPERATIVA SEGURA")

# CONTROL DE POZOS

st.header("Control de Pozos")

sidpp = st.slider("SIDPP (psi)",0,1500,300)
sicp = st.slider("SICP (psi)",0,2000,500)

kmw = mud_weight + sidpp/(0.052*profundidad)

st.metric("Kill Mud Weight requerido",round(kmw,2))

# PIT GAIN

st.header("Monitoreo de Volumen")

pit = st.slider("Pit Gain (bbl)",0,50,0)

if pit > 5:
    st.error("KICK DETECTADO")

elif pit > 0:
    st.warning("GANANCIA DE VOLUMEN")

else:
    st.success("Volumen estable")

# PARAMETROS DE PERFORACION

st.header("Panel del Perforador")

rpm = st.slider("RPM",0,200,120)
wob = st.slider("WOB (klb)",0,60,25)
flow = st.slider("Flow rate (gpm)",0,1000,500)

rop = (rpm*0.12)+(wob*0.35)

col1,col2,col3,col4 = st.columns(4)

col1.metric("RPM",rpm)
col2.metric("WOB",wob)
col3.metric("Flow",flow)
col4.metric("ROP (ft/hr)",round(rop,1))

# PERFIL DE PRESIONES

st.header("Perfil de Presiones")

prof = np.linspace(0,profundidad,100)

hidro = 0.052*mud_weight*prof
form = grad_form*prof
frac = grad_frac*prof

fig,ax = plt.subplots()

ax.plot(hidro,prof,label="Hidrostática")
ax.plot(form,prof,label="Formación")
ax.plot(frac,prof,label="Fractura")

ax.invert_yaxis()

ax.set_xlabel("Presión (psi)")
ax.set_ylabel("Profundidad (ft)")

ax.legend()

st.pyplot(fig)

# VISUALIZACION DEL POZO

st.header("Visualización del Pozo")

avance = st.slider("Posición del trépano",0,profundidad,int(profundidad*0.5))

fig2,ax2 = plt.subplots()

ax2.plot([0,0],[0,profundidad],linewidth=10)

ax2.scatter(0,avance,s=300)

if escenario == "Kick de gas":
    gas = profundidad*0.75
    ax2.scatter(0,gas,s=400)

ax2.set_ylim(profundidad,0)

ax2.set_xlim(-1,1)

ax2.set_xticks([])

ax2.set_title("Estado del Pozo")

st.pyplot(fig2)

# MIGRACION DE GAS

if escenario == "Kick de gas":

    st.header("Migración de Gas")

    tiempo = st.slider("Tiempo de migración (min)",0,60,10)

    posicion = profundidad - (tiempo*40)

    fig3,ax3 = plt.subplots()

    ax3.plot([0,0],[0,profundidad],linewidth=10)

    ax3.scatter(0,posicion,s=500)

    ax3.set_ylim(profundidad,0)
    ax3.set_xlim(-1,1)
    ax3.set_xticks([])

    ax3.set_title("Gas Migrando")

    st.pyplot(fig3)

# MODO ENTRENAMIENTO

st.header("Modo Entrenamiento MENFA")

if escenario == "Kick de gas":

    st.write("Objetivo del alumno:")
    st.write("1 Detectar el kick")
    st.write("2 Cerrar el pozo")
    st.write("3 Calcular Kill Mud Weight")

elif escenario == "Pérdida de circulación":

    st.write("Objetivo del alumno:")
    st.write("Reducir presión hidrostática")

elif escenario == "Pozo bajo balance":

    st.write("Objetivo del alumno:")
    st.write("Controlar entrada de formación")

else:

    st.write("Operación normal de perforación")

import streamlit as st

from modulos.panel_perforador import panel_perforador
from modulos.torque_drag import panel_torque
from modulos.bombas_lodo import panel_bombas
from modulos.geonavegacion import geonavegacion
from modulos.graficas_operativas import graficas_operativas

from evaluacion.examen import modulo_examen

st.set_page_config(page_title="Simulador MENFA", layout="wide")

st.title("Simulador Operativo de Perforación - MENFA")

menu = st.sidebar.selectbox(
"Menú",
[
"Panel del Perforador",
"Torque y Drag",
"Bombas de Lodo",
"Geonavegación",
"Gráficas Operativas",
"Evaluación y Certificación"
]
)

if menu == "Panel del Perforador":
    panel_perforador()

if menu == "Torque y Drag":
    panel_torque()

if menu == "Bombas de Lodo":
    panel_bombas()

if menu == "Geonavegación":
    geonavegacion()

if menu == "Gráficas Operativas":
    graficas_operativas()

if menu == "Evaluación y Certificación":
    modulo_examen()
    "simulador_menfa/"

import streamlit as st

from modulos.panel_cabina import panel_cabina
from modulos.torque_drag_avanzado import torque_drag
from modulos.sistema_circulacion import sistema_circulacion
from modulos.geonavegacion import geonavegacion
from modulos.control_pozos import control_pozos
from modulos.deteccion_kick import deteccion_kick
from modulos.graficas_tiempo_real import graficas_rt

from evaluacion.examen import modulo_examen

st.set_page_config(page_title="Simulador MENFA",layout="wide")

st.title("Centro de Entrenamiento MENFA - Simulador de Perforación")

menu = st.sidebar.selectbox(
"Menú del simulador",
[
"Cabina del Perforador",
"Torque y Drag",
"Sistema de Circulación",
"Geonavegación",
"Control de Pozos",
"Detección de Kick",
"Gráficas en Tiempo Real",
"Evaluación MENFA"
]
)

if menu == "Cabina del Perforador":
    panel_cabina()

if menu == "Torque y Drag":
    torque_drag()

if menu == "Sistema de Circulación":
    sistema_circulacion()

if menu == "Geonavegación":
    geonavegacion()

if menu == "Control de Pozos":
    control_pozos()

if menu == "Detección de Kick":
    deteccion_kick()

if menu == "Gráficas en Tiempo Real":
    graficas_rt()

if menu == "Evaluación MENFA":
    modulo_examen()
import streamlit as st

from modulos.panel_cabina import panel_cabina
from modulos.torque_drag import torque_drag
from modulos.bombas import bombas
from modulos.geonavegacion import geonavegacion
from modulos.control_pozos import control_pozos
from modulos.deteccion_kick import deteccion_kick
from modulos.graficas_rt import graficas_rt

from evaluacion.examen import examen

st.set_page_config(page_title="Simulador MENFA",layout="wide")

st.title("SIMULADOR DE PERFORACIÓN MENFA")

menu = st.sidebar.selectbox(

"Menú del simulador",

[
"Cabina del perforador",
"Torque y Drag",
"Bombas",
"Geonavegación",
"Control de pozos",
"Detección de Kick",
"Gráficas",
"Evaluación"
]

)

if menu == "Cabina del perforador":
    panel_cabina()

if menu == "Torque y Drag":
    torque_drag()

if menu == "Bombas":
    bombas()

if menu == "Geonavegación":
    geonavegacion()

if menu == "Control de pozos":
    control_pozos()

if menu == "Detección de Kick":
    deteccion_kick()

if menu == "Gráficas":
    graficas_rt()

if menu == "Evaluación":
    examen()
