# Desenvolva um programa que armazene quatro notas de 0 a 10 em uma lista. 
# E que apresente a média final.
# Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", 
# Caso contrário, armazenar a nota da reavaliação, substituir a menor nota e recalcular a média. 
# Caso a nova média seja igual superior a 6, apresentar a mensagem "APROVADO", 
# Caso contrário, apresentar a mensagem "REPROVADO"

notas = [0,0,0,0]
notas[0] = float(input("Nota da primeira prova: "))
notas[1] = float(input("Nota da segunda prova: "))
notas[2] = float(input("Nota da terceira prova: "))
notas[3] = float(input("Nota da quarta prova: "))

prova_final = 0
soma = sum(notas)
média = soma/4
print(f'Sua média foi: {média}')

if média >= 7:
    print("APROVADO")
else:
    print("Faça a reavaliação!")
    reav = float(input("Nota da reavaliação: "))
    if reav >= min(notas):
        print("Nota válida!")
        notas.remove(min(notas)) 
        notas.append(reav)
    soma = sum(notas)
    média = soma/4
    print(f'Sua nova média foi: {média}')
    if média >= 7:
        print("APROVADO")
    else:
        print("REPROVADO")
# Fim do programa
# Autor: Matheus Martins
