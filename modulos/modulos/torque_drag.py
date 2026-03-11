import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
__init__.py
def torque_drag():

    st.subheader("Torque y Drag")

    profundidad = st.slider("Profundidad ft",1000,20000,8000)

    friccion = st.slider("Coeficiente fricción",0.1,0.5,0.25)

    peso = st.slider("Peso sarta klb",10,200,90)

    torque = peso * friccion * profundidad/120

    st.metric("Torque estimado",int(torque))

    x = np.linspace(0,profundidad,100)
    y = x * friccion

    fig,ax = plt.subplots()

    ax.plot(x,y)

    ax.set_xlabel("Profundidad")
    ax.set_ylabel("Torque relativo")

    st.pyplot(fig)

    if torque > 25000:

        st.error("Riesgo de pega diferencial")
