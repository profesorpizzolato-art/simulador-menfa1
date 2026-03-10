import streamlit as st
from PIL import Image

def panel_bombas():

    st.subheader("Bombas de Lodo")

    imagen = Image.open("assets/bomba_lodo.png")
    st.image(imagen,width=400)

    for i in range(1,4):

        st.write("Bomba",i)

        estado = st.selectbox(
        "Estado",
        ["OFF","ON"],
        key=i
        )

        if estado == "ON":

            spm = st.slider("SPM",0,200,120,key=f"spm{i}")
            presion = st.slider("Presión psi",0,5000,3000,key=f"pres{i}")

            st.metric("SPM",spm)
            st.metric("Presión",presion)

        else:
            st.warning("Bomba apagada")
