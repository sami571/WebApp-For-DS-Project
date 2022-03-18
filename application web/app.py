#app.py
import app1
import app2
import app3
import app4
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

img = Image.open("assurances.png")
if img.mode != 'RGB':
    img = img.convert('RGB')
st.image(img, width=200)
PAGES = {
    "Détection de fraude": app1,
    "Prédiction de la classe Bonus-Malus": app2,
    "Analyse Sentimentale des tweets": app3,
    "DashBoard Power BI": app4
}

st.sidebar.title('CGA')
selection = st.sidebar.radio("Selectionnez la page", list(PAGES.keys()))
page = PAGES[selection]
page.app()
