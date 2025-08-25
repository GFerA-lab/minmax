#import random

"""""
import time
import os

laberinto = [
    list("##############"),
    list("#    #      ##"), 
    list("#  ### ####  #"),
    list("#      ##### #"),
    list("#   ## #     #"),
    list("######## #####")
]

def verificar_colision(fila_personaje, col_personaje, fila_encontrar, col_encontrar):
    if fila_personaje == fila_encontrar and col_personaje == col_encontrar:
        return True
    return False

def calcular_distancia(tablero, fila_personaje, col_personaje, fila_encontrar, col_encontrar):    
    #return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    filas = len(tablero)
    columnas = len(tablero[0])
    contador = 0
    ban = False
    while True:
        
        while True:
            #derecha
            if col_personaje + 1 < columnas and tablero[fila_personaje][col_personaje +1] != "#":
                col_personaje += 1
                contador += 1
                if verificar_colision(fila_personaje, col_personaje, fila_encontrar, col_encontrar):
                    break
            else:
                ban = True
                break
        
        if ban: 
            break
        
        while True:
        #arriba
            if fila_personaje - 1 >= 0 and tablero[fila_personaje-1][col_personaje] != "#":
                fila_personaje -= 1
                contador += 1
                if verificar_colision(fila_personaje, col_personaje, fila_encontrar, col_encontrar):
                    break
            else:
                ban = True
                break
        
        if ban: 
            break
        
        while True:
            #izquierda
            if col_personaje - 1 < columnas and tablero[fila_personaje][col_personaje-1] != "#":
                col_personaje -=1
                contador +=1
                if verificar_colision(fila_personaje, col_personaje, fila_encontrar, col_encontrar):
                    break
            else:
                ban = True
                break
        
        if ban: 
            break
        
        while True:
        #abajo
            if fila_personaje + 1 >= 0 and tablero[fila_personaje][col_personaje-1] != "#":
                fila_personaje += 1
                contador += 1
                if verificar_colision(fila_personaje, col_personaje, fila_encontrar, col_encontrar):
                    break
            else:
                ban = True
                break
            
    return contador
"""

def buscar_objetivo(laberinto, x, y, x_obejtivo, y_objetivo, solucion, contador = 0):
    # Verifica si hemos llegado a la salida
    if x == len(laberinto) - 1 and y == len(laberinto[0]) - 1:
        solucion[x_obejtivo][y_objetivo] = 1
        contador += 1
        return True, contador

    # Verifica si la posición actual es válida
    if 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and (laberinto[x][y] == 0 or solucion[x][y] == 0):
        # Marca la posición como parte de la solución
        solucion[x][y] = 1
        contador += 1

        # Mover hacia abajo
        boolean, contador = buscar_objetivo(laberinto, x + 1, y, x_obejtivo, y_objetivo, solucion)
        if boolean:
            return True, contador

        # Mover hacia la derecha
        boolean, contador = buscar_objetivo(laberinto, x, y + 1, x_obejtivo, y_objetivo, solucion)
        if boolean:
            return True, contador

        # Mover hacia arriba
        boolean, contador = buscar_objetivo(laberinto, x - 1, y, x_obejtivo, y_objetivo, solucion)
        if boolean:
            return True, contador

        # Mover hacia la izquierda
        boolean, contador = buscar_objetivo(laberinto, x, y - 1, x_obejtivo, y_objetivo, solucion)
        if boolean:
            return True, contador

        # Si ninguna dirección funciona, retrocede
        solucion[x][y] = 0
        contador -= 1
        return False, contador

    return False, contador


