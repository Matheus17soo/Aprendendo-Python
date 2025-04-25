# Como no desafio que encotrei no github, a solução usa algumas funções 
# e maneiras diferentes para o mesmo resultado.
# Vou refazer o segundo desafio da lista de notas, aplicando as seguintes funções.
# While, len()

print("Desafio 2 - Lista de Notas Versão 2") 
notas = [] 
count = 1 
nprovas = input("Quantas provas você quer inserir? (4) ")
if nprovas == "":
    nprovas = 4
else:
    nprovas = int(nprovas)
print("Digite -1 para parar de inserir notas.") 

while count <= nprovas: 
    nota = float(input("Digite a nota: ")) # Solicita a nota ao usuário
    if nota == -1: # Condição de parada
        print("Encerrando o programa.")
        exit() # Encerra o programa completamente.
    elif 0 <= nota <= 10: # Verifica se a nota está dentro do intervalo válido
        notas.append(nota) # Adiciona a nota à lista
        count += 1 # Incrementa o contador
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.") # Mensagem de erro

# Calcula a média das notas

if len(notas) <= 0:
    print("Nenhuma nota inserida!")
else:
    media = sum(notas) / len(notas)
    if media >= 7:
        print("APROVADO+")
        print(f"Média: {media:.2f}")
    else:
        # Reavaliação
        print(f"Média: {media:.2f}")
        print("Fazer a Reavaliação")
        while True:
            reav = float(input("Nota da Reavaliação: "))
            if 0 <= reav <= 10:
                notas.remove(min(notas))
                notas.append(reav)
                break
            elif reav == -1:
                print("Encerrando o programa.")
                exit()
            else:
                print("Nota inválida. Digite uma nota entre 0 e 10.")

        media = sum(notas) / len(notas)
        if media < 7:
            print("REPROVADO")
            print(f"Média: {media:.2f}")
        else:
            print("APROVADO")
            print(f"Média: {media:.2f}")
        

# Autor: Matheus Martins
# 17 de Abril de 2025