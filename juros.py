def juros(j, n):
    return j ** n


divida = float(input("Quanto era a sua dívida?"))
meses = int(input("Há quantos meses você está devendo?:"))
tx_juros = float(input("Qual é a taxa de juros básicas?:"))
print("A sua dívida atual é", divida * juros(1 + (tx_juros/100), meses))
