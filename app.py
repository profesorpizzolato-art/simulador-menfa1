import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Simulador MENFA", layout="wide")

st.title("SIMULADOR DE PERFORACIÓN Y CONTROL DE POZOS")
st.subheader("MENFA - Instituto Privado de Capacitación Laboral")

st.sidebar.header("Parámetros del Pozo")

profundidad = st.sidebar.slider("Profundidad del pozo (ft)", 1000, 20000, 8000)

densidad_lodo = st.sidebar.slider("Peso del lodo (ppg)", 8.0, 18.0, 10.0)

presion_formacion = st.sidebar.slider("Gradiente presión formación (psi/ft)", 0.3, 1.0, 0.6)

gradiente_fractura = st.sidebar.slider("Gradiente fractura (psi/ft)", 0.6, 1.4, 0.9)

st.sidebar.subheader("Escenario")

escenario = st.sidebar.selectbox(
    "Seleccionar escenario",
    ["Normal", "Kick (entrada de gas)", "Pérdida de circulación"]
)

# Cálculos

presion_hidrostatica = 0.052 * densidad_lodo * profundidad
presion_formacion_total = presion_formacion * profundidad
presion_fractura_total = gradiente_fractura * profundidad

st.subheader("Presiones calculadas")

col1, col2, col3 = st.columns(3)

col1.metric("Presión Hidrostática", f"{round(presion_hidrostatica,0)} psi")
col2.metric("Presión Formación", f"{round(presion_formacion_total,0)} psi")
col3.metric("Presión Fractura", f"{round(presion_fractura_total,0)} psi")

# Diagnóstico

if presion_hidrostatica < presion_formacion_total:
    st.error("RIESGO DE KICK — presión insuficiente")

elif presion_hidrostatica > presion_fractura_total:
    st.warning("RIESGO DE FRACTURA — presión excesiva")

else:
    st.success("Pozo en condición estable")

# Gráfico

prof = np.linspace(0, profundidad, 50)

hidro = 0.052 * densidad_lodo * prof
form = presion_formacion * prof
frac = gradiente_fractura * prof

fig, ax = plt.subplots()

ax.plot(hidro, prof, label="Presión Hidrostática")
ax.plot(form, prof, label="Presión Formación")
ax.plot(frac, prof, label="Presión Fractura")

ax.invert_yaxis()

ax.set_xlabel("Presión (psi)")
ax.set_ylabel("Profundidad (ft)")
ax.legend()

st.pyplot(fig)
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Simulador MENFA", layout="wide")

st.title("SIMULADOR DE PERFORACIÓN Y CONTROL DE POZOS")
st.subheader("MENFA - Instituto Privado de Capacitación Laboral")

st.sidebar.header("Parámetros del Pozo")

profundidad = st.sidebar.slider("Profundidad del pozo (ft)", 1000, 20000, 8000)

densidad_lodo = st.sidebar.slider("Peso del lodo (ppg)", 8.0, 18.0, 10.0)

presion_formacion = st.sidebar.slider("Gradiente presión formación (psi/ft)", 0.3, 1.0, 0.6)

gradiente_fractura = st.sidebar.slider("Gradiente fractura (psi/ft)", 0.6, 1.4, 0.9)

st.sidebar.subheader("Escenario")

escenario = st.sidebar.selectbox(
    "Seleccionar escenario",
    ["Normal", "Kick (entrada de gas)", "Pérdida de circulación"]
)
rpm = st.sidebar.slider("RPM", 0, 200, 120)
wob = st.sidebar.slider("Weight on Bit (klb)", 0, 60, 25)
flow = st.sidebar.slider("Caudal de bombeo (gpm)", 0, 1000, 500)
st.subheader("Parámetros de perforación")

c1, c2, c3 = st.columns(3)

c1.metric("RPM", rpm)
c2.metric("WOB", wob)
c3.metric("Flow rate", flow)
# Cálculos

presion_hidrostatica = 0.052 * densidad_lodo * profundidad
presion_formacion_total = presion_formacion * profundidad
presion_fractura_total = gradiente_fractura * profundidad

st.subheader("Presiones calculadas")

col1, col2, col3 = st.columns(3)

