numeros = [0] * 100
telefones =['555-1234',
            '555-4321',
            '555-1111',
            '555-2222']
print(telefones[0])
print(telefones[3])
telefones[3] = '00000'
print(telefones[3])
telefones.append('666')
print(telefones)

for umtelefone in telefones:
    print(umtelefone)

#ISSO NAO FUNCIONA
listalimpa = []
#listalimpa[0] = 'lalalla'
listalimpa.append('lalalal')


print('Tamanho - length', len(numeros))
for i in range(len(numeros)):
    numeros[i] = -1

print(numeros)

