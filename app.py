import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

st.header ('PAINEL DE CONTROLE - PROJETO SPRINT 5')

histograma= st.checkbox('Criar um histograma')

if histograma: # se a caixa de seleção for selecionada
  st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

if histograma: # se o botão for clicado
  
    # criar um histograma
    fig = px.histogram(car_data, x="price")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

dispersao = st.checkbox('Criar um gráfico de dispersão')

if dispersao: # se a caixa de seleção for selecionada
  st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

if dispersao: # se o botão for clicado
  
    # criar um histograma
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)



