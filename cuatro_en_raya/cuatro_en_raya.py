import flet as ft
import numpy as np

N_Row = 6
N_Col = 7

def main(page: ft.Page):
    t = np.zeros((N_Row, N_Col))
    print(t)

    tablero = []
    for _ in range(N_Row):
        row = []
        for _ in range(N_Col):
            row.append(ft.ElevatedButton(text=""))
        tablero.append(row)

    for row in tablero:
        print(row)

if __name__ == '__main__':
    ft.app(target=main)

# class TableroDeJuego(ft.Container):
#     def create_tablero(self):
#         self.tablero = np.zeros((N_Row, N_Col))
#         return self.tablero
#
# if __name__ == '__main__':
#     tablero = TableroDeJuego()  # Instanciar la clase TableroDeJuego
#     print(tablero)
#     ft.app(target=tablero.create_tablero)
