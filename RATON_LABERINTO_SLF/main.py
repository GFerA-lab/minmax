import copy

def buscar_objetivo(laberinto, x, y, x_obejtivo, y_objetivo, solucion, contador):
    if x == x_obejtivo and y == y_objetivo:
        solucion[x][y] = 1
        contador += 1
        return True, contador

    if 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 0 and solucion[x][y] == 0:
        solucion[x][y] = 1
        contador += 1

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

def get_valid_moves(tablero, fila, col):
    moves = []
    filas = len(tablero)
    columnas = len(tablero[0])

    if fila + 1 < filas and tablero[fila+1][col] != 1:
        moves.append((fila+1, col))

    if fila - 1 >= 0 and tablero[fila-1][col] != 1:
        moves.append((fila-1, col))

    if col + 1 < columnas and tablero[fila][col+1] != 1:
        moves.append((fila, col+1))

    if col - 1 >= 0 and tablero[fila][col-1] != 1:
        moves.append((fila, col-1))

    return moves

def movimiento(laberinto, fila, col, pasos, gato, otro_fila, otro_col):
    if pasos == 0:
        solucion = [[0 for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
        contador = 0
        boolean, contador = buscar_objetivo(laberinto, fila, col, otro_fila, otro_col, solucion, contador)
        return contador, None

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

def mostrar(laberinto):
    simbolos = {0: "⬜", 1: "🟩", 2: "🐭", 3: "🐱", 4: "🚪", 5: "😿", 6:"😼"}

    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            print(simbolos[laberinto[i][j]], end=" ")
        print()
    print()

def validar_direccion(tablero, direccion, fila_jugador, col_jugador):
    
    movimientos = {
        "W": (-1, 0),  # arriba
        "S": (1, 0),   # abajo
        "A": (0, -1),  # izquierda
        "D": (0, 1)    # derecha
    }
    
    direccion = direccion.upper()
    if direccion in movimientos:
        x_aux, y_aux = movimientos[direccion]
        moves = get_valid_moves(tablero, fila_jugador, col_jugador)

        if (fila_jugador + x_aux, col_jugador + y_aux) in moves:
            return True, (fila_jugador + x_aux, col_jugador + y_aux)
    
    return False, (fila_jugador, col_jugador)

def main():
    laberinto = [
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0]
    ]

    aux_laberinto = copy.deepcopy(laberinto)

    raton_fila, raton_col = 0, 0
    gato_fila, gato_columna = 3, 4

    laberinto[raton_fila][raton_col] = 2
    laberinto[gato_fila][gato_columna] = 3

    fila_salida = 4
    col_salida = 4
    laberinto[fila_salida][col_salida] = 4

    mostrar(laberinto)

    while True :

        direccion = input("Ingrese la direccion W/S/D/A: ")

        if direccion.isalpha() and len(direccion) == 1:

            validacion, mov_raton = validar_direccion(aux_laberinto, direccion, raton_fila, raton_col)

            if validacion:
                laberinto[raton_fila][raton_col] = 0
                raton_fila, raton_col = mov_raton
                laberinto[raton_fila][raton_col] = 2
            else:
                print("NO puedes ir hacia allí")
        else:
            print("Ingrese una direccion valida")

        if raton_fila == fila_salida and raton_col == col_salida:
            print("El raton llego a la Salida")
            laberinto[raton_fila][raton_col] = 4
            laberinto[gato_fila][gato_columna] = 5
            break
        eval1, mov_gato = movimiento(aux_laberinto, gato_fila, gato_columna, 3, True, raton_fila, raton_col)

        laberinto[gato_fila][gato_columna] = 0
        laberinto[fila_salida][col_salida] = 4
        gato_fila, gato_columna = mov_gato
        laberinto[gato_fila][gato_columna] = 3

        if gato_fila == raton_fila and gato_columna == raton_col:
            laberinto[raton_fila][raton_col] = 0
            laberinto[gato_fila][gato_columna] = 6
            print("El gato atrapo al raton")
            break

        mostrar(laberinto)
    
    mostrar(laberinto)

if __name__ == "__main__":
    main()
