# Carregue a data atual do computador. 
# E, com base na data atual, apresente a data de dois dias no futuro.

from datetime import datetime, timedelta

data_atual = datetime.now()
dias_inteiros = float(input("Quantos dias você quer avançar? "))
horas = float(input("E quantas horas você quer avançar? "))

dias = dias_inteiros + horas/24

data_futura = data_atual + timedelta(dias)
print(data_atual)
print(data_futura)