col1.metric("Presión Hidrostática", f"{round(presion_hidrostatica,0)} psi")
col2.metric("Presión Formación", f"{round(presion_formacion_total,0)} psi")
col3.metric("Presión Fractura", f"{round(presion_fractura_total,0)} psi")

# Diagnóstico

if presion_hidrostatica < presion_formacion_total:
    st.error("RIESGO DE KICK — presión insuficiente")

elif presion_hidrostatica > presion_fractura_total:
    st.warning("RIESGO DE FRACTURA — presión excesiva")

else:
    st.success("Pozo en condición estable")

# Gráfico

prof = np.linspace(0, profundidad, 50)

hidro = 0.052 * densidad_lodo * prof
form = presion_formacion * prof
frac = gradiente_fractura * prof

fig, ax = plt.subplots()

ax.plot(hidro, prof, label="Presión Hidrostática")
ax.plot(form, prof, label="Presión Formación")
ax.plot(frac, prof, label="Presión Fractura")

ax.invert_yaxis()

ax.set_xlabel("Presión (psi)")
ax.set_ylabel("Profundidad (ft)")
ax.legend()

st.pyplot(fig)

st.subheader("Interpretación")

if escenario == "Kick (entrada de gas)":
    st.write("El gas reduce la presión hidrostática y provoca una entrada de formación.")

elif escenario == "Pérdida de circulación":
    st.write("La presión supera el gradiente de fractura y el lodo se pierde hacia la formación.")

else:
    st.write("La perforación se mantiene dentro de la ventana operativa.")
st.subheader("Interpretación")

if escenario == "Kick (entrada de gas)":
    st.write("El gas reduce la presión hidrostática y provoca una entrada de formación.")

elif escenario == "Pérdida de circulación":
    st.write("La presión supera el gradiente de fractura y el lodo se pierde hacia la formación.")

else:
    st.write("La perforación se mantiene dentro de la ventana operativa.")
    if escenario == "Kick (entrada de gas)":

    st.subheader("Simulación de migración de gas")

    tiempo = st.slider("Tiempo de migración (min)",0,60,10)

    posicion_gas = profundidad - (tiempo * 50)

    fig3, ax3 = plt.subplots()

    ax3.plot([0,0],[0,profundidad], linewidth=10)
    ax3.scatter(0,posicion_gas,s=400)

    ax3.set_ylim(profundidad,0)
    ax3.set_xlim(-1,1)
    ax3.set_title("Migración del gas")

    ax3.set_xticks([])

    st.pyplot(fig3)
    st.subheader("Control de Pozos")

sidpp = st.slider("SIDPP (psi)",0,1500,300)

kmw = densidad_lodo + sidpp/(0.052*profundidad)

st.metric("Kill Mud Weight requerido", round(kmw,2))
sicp = st.slider("SICP (psi)",0,2000,500)

st.metric("Presión casing (SICP)", sicp)
st.subheader("Monitoreo de Volumen")

pit_gain = st.slider("Pit Gain (bbl)",0,50,0)

if pit_gain > 5:
    st.error("Posible Kick detectado")
elif pit_gain > 0:
    st.warning("Ganancia de volumen detectada")
else:
    st.success("Volumen estable")
    st.subheader("Panel del Perforador")

col1,col2,col3,col4 = st.columns(4)

col1.metric("RPM", rpm)
col2.metric("WOB", wob)
col3.metric("Flow rate", flow)
col4.metric("Pit Gain", pit_gain)
rop = (rpm*0.1)+(wob*0.3)

st.metric("ROP estimado (ft/hr)", round(rop,1))
avance = st.slider("Avance de perforación",0,profundidad,int(profundidad*0.5))

fig4, ax4 = plt.subplots()

ax4.plot([0,0],[0,profundidad],linewidth=10)
ax4.scatter(0,avance,s=300)

ax4.set_ylim(profundidad,0)
ax4.set_xlim(-1,1)

ax4.set_title("Posición del trépano")

ax4.set_xticks([])

st.pyplot(fig4)
st.subheader("Escenario de entrenamiento")

if escenario == "Kick (entrada de gas)":
    st.write("Objetivo del alumno: detectar el kick y cerrar el pozo.")

elif escenario == "Pérdida de circulación":
    st.write("Objetivo del alumno: reducir presión de lodo.")

else:
    st.write("Operación de perforación normal.")
    
