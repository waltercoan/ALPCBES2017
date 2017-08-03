idade = 0
nota = 0
somaidade=0
mediaidade=0
contotimos=0
contregular=0
contbom=0
for pessoa in range(15):
    print("Pessoa: ", pessoa+1)
    idade = int(input("Digite sua idade\n"))
    nota = int(input("Digite nota: otimo=3 bom=2 reg=1\n"))
    if nota == 3:
        somaidade = somaidade + idade
        contotimos = contotimos + 1
    if nota == 1:
        contregular = contregular + 1
    if nota == 2:
        contbom = contbom + 1
    #aqui1

mediaidade = somaidade / contotimos
print("A media das idades dos otimos e: ", mediaidade)
print("O numero de votos regular foi: ", contregular)
perc = (contbom * 100) / 15
print("O perc de votos bom e:", perc)
#- a média das idades das pessoas que responderam ótimo
#- a quantidade de pessoas que respondeu regular
#- a percentagem de pessoas que respondeu bom entre
# todos os espectadores analisados
