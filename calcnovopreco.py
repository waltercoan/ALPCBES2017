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



