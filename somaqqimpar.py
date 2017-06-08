print("Digite um numero inicial")
ini = int(input())
print("Digite um numero final")
fim = int(input())

cont = ini
soma = 0
while(cont <= fim):
    if cont % 2 == 1:
        print(cont, end=" ")
        soma = soma + cont
    cont = cont + 1
print("A soma dos impares e", soma)
