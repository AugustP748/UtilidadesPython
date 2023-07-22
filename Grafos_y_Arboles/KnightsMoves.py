import numpy as np

def verifyValue(tablero,ejex,ejey) -> bool:
    if ejex < 0 or ejey < 0 or ejex > len(tablero) or ejey > len(tablero):
        return False
    else:
        return True

def bfs():
    ...

def movimientos(tablero,ejex,ejey):
    counter:int = 0
    



if __name__ == '__main__':
    tablero = np.zeros((8,8))
    ejex:int = 4
    ejey:int = 7
    tablero[ejey,ejex] = 1 #posición del caballo
    ObjetivoX = 0
    ObjetivoY = 1
    tablero[ObjetivoY,ObjetivoX] = 2 #objetivo
    
    movimientos(tablero,ejex-2,ejey-1)

    #movimientos(tablero,ejex-2,ejey-1)
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
    
    print(tablero)