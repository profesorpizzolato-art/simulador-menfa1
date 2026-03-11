import streamlit as st
from evaluacion.preguntas import preguntas
from evaluacion.certificado import generar_certificado


def examen():

    st.title("Evaluación MENFA")

    nombre = st.text_input("Nombre del alumno")

    respuestas = []

    for i,p in enumerate(preguntas):

        r = st.radio(
            p["pregunta"],
            p["opciones"],
            key=i
        )

        respuestas.append(r)

    if st.button("Finalizar examen"):

        puntaje = 0

        for i,p in enumerate(preguntas):

            if respuestas[i] == p["correcta"]:
                puntaje += 1

        st.write("Resultado:",puntaje,"/60")

        if puntaje >= 42:

            st.success("APROBADO")

            generar_certificado(nombre,puntaje)

        else:
            st.error("NO APROBADO")
