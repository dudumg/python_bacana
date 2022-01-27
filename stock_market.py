from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import streamlit as st
import time
import numpy as np

import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go

st.title('Calculadora de valores')

def juros_compostos(j, n):
    return j ** n

def juros_simples(j, n):
    return j * n
#def IPCA(

#opcoes = st.sidebar.selectbox('Escolha a sua opção de módulo:', ('Calculadora de Juros','Bolsa de Valores(NYSE)','IPCA mensal'))
opcoes = st.sidebar.selectbox('Escolha a sua opção de módulo:', ('Calculadora de Juros','Bolsa de Valores(NYSE)'))

if opcoes == 'Bolsa de Valores(NYSE)':
    st.write ('A bolsa que estamos utilizando é a NYSE')
    stocks = st.sidebar.multiselect('Escolha a/as ações que você deseja:',('PBR','NU','UBER','MSFT','AAPL','ERJ'))
    for simbolo in stocks:
        data = yf.download(tickers=simbolo, period='1d', interval='1m')
        #declare figure
        fig = go.Figure()

        #Candlestick
        fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))

        # Add titles
        fig.update_layout(
            title=simbolo + ' (evolução do preço ao vivo)',
            yaxis_title='Preço da Ação (USD por Ação)')

        # X-Axes
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
                ])
            )
        )
        st.plotly_chart(fig, use_container_width=True)

if opcoes == 'Calculadora de Juros':
    
    tipo_juros = st.sidebar.radio('Tipo de juros:',('Simples','Compostos'))

    #divida = float(input("Quanto era a sua dívida?"))
    divida = st.number_input('Quanto era a sua dívida')
    #meses = int(input("Há quantos meses você está devendo?:"))
    meses = st.number_input('Há quantos meses você está devendo?', format='%d', step=1)
    #tx_juros = float(input("Qual é a taxa de juros básica mensal?:"))
    tx_juros = st.number_input('Qual é a taxa de juros básica mensal?')
    #print("A sua dívida atual é", divida * juros(1 + (tx_juros/100), meses))
    if tipo_juros == 'Simples':
        st.write("A sua dívida atual é", "{:,.2f}".format(divida * (1 + juros_simples(tx_juros/100, meses))))
    else:
        st.write("A sua dívida atual é", "{:,.2f}".format(divida * juros_compostos(1 + (tx_juros/100), meses)))

#if opcoes == 'IPCA mensal':
#    mes = st.number_input('Digite o mês que você deseja (01 - 12):')
#    ano = st.number_input('Digite o ano que você deseja (2000 - 2021):')
 

    
        
 
    




