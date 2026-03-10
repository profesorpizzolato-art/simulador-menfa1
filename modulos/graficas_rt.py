import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def graficas_rt():

    st.subheader("Parámetros en tiempo real")

    tiempo = np.arange(0,50)

    rop = np.random.normal(40,5,50)
    torque = np.random.normal(15000,1500,50)

    fig,ax = plt.subplots()

    ax.plot(tiempo,rop,label="ROP")
    ax.plot(tiempo,torque,label="Torque")

    ax.legend()

    st.pyplot(fig)
