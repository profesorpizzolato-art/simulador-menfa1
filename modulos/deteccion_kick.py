import streamlit as st
__init__.py
def deteccion_kick():

    st.subheader("Detección de Kick")

    flujo = st.slider("Flow out",0,150,100)

    pit = st.slider("Pit volume",0,1500,900)

    spp = st.slider("SPP",0,5000,3200)

    if flujo > 115 and pit > 920:

        st.error("KICK DETECTADO")

    else:

        st.success("Sistema estable")
