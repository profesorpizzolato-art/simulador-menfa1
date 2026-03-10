import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def geonavegacion():

    st.subheader("Geonavegación")

    md = np.linspace(0,3000,200)

    techo = 20 + np.sin(md/200)*3
    base = -20 + np.sin(md/200)*3

    trayectoria = np.sin(md/300)*10

    fig,ax = plt.subplots()

    ax.plot(md,techo,label="Techo reservorio")
    ax.plot(md,base,label="Base reservorio")
    ax.plot(md,trayectoria,label="Trayectoria pozo")

    ax.fill_between(md,base,techo,alpha=0.2)

    ax.legend()

    st.pyplot(fig)