"""
def buscar_objetivo(laberinto, x, y, solucion):
    # 1. Caso base: si (x,y) está fuera del laberinto
    if x < 0 or x >= len(laberinto) or y < 0 or y >= len(laberinto[0]):
        return False

    # 2. Caso base: si llegamos a la meta
    if laberinto[x][y] == "G":  # ejemplo
        solucion[x][y] = 1
        return True

    # 3. Si ya pasamos por aquí o es un muro
    if laberinto[x][y] == 1 or solucion[x][y] == 1:
        return False

    # Marcar como parte de la solución
    solucion[x][y] = 1

    # Explorar vecinos
    if (buscar_objetivo(laberinto, x+1, y, solucion) or
        buscar_objetivo(laberinto, x-1, y, solucion) or
        buscar_objetivo(laberinto, x, y+1, solucion) or
        buscar_objetivo(laberinto, x, y-1, solucion)):
        return True

    # Si no sirve este camino, retroceder
    solucion[x][y] = 0
    return False

"""
def get_valid_moves(tablero, fila, col):
    moves = []
    filas = len(tablero)
    columnas = len(tablero[0])

    if fila + 1 < filas and tablero[fila+1][col] != "#":
        moves.append((fila+1, col))
    if fila - 1 >= 0 and tablero[fila-1][col] != "#":
        moves.append((fila-1, col))
    if col + 1 < columnas and tablero[fila][col+1] != "#":
        moves.append((fila, col+1))
    if col - 1 >= 0 and tablero[fila][col-1] != "#":
        moves.append((fila, col-1))

    return moves

def movimiento(laberinto, fila, col, pasos, gato, otro_fila, otro_col):
    if pasos == 0:
        solucion = [[0 for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
        boolean, contador = buscar_objetivo(laberinto, fila, col, otro_fila, otro_col, solucion)
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

"""
def movimiento_raton(laberinto, raton_fila, raton_col, gato_fila, gato_col):
    moves = get_valid_moves(laberinto, raton_fila, raton_col)
    max_dist = -1
    mejor_move = (raton_fila, raton_col)
    for fila, col in moves:
        dist = calcular_distancia((fila, col), (gato_fila, gato_col))
        if dist > max_dist:
            max_dist = dist
            mejor_move = (fila, col)
    return mejor_move

def movimiento_gato(laberinto, gato_fila, gato_col, raton_fila, raton_col):
    moves = get_valid_moves(laberinto, gato_fila, gato_col)
    moves_raton = get_valid_moves(laberinto, raton_fila, raton_col)
    min_dist = float('inf')
    mejor_move = (gato_fila, gato_col)
    for fila, col in moves:
        for fila2, col2 in moves_raton:
            dist = calcular_distancia((fila, col), (fila2, col2))
            if dist < min_dist:
                min_dist = dist
                mejor_move = (fila, col)
    return mejor_move

def main():
    raton_fila, raton_col = 1, 1
    gato_fila, gato_columna = 5, 8

    laberinto[raton_fila][raton_col] = "R"
    laberinto[gato_fila][gato_columna] = "G"

    while True:
        mostrar()
        time.sleep(1)

        # Verificar colisión
        laberinto[raton_fila][raton_col] = " "
        laberinto[gato_fila][gato_columna] = " "
        dist_gato, mov_gato = movimiento(laberinto, gato_fila, gato_columna, 10, True, raton_fila, raton_col)
        gato_fila, gato_columna = mov_gato

        dist_raton, mov_raton = movimiento(laberinto, raton_fila, raton_col, 10, False, gato_fila, gato_columna)
        raton_fila, raton_col = mov_raton

        gato_fila, gato_columna = mov_gato
        raton_fila, raton_col = mov_raton

        laberinto[raton_fila][raton_col] = "R"
        laberinto[gato_fila][gato_columna] = "G"

        if raton_fila == gato_fila and raton_col == gato_columna:
            mostrar()
            print("¡El gato atrapó al ratón!")

            break


if __name__ == "__main__":
    main()

"""
def mostrar(laberinto):
    print("\n".join("".join(fila) for fila in laberinto))
    print()

def main():
    laberinto = [
        [0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    raton_fila, raton_col = 0, 0
    gato_fila, gato_columna = 3, 4

    laberinto[raton_fila][raton_col] = "R"
    laberinto[gato_fila][gato_columna] = "G"

    mostrar(laberinto)

    # if buscar_objetivo(laberinto, 0, 0, solucion):
    #     for fila in solucion:
    #         print(fila)
    # else:
    #     print("No hay solución para el laberinto.")

if __name__ == "__main__":
    main()
