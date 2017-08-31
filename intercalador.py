listaA=[0] * 10
listaB=[0] * 10
listaInter = [0] * 201

for pos in range(10):
    listaA[pos] = int(input("Digite um numero"))

for pos in range(10):
    listaB[pos] = int(input("Digite outro numero"))

proxlivre=0
for i in range(10):
    listaInter[proxlivre] = listaA [i]
    proxlivre = proxlivre + 1
    listaInter[proxlivre] = listaB [i]
    proxlivre = proxlivre + 1

print(listaInter)
