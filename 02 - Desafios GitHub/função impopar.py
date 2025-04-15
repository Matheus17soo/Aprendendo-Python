# Desenvolva um programa que tenha uma função 
# Que verifique se um número inteiro qualquer é par ou impar.

def impopar():
    if num == 0:
        print(f'O número {num} é Indefinido')
    elif num%2 == 1:
        print(f'O número {num} é Impar')
    else:
        print(f'O número {num} é Par')

num = int(input('digite um número: '))
impopar()