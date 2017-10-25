dados = [[0] * 3 for i in range(5)]

for lin in range(4):
    print("Armazem: ", lin+1)
    for col in range(3):
        print("\tProduto: ", col+1)
        dados[lin][col] = int(input("\tDigite a QTD:"))

for col in range(3):
    print("Produto: ", col+1)
    dados[4][col] = float(input("Digite o preco:"))

#a.	A quantidade de itens  armazenas em cada armazém
somaqtd= [0] * 4
for lin in range(4):
    for col in range(3):
        somaqtd[lin] = somaqtd[lin] + dados[lin][col]
    print("O total do armazem ", lin+1, " e de ", somaqtd[lin])

#b.	Qual o armazém possui maior estoque do produto 2;
omaiorvalor=0
oarmmaior=0
for lin in range(4):
    #print(dados[lin][1])
    if omaiorvalor < dados[lin][1]:
        omaiorvalor = dados[lin][1]
        oarmmaior = lin
print("O produto 2 tem a maior qtd no armazem ", oarmmaior)
print(" com ", omaiorvalor, " produtos")

somaarm=0
omenor=0
oarmzemmenor=0
#c.	Qual o armazém possui menor estoque
for lin in range(4):
    for col in range(3):
        somaarm = somaarm + dados[lin][col]
    #aquiohhhhhhhhhhhhhhhhhhhh
    if lin == 0:
        omenor = somaarm
        oarmzemmenor = lin
    else:
        if somaarm < omenor:
            omenor = somaarm
            oarmzemmenor = lin
    somaarm = 0
print("O armazem ", oarmzemmenor, " possui a menor qtd com ", omenor)
#d.	Qual o custo total de cada produto
#e.	Qual o custo total de cada armazém
