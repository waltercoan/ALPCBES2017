x = [1,2,3,4,5,6,7,8,9,10]
y = [11,2,13,4,15,6,17,8,19,10]
uniao = [0] * 20

print("Conjunto X:", x)
print("Conjunto Y:", y)

print("Conjunto UNIÃO")
#a.	a união de X com Y (todos os elementos de
# X e os elementos de Y que não estejam em X)
for pos in range(10):
    uniao[ pos ] = x[pos]

proxlivre = 10
for pos in range(10):
    achou = False
    for pos2 in range(10):
        print("y:",y[pos], " x:", x[pos2])
        if y[pos] == x[pos2]:
            achou = True
            break
    if not achou:
        uniao[proxlivre] = y[pos]
        proxlivre += 1

print(uniao)
#b.	a diferença entre X e Y
# (todos os elementos de X que não existam em Y)

diferenca = [0] * 10
proxlivre = 0
for posx in range(10):
    print(x[posx])
    achei = False
    for posy in range(10):
        print(y[posy], end=" ")
        if x[posx] == y[posy]:
            achei = True
            break
    print("\n")
    if achei == False:
        diferenca[proxlivre] = x[posx]
        proxlivre += 1
print("Diferença")
print(diferenca)

soma = [0] * 10

for pos in range(10):
    soma[pos] = x[pos] + y[pos]

print("Soma")
print(soma)

produto = [0] * 10
for pos in range(10):
    produto[pos] = x[pos] * y[pos]

print("Produto")
print(produto)

inter = [0] * 10
proxlivre = 0
for posx in range(10):
    print("X:", x[posx])
    for posy in range(10):
        print(y[posy], end=" ")
        if x[posx] == y[posy]:
            inter[proxlivre] = x[posx]
            proxlivre += 1
            break
print("Inter")
print(inter)
