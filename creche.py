numturma=0
numsala = 0
numcriancas = 0
sexo = ""
print("Digite o numero de turmas")
numturma = int(input())
contcrianca=0
acumcrianca=0
contmenino=0
contmenina=0
omaiornummen=0
omenornummenina=0
numsalamaior=0
numsalamenor=0
for t in range(numturma):
    print("Turma: ", t+1)
    print("Digite o numero da sala")
    numsala = int(input())
    print("Digite o numero de crianças")
    numcriancas = int(input())
    #acumulador
    acumcrianca = acumcrianca + numcriancas
    contmenino = 0
    contmenina = 0
    for c in range(numcriancas):
        print("Criança: ", c+1)
        print("Digite o sexo m/f")
        sexo = input()
        if sexo == 'm' or sexo == 'M':
            contmenino = contmenino + 1
        else:
            contmenina = contmenina + 1
        contcrianca = contcrianca + 1
    #logica do maior
    if contmenino > omaiornummen:
        omaiornummen = contmenino
        numsalamaior = numsala
    #logica do menor
    if t == 0:
        omenornummenina = contmenina
        numsalamenor = numsala
    else:
        if contmenina < omenornummenina:
            omenornummenina = contmenina
            numsalamenor = numsala

#O numero da sala com o menor número de meninas.

print("O numero total de criancas e", contcrianca)
print("O numero total de criancas e", acumcrianca)

media = contcrianca / numturma
print("A media de alunos e", media)
print("A sala ", numsalamaior , " tem a maior quantidade")
print(" de meninos com ", omaiornummen)
print("A sala ", numsalamenor, " tem a menor quantidade")
print(" de meninas com ", omenornummenina)
