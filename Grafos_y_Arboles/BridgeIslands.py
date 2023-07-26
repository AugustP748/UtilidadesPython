class Bridge:
  def __init__(self):
    self.ArrayLimits = []
    self.distances = []
    #self.distance:int = 0
    
  def shortestBridge(self, A):
    # Tu código aquí 👇
    self.searchLimit(A)
    
    return self.CalculateDistance()

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
        #A[row][col]=3
        break
        
    return
      
  def CalculateDistance(self):
    for i in self.ArrayLimits:
      minX,minY=self.MinEjeYValue(i)
      self.distances.append(minX)
      self.distances.append(minY)
    return self.distances

  def MinEjeYValue(self,element):
    menorY:int=10
    menorX:int=10
    for j in self.ArrayLimits:
      if element[0] == j[0]:
        if abs(element[1] - j[1]) < menorY:
          menorY = abs(element[1] - j[1])

      if element[1] == j[1]:
        if abs(element[0] - j[0]) < menorX:
          menorX = abs(element[0] - j[0])
    return menorX,menorY




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
  print(response) #2

  #for i in mapa:
    #print(i)