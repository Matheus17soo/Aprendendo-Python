# Desenvolva um programa que armazene quatro notas em uma lista e que apresente: 
# A média final, 
# A maior nota 
# E a menor nota

notas = [0,0,0,0]

notas[0] = float(input("nota do primeiro bimestre: "))
notas[1] = float(input("nota do segundo bimestre: "))
notas[2] = float(input("nota do terceiro bimestre: "))
notas[3] = float(input("nota do quarto bimestre: "))

soma = sum(notas)
média = soma/4

print(f'Sua nota total foi: {soma}, e sua média foi: {média}')

