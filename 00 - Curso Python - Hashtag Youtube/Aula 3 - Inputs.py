# INPUTS
#email = input("escreva seu email: ")
#nome = input("escreva seu nome: ")

#print(nome, email)

#faturamento = float(input("qual foi o faturamento? "))
#print(f"faturamento: {faturamento:.2f}")
#imposto = faturamento*0.1
#print(imposto)

#LISTAS
vendas = [100, 50, 14, 20, 30, 700]
#total = sum(vendas)
#print(total)

#TAMANHO DE LISTA
#quantidade_vendas = len(vendas)
#print(quantidade_vendas)

#MAX E MIN
#print(max(vendas))
#print(min(vendas))

#PEGAR A POSIÇÃO
#print(vendas[0])

lista_produtos = [ "camisa", "calça", "cueca", "meia", "tênis"]
#print(lista_produtos[0])

#produto_procurado = input("pesquise aqui: ")
#produto_procurado = produto_procurado.lower()
#print(produto_procurado in lista_produtos)

#ADICIONAR UM ITEM
lista_produtos.append("blusa")
print(lista_produtos)

#REMOVER UM ITEM
#lista_produtos.remove("meia")
print(lista_produtos)

lista_produtos.pop(0)
print(lista_produtos)

#EDITAR UM ITEM
precos = [1000, 1500, 3500]
precos[0] = precos[0]*2
precos[1] = 1450
print(precos)

#CONTAR QUANTAS VEZES UM ITEM APARECE
print(lista_produtos.count("meia"))

#ORDENAR
lista_produtos.sort(reverse=False)
vendas.sort(reverse=True)
print(lista_produtos,vendas)

