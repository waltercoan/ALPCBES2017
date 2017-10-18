vendas = [[0] * 4 for i in range(5)]

for vendedor in range(5):
    print("Vendedor: ", vendedor+1)
    for semana in range(4):
        print("\tSemana: ", semana+1)
        vendas[vendedor][semana] = float(input("\tDigite as vendas"))

#a.	O total de vendas do mês de cada vendedor
total = 0
for vendedor in range(5):
    for semana in range(4):
        total = total + vendas[vendedor][semana]
    print("O total do vendedor ", vendedor+1, " e ", total)
    total = 0

#b.	O total de vendas de cada semana (todos os vendedores juntos)
totalsemana = 0
for semana in range(4):
    for vendedor in range(5):
        totalsemana = totalsemana + vendas[vendedor][semana]
    print("O total da semana ", semana+1, " e ", totalsemana)
    totalsemana = 0

#c.	O total de vendas do mês
somatudo=0
for vendedor in range(5):
    for semana in range(4):
        somatudo += vendas[vendedor][semana]

print("O total geral e ", somatudo)
