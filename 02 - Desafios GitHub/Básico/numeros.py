# Desenvolva um programa que leia um número inteiro qualquer 
# e que apresete o número informado, seguido do seu antecessor e do seu sucessor.
try:
    numero = int(input("Digite um número: "))
    print(f"O número é {numero}, \nO antecessor é {numero-1}, \nO sucessor é {numero+1}.")
    # alt 92 = \
    # \n serve para quebra a linha.
except ValueError:
    print("Erro: Por favor, digite um número inteiro.")

# Aqui eu brinquei com o try, mas você pode executar somente o código das linhas 4 e 5.
# O int() é importante para transformar o input de string para inteiro.