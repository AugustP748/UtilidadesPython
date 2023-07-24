def verifyCultivo(cultivo):
    if any(1 in sublist for sublist in cultivo):
        return False
    else:
        return True

def UpdateCultivo(cultivo,contamination):
    for row in range(len(cultivo)):
            for col in range(len(cultivo[0])):
                if (row,col) in contamination:
                    cultivo[row][col] = 2
    return  

def orangesRotting(cultivo):
    visited = set()
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    contamination = []
    counter:int=0

    while counter < 4:
        for row in range(len(cultivo)):
            for col in range(len(cultivo[0])):
                #print(cultivo[row][col])
                if cultivo[row][col] == 2 and (row,col) not in visited:
                    visited.add((row,col))

                    for direction in directions:
                        new_row=row+direction[0]
                        new_col=col+direction[1]
                        if new_row < 0 or new_col < 0 or new_row >= len(cultivo) or new_col >= len(cultivo[0]):
                            continue
                        elif cultivo[new_row][new_col] == 1 and (new_row,new_col) not in contamination:
                            contamination.append((new_row,new_col))
                        
                        new_row = 0
                        new_col = 0
        
        counter+=1 
        UpdateCultivo(cultivo,contamination)
        contamination = []
        if verifyCultivo(cultivo):
            return counter
                  
    

if __name__ == '__main__':
        # Ejemplo de matriz de cultivo de naranjas


