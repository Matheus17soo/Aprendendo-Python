print("Desafio Médio - Estoque com preços")

# Você tem um lista de produtos com seus preços (use um dicionário). 
# O usuário digita o nome de um produto e o programa deve:
# Dizer se o produto existe no estoque.
# Se existir, mostrar o preço.
# Se não existir, mostrar "Produto indisponível"

produtos = {
    "calça":{"preco":59,"estoque":0},
    "camisa":{"preco":29,"estoque":3},
    "cueca":{"preco":19,"estoque":3},
    "meia":{"preco":9,"estoque":3},
    "blusa":{"preco":99,"estoque":3}
}

while True:
    print("\nMenu:")
    print("1 - Consultar produto")
    print("2 - Alterar produto")
    print("3 - Novo produto")
    print("4 - Sair")
    opt = str(input("\nEscolha uma opção: ")).strip()

    print(opt)
    if opt == "1": #consultar produto
        procurado = input("Qual produto você procura? ")
        procurado = procurado.lower()

        if procurado in produtos:
            item = produtos[procurado] # retorna o dicionário do item porcurado
            if item["estoque"] > 0:
                print("\nVocê procurou:",procurado.capitalize())
                preco = round(float(item["preco"]),2)
                print(f"Produto encontrado! \n{procurado.capitalize()} custa: R$ {preco}")
            else:
                print("Não temos no estoque!")
            
        else:
            print("Item não encontrado!")

    elif opt == "2": #alterar produto
        procurado = input("Qual produto você procura? ")
        procurado = procurado.lower()

        if procurado in produtos:
            print("\nVocê vai alterar:",procurado.capitalize())
            novo_preco = float(input("Novo preço: "))
            novo_estoque = int(input("Nova quantidade: "))
            item = produtos[procurado] # retorna o dicionário do item porcurado
            item["preco"] = novo_preco
            item["estoque"] = novo_estoque
            print(f"\n{procurado.capitalize()} agora custa: R$ {item['preco']}",
                  f"\nE temos {item['estoque']}")
        else:
            print(f"{procurado.capitalize()} não encontrado!")
            
    elif opt == "3": #novo produto
        print("\nVocê escolheu adicionar um novo produto.")

    elif opt == "4": #sair
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")