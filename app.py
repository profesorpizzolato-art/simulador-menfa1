
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador MENFA - Perforación", layout="wide")

st.title("Simulador Profesional de Perforación - MENFA")

st.sidebar.header("Parámetros del Pozo")

profundidad = st.sidebar.slider("Profundidad (ft)", 1000, 15000, 8000)
mud_weight = st.sidebar.slider("Peso de Lodo (ppg)", 8.0, 18.0, 10.0)
presion_formacion = st.sidebar.slider("Presión de Formación (psi)", 1000, 15000, 6000)

presion_hidrostatica = 0.052 * mud_weight * profundidad
diferencial = presion_hidrostatica - presion_formacion

st.subheader("Resultados")

col1, col2, col3 = st.columns(3)

col1.metric("Presión Hidrostática (psi)", f"{presion_hidrostatica:,.0f}")
col2.metric("Presión Formación (psi)", f"{presion_formacion:,.0f}")
col3.metric("Diferencial (psi)", f"{diferencial:,.0f}")

if diferencial < 0:
    st.error("Riesgo de KICK - Presión de formación mayor que hidrostática")
elif diferencial > 1000:
    st.warning("Posible fractura de formación")
else:
    st.success("Pozo en condición segura")

prof_range = np.linspace(1000, profundidad, 100)
presion_curve = 0.052 * mud_weight * prof_range

fig, ax = plt.subplots()
ax.plot(prof_range, presion_curve)
ax.axhline(presion_formacion)
ax.set_xlabel("Profundidad (ft)")
ax.set_ylabel("Presión (psi)")
ax.set_title("Perfil de Presión")
st.pyplot(fig)
