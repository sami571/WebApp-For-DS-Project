# app4.py
import streamlit as st
def app():
    st.title('Dashboard PowerBI')
    st.write('Bienvenu dans la partie Dashboard PowerBI')
    st.markdown("""
    <iframe width="1100" height="600" src="https://app.powerbi.com/reportEmbed?reportId=061d6129-fe72-4456-b298-706284d7f519&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLW5vcnRoLWV1cm9wZS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldC8ifQ%3D%3D" frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)