# PRINT
fatur = 1000
custo = 700
imposto = 0.1*fatur
lucro = fatur-custo-imposto
margl = lucro*100/fatur
print("a empresa faturou", fatur)
print("o custo foi de", custo)
print("o lucro foi", lucro)
print("a margem de lucro é", margl,"%")

tempo_em_meses = 170
tempo_em_anos = int(tempo_em_meses/12)
print(tempo_em_anos,"anos")
print("e",tempo_em_meses%12,"meses")