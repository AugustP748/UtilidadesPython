def verifyCultivo(cultivo):
    if 1 in cultivo:
        return True
    else:
        return False

def orangesRotting(cultivo):
    cola = ()
    visited = set()
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    counter:int=0

    while counter < 3:
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
                        elif cultivo[new_row][new_col] == 1:
                            #visited.add((new_row,new_col))
                            cultivo[new_row][new_col] = 2
                        
                        new_row = 0
                        new_col = 0
        
        counter+=1
        if verifyCultivo(cultivo):
            return counter
                  
    

if __name__ == '__main__':
        # Ejemplo de matriz de cultivo de naranjas
    cultivo = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    days = orangesRotting(cultivo)
    for i in cultivo:
        print(i)
    
    print("day: ", days)
    #for j in v:
    #    print(j)

    #print(len(cultivo))
