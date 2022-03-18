# app1.py
from re import search
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from PIL import Image
def app():
    st.title('Détection de Fraude')
    st.write('Pour savoir si votre client est potentiellement frauduleux ou non, veuillez remplir ces informations personnelles')
    st.header("**Informations personelles :**")
    
    colSinistre, colVehicule = st.beta_columns(2)
    with colSinistre:
        st.subheader("Informations relatives aux Sinistres :")
        nb_sin_total = st.number_input("Nombre de Sinistre Totals : ", min_value=0, format='%d')
        nb_sin_c = st.number_input("Nombre de Sinistre Corporels : ", min_value=0, format='%d')
        if (nb_sin_c>nb_sin_total):
            st.error("Le nombre de sinistre corporels ne peut pas dépasser le nombre de sinistres totals")
    with colVehicule:
        st.subheader("Informations relatives aux Vehicule :")
        age_vehicule = st.number_input("Age du véhicule : ", min_value=0, format='%d')

    colPolice, colAssure = st.beta_columns(2)
    with colPolice:
        st.subheader("Informations de la police :")
        
        etat_police = st.selectbox(
                        'Etat de la police',
                        ('2', '0', '1'))
        nature_police = st.selectbox(
                        'Nature de la police',
                        ('0', '1'))
        type_intermédiaire = st.selectbox(
                        'Type intermédiaire',
                        ('0', '1'))
        Classe_Bonus_Malus_CGA = st.number_input("Classe bonus malus attribué par la cga : ", min_value=0, format='%d')
        Classe_Bonus_Malus_Compagnie = st.number_input("classe bonus malus attribué par la compagnie : ", min_value=0, format='%d')
        Duree = st.number_input("Durée de souscription du contrat d'assurance: ", min_value=0, format='%d')
    Assure=[nb_sin_c,nb_sin_total,Duree,Classe_Bonus_Malus_Compagnie,Classe_Bonus_Malus_CGA,etat_police,nature_police,type_intermédiaire]
    with colAssure:
        st.subheader(" ")
        st.text(" ")
        st.text(" ")
        submit = st.button("Prédire si l'assuré est frauduleux ou non")
        if submit:
            x_under=pd.read_excel("C://Users//ASUS//Downloads//x_under.xlsx") 
            y_under=pd.read_excel("C://Users//ASUS//Downloads//y_under.xlsx") 
            x_under.drop(['Unnamed: 0'],axis=1,inplace=True)
            train_X, test_X, train_y, test_y = train_test_split(
            x_under, y_under, test_size=0.2,random_state=0)
            clf = RandomForestClassifier(n_estimators=14)
            clf.fit(train_X, train_y)
            lst=[Assure]
            probas = clf.predict(lst)
            if (probas[0][1]==1):
                img = Image.open("red_cross.png")
                st.image(img, width=200)
                st.text("L'assuré est frauduleux")
            else :
                img = Image.open("green_check.png")
                st.image(img, width=200)
                st.text("L'assuré n'est pas frauduleux")
            
        
    
    