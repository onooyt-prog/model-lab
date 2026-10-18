import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .stApp{
            background: #000;
            color: #eee;
        }


        h1, h2, h3,
        [data-testid='stMetricValue']{
            color:#39ff14
        }

        .stButton > button{
            background: #39ff14;
            color:#000;
        }

        .stButton > button:hover{
            background:#80ff65
        }
        </style>
    """, unsafe_allow_html=True)