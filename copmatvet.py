m = [[0] * 3 for i in range(3)]
v = [0] * 9

for i in range(9):
    v[i] = i+1
i=0
for lin in range(3):
    for col in range(3):
        m[lin][col] = v[i]
        i = i + 1
print(m)

i=0
for lin in range(3):
    for col in range(3):
        v[i] = m[lin][col]
        i = i + 1
print (v)
