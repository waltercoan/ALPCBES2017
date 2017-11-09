# DICA
# 1h = 3600s
# 1m = 60s

def converte(seg):
    horas = int(seg / 3600)
    sobrou = seg - (horas * 3600)
    print("Horas:", horas)
    #print("Sobrou segundos", sobrou)
    minutos = int(sobrou / 60)
    print("Minutos: ", minutos)
    segundos = (sobrou - (minutos * 60))
    print("Segundos ", segundos)

converte(10000)

