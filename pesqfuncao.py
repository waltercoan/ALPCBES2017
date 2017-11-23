sexo = [''] * 5
corolho = [''] * 5
corcabelo = [''] * 5
idade = [0] * 5

def ledados():
    global sexo, corolho, corcabelo, idade
    for i in range(5):
        sexo[i] = input("Digite o sexo (m/f)")
        corolho[i] = input("Digite cor olho (a/c)")
        corcabelo[i] = input("Digite cor cabelo (l/p/c)")
        idade[i] = int(input("Digite sua idade"))
    #aquiohhh
def media():
    global sexo, corolho, corcabelo, idade
    somaidade = 0
    media = 0
    contador=0
    for i in range(5):
        if corolho[i] == 'c' and corcabelo[i] == 'p':
            somaidade = somaidade + idade[i]
            contador += 1

    media = somaidade / contador
    return media

def maioridade():
    global sexo, corolho, corcabelo, idade
    omaior=0
    for i in range(5):
        if idade[i] > omaior:
            omaior = idade[i]
    return omaior

def conttheone():
    global sexo, corolho, corcabelo, idade
    contador = 0
    for i in range(5):
        if sexo[i] == 'f' and (idade[i]>= 18 and idade[i]<=35) and \
            corcabelo[i] == 'l' and corolho[i] == 'a':
            contador += 1

    return contador



ledados()
pegamedia = media()
print("A media calculada e: ", pegamedia)
pegaomaior = maioridade()
print("A maior idade e ",  pegaomaior)
pegacontador = conttheone()
print("A qtd de pra casar e", pegacontador)
