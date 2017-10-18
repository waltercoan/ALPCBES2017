import random
mat = [[0] * 5 for i in range(3)]

mat = [[0,0,0,0,0],
       [16,16,16,16,16],
       [0,0,0,0,0]]

for lin in range(3):
    for col in range(5):
        #mat[lin][col] = int(input("Digite algum numero?"))
        mat[lin][col] = random.randint(0, 100)

contador = 0

for lin in range(3):
    for col in range(5):
        if mat[lin][col] >= 15 and mat[lin][col] <= 20:
        #if  15 <= mat[lin][col] <= 20:
            contador += 1

print("O numero de elementos entre 15 e 20 e:", contador)
