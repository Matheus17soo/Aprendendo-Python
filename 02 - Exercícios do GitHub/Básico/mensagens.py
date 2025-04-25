# Desenvolva um programa que apresente na tela a seguinte mensagem: Hello World
# Em seguida que pergunte o seu nome e, ao teclar Enter, 
# apresente uma saudação personalizada.
# Como a esta altura do campeonato 
# você provavelmente já sabe usar print e input pode pular.
# Farei somente como referência.

print("Hello World")
nome = input("Me diga seu nome: ")
nome = nome.lower() # as letras ficam todas minusculas.
nome = nome.title() # retorna os nomes com as inicias maiusculas.

# print("Olá", nome)
print(f"Olá {nome}!")

# Autor: Matheus Martins
# Data: 17 de Abril de 2025