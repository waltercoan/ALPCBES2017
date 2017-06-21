salmin = 0
qtdkw=1
tipo = 0
valkw=0
valconta=0
contador=0
somafaturamento=0
print("Digite o valor do salario minimo")
salmin = float(input())
valkw = salmin / 8
print("O valor do quilowatt e: ", valkw)
#aqui1

while(True):
    print("Digite a quantidade consumida em KW")
    qtdkw = float(input())
    if qtdkw ==0:
        break
    print("Digite o tipo: 1 Res, 2 Com, 3 Ind")
    tipo = int(input())
    valconta = valkw * qtdkw
    if tipo == 1:
        valconta = valconta + (valconta * 5 / 100)
    else:
        if tipo == 2:
            valconta = valconta + (valconta * 10 / 100)
        else:
            valconta = valconta + (valconta * 15 / 100)
    print("O valor da conta e", valconta)
    #acumulador
    somafaturamento = somafaturamento + valconta
    #isso e um contador
    if valconta >= 500 and valconta <= 1000:
        contador = contador + 1
print("O numero de pessoas com a conta entre 500")
print("e 1000 reais e de: ", contador)

print("O faturamento da empresa e ", somafaturamento)

