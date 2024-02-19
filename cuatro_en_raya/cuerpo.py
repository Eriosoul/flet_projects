import flet as ft
import numpy as np

N_Row = 6
N_Col = 7


class CuatroEnRaya(ft.Container):
    def __init__(self):
        super().__init__()
        self.tablero = np.zeros((N_Row, N_Col), dtype=int)
        self.player_colors = ["1", "2"]
        self.current_player = 0

    def on_button_click(self, event):
        button = event.control
        col = button.column_index  # Obtenemos el índice de la columna del botón

        if self.espacio_valido(self.tablero, col):
            # Obtener la fila correspondiente en el tablero
            fila = self.obtener_fila(self.tablero, col)
            # Asignar la ficha al tablero en la posición correcta
            fila[col] = self.current_player + 1

            button.text = self.player_colors[self.current_player]
            self.current_player = (self.current_player + 1) % 2

            # Imprimir el tablero actualizado
            self.imprimir_tablero(self.tablero)

            # Actualizar la página después de cada movimiento
            event.page.update()

            # Verificar si hay un ganador después de cada movimiento
            if self.ganador(self.tablero, self.current_player + 1):
                event.page.title = f"¡Jugador {self.current_player + 1} ha ganado!"
                print(event.page.title)

                event.page.update()
                self.show_winner_dialog(event.page, self.current_player + 1)
                self.reset_game(event.page)  # Restablecer el juego después de mostrar el diálogo del ganador
                return

                # Verificar si hay empate
            if self.empate(self.tablero):
                event.page.title = "¡Empate!"
                event.page.update()
                self.reset_game(event.page)  # Restablecer el juego después de un empate
                return

            # Cambiar el título para indicar el turno del siguiente jugador
            if self.current_player == 0:
                event.page.title = "Turno del Jugador 1"
            else:
                event.page.title = "Turno del Jugador 2"

    def reset_game(self, page):
        # Limpiar el tablero
        self.tablero = np.zeros((N_Row, N_Col), dtype=int)

        # Restablecer el jugador actual
        self.current_player = 0

        # Actualizar los botones del tablero en la página
        for row_idx, row in enumerate(page.controls):
            if isinstance(row, ft.Row):
                for col_idx, button in enumerate(row.controls):
                    if isinstance(button, ft.ElevatedButton):
                        button.text = ""  # Limpiar el texto del botón

        # Restablecer los marcadores de los jugadores
        for control in page.controls:
            if isinstance(control, ft.ElevatedButton) and control.height == 20:
                control.text = "0"  # Reiniciar el marcador a 0

    def espacio_valido(self, tablero, col):
        return tablero[N_Row - 1][col] == 0

    def obtener_fila(self, tablero, col):
        for fila in tablero:
            if fila[col] == 0:
                return fila

    def ganador(self, tablero, pieza):
        # Mirar movimientos horizontales
        for f in range(N_Row):
            for c in range(N_Col - 3):
                if tablero[f][c] == pieza and tablero[f][c + 1] == pieza and tablero[f][c + 2] == pieza and tablero[f][
                    c + 3] == pieza:
                    return True
        # Mirar movimientos verticales
        for c in range(N_Col):
            for f in range(N_Row - 3):
                if tablero[f][c] == pieza and tablero[f + 1][c] == pieza and tablero[f + 2][c] == pieza and \
                        tablero[f + 3][c] == pieza:
                    return True
        # Mirar movimientos en diagonal (pendiente positiva)
        for f in range(N_Row - 3):
            for c in range(N_Col - 3):
                if tablero[f][c] == pieza and tablero[f + 1][c + 1] == pieza and tablero[f + 2][c + 2] == pieza and \
                        tablero[f + 3][c + 3] == pieza:
                    return True
        # Mirar movimientos en diagonal (pendiente negativa)
        for f in range(N_Row - 3):
            for c in range(3, N_Col):
                if tablero[f][c] == pieza and tablero[f + 1][c - 1] == pieza and tablero[f + 2][c - 2] == pieza and \
                        tablero[f + 3][c - 3] == pieza:
                    return True
        return False

    def show_winner_dialog(self, page, winner):
        winner_text = f"¡Jugador {winner} ha ganado!"
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("¡Partida terminada!"),
            content=ft.Text(winner_text),
            actions=[
                ft.TextButton("OK", on_click=lambda e: None)
            ]
        )
        page.add(dialog)

    def empate(self, tablero):
        # Lógica para verificar si hay empate
        # Debes implementar esta función según tu lógica de juego
        return False

    def asignar_pieza(self, tablero, fila, col, pieza):
        tablero[fila][col] = pieza

    def imprimir_tablero(self, tablero):
        print(np.flipud(tablero))


def main(page: ft.Page):
    juego = CuatroEnRaya()
    row0 = ft.Row(
        controls=[
            ft.Text("Player 1"),
            ft.ElevatedButton(height=20, bgcolor="Red", text="0"),
            ft.ElevatedButton(text=" - "),
            ft.Text("Player 2"),
            ft.ElevatedButton(height=20, bgcolor="Yellow", text="0")
        ]
    )
    page.add(row0)

    for fila_idx, fila in enumerate(juego.tablero):
        row_controls = []
        for col_idx, _ in enumerate(fila):
            button = ft.ElevatedButton(text="")
            button.row_index = fila_idx  # Asignamos el índice de fila como atributo personalizado
            button.column_index = col_idx  # Asignamos el índice de columna como atributo personalizado
            button.on_click = juego.on_button_click  # Conectar el evento de clic con la lógica del juego
            row_controls.append(button)
        row = ft.Row(controls=row_controls)
        page.add(row)

    # Establecer el título inicial
    page.title = "Turno del Jugador 1"

    # Agregar el juego a la página
    page.add(juego)

ft.app(target=main)
