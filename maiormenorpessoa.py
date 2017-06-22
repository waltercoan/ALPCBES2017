#http://www.pythontutor.com/visualize.html#mode=edit
altura = 0
pessoa=0
sexo = ''
omaior=0
omenor=0
somaaltfem=0
contfem=0
contmasc=0
sexodomaior=''
while(pessoa < 10):
    print("Pessoa > ", pessoa)
    print("Digite sua altura")
    altura = float(input())
    print("Digite o sexo (M/F)")
    sexo = input()

    if sexo == 'f' or sexo == 'F':
        somaaltfem = somaaltfem + altura
        contfem = contfem + 1
    else:
        contmasc = contmasc + 1


    if altura > omaior:
        omaior = altura
        sexodomaior = sexo

    if pessoa == 0:
        omenor = altura
    else:
        if altura < omenor:
            omenor = altura

    pessoa = pessoa + 1
print("A maior altura e: ", omaior, " do sexo: ", sexodomaior)
print("A menor altura e: ", omenor)

mediafem = somaaltfem / contfem
print("A media da altura das mulheres e", mediafem)
print("O numero total de homens e", contmasc)
