class Bridge:
  def shortestBridge(self, A):
    # Tu código aquí 👇
    return len(A)

def dfs(mapa, row, col):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    # Verificar los límites de la matriz y si la celda actual es una isla
    if row < 0 or col < 0 or row >= len(mapa) or col >= len(mapa[0]) or mapa[row][col] != 1:
        return
    
    # Marcar la celda actual como visitada
    mapa[row][col] = '#'
    
    # Explorar las celdas vecinas en todas las direcciones (arriba, abajo, izquierda, derecha)
    dfs(mapa, row-1, col)  # Arriba
    dfs(mapa, row+1, col)  # Abajo
    dfs(mapa, row, col-1)  # Izquierda
    dfs(mapa, row, col+1)  # Derecha


def numIslands(mapa):
    if not mapa or not mapa[0]:
        return 0
    
    num_islands = 0
    rows, cols = len(mapa), len(mapa[0])
    
    for row in range(rows):
        for col in range(cols):
            if mapa[row][col] == 1:
                num_islands += 1
                dfs(mapa, row, col)
    
    return num_islands


mapa = [
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,1,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1],
]
response = Bridge().shortestBridge(mapa)
print(response) #1

mapa = [
  [1,1,0,0,1],
  [1,1,0,0,1],
  [1,0,0,0,1],
  [1,0,0,0,1],
  [1,0,0,1,1],
]
response = Bridge().shortestBridge(mapa)
print(response) #2