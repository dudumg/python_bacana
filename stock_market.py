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

stocks = st.sidebar.multiselect('Escolha a/as ações que você deseja:',('PBR','NU','UBER','MSFT','AAPL','ERJ'))
for simbolo in stocks:
    data = yf.download(tickers=simbolo, period='5d', interval='5m')
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
    title=simbolo + ' live share price evolution',
    yaxis_title='Stock Price (USD per Shares)')

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


tipo_juros = st.sidebar.radio('Tipo de juros:',('Simples','Compostos'))

#divida = float(input("Quanto era a sua dívida?"))
divida = st.number_input('Quanto era a sua dívida')
#meses = int(input("Há quantos meses você está devendo?:"))
meses = st.number_input('Há quantos meses você está devendo?')
#tx_juros = float(input("Qual é a taxa de juros básicas?:"))
tx_juros = st.number_input('Qual é a taxa de juros básica?')
#print("A sua dívida atual é", divida * juros(1 + (tx_juros/100), meses))
if tipo_juros == 'Simples':
    st.write("A sua dívida atual é", divida * juros_simples(1 + (tx_juros/100), meses))
else:
    st.write("A sua dívida atual é", divida * juros_compostos(1 + (tx_juros/100), meses))
