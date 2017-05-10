valvendmed = 0
precoatual = 0
reajuste = 0
novopreco = 0
print("Digite o val medio de venda mensal")
valvendmed = float(input())
print("Digite o valor do preco atual")
precoatual = float(input())

if valvendmed < 500 or precoatual < 30:
    reajuste = (precoatual * 12) / 100
    novopreco = precoatual + reajuste
else:
    if (valvendmed >= 500 and valvendmed < 1600) or \
        (precoatual >= 30 and precoatual < 80):
        reajuste = (precoatual * 15) / 100
        novopreco = precoatual + reajuste
    else:
        reajuste = (precoatual * 25) / 100
        novopreco = precoatual - reajuste
print("O novo preco e", novopreco)
print("E o reajuste foi de", reajuste)


