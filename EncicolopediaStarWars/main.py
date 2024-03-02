import flet as ft
from templates.get_data import TheStarWarsAPIData

def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text("Introduce el nombre del pesonaje:"),
    )
    snack_bar = ft.SnackBar(ft.Text("", color=ft.colors.WHITE), bgcolor=ft.colors.WHITE)
    page.add(snack_bar)

    def text_changed(e):
        char_name = e.control.value  # Obtener el valor del TextField
        print("El nombre es:", char_name)
        try:
            t = TheStarWarsAPIData()  # Crear una instancia de TheStarWarsAPIData
            t.check_status()  # Llamar al método para obtener los datos
            data_star_wars = t.get_data_star_wars()  # Obtener los datos del personaje
            # Aquí puedes usar los datos obtenidos como desees
            button.update()
            print(data_star_wars)
        except Exception as ex:
            button.text = 'Download Video!'
            image.src = ''
            image.update()

            snack_bar.text = "Personaje no encontrado"
            snack_bar.open = True
            snack_bar.update()
            print('Not a Link', ex)

    txt = ft.TextField(hint_text='Escribe el nombre de tu pesonaje de star wars: ', on_change=text_changed)
    image = ft.Image(src='')
    button = ft.ElevatedButton('Buscar personaje!', )

    page.add(
        image,
        txt,
        button
    )

if __name__ == '__main__':
    ft.app(target=main)
