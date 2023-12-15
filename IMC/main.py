import flet as ft


# styling to get data
data_style: dict = {
    "main": {
        "expand": 2,
        "bgcolor": "",
        "padding": ft.padding.only(left=35, right=35)
    },
    "input": {
        "height": 38,
        "border_color": "#aeaeb3",
        "focused_border_color": "black",
        "border_radius": 5,
        "cursor_height": 16,
        "cursor_color": "black",
        "content_padding": 10,
        "border_width": 1.5,
        "text_size": 12,
    }
}

class ColectingData(ft.Container):
    def __init__(self):
        super().__init__(**data_style["main"])

        self.peso = ft.TextField(hint_text="Peso...", **data_style["input"])
        self.altura = ft.TextField(hint_text="Altura...", **data_style["input"])
        self.bmi_text = ft.Text(value="BMI: ")
        self.text_number = ft.Text("0")
        self.c = ft.Container(width=100, height=100, bgcolor=ft.colors.GREEN_200)

        self.add_button = ft.ElevatedButton(
            text="Save",
            color="white",
            bgcolor="blue600",
            height=45,
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=5)}),
            on_click=self.save_data
        )

        self.content = ft.Row(
            spacing=1,
            controls=[
                self.peso,
                self.altura,
                self.add_button,
                self.bmi_text,
                self.text_number
            ]
        )

    def save_data(self, e):
        try:
            weight = float(self.peso.value)
            height = float(self.altura.value)
            bmi = weight / (height ** 2)
            self.bmi_text.value = f"BMI: {bmi:.2f}"
            if bmi > 24.9:
                self.c = ft.Container(width=100, height=100, bgcolor=ft.colors.RED)
            elif 18.5 < bmi <= 24.9:
                self.c = ft.Container(width=100, height=100, bgcolor=ft.colors.GREEN_200)
            else:
                # Handle other cases if needed
                pass
            # updatin the data what it will show to us
            self.content = ft.Row(
                spacing=1,
                controls=[
                    self.peso,
                    self.altura,
                    self.add_button,
                    self.bmi_text,
                ]
            )

            self.update()

        except ValueError:
            print("Invalid input. Please enter numeric values for weight and height.")




def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text('Calculadora de índice de masa corporal'),
        center_title=True
    )

    form: ft.Container = ColectingData()
    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Row(
                    expand=5,
                    controls=[form],
                )
            ],

        ),
    )
    page.update()

if __name__ == '__main__':
    ft.app(target=main)