import streamlit as st
import time
import numpy as np

st.title('Calculadora de valores')

def juros_compostos(j, n):
    return j ** n

def juros_simples(j, n):
    return j * n

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
