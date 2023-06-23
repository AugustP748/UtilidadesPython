#from Numeros_Pseudoaleatorios import 

def Normal(m,d):
    sum: float = 0
    for i in range(0,12):
        u = 0.2548
        sum+=u
        
    x = d*(sum+6)+m
    return x


def Poisson(a,x):
    ...