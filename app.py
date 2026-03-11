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
from panel_perforador import panel_perforador.py
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
    assets/logo_menfa.png
import streamlit as st

from modulos.estilo_scada import estilo_scada
from modulos.panel_scada import panel_scada
from modulos.centro_control import centro_control

st.set_page_config(layout="wide")

estilo_scada()
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# 1. Configuración de Rutas (Evita errores de ModuleNotFoundError)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

# 2. Configuración de Página (ÚNICA VEZ al inicio)
st.set_page_config(page_title="MENFA Drilling Simulator", layout="wide")

# 3. Importación Segura de Módulos
# Nota: Si el archivo no existe en la carpeta 'modulos', el simulador no se romperá.
try:
    from modulos.panel_perforador import panel_perforador
except ImportError:
    panel_perforador = None

# --- INTERFAZ PRINCIPAL ---
st.title("MENFA DRILLING & WELL CONTROL SIMULATOR")
st.subheader("Centro de Entrenamiento Técnico Petrolero")

# Menú Lateral
menu = st.sidebar.selectbox(
    "Seleccione Módulo",
    ["Dashboard Principal", "Panel del Perforador", "Control de Pozos", "Visualización 2D"]
)

# --- MÓDULO: DASHBOARD PRINCIPAL ---
if menu == "Dashboard Principal":
    st.sidebar.header("Parámetros del Pozo")
    profundidad = st.sidebar.slider("Profundidad (ft)", 1000, 20000, 8000)
    mud_weight = st.sidebar.slider("Peso de lodo (ppg)", 8.0, 18.0, 10.0)
    grad_form = st.sidebar.slider("Gradiente formación (psi/ft)", 0.30, 1.0, 0.65)
    grad_frac = st.sidebar.slider("Gradiente fractura (psi/ft)", 0.8, 1.5, 1.1)

    # Cálculos base
    ph = 0.052 * mud_weight * profundidad
    pf = grad_form * profundidad
    pfrac = grad_frac * profundidad

    st.header("Panel de Presiones")
    c1, c2, c3 = st.columns(3)
    c1.metric("Hidrostática", f"{round(ph)} psi")
    c2.metric("Formación", f"{round(pf)} psi")
    c3.metric("Fractura", f"{round(pfrac)} psi")

    # Diagnóstico
    if ph < pf:
        st.error("🚨 RIESGO DE KICK: Presión de formación supera la hidrostática.")
    elif ph > pfrac:
        st.warning("⚠️ RIESGO DE FRACTURA: Presión excesiva para la formación.")
    else:
        st.success("✅ VENTANA OPERATIVA SEGURA")

    # Gráfica de Perfil de Presiones
    st.write("### Perfil de Presiones vs Profundidad")
    z = np.linspace(0, profundidad, 100)
    fig, ax = plt.subplots()
    ax.plot(0.052 * mud_weight * z, z, label="Hidrostática", color='blue')
    ax.plot(grad_form * z, z, '--', label="Formación", color='red')
    ax.plot(grad_frac * z, z, ':', label="Fractura", color='green')
    ax.invert_yaxis()
    ax.set_ylabel("Profundidad (ft)")
    ax.set_xlabel("Presión (psi)")
    ax.legend()
    st.pyplot(fig)

# --- MÓDULO: PANEL DEL PERFORADOR ---
elif menu == "Panel del Perforador":
    if panel_perforador:
        panel_perforador()
    else:
        st.warning("Módulo 'panel_perforador.py' no encontrado en la carpeta /modulos")
        # Backup si no encuentra el módulo
        st.info("Mostrando controles básicos:")
        rpm = st.slider("RPM", 0, 200, 100)
        wob = st.slider("WOB (klb)", 0, 60, 20)
        rop = (rpm * 0.1) + (wob * 0.4)
        st.metric("ROP Estimada", f"{round(rop, 1)} ft/hr")

# --- MÓDULO: CONTROL DE POZOS ---
elif menu == "Control de Pozos":
    st.header("Cálculos de Control (Kill Sheet)")
    sidpp = st.number_input("SIDPP (psi)", value=300)
    sicp = st.number_input("SICP (psi)", value=500)
    
    # Reutilizamos profundidad y mud_weight si es necesario, o definimos nuevos
    depth = st.number_input("Profundidad TVD (ft)", value=8000)
    mw_actual = st.number_input("Peso Lodo Actual (ppg)", value=10.0)
    
    kmw = mw_actual + (sidpp / (0.052 * depth))
    st.success(f"Kill Mud Weight (KMW) Requerido: {round(kmw, 2)} ppg")

# --- MÓDULO: VISUALIZACIÓN 2D ---
else:
    st.header("Esquema del Pozo")
    pos_bit = st.slider("Posición del Trépano (ft)", 0, 10000, 5000)
    fig2, ax2 = plt.subplots(figsize=(2, 6))
    ax2.plot([0, 0], [0, 10000], color='black', linewidth=4) # Hueco
    ax2.scatter(0, pos_bit, marker='v', color='red', s=200, label="Bit") # Trépano
    ax2.set_ylim(10000, 0)
    ax2.set_xlim(-1, 1)
    ax2.set_xticks([])
    st.pyplot(fig2)


st.title("SIMULADOR MENFA")

centro_control()

panel_scada()
