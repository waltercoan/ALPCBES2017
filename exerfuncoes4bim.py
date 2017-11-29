matrictel =[0] * 15
numtelefone = [0] * 15
tempo = [0] * 15
objetivo = [False] * 15
matricatend = 0
opcao=0
proxlivre=0
#aqui vao ficar as funções....

def registrarchamada(mattele):
    global proxlivre
    novotelefone = int(input("Digite o numero do telefone"))
    novotempo = int(input("Digite o tempo em minutos"))
    novasituacao = input("Foi atendido s/n") == 's'
    numtelefone[proxlivre] = novotelefone
    tempo[proxlivre] = novotempo
    objetivo[proxlivre] = novasituacao
    matrictel[proxlivre] = mattele
    proxlivre +=1

    pass

def relatoriochamadas():
    print("Chamados com sucesso")
    for i in range(15):
        if objetivo[i] == True:
            print("Atendente", matrictel[i])
            print("Num Telefone", numtelefone[i])
            print("Tempo", tempo[i])
    print("Chamados sem sucesso")
    for i in range(15):
        if objetivo[i] == False:
            print("Atendente", matrictel[i])
            print("Num Telefone", numtelefone[i])
            print("Tempo", tempo[i])

def melhorchamado():
    omenortempo = 99999
    numtelefonemenor = 0
    for i in range(15):
        if objetivo[i] == True:
            if tempo[i] < omenortempo:
                omenortempo = tempo[i]
                numtelefonemenor = numtelefone[i]
    return numtelefonemenor, omenortempo

matricatend = int(input("Digite a Matricula atendente"))
while(opcao != 9):
    print("Sistema de telemarketing")
    print("1 - Registrar chamada")
    print("2 - Relatorio de chamadas")
    print("3 - Melhor Chamado")
    print("9 - Sair")
    opcao = int(input("Digite o numero desejado"))
    if opcao == 1:
        registrarchamada(matricatend)
    if opcao == 2:
        relatoriochamadas()
    if opcao == 3:
        telefone,omenor = melhorchamado()
        print("O telefone do chamado com o menor tempo e", telefone)

