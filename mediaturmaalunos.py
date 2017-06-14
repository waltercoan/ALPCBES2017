print("Digite o numero de turmas")
totturma = int(input())
contt=0
conta=0
somaturmas = 0
while(contt < totturma):
    print("Turma:", (contt+1))
    print("Digite o numero de alunos")
    totalunos = int(input())
    somanotas = 0
    while(conta < totalunos):
        print("Aluno:", (conta+1))
        print("Digite a nota")
        nota = float(input())
        somanotas = somanotas + nota
        conta = conta + 1
    mediaturma = somanotas / totalunos
    print("Media da turma e:", mediaturma)
    somaturmas = somaturmas + mediaturma
    conta=0
    contt = contt + 1
mediaescola = somaturmas / totturma
print("A media da escola e", mediaescola)
