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

st.pyplot(fig)
