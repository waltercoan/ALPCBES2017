precoatual = 0
novopreco = 0

print("Digite o preco atual")
precoatual = float(input())

if precoatual <= 50:
    novopreco = precoatual + (precoatual * 5 / 100)
else:
    if precoatual <= 100:
        novopreco = precoatual + (precoatual * 10 / 100)
    else:
        novopreco = precoatual + (precoatual * 15 / 100)
print("O novo preco e", novopreco)

if novopreco <=80:
    print("Barato")
else:
    if novopreco > 80 and novopreco <= 120:
        print("Normal")
    else:
        if novopreco > 120 and novopreco <= 200:
            print("Caro")
        else:
            print("Muito Caro")







