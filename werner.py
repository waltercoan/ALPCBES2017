conja = [1,3,4]
conjb = [2,3,5]

for i in range(len(conja)):
    for j in range(len(conjb)):
        result = conja[i] + conjb[j] > 5
        print(str(conja[i]) + " + " + str(conjb[j]) + " > 5 = " + str(result))
