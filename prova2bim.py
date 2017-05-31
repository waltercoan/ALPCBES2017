pesokg = 0
tipo = ""
valcusto = 0
pesoton=0
tempo=0
valhora = 0

print("Digite o peso em quilogramas")
pesokg = float(input())
print("Digite o tipo [D]omestico ou [I]ndustrial")
tipo = input()
print("Digite o valor do custo")
valcusto = float(input())

pesoton = pesokg / 1000

if tipo == "I":
    if pesoton > 8:
        tempo = 2 * pesoton
    else:
        tempo = 1 * pesoton
else:
    if pesoton <= 3:
        tempo = 4
    else:
        tempo = 7
print(" O tempo necessario e ",  tempo)

if tempo <= 1:
    valhora = (valcusto * 15) / 100
else:
    if tempo > 1 and tempo < 4:
        valhora = (valcusto * 12) / 100
    else:
        valhora = (valcusto * 10) / 100
print("O valor da hora e" , valhora)

valfinal = valhora * tempo
print("O valor final e", valfinal)
















