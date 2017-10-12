velha = [[' '] * 3 for i in range(3)]

jogador = 1
while(True):
    for linha in range(3):
        for col in range(3):
            print(velha[linha][col], end="")
            if col != 2:
                print("|",end="")
        if linha != 2:
            print("\n-------")
    print()
    if jogador == 1:
        print("Jogador: X")
    else:
        print("Jogador: O")
    linha = int(input("Digite a linha")) - 1
    coluna = int(input("Digite a coluna")) - 1

    if jogador == 1:
        velha[linha][coluna] = "X"
        jogador = 2
    else:
        velha[linha][coluna] = "O"
        jogador = 1
#nao permitir que um jogador, jogue sobre o outro
#quem ganhou o jogo
