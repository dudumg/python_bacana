segundos = int(input("Por favor digite o número de segundos que deseja converter"))

dias = segundos // 86400
segundos_sobrados = segundos % 86400
horas = segundos_sobrados // 3600
segundos_sobra = segundos_sobrados % 3600
minutos = segundos_sobra // 60
segundo_restantes = segundos_sobra % 60

print(dias," dias", horas," horas", minutos, " minutos e", segundo_restantes, " segundos.")
