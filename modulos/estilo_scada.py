import streamlit as st

def estilo_scada():

    st.markdown("""
    <style>

    .stApp{
        background: radial-gradient(circle at center,#07121c,#02060a);
        color:white;
    }

    .panel{
        border:2px solid #ff7a18;
        border-radius:12px;
        padding:15px;
        background:rgba(0,0,0,0.45);
        box-shadow:0 0 15px rgba(255,122,24,0.6);
    }

    .titulo{
        font-size:26px;
        font-weight:bold;
        color:#ff7a18;
        text-align:center;
        margin-bottom:10px;
    }

    .indicador{
        text-align:center;
        font-size:20px;
        font-weight:bold;
        color:#00e5ff;
    }

    </style>
    """, unsafe_allow_html=True)
