print("Desafio Médio - Estoque com preços")

# Você tem um lista de produtos com seus preços (use um dicionário). 
# O usuário digita o nome de um produto e o programa deve:
# Dizer se o produto existe no estoque.
# Se existir, mostrar o preço.
# Se não existir, mostrar "Produto indisponível"

produtos = {
    "calça":{"preço":59,"estoque":0},
    "camisa":{"preço":29,"estoque":3},
    "cueca":{"preço":19,"estoque":3},
    "meia":{"preço":9,"estoque":3},
    "blusa":{"preço":99,"estoque":3}
}

while True:
    print("\nMenu:")
    print("1 - Consultar produto")
    print("2 - Alterar produto")
    print("3 - Novo produto")
    print("4 - Listar produtos")
    print("5 - Sair")
    opcao = str(input("\nEscolha uma opção: "))
    
    if opcao == "1": #consultar produto
        procurado = input("Qual produto você procura? ")
        procurado = procurado.lower()

        if procurado in produtos:
            item = produtos[procurado] # retorna o dicionário do item porcurado
            if item["estoque"] > 0:
                preço = round(float(item["preço"]),2)
                print(f"Produto encontrado! \n{procurado.capitalize()} custa: R$ {preço} \nE temos: {item['estoque']} unidades.")
            else:
                print("\nVocê procurou:",procurado.capitalize())
                print("Não temos no estoque!")
            
        else:
            print("Item não encontrado!")

    elif opcao == "2": #alterar produto
        procurado = input("Qual produto você procura? ")
        procurado = procurado.lower()

        if procurado in produtos:
            print("\nVocê vai alterar:",procurado.capitalize())
            novo_preço = float(input("Novo preço: "))
            novo_estoque = int(input("Nova quantidade: "))
            item = produtos[procurado] # retorna o dicionário do item porcurado
            item["preço"] = novo_preço
            item["estoque"] = novo_estoque
            print(f"\n{procurado.capitalize()} agora custa: R$ {item['preço']}",
                  f"\nE temos {item['estoque']}")
        else:
            print(f"{procurado.capitalize()} não encontrado!")
            
    elif opcao == "3": #novo produto
        novo = input("Qual produto você quer adicionar? ")
        novo = novo.lower()

        if novo in produtos:
            print("Produto já está cadastrado, use Alterar produto")
        else:
            preço = float(input("Preço: "))
            estoque = int(input("Quantidade: "))
            produtos[novo] = {"preço":preço,"estoque":estoque}
            print(f"{novo.capitalize()} cadastrado, custa: R$ {preço} \nE temos {estoque} unidades")

    elif opcao == "4": #listar todos os produtos
        print("\nEstoque completo:")
        for nome, dados in produtos.items():
            preco = round(float(dados["preço"]), 2)
            estoque = dados["estoque"]
            print(f"{nome.capitalize()} - R$ {preco} - {estoque} unidades")
    elif opcao == "5": #sair
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
        print(f"Você digitou: {opcao}")
4