#numcontas = [0] * 10
#saldos = [0] * 10
numcontas = [10,20,30,40,50,60,70,80,90,100]
saldos = [0,10,0,10,0,10,0,10,0,10]
'''
print("Entrada de dados")
for p in range(10):
    print("Pessoa ", p+1)
    repete = True
    while(repete):
        contatemp = int(input("Digite numero da conta"))
        achei = False
        for i in range(10):
            if numcontas[i] == contatemp:
                achei = True
                print("Numero de conta invalido")
                break
        if achei == False:
            print("Numero de conta VALIDO")
            repete = False
            numcontas[p] = contatemp
            saldos[p] = float(input("Digite o saldo"))
'''
opcao = 0
while(opcao != 4):
    print("Menu")
    print("1 - Efetuar deposito")
    print("2 - Efetuar saque")
    print("3 - Consultar ativos")
    print("4 - Sair")
    opcao = int(input("Digite o numero da opcao desejada"))
    if opcao == 1:
        print("DEPOSITO")
        contdep = int(input("Digite o numero da conta"))
        achei = False
        for i in range(10):
            if numcontas[i] == contdep:
                achei = True
                valdep = float(input("Digite o valor do deposito"))
                saldos[i] = saldos[i] + valdep
                break
        if achei == False:
            print("Numero de conta inválido")
        pass
    if opcao == 2:
        print("SAQUE")
        contasaque = int(input("Digite a conta para o saque"))
        achei = False
        for i in range(10):
            if numcontas[i] == contasaque:
                achei = True
                valsaque = float(input("Digite o valor do saque"))
                if valsaque > 0 and valsaque <= saldos[i]:
                    saldos[i] = saldos[i] - valsaque
                    print("Saque realizado com sucesso")
                else:
                    print("Valor do saque invalido ou saldo insuficiente")
                break
        if achei == False:
            print("Numero de conta inválido")
        pass
    if opcao == 3:
        print("LISTA ATIVOS")
        for i in range(10):
            print("Conta:", numcontas[i], " Saldo: R$", saldos[i])
        pass
    if opcao == 4:
        print("Valeu ai, bom dia...")
#aqui2
