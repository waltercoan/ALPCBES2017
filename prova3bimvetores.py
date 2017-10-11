nummax = 30
cep = [0] * nummax
codcombo = [0] * nummax
qtd = [0] * nummax

opcao = 0
proxlivre = 0
while(opcao != 5):
    print("1 - Registrar pedido")
    print("2 - Pedido maior/menor")
    print("3 - Contagem pedidos")
    print("4 - Relatorio financeiro")
    print("5 - Sair")
    opcao = int(input("Digite o numero da opcao"))

    if opcao == 1:
        cep[proxlivre] = int(input("Digite o CEP"))
        codcombo[proxlivre] \
            = int(input("Digite o codigo do combo"))
        qtd[proxlivre] = int(input("Digite a quantidade"))
        proxlivre += 1

    if opcao == 2:
        omaior=0
        cepdomaior=0
        omenor = 0
        cepdomenor = 0
        for p in range(proxlivre):
            if qtd[p] > omaior:
                omaior = qtd[p]
                cepdomaior = cep[p]
            if p == 0:
                omenor = qtd[p]
                cepdomenor = cep[0]
            else:
                if qtd[p] < omenor:
                    omenor = qtd[p]
                    cepdomenor = cep[0]
        print("No cep " , cepdomaior, " foi maior pedido com ", omaior)
        print("No cep ", cepdomenor, " foi o menor pedido com ", omenor)

    if opcao == 3:
        qtdtipo1 = 0
        qtdtipo2 = 0
        qtdtipo3 = 0
        for p in range(proxlivre):
            if qtd[p] >= 2:
                if codcombo[p] == 10:
                    qtdtipo1 += 1
                if codcombo[p] == 30:
                    qtdtipo2 += 1
                if codcombo[p] == 50:
                    qtdtipo3 += 1

        print("O total do tipo 10 é ",  qtdtipo1)
        print("O total do tipo 30 é ",  qtdtipo2)
        print("O total do tipo 50 é ",  qtdtipo3)

    if opcao == 4:
        for p in range(proxlivre):
            print(" CEP" , cep[p], " Codigo ", codcombo[p], " qtd ", qtd[p])
            preco = 0
            if codcombo[p] == 10:
                preco = 20 * qtd[p]
            if codcombo[p] == 30:
                preco = 60 * qtd[p]
            if codcombo[p] == 50:
                preco = 90 * qtd[p]
            print("Preco pedido R$", preco)





