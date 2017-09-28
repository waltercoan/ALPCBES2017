lista = [1,3,5,7,11,15,19,20]
proc = int(input("Digite o numero procurado"))

inicio = 0
fim = len(lista)-1
achei=False
while(inicio <= fim):
    meio = int((inicio+fim)/2)
    if proc == lista[meio]:
        print("Encontrei...")
        achei=True
        break
    else:
        if proc > lista[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1
if achei==False:
    print("nao achou")
