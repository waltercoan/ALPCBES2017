'''import time
while(True):
    print("Mae eu fiz a matrix...")
    time.sleep(0.1)

v=0
while(v <= 10):
    print(v)
    v = v + 1

import time
v=10
while(v >= 0):
    print(v)
    v = v - 1
    time.sleep(1)
'''

i = 0
soma = 0
while (i < 200):
    i = i + 1
    if i % 2 == 1:
        print(i,end=" ")
        soma = soma + i
        if i % 11 ==0:
            print()
print("\nA soma dos 100 primeiros impares e", soma)














