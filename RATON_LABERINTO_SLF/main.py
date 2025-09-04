import copy

def buscar_objetivo(laberinto, x, y, x_obejtivo, y_objetivo, solucion, contador):

    #Verificar si encontramos al objetivo
    if x == x_obejtivo and y == y_objetivo:
        solucion[x][y] = 1
        contador += 1
        return True, contador

    # Verificar si la posicion es valida
    if 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 0 and solucion[x][y] == 0:
        solucion[x][y] = 1
        contador += 1

        # Si el objetivo se encuentra hacia la derecha ir primero hacia allí
        if y <= y_objetivo:

            # Mover hacia abajo
            boolean, contador = buscar_objetivo(laberinto, x + 1, y, x_obejtivo, y_objetivo, solucion, contador)
            if boolean:
                return True, contador

            # Mover hacia la derecha
            boolean, contador = buscar_objetivo(laberinto, x, y + 1, x_obejtivo, y_objetivo, solucion, contador)
            if boolean:
                return True, contador
            
            # Mover hacia arriba
            boolean, contador = buscar_objetivo(laberinto, x - 1, y, x_obejtivo, y_objetivo, solucion, contador)
            if boolean:
                return True, contador
            
            # Mover hacia la izquierda
            boolean, contador = buscar_objetivo(laberinto, x, y - 1, x_obejtivo, y_objetivo, solucion, contador)
            if boolean:
                return True, contador

            # Si ninguna dirección funciona, retrocede
            solucion[x][y] = 0
            contador -= 1
            return False, contador
        
        # Si el objetivo se encuentra hacia la izquierda ir primero hacia allí
        else:
            
            # Mover hacia arriba
            boolean, contador = buscar_objetivo(laberinto, x - 1, y, x_obejtivo, y_objetivo, solucion, contador)
            if boolean:
                return True, contador
            
            # Mover hacia la izquierda
            boolean, contador = buscar_objetivo(laberinto, x, y - 1, x_obejtivo, y_objetivo, solucion, contador)
            if boolean:
                return True, contador

            # Mover hacia abajo
            boolean, contador = buscar_objetivo(laberinto, x + 1, y, x_obejtivo, y_objetivo, solucion, contador)
            if boolean:
                return True, contador

            # Mover hacia la derecha
            boolean, contador = buscar_objetivo(laberinto, x, y + 1, x_obejtivo, y_objetivo, solucion, contador)
            if boolean:
                return True, contador

            # Si ninguna dirección funciona, retrocede
            solucion[x][y] = 0
            contador -= 1
            return False, contador

    return False, contador

# Verificar los movimeintos que el personaje puede hacer
def get_valid_moves(tablero, fila, col):
    moves = []
    filas = len(tablero)
    columnas = len(tablero[0])

    # Verificar abajo
    if fila + 1 < filas and tablero[fila+1][col] != 1:
        moves.append((fila+1, col))

    # Verificar arriba
    if fila - 1 >= 0 and tablero[fila-1][col] != 1:
        moves.append((fila-1, col))

    # Verificar derecha
    if col + 1 < columnas and tablero[fila][col+1] != 1:
        moves.append((fila, col+1))

    # Verificar izquierda
    if col - 1 >= 0 and tablero[fila][col-1] != 1:
        moves.append((fila, col-1))

    return moves

# Minimax
def movimiento(laberinto, fila, col, pasos, gato, otro_fila, otro_col):
    #Verificar si se llego a la profundidad deseada
    if pasos == 0:
        solucion = [[0 for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))] # matriz para guardar camino recorrido
        contador = 0 # Contador de pasos

        # Buscar que tan lejos se encuentra el personaje de su objetivo
        boolean, contador = buscar_objetivo(laberinto, fila, col, otro_fila, otro_col, solucion, contador)
        return contador, None

    # Gato intenta minimizar la distancia con el raton
    if gato:
        minEval = float('inf')
        best_move = None
        for move in get_valid_moves(laberinto, fila, col):
            temp_fila, temp_col = move
            evaluation = movimiento(laberinto, otro_fila, otro_col, pasos-1, False, temp_fila, temp_col)[0]
            if evaluation < minEval:
                minEval = evaluation
                best_move = move
        return minEval, best_move
    
    # Raton busca maximizar su distancia del gato
    else:
        maxEval = float('-inf')
        best_move = None
        for move in get_valid_moves(laberinto, fila, col):
            temp_fila, temp_col = move
            evaluation = movimiento(laberinto, otro_fila, otro_col, pasos-1, True, temp_fila, temp_col)[0]
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = move
        return maxEval, best_move

