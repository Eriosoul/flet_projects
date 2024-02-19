import numpy as np

N_Row = 6
N_Cols = 7
def create_tabler():
    # es lo mismo que esto == self.tablero = [["" for _ in range(7)] for _ in range(6)]
    tabler = np.zeros((N_Row, N_Cols))
    return tabler
def expacio_valido(tablero, col):
    return tablero[N_Row - 1][col] == 0

def siguente_fila_vacia(tablero, col):
    for f in range(N_Row):
        if tablero[f][col] == 0:
            return f

def asignar_pieza(tablero, fila, col, pieza):
    tablero[fila][col] = pieza

def imprimir_tablero(tablero):
    print(np.flipud(tablero))

def ganador(tablero, pieza):
    # mirar movimientos horizontal
    for c in range(N_Cols-3):
        for f in range(N_Row):
            if tablero[f][c] == pieza and tablero[f][c+1] == pieza and tablero[f][c+2] == \
                    pieza and tablero[f][c+3] == pieza:
                return True
    # mirar movimientos Vertical
    for c in range(N_Cols):
        for f in range(N_Row - 3):
            if tablero[f][c] == pieza and tablero[f+ 1][c] == pieza and tablero[f + 2][c] == \
                    pieza and tablero[f+ 3][c] == pieza:
                return True
    # mirar movimientos pendiente positiva
    for c in range(N_Cols - 3):
        for f in range(N_Row - 3):
            if tablero[f][c] == pieza and tablero[f + 1][c + 1] == pieza and tablero[f + 2][c + 2] == \
                    pieza and tablero[f + 3][c + 3] == pieza:
                return True
    # mirar movimientos pendiente negativa
    for c in range(N_Cols):
        for f in range(3, N_Row):
            if tablero[f][c] == pieza and tablero[f - 1][c + 1] == pieza and tablero[f - 2][c + 2] == \
                    pieza and tablero[f - 3][c + 3] == pieza:
                return True

tablero = create_tabler()
imprimir_tablero(tablero)

game_over, turn = False, 0


while not game_over:
    # Solicitar entrada jugador 1
    if turn == 0:
        col = int(input("Jugador 1: "))
        if expacio_valido(tablero, col):
            fila = siguente_fila_vacia(tablero, col)
            asignar_pieza(tablero, fila, col, 1)
            imprimir_tablero(tablero)
            if ganador(tablero, 1):
                print("Gano el jugador 1")
                imprimir_tablero(tablero)
                game_over = True
    else:
        col = int(input("Jugador 2: "))
        if expacio_valido(tablero, col):
            fila = siguente_fila_vacia(tablero, col)
            asignar_pieza(tablero, fila, col, 2)
            imprimir_tablero(tablero)
            if ganador(tablero, 2):
                print("Gano el jugador 2")
                imprimir_tablero(tablero)
                game_over = True
    # incrementamos el turn de 0 a 1
    turn += 1
    # hacemos modulo de turn y se vuelve 0
    turn = turn % 2