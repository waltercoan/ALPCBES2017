altura = 0
sexo = ""
omaisalto=0
omaisbaixo=0
somaaltura=0
contmulher=0
conthomens=0
sexodomaisalto=""
for p in range(10):
    print("Pessoa:", p+1)
    print("Digite a altura")
    altura = float(input())
    print("Digite o sexo M/F")
    sexo = input()
    if sexo == 'f' or sexo == 'F':
        #somaaltura = somaaltura + altura
        somaaltura += altura
        #contmulher = contmulher + 1
        contmulher += 1
    else:
        conthomens +=1

    if altura > omaisalto:
        omaisalto = altura
        sexodomaisalto = sexo


    if p == 0:
        omaisbaixo = altura
    else:
        if altura < omaisbaixo:
            omaisbaixo = altura
print("A altura do mais alto e", omaisalto)
print("E seu sexo e", sexodomaisalto)
print("A altura do mais baixo e", omaisbaixo)
media = somaaltura / contmulher
print("A media da altura das mulheres e", media)
print("O numero de homens e", conthomens)
