def eunaoacredito():
    print("Eu nao acredito que isso funciona")

def soma(num1, num2=0):
    resul = num1 + num2
    print("A soma e", resul)

def resultadodamegasenna():
    return "4,8,15,16,23,42"

def tabuada(multiplicador, numerador):
    result = multiplicador * numerador
    return result
    #return multiplicador * numerador

#recursividade
def perigo(x):
    print("Perigo ", x)
    if x < 100:
        perigo(x+1)



print("Codigo principal")
eunaoacredito()
print("voltei")
soma(2,2)
soma(2,num2=200)
#pnum1 = int(input("Digita qq coisa"))
#pnum2 = int(input("Digita outra qq coisa"))
#soma(pnum1, pnum2)
oquevortou = resultadodamegasenna()
print(oquevortou)

x = tabuada(7,9)
print(x)

perigo(0)