# Imprimir laberinto con emonjis
def mostrar(laberinto):
    simbolos = {0: "⬜", 1: "🟩", 2: "🐭", 3: "🐱", 4: "🚪", 5: "😿", 6:"😼"}

    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            print(simbolos[laberinto[i][j]], end=" ")
        print()
    print()

# Validar movineto ingresado
def validar_direccion(tablero, direccion, fila_jugador, col_jugador):
    
    movimientos = {
        "W": (-1, 0),  # arriba
        "S": (1, 0),   # abajo
        "A": (0, -1),  # izquierda
        "D": (0, 1)    # derecha
    }
    
    direccion = direccion.upper()

    # Verificar letra ingresada
    if direccion in movimientos:
        x_aux, y_aux = movimientos[direccion]
        # Verificar movimeintos posibles
        moves = get_valid_moves(tablero, fila_jugador, col_jugador)

        # Si el movimiento es posible retornar nueva posicion
        if (fila_jugador + x_aux, col_jugador + y_aux) in moves:
            return True, (fila_jugador + x_aux, col_jugador + y_aux)
    
    #Si la letra no es correcta o no es posible el movimiento retornar falso y la posicion original
    return False, (fila_jugador, col_jugador)

def main():
    # Definir laberinto
    laberinto = [
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0]
    ]

    # Copia del laberinto para validaciones
    aux_laberinto = copy.deepcopy(laberinto)

    # Posicion de personjes
    raton_fila, raton_col = 0, 0
    gato_fila, gato_columna = 3, 4

    # Colocar personajes en el laberinto
    laberinto[raton_fila][raton_col] = 2
    laberinto[gato_fila][gato_columna] = 3

    # Posicion Salida
    fila_salida = 4
    col_salida = 4
    laberinto[fila_salida][col_salida] = 4

    mostrar(laberinto)

    while True :

        direccion = input("Ingrese la direccion W/S/D/A: ")

        # Verificar que lo ingresado sea una letra y de un digito
        if direccion.isalpha() and len(direccion) == 1:
            
            #Retorna True si se puede el movimiento y false si no
            validacion, mov_raton = validar_direccion(aux_laberinto, direccion, raton_fila, raton_col)

            # Si True se actualiza la posicion del raton
            if validacion:
                laberinto[raton_fila][raton_col] = 0
                raton_fila, raton_col = mov_raton
                laberinto[raton_fila][raton_col] = 2
            else:
                print("NO puedes ir hacia allí")
        else:
            print("Ingrese una direccion valida")
        
        # Verificar si el gato atrapo al raton
        if gato_fila == raton_fila and gato_columna == raton_col:
            laberinto[raton_fila][raton_col] = 0
            laberinto[gato_fila][gato_columna] = 6
            print("El gato atrapo al raton")
            break
        
        # Verificar si el raton llego a la salida
        if raton_fila == fila_salida and raton_col == col_salida:
            print("El raton llego a la Salida")
            laberinto[raton_fila][raton_col] = 4
            laberinto[gato_fila][gato_columna] = 5
            break
        
        # Encontrar movimiento para el gato
        eval1, mov_gato = movimiento(aux_laberinto, gato_fila, gato_columna, 3, True, raton_fila, raton_col)

        # Actualizar posicion del gato
        laberinto[gato_fila][gato_columna] = 0
        laberinto[fila_salida][col_salida] = 4 # Actualizar salida por si el gato estaba sobre ella
        gato_fila, gato_columna = mov_gato
        laberinto[gato_fila][gato_columna] = 3

        # Verificar si el gato atrapo al raton
        if gato_fila == raton_fila and gato_columna == raton_col:
            laberinto[raton_fila][raton_col] = 0
            laberinto[gato_fila][gato_columna] = 6
            print("El gato atrapo al raton")
            break
        
        # Imprimir laberinto
        mostrar(laberinto)
    
    # Imprimir laberinto
    mostrar(laberinto)

if __name__ == "__main__":
    main()
