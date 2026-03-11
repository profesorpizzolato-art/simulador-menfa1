import streamlit as st
__init__.py
def panel_perforador():

    st.header("Panel del Perforador")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        wob = st.slider("WOB (klb)",0,80,30)

    with col2:
        rpm = st.slider("RPM",0,220,120)

    with col3:
        torque = st.slider("Torque (lb-ft)",0,40000,15000)

    with col4:
        rop = st.slider("ROP (ft/hr)",0,200,40)

    st.divider()

    col5,col6,col7 = st.columns(3)

    with col5:
        spp = st.slider("SPP psi",0,5000,3200)

    with col6:
        flow = st.slider("Flow gpm",0,1200,650)

    with col7:
        pit = st.slider("Pit Volume bbl",0,1500,900)

    st.success("Sistema de perforación operativo")
