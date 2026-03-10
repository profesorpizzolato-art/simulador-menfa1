import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# 1. Configuración de ruta para encontrar módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 2. Configuración de página (SOLO UNA VEZ al principio)
st.set_page_config(page_title="Simulador MENFA", layout="wide")

# 3. Intentar importar módulos (con manejo de errores para diagnóstico)
try:
    from modulos.panel_perforador import panel_perforador
    # Agrega aquí otros módulos si ya existen los archivos .py en la carpeta modulos
    # from modulos.torque_drag import torque_drag
except ImportError as e:
    st.error(f"Error al cargar módulos: {e}")
    st.info("Asegúrate de que la carpeta 'modulos' tenga un archivo __init__.py vacío.")

# 4. Título Principal
st.title("MENFA DRILLING & WELL CONTROL SIMULATOR")
st.subheader("Centro de Entrenamiento Técnico Petrolero")

# 5. Menú de Navegación
menu = st.sidebar.selectbox(
    "Menú del Simulador",
    [
        "Simulador Rápido",
        "Panel del Perforador Especializado",
        "Control de Pozos",
        "Evaluación"
    ]
)

# --- OPCIÓN 1: SIMULADOR RÁPIDO (El código que tenías al principio) ---
if menu == "Simulador Rápido":
    st.header("Parámetros del Pozo")
    
    col_a, col_b = st.columns(2)
    with col_a:
        profundidad = st.slider("Profundidad (ft)", 1000, 20000, 8000)
        mud_weight = st.slider("Peso de lodo (ppg)", 8.0, 18.0, 10.0)
    with col_b:
        grad_form = st.slider("Gradiente formación (psi/ft)", 0.30, 1.0, 0.65)
        grad_frac = st.slider("Gradiente fractura (psi/ft)", 0.8, 1.5, 1.1)

    # Cálculos
    ph = 0.052 * mud_weight * profundidad
    pf = grad_form * profundidad
    pfrac = grad_frac * profundidad

    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Presión Hidrostática", f"{round(ph)} psi")
    c2.metric("Presión Formación", f"{round(pf)} psi")
    c3.metric("Presión Fractura", f"{round(pfrac)} psi")

    if ph < pf:
        st.error("⚠️ RIESGO DE KICK (Brote)")
    elif ph > pfrac:
        st.warning("⚠️ RIESGO DE FRACTURA")
    else:
        st.success("✅ VENTANA OPERATIVA SEGURA")

# --- OPCIÓN 2: PANEL DEL PERFORADOR (Llama a tu módulo externo) ---
elif menu == "Panel del Perforador Especializado":
    try:
        panel_perforador()
    except NameError:
        st.warning("El módulo 'panel_perforador' no pudo ser cargado.")

# --- OPCIÓN 3: CONTROL DE POZOS ---
elif menu == "Control de Pozos":
    st.header("Cálculos de Control de Pozos")
    sidpp = st.number_input("SIDPP (psi)", 0, 5000, 300)
    prof_control = st.number_input("Profundidad Actual (ft)", 1000, 25000, 8000)
    mw_actual = st.number_input("Peso de lodo actual (ppg)", 8.0, 19.0, 10.0)
    
    kmw = mw_actual + (sidpp / (0.052 * prof_control))
    st.metric("Kill Mud Weight (KMW) requerido", f"{round(kmw, 2)} ppg")

else:
    st.write("Módulo de evaluación en desarrollo.")
