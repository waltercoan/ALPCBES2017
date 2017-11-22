def fazalgo(*dados):
    for i in dados:
        print(i)
    pass

#fazalgo(52)
#azalgo(52,1)
#fazalgo(52,1,1,1,1,1,1,1,1,1,1,1,1,"eunaoacredito")

tabuada = lambda x,y : x * y
#print(tabuada(2,7))
#outronome = tabuada
#print(outronome(7,9))

def geratabuada(num, regra):
    for i in range(11):
        print(regra(num,i))

geratabuada(7,tabuada)
