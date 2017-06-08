n=0
print("digite um numero")
n = int(input())

cont = 0
fat = 1
if n < 0:
    print("Não e possivel calcular o fatorial")
else:
    if n == 0:
        print("0! = 1")
    else:
        cont  = n
        while (cont > 1):
            fat = fat * cont
            cont = cont - 1
            print(cont)
        print("O resultado e ", fat)

