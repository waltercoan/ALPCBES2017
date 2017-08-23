idade = 0
peso = 0
altura = 0
menordeidade=0
somaidade = 0
somaaltura=0
contagordo=0
omaior=0
timedomaior=0
omenor=0
timedomagro=0
for time in range(5):
    print("Time: ",  time+1)
    for jogador in range(11):
        print("Jogador: ", jogador+1)
        idade = int(input("Digite a idade"))
        somaidade = somaidade + idade
        peso = float(input("Digite o peso"))

        if time ==0 and jogador == 0:
            omenor = peso
            timedomagro = time + 1
        else:
            if peso < omenor:
                omenor = peso
                timedomagro = time + 1

        if peso > 80:
            contagordo += 1
        altura = float(input("Digite a altura"))

        if altura > omaior:
            omaior = altura
            timedomaior = time + 1
        somaaltura += altura
        if idade < 18:
            menordeidade += 1
            #aqui2
    media = somaidade / 11
    print("A media de idade do time e: ", media)
    somaidade = 0

print("O numero de jog menores de idade e", menordeidade)
medialtura = somaaltura / 55
print("A media da altura de todos os jog e: ", medialtura)
perc = (contagordo * 100) / 55
print("O perc de gordinhos e: ", perc)
print("O time ", timedomaior, " tem o maior jogador com")
print(" a altura de ", omaior)
print("O time ", timedomagro, " tem o jogador com")
print(" o menor peso de", omenor)

# qual o numero do time que tem o jogador mais alto
# qual o numero do time que tem o jogador mais leve
