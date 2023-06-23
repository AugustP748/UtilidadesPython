
if __name__ == '__main__':
    
    print("Método de Lehmer")
    
    n = "35451"
    t = "73"
    TOT = "4"
    MU_LIST: list = []
    
    print()
    print("========== INICIO==========")
    #t : str = input("Número Entero (t): ")
    #n0 : str = input("Semilla (n0): ")
    #TOT : str = input("Cantidad de números a generar: ")
    print("Número Entero (t): ",t)
    print("Semilla (M): ",n)
    print("Cantidad de Números a generar: ", TOT)
    print()
    
    for i in range (0,int(TOT)):
        
        aux: int = int(n) * int(t)
        cadena_aux = str(aux)
        first_cut: str = cadena_aux[:len(t)]
        last_cut: str = cadena_aux[len(t):]
        
        n = int(last_cut) - int(first_cut)
        mu: float = float("0."+str(n))
        MU_LIST.append(mu)
        
        print(n)
        
    print(MU_LIST)
        
    