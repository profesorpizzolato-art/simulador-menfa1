import streamlit as st
from evaluacion.preguntas import preguntas
from evaluacion.certificado import generar_certificado

def modulo_examen():

    st.title("Evaluación Técnica MENFA")

    nombre = st.text_input("Nombre del participante")

    puntaje = 0

    respuestas = []

    for i,p in enumerate(preguntas):

        r = st.radio(
        p["pregunta"],
        p["opciones"],
        key=i
        )

        respuestas.append(r)

    if st.button("Finalizar evaluación"):

        for i,p in enumerate(preguntas):

            if respuestas[i] == p["correcta"]:
                puntaje +=1

        st.write("Resultado:",puntaje,"/",len(preguntas))

        if puntaje >= 42:
            st.success("Aprobado")
            generar_certificado(nombre,puntaje)
        else:
            st.error("No aprobado")
