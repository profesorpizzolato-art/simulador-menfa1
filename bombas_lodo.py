import streamlit as st

def bombas_lodo():

    st.header("Sistema de Bombas de Lodo")

    for i in range(1,4):

        st.subheader(f"Bomba {i}")

        estado = st.selectbox(
            "Estado",
            ["OFF","ON"],
            key=f"estado{i}"
        )

        if estado == "ON":

            spm = st.slider(
                "SPM",
                0,200,110,
                key=f"spm{i}"
            )

            presion = st.slider(
                "Presión psi",
                0,5000,3000,
                key=f"pres{i}"
            )

            st.metric("SPM",spm)
            st.metric("Presión",presion)

        else:
            st.warning("Bomba apagada")
