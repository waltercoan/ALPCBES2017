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
#b.	a diferença entre X e Y
# (todos os elementos de X que não existam em Y)



print(uniao)
