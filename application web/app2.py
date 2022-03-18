# app2.py
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
def app():
    st.title('Prediction Classe Bonus Malus')
    st.write(' à partir des informations que vous fournissez , on peut prédire la classe bonus malus de l\'assuré ')
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
        st.subheader("Informations de la police d'assurance :")

        etat_police = st.selectbox(
                        'Etat de la police',
                        ('2', '0', '1'))
        nature_police = st.selectbox(
                        'Nature de la police',
                        ('0', '1'))
        type_intermédiaire = st.selectbox(
                        'Type intermédiaire',
                        ('0', '1'))
        Classe_Bonus_Malus_Compagnie = st.number_input("classe bonus malus attribué par la compagnie : ", min_value=0, format='%d')
        Duree = st.number_input("Durée de souscription du contrat d'assurance: ", min_value=0, format='%d')
   
    Assure=[nb_sin_c,nb_sin_total,Duree,Classe_Bonus_Malus_Compagnie,etat_police,nature_police,type_intermédiaire]
    submit = st.button("Prédire la classe Bonus Malus de l'assuré")
    if submit:
        x_under=pd.read_excel("C://Users//ASUS//Downloads//x_under.xlsx") 
        x_under.drop(['Unnamed: 0'],axis=1,inplace=True)
        X=x_under.drop(['ClasseBonusMalusCGA'],axis=1)
        Y=x_under['ClasseBonusMalusCGA']
        X=X.values
        Y=Y.values
        X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2,random_state=0)
        regressor = DecisionTreeRegressor()
        regressor.fit(X_train, y_train)
        lst=[Assure]
        classe= regressor.predict(lst)
        st.text("Classe Bonus malus : {} ".format(round(classe[0])))
