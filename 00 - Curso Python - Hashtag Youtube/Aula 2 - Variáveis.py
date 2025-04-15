# VARIÁVEIS
faturamento = 1200
custo = 700
imposto =0.1*faturamento
lucro = round(faturamento-custo-imposto)
margem = lucro/faturamento

#duas formas de fazer a mesma coisa
print("O faturamento da empresa é:{}, Custo:{}, Lucro:{}".format(faturamento,custo,lucro))
print(f"O faturamento da empresa é:{faturamento}, Custo:{custo}, Lucro:{lucro}")

email = "matheusaugustomartins1997@gmail.com"
print(email)
#maiuscula
email = email.upper()
print(email)
#minuscula
email = email.lower()
print(email)
#encontrar um caracter
print(email.find("@"))
# se = -1 ele não encontrou

#tamanho do texto
print(len(email))

#pegar uma caracter
print(email[0]) #numeros negativos pegam de tras para frente

#pegar um pedaço do texto
print(email[:5])
print(email[:email.find("@")])
print(email[email.find("@")+1:])

#trocar um pedaço do texto
novoemail = email.replace("gmail.com","hotmail.com")
print(novoemail)

nome = "matheus augusto martins"
#trabalhar com nome
print(nome.capitalize()) #primeira letra maiuscula
print(nome.title()) #primeira letra maiuscula de cada palavra

#pegar o servidor do email
posição_do_arroba = email.find("@")+1
servidor = email[posição_do_arroba:]
print(servidor)

#pegar o 1° nome
pos_espaço = nome.find(" ")
print(pos_espaço)
primeiro = nome[:pos_espaço]
print(primeiro)

#pegar o sobrenome
restonome = nome[pos_espaço+1:]
print(restonome)
pos_espaço1 = restonome.find(" ")+1
sobrenome = restonome[pos_espaço1:]
print(sobrenome)
#casos especiais - formatação numérica
margem = round(margem,2)
print(f"O faturamento da empresa é: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}, Margem: {margem:.1%}")
