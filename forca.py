#implementar o controle de vencer e perder o jogo
#implementar a substituição de todas as letras quando encontrado

palavra = "mafagafinhos"
tamanho = len(palavra)
continua = True
dica = "-" * tamanho
while(continua):
    print("     --------  ")
    print("     O      |  ")
    print("    -|-     |  ")
    print("     |      |  ")
    print("    / \     |  ")
    print("            |  ")
    print(dica)
    umaletra = input("Digite uma letra")
    posicao = palavra.find(umaletra)
    if(posicao != -1):
        dica = dica[:posicao] + palavra[posicao] + dica[posicao + 1:]
        pass
    pass
