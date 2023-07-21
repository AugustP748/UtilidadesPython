def dfs(matriz,row,col):
    if  row < 0 or col < 0 or row >= len(matriz) or col >= len(matriz[0]) or matriz[row][col] != '1':
        return
    matriz[row][col] = '#'
    
    dfs(matriz,row+1,col)
    dfs(matriz,row-1,col)
    dfs(matriz,row,col+1)
    dfs(matriz,row,col+1)
    
    

def CantidadIslas(matriz):
    counter:int = 0
    #filas y columnas
    for row in range(len(matriz)):
        for col in range(len(matriz[0])):
            #print(matriz[row][col])
            if matriz[row][col] == '1':
                dfs(matriz,row,col)
                counter+=1
    print(matriz)
    return counter
    



if __name__ == '__main__':
    grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
    ]
    
    print("Cantidad de islas: ",CantidadIslas(grid))
    
    
"""    mapa = [
["1","1","0","0","1"],
["1","1","1","0","1"],
["0","0","1","0","1"],
["0","0","0","0","1"],
["0","0","0","0","1"],
]
    
    mapa = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"],
]"""
    