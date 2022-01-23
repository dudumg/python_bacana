peso = int(input("Por favor digite o seu peso:"))
altura = float(input("Por favor digite a sua altura:"))

IMC = peso/(altura**2)

print("O seu IMC é,", IMC)

print("Caregando próxima calculadora...")

metros_flt = float(input("Por favor, digite a quantidade de metros:"))

kilometros = metros_flt//1000
centimetros = metros_flt * 100

print(kilometros,"kilometros,",metros_flt,"metros, e", centimetros,"centimetros")

print("Caregando próxima calculadora...")

segundos = int(input("Digite a quantidade de segundos:"))

hora = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_rest_totais = segundos_restantes % 60

print(hora,"horas", minutos,"minutos e", segundos_rest_totais," segundos")
