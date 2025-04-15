# CONDIÇÕES
vendas = 5000
meta1 = 4500 #bônus 1%
meta2 = 5500 #bônus 2% 

# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente

if vendas >= meta2:
    print("Vendedor ganha bônus")
    print(f"Bateu a meta de R${meta2} de vendas")
    print(f"Vendeu um total de R${vendas}")
    bonus = 0.02*vendas
    print("Bonus do vendedor: R$", bonus)
elif vendas >= meta1:
    print("Vendedor ganha bônus")
    print(f"Bateu a meta de R${meta1} de vendas")
    print(f"Vendeu um total de R${vendas}")
    bonus = 0.01*vendas
    print("Bonus do vendedor: R$", bonus)
else:
    print("Vendedor não ganha bônus")
    print("Não bateu a meta de vendas")

print("Acabou o programa")

#if aplicado a listas
produtos = [ "camisa", "calça", "cueca", "meia", "tênis"]
procurado = input("Procure um produto: ")
procurado = procurado.lower()

if procurado in produtos:
    print("Produto no estoque!")
else:
    print("Não temos este produto!")
    