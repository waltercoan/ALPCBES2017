from basicaolistas import omenor

numatend  = 10
cep       = [0] * numatend
valor     = [0] * numatend
realizado = [0] * numatend

print("Entrada da agenda de atendimentos")

for a in range(numatend):
    print("Atendimento n: ", a+1)
    cep[a]       = int(input("Digite o CEP da casa"))
    valor[a]     = float(input("Digite o valor cobrado"))
    realizado[a] = int(input("Atend realizado: 1 SIM 0 NÃO"))

omaior = 0
cepmaior=0
for a in range(numatend):
    if realizado[a] == 1:
        if valor[a] > omaior:
            omaior = valor[a]
            cepmaior = cep[a]
print("O cep", cepmaior, " pagou o maior valor de ", omaior)

omenor = 0
cepmenor = 0
oprimeiro = True
for a in range(numatend):
    if realizado[a] == 1:
        if oprimeiro:
            omenor = valor[a]
            cepmenor = cep[a]
            oprimeiro = False
        else:
            if valor[a] < omenor:
                omenor = valor[a]
                cepmenor = cep[a]
print("O cep", cepmenor, " pagou o menor valor de ", omenor)
#ii.	quantos atendimentos foram perdidos no dia
# e quanto dinheiro o chaveiro deixou de receber?

contperdido=0
somadeixoureceber=0
for a in range(numatend):
    if realizado[a] == 0:
        contperdido = contperdido + 1
        somadeixoureceber = somadeixoureceber + valor[a]

print("O numero de atendimentos perdidos foi de ", contperdido)
print("E o chaveiro deixou de receber R$ ", somadeixoureceber)

#iii.	liste em tela uma nova agenda do próximo dia
# de trabalho do chaveiro para atender sequencialmente as
# casas que não foram atendidas no dia anterior.

print("Agenda do proximo dia")
for a in range(numatend):
    if realizado[a] == 0:
        print("CEP " , cep[a], " valor R$ ", valor[a])



