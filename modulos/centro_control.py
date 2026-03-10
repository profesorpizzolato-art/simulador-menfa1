import streamlit as st
from PIL import Image

def centro_control():

    col1,col2,col3 = st.columns([1,2,1])

    with col2:

        logo = Image.open("assets/logo_menfa.png")

        st.image(logo,width=300)

        st.markdown(
        "<div class='indicador'>SIMULADOR OPERATIVO DE PERFORACIÓN</div>",
        unsafe_allow_html=True
        )
