def soma(a, b, c):
    if a > 1:
        soma = 0
        for i in range(b,c+1):
            if i % a == 0:
                soma = soma + i
        return soma
    else:
        raise Exception()

if __name__ == '__main__':
    a = int(input("Digite A"))
    b = int(input("Digite B"))
    c = int(input("Digite C"))
    retorno = soma(a,b,c)
    print("Retorno: ", retorno)
