import streamlit as st
from PIL import Image

def panel_cabina():

    st.subheader("Panel del Perforador")

    img = Image.open("assets/rig_panel.png")
    st.image(img)

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        wob = st.slider("WOB klb",0,80,25)
        rpm = st.slider("RPM",0,220,120)

    with col2:
        torque = st.slider("Torque lb-ft",0,40000,15000)
        rop = st.slider("ROP ft/hr",0,200,40)

    with col3:
        spp = st.slider("SPP psi",0,5000,3200)
        flow = st.slider("Flow gpm",0,1200,650)

    with col4:
        hookload = st.slider("Hookload klb",0,500,210)
        pit = st.slider("Pit volume bbl",0,1500,850)

    st.success("Sistema de perforación operativo")
