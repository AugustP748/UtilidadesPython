def dfs(grid, row, col):
    # Verificar los límites de la matriz y si la celda actual es una isla
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
        return
    
    # Marcar la celda actual como visitada
    grid[row][col] = '#'
    
    # Explorar las celdas vecinas en todas las direcciones (arriba, abajo, izquierda, derecha)
    dfs(grid, row-1, col)  # Arriba
    dfs(grid, row+1, col)  # Abajo
    dfs(grid, row, col-1)  # Izquierda
    dfs(grid, row, col+1)  # Derecha


def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    num_islands = 0
    rows, cols = len(grid), len(grid[0])
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                num_islands += 1
                dfs(grid, row, col)
    
    return num_islands

if __name__ == '__main__':
    grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
    ]
    mapa = [
  [1,1,1,1,1],
  [1,0,0,0,1],
  [1,0,1,0,1],
  [1,0,0,0,1],
  [1,1,1,1,1],
]
    print(numIslands(mapa))