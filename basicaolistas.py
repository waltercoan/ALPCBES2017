lista = [0] * 10
#lista = [0,0,0,0,0,0,0,0,0,0,0]
### passa pelo vetor inteiro alimentando com um numero
#digitado
for i in range(10):
    lista[i] = int(input("Digita alguma coisa"))
    pass
soma=0
for i in range(10):
    soma = soma + lista[i]
print("A soma e: ", soma)

soma=0
for i in range(10):
    soma = soma + lista[i]
    #aqui1
media = soma / 10
print("A media dos numeros e", media)

omaior=0
for i in range(10):
    if lista[i] > omaior:
        omaior = lista[i]
print("O maior de todos e", omaior)

omenor = 0
for i in range(10):
    if i == 0:
        omenor = lista[i]
    else:
        if lista[i] < omenor:
            omenor = lista[i]
print("O menor de todos", omenor)

#busca sequencial
#boleano - logica
achei = False
numeroprocurado = int(input("Digite o numero procurado?"))
for i in range(10):
    if numeroprocurado == lista[i]:
        print("Achei...")
        achei = True
        break
if not achei:
    print("Não achei nada...")





