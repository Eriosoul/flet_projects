import flet as ft
from get_data import TheStarWarsAPIData
from lib.star_wars import DataStarWars


def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text("Introduce el nombre del personaje:"),
    )
    snack_bar = ft.SnackBar(ft.Text("", color=ft.colors.WHITE), bgcolor=ft.colors.WHITE)
    page.add(snack_bar)

    def button_clicked(e):
        char_name: str = txt.value.strip()  # Eliminar espacios en blanco adicionales
        print("El nombre es:", char_name)
        try:
            t: TheStarWarsAPIData = TheStarWarsAPIData()
            data_star_wars = t.get_data_star_wars(char_name)  # Pasar el nombre del personaje
            if data_star_wars:
                # Actualizar la interfaz de usuario con los datos del personaje
                snack_bar.text = f"Datos del personaje: {data_star_wars.name}"
                snack_bar.open = True
                snack_bar.update()
                # También puedes mostrar otros datos del personaje según sea necesario

            else:
                print("Personaje no encontrado")
        except Exception as ex:
            # Manejar cualquier error que ocurra durante la búsqueda
            snack_bar.text = "Error al buscar el personaje"
            snack_bar.open = True
            snack_bar.update()
            print('Error:', ex)

    txt = ft.TextField(hint_text='Escribe el nombre de tu personaje de Star Wars: ')
    button = ft.ElevatedButton('Buscar personaje!', on_click=button_clicked)

    page.add(
        txt,
        button,

    )

if __name__ == '__main__':
    ft.app(target=main)
