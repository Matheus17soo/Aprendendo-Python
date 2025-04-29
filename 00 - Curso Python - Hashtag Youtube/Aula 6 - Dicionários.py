# Aula de dicionários e estruturas de dados

# produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5', 'produto 6']
# preços = [1000, 500, 600, 6000, 2500, 300]

dicionario = {'produto 1': 1000, 
              'produto 2': 500, 
              'produto 3': 600, 
              'produto 4': 6000, 
              'produto 5': 2500, 
              'produto 6': 300
              }

# pega um elemento
print(dicionario['produto 1'])

# edita um elemento
dicionario['produto 1'] = dicionario['produto 1'] * 1.3
print(dicionario)

# lê a quantidade de itens
print(len(dicionario))

# deleta um item
dicionario.pop('produto 6')
print(dicionario)

# atribui ou edita o valor de um item
dicionario['produto 7'] = 9000
print(dicionario)

# dicionario.pop('produto 7')
# print(dicionario)

# verifica se o item esta no dicionário
if 'produto 7' in dicionario:
    print('Produto 7 existe no dicionário')
else:
    print('Produto 7 não existe no dicionário')

# verifica se um valor esta no dicionario
if 9000 in dicionario.values():
    print('9000 existe no dicionário')
else:
    print('9000 não existe no dicionário')

# edita ou adiciona um item
nome_produto = input("Nome do produto: ").lower()
preco_produto = float(input("Preço do produto: "))

dicionario[nome_produto] = preco_produto
print(dicionario)

for item in dicionario:
    dicionario[item] = float(dicionario[item] * 1.1).__round__(1)

print(dicionario)



