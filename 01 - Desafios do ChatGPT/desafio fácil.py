print("Desafio Fácil - Bônus por desempenho simples")

#Crie um programa que pergunte o nome de 3 vendedores e quanto cada um vendeu. 
# Depois, diga se cada um bateu a meta de R$4500 e calcule o bônus de 1% caso tenha batido.

#Exemplo de saída esperada:

#Digite o nome do vendedor: Ana  
#Digite o valor vendido por Ana: 4700  
#Ana bateu a meta! Bônus: R$47.0

meta = 4500
nome_vendedor = input("Digite seu nome: ")
nome_vendedor = nome_vendedor.lower().capitalize()

valor_vendido = float(input("Digite o valor que você vendeu: "))
bonus = 0.01*valor_vendido

if valor_vendido >= meta:
        print(f"{nome_vendedor}, você bateu a meta! Bônus: R${bonus:.2f}")
else:
        print(f"{nome_vendedor}, não foi dessa vez.")

print("FIM DO PROGRAMA")