import flet as ft # pip install flet or pip3 install flet
play = 0
button_states = ["yellow", "red"]

def main(page: ft.Page):
    page.add(ft.Text(value="Hello world"))
    page.title = "Cuatron en raya"
    player1 = ft.Text("Jugador 1")
    player2 = ft.Text("Jugador 2")
      # Inicializa play fuera de la función

    def on_button_click(event):
        global play
        # Obtener el color actual del botón
        current_color = event.control.bgcolor
        # Si el botón es rojo, no se puede cambiar a amarillo
        if current_color == "red":
            return
        # Alterna los colores en cada clic
        play = (play + 1) % 2
        event.control.bgcolor = button_states[play]
        page.update()


    # Crear una fila de botones elevados representando los cuadrados
    row0 = ft.Row(
        controls=[
            player1,
            ft.ElevatedButton(height=20, bgcolor="Red"),
            ft.ElevatedButton(text=" - "),
            player2,
            ft.ElevatedButton(height=20, bgcolor="yellow")
        ]
    )
    page.add(row0)


    row1 = ft.Row(
        controls=[
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
        ]
    )
    page.add(row1)

    row2 = ft.Row(
        controls=[
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
        ]
    )
    page.add(row2)

    row3 = ft.Row(
        controls=[
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
        ]
    )
    page.add(row3)

    row4 = ft.Row(
        controls=[
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
        ]
    )
    page.add(row4)

    row5 = ft.Row(
        controls=[
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
        ]
    )
    page.add(row5)

    row6 = ft.Row(
        controls=[
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
            ft.ElevatedButton(text="", on_click=on_button_click),
        ]
    )
    page.add(row6)
    row_list = [row1, row2, row3, row4, row5, row6]
    print(row_list)


ft.app(target=main)

# class CuatroEnRaya:
#     def __init__(self):
#         self.tablero = [["" for _ in range(7)] for _ in range(6)]
#         print(self.tablero)
#
#
# if __name__ == '__main__':
#     CuatroEnRaya()