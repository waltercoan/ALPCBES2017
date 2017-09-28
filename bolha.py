import random
lista = [0] * 10

for i in range(10):
    #lista[i] = int(input("Digite um numero"))
    lista[i] = random.randint(0,10000)

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
#lista.sort()
print(lista)


