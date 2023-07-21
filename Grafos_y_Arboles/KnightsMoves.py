import numpy as np

def movimientos(tablero,ejex,ejey):
    
    
    tablero[ejey-1][ejex-2] = 4
    tablero[ejey-1][ejex+2] = 4
    tablero[ejey-2][ejex-1] = 4
    tablero[ejey-2][ejex+1] = 4
    
    try:
        tablero[ejey+1][ejex-2] = 4
        tablero[ejey+1][ejex+2] = 4
        tablero[ejey+2][ejex-1] = 4
        tablero[ejey+2][ejex+1] = 4
        
    except:
        ...



if __name__ == '__main__':
    tablero = np.zeros((8,8))
    ejex:int = 4
    ejey: int = 7
    tablero[ejey,ejex] = 1 #posición del caballo
    tablero[1,2] = 2 #objetivo
    
    movimientos(tablero,ejex,ejey)
    print(tablero)