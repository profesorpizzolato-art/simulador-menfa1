from PIL import Image, ImageDraw, ImageFont
import streamlit as st

def generar_certificado(nombre,puntaje):

    img = Image.new("RGB",(1200,800),"white")

    draw = ImageDraw.Draw(img)

    texto = f"""
CERTIFICADO MENFA

Se certifica que

{nombre}

Aprobó el simulador operativo
de perforación petrolera

Puntaje: {puntaje}/60
"""

    draw.text((200,300),texto,fill="black")

    img.save("certificado.png")

    st.image("certificado.png")
