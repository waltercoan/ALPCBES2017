idade =0
contador=0
faixa1=0
faixa2=0
faixa3=0
faixa4=0
faixa5=0
while(contador <15):
    print("Digite a idade")
    idade = int(input())
    if idade <= 15:
        faixa1 = faixa1 + 1
    else:
        if idade >= 16 and idade <= 30:
            faixa2 = faixa2 + 1
        else:
            if idade >= 31 and idade <=45:
                faixa3 = faixa3 + 1
            else:
                if idade >= 46 and idade <= 60:
                    faixa4 = faixa4 + 1
                else:
                    faixa5 = faixa5 + 1
    contador = contador + 1
#engsoftware@univille.br
perc1 = (faixa1 * 100 / 15)
print("Faixa 1: ", faixa1, " com perc de:", perc1)
perc2 = (faixa2 * 100 / 15)
print("Faixa 2: ", faixa2, " com perc de:", perc2)
perc3 = (faixa3 * 100 / 15)
print("Faixa 3: ", faixa3, " com perc de:", perc3)
perc4 = (faixa4 * 100 / 15)
print("Faixa 4: ", faixa4, " com perc de:", perc4)
perc5 = (faixa5 * 100 / 15)
print("Faixa 5: ", faixa5, " com perc de:", perc5)
