class Bridge:
  def __init__(self):
    self.ArrayLimits = []
    self.visited = []
    self.distance:int = 0
    
  def shortestBridge(self, A):
    # Tu código aquí 👇
    rows, cols = len(A), len(A[0])
    
    """for row in range(rows):
        for col in range(cols):
            if A[row][col] == 1:
                self.dfs(A, row, col)"""
    self.searchLimit(A)
    self.CalculateDistance()
    return self.ArrayLimits

  def dfs(self,grid, row, col):
      # Verificar los límites de la matriz y si la celda actual es una isla
      if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
          return
      
      # Marcar la celda actual como visitada
      grid[row][col] = '#'
      
      # Explorar las celdas vecinas en todas las direcciones (arriba, abajo, izquierda, derecha)
      self.dfs(grid, row-1, col)  # Arriba
      self.dfs(grid, row+1, col)  # Abajo
      self.dfs(grid, row, col-1)  # Izquierda
      self.dfs(grid, row, col+1)  # Derecha

  def searchLimit(self,A):
    for row in range(len(A)):
      for col in range(len(A[0])):
        if A[row][col] == 1:
          self.limits(A,row,col)
          
  
  def limits(self,A,row,col):
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    for direct in directions:
      new_row = row+direct[0]
      new_col = col+direct[1]
      if new_row < 0 or new_col < 0 or new_row >= len(A) or new_col >= len(A[0]):
        continue
      elif A[new_row][new_col] == 0:
        self.ArrayLimits.append((row,col))
        A[row][col]=3
        break
        
    return
      
  def CalculateDistance(self):
    for i in self.ArrayLimits:
      
      
      print(i)


if __name__ == '__main__':

  mapa = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1],
  ]
  #response = Bridge().shortestBridge(mapa)
  #print(response) #1

  mapa = [
    [1,1,0,0,1],
    [1,1,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,1,1],
  ]
  response = Bridge().shortestBridge(mapa)
  #print(response) #2

  for i in mapa:
    print(i)