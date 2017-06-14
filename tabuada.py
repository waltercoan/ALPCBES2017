tab = 0
cont = 1
print("Digite o numero da tabuada")
tab = int(input())

print("Gerando tabuada")
while(cont <= 10):
    result = tab * cont
    print(tab, " x ", cont, " = ", result)
    cont = cont + 1
