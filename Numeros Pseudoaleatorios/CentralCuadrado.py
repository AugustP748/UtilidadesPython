import copy



def TakeCentralValues(cadena: str,paridad:int) -> str:
    """ This function take the central values of a string value and return the N central numbers"""   
    longitud: int = len(cadena)
    initial_position: int = longitud // 2 - paridad
    end_position: int = initial_position + int(N)
    value: str = cadena[initial_position:end_position]
    return value

def ShowResults(number_mu:int,old_M:str,cadena:str,mu:float):
    long_X: int = len(str(X))
    long_tot: int = long_X-int(N)
    print("==========mu%s==========" % number_mu)
    print("X = M^2 = %s^2 = %s -> Longitud:%s" % (old_M, X,long_X))
    print("Longitud - N = %s - %s = %s" % (long_X,N,long_tot))
    if long_tot % 2 == 0:
        print("%s es Par"%long_tot)
    else:
        print("%s es Impar"%long_tot)
        print("%s * 10 = %s"%(X,cadena))
    
    print("M = los %s digitos centrales de %s"%(N,cadena))
    print("Entonces, M = %s" % M)
    print("Por lo tanto mu{} es {:.{digits}f}".format(number_mu,mu,digits=int(N)))
    print()

if __name__ == '__main__':
    
    print("Método de la parte central del cuadrado")

    
    N = 4
    M = 3708
    TOT = 5
    old_M: str 
    paridad: int = 1
    MU_LIST: list = []
    print()
    print("========== INICIO==========")
    #N : str = input("Número de Digitos (N): ")
    #M : str = input("Semilla (M): ")
    #TOT : str = input("Cantidad de números a generar: ")
    print("Número de Digitos (N): ",N)
    print("Semilla (M): ",M)
    print("Cantidad de Números a generar: ", TOT)
    print()
    
    if N % 2 == 0:
        paridad = 2 
    
    for i in range (0,int(TOT)):

        X: int = pow((int(M)),2)
        cadena_X: str = str(X)
        if len(cadena_X[:-int(N)]) % 2 != 0:
            cadena_X = str(X*10) # Si es impar, multiplicamos x10 a X
        
        old_M = copy.copy(M)
        M = TakeCentralValues(cadena_X,paridad)

        mu: float = float("0."+M)
        MU_LIST.append(mu)
        ShowResults(i+1,old_M,cadena_X,mu)
        
        if int(M) == 0:
            print("M es 0.00, por lo tanto, no se puede continuar")
            print()
            break
    
    print(MU_LIST)