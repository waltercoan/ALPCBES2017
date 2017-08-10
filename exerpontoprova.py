numeroaluno=0
alturaaluno = 0
omaisalto=0
numeromaisalto=0
omaisbaixo=0
numeromaisbaixo=0
for i in range(10):
    print("Digite o número do aluno")
    numeroaluno = int(input())
    print("Digite a altura do aluno")
    alturaaluno = int(input())
    if alturaaluno > omaisalto:
        omaisalto = alturaaluno;
        numeromaisalto = numeroaluno
    if i==0:
        omaisbaixo = alturaaluno
        numeromaisalto = numeroaluno
    else:
        if alturaaluno < omaisbaixo:
            omaisbaixo = alturaaluno
            numeromaisalto = numeroaluno

print("O aluno numero ", numeromaisalto, " tem a maior altura de", omaisalto)
print("O aluno numero ", numeromaisbaixo, " tem a menor altura de", omaisbaixo)
