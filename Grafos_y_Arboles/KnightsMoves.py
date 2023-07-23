from collections import deque

def minKnightMoves(x, y, target_x, target_y):
    # Movimientos posibles del caballo en el tablero de ajedrez
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    
    # Función para verificar si una posición está dentro del tablero
    def is_inside_board(x, y):
        return abs(x) <= 300 and abs(y) <= 300
    
    # Inicializar la cola para el BFS
    queue = deque([(x, y, 0)])
    visited = set([(x, y)])
    
    while queue:
        curr_x, curr_y, steps = queue.popleft()
        if curr_x == target_x and curr_y == target_y:
            return steps
        
        for dx, dy in moves:
            next_x, next_y = curr_x + dx, curr_y + dy
            
            # Verificar si la siguiente posición está dentro del tablero y no ha sido visitada
            if (next_x, next_y) not in visited and is_inside_board(next_x, next_y):
                visited.add((next_x, next_y))
                queue.append((next_x, next_y, steps + 1))
    
    return -1  # Si no se puede alcanzar la posición objetivo, devuelve -1

# Ejemplo de uso:
initial_x, initial_y = 0, 0
target_x, target_y = 5, 5
print(minKnightMoves(initial_x, initial_y, target_x, target_y))  # Salida: 1
