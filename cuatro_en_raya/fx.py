import flet as ft

def main(page: ft.Page):
    def on_button_click(event):
        event.target.bgcolor = "blue"  # Cambiar el color de fondo del botón al hacer clic

    page.title = "Cuatro en raya"
    player1 = ft.Text("Jugador 1")
    player2 = ft.Text("Jugador 2")

    # Crear una fila de botones elevados representando los cuadrados
    row0 = ft.Row(
        controls=[
            player1,
            ft.ElevatedButton(height=20, bgcolor="red"),
            ft.ElevatedButton(text="", on_click=on_button_click),
            player2,
            ft.ElevatedButton(height=20, bgcolor="yellow")
        ]
    )
    page.add(row0)

    # Agrega más filas de botones aquí...

ft.app(target=main)