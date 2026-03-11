import streamlit as st
__init__.py
def bombas():

    st.subheader("Sistema de bombas")

    for i in range(1,4):

        st.write("Bomba",i)

        estado = st.selectbox(
        f"Estado bomba {i}",
        ["OFF","ON"]
        )

        if estado == "ON":

            spm = st.slider(
            f"SPM bomba {i}",
            0,200,110
            )

            presion = st.slider(
            f"Presión bomba {i}",
            0,5000,3000
            )

            st.metric("SPM",spm)
            st.metric("Presión",presion)

        else:

            st.warning("Bomba apagada")
