lista_vendas = [1000, 500, 800, 1500, 2000, 2300]

meta = 1200
percentual_bonus = 0.1
i = 1

for venda in lista_vendas:

    if venda >= meta:
        bonus = percentual_bonus * venda
        print(f"Vendedor Nº {i}")
        print(f"Vendeu: R$ {venda} \nE terá bônus de: R$ {bonus:0.0f}\n") 
    else:
        print(f"Vendedor Nº {i}")
        print(f"Vendeu: R$ {venda} \nE não terá bônus!\n")
    i += 1

    