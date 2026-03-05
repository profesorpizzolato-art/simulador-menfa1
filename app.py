import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador MENFA", layout="wide")

st.title("Simulador de Perforación y Control de Pozos")
st.subheader("Centro de Entrenamiento MENFA IPCL")

st.markdown("Simulador educativo para análisis de presión en perforación")

st.sidebar.header("Parámetros del Pozo")

profundidad = st.sidebar.slider("Profundidad (ft)", 1000, 20000, 8000)

mud_weight = st.sidebar.slider("Peso de Lodo (ppg)", 8.0, 18.0, 10.0)

grad_formacion = st.sidebar.slider(
    "Gradiente de Formación (psi/ft)", 0.30, 1.00, 0.60
)

grad_fractura = st.sidebar.slider(
    "Gradiente de Fractura (psi/ft)", 0.70, 1.50, 1.00
)

# CALCULOS

presion_hidrostatica = 0.052 * mud_weight * profundidad

presion_formacion = grad_formacion * profundidad

presion_fractura = grad_fractura * profundidad

# RESULTADOS

st.subheader("Resultados de Presión")

col1, col2, col3 = st.columns(3)

col1.metric("Presión Hidrostática (psi)", f"{presion_hidrostatica:,.0f}")

col2.metric("Presión Formación (psi)", f"{presion_formacion:,.0f}")

col3.metric("Presión Fractura (psi)", f"{presion_fractura:,.0f}")

# ANALISIS OPERATIVO

st.subheader("Estado del Pozo")

if presion_hidrostatica < presion_formacion:

    st.error("ALERTA: POSIBLE KICK")

elif presion_hidrostatica > presion_fractura:

    st.warning("RIESGO DE FRACTURA DE FORMACIÓN")

else:

    st.success("VENTANA OPERATIVA SEGURA")

# PERFIL DE PRESIONES

st.subheader("Perfil de Presiones vs Profundidad")

prof_range = np.linspace(1000, profundidad, 100)

hidro_curve = 0.052 * mud_weight * prof_range

form_curve = grad_formacion * prof_range

frac_curve = grad_fractura * prof_range

fig, ax = plt.subplots()

ax.plot(prof_range, hidro_curve, label="Presión Hidrostática")

ax.plot(prof_range, form_curve, label="Presión Formación")

ax.plot(prof_range, frac_curve, label="Presión Fractura")

ax.set_xlabel("Profundidad (ft)")

ax.set_ylabel("Presión (psi)")

ax.set_title("Ventana Operativa de Perforación")

ax.legend()
avance = st.sidebar.slider("Avance de perforación (ft)", 0, profundidad, int(profundidad*0.6))
st.pyplot(fig)
st.header("Visualización del Pozo")

fig2, ax2 = plt.subplots()

# Dibujar pozo
ax2.plot([0,0],[0,profundidad], linewidth=6)

# Posición del trépano
ax2.scatter(0, avance, s=200)

ax2.set_ylim(profundidad,0)
ax2.set_xlim(-1,1)

ax2.set_title("Posición del Trépano")
ax2.set_ylabel("Profundidad (ft)")

st.pyplot(fig2)
st.header("Columna de Lodo")

fig3, ax3 = plt.subplots()

ax3.fill_between([0,1],0,avance)

ax3.set_ylim(profundidad,0)

ax3.set_title("Columna Hidrostática")

st.pyplot(fig3)
kick_altura = st.sidebar.slider("Altura del Gas Kick (ft)",0,profundidad,0)

if kick_altura > 0:

    st.header("Migración de Gas")

    fig4, ax4 = plt.subplots()

    ax4.plot([0,0],[0,profundidad],linewidth=5)

    ax4.scatter(0,kick_altura,s=200)

    ax4.set_ylim(profundidad,0)

    ax4.set_title("Burbuja de Gas Migrando")

    st.pyplot(fig4)
    st.header("Modo Entrenamiento")

st.write("Escenario de entrenamiento:")

if presion_hidrostatica < presion_formacion:
    st.write("El alumno debe detectar un Kick")

elif presion_hidrostatica > presion_fractura:
    st.write("El alumno debe reducir peso de lodo")

else:
    st.write("Condición de perforación normal")
    
