#variavel global
numero = 1

def alteraNumero():
    #local
    global numero
    numero = 3

numero = 2
alteraNumero()
print("Numero e: ", numero)
