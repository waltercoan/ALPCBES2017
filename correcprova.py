gaba = [0] * 10

print("Digite o gabarito")
for q in range(10):
    gaba[q] = int(input("Digite resp da questao " + str(q+1) + ":"))

print(gaba)
aprovados = 0
for aluno in range(15):
    print("Aluno: ", aluno+1)
    nota = 0
    matricula = int(input("Digite sua matricula:"))
    for q in range(10):
        print ("Questao ", q+1, ":")
        respaluno = int(input())
        if gaba[q] == respaluno:
            nota = nota + 1
    print("NOTA:", nota)
    if nota >= 6:
        aprovados = aprovados + 1

perc = (100 * aprovados) / 15
print("O perc de aprovados e: ", perc)

#A percentagem de aprovação, sabendo-se que a nota mínima é 6,0
