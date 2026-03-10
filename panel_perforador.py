import streamlit as st
from PIL import Image

def panel_perforador():

    st.subheader("Cabina del Perforador")

    imagen = Image.open("assets/rig_floor.png")
    st.image(imagen)

    col1,col2,col3 = st.columns(3)

    with col1:
        wob = st.slider("WOB klb",0,80,25)
        rpm = st.slider("RPM",0,200,120)

    with col2:
        torque = st.slider("Torque lb-ft",0,40000,15000)
        rop = st.slider("ROP ft/hr",0,200,45)
import streamlit as st
from PIL import Image

def panel_perforador():

    st.subheader("Cabina del Perforador")

    imagen = Image.open("assets/rig_floor.png")
    st.image(imagen)

    col1,col2,col3 = st.columns(3)

    with col1:
        wob = st.slider("WOB klb",0,80,25)
        rpm = st.slider("RPM",0,200,120)

    with col2:
        torque = st.slider("Torque lb-ft",0,40000,15000)
        rop = st.slider("ROP ft/hr",0,200,45)

    with col3:
        presion = st.slider("SPP psi",0,5000,3000)
        flow = st.slider("Flow gpm",0,1200,650)

    st.success("Sistema operativo activo")
    with col3:
        presion = st.slider("SPP psi",0,5000,3000)
        flow = st.slider("Flow gpm",0,1200,650)

    st.success("Sistema operativo activo")
