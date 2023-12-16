import flet as ft


# styling to get data
data_style: dict = {
    "main": {
        "expand": 2,
        "bgcolor": "",
        "padding": ft.padding.all(20),
    },
    "input": {
        "height": 45,
        "border_color": "#009688",
        "focused_border_color": "#004D40",
        "border_radius": 8,
        "cursor_height": 16,
        "cursor_color": "#004D40",
        "content_padding": 10,
        "border_width": 2,
        "text_size": 14,
    },
    "result": {
        "text_size": 18,
        "weight": "bold",
        "color": "#004D40",
    }
}

class ColectingData(ft.Container):
    def __init__(self):
        super().__init__(**data_style["main"])

        self.peso = ft.TextField(hint_text="Peso KG...", **data_style["input"])
        self.altura = ft.TextField(hint_text="Altura CM...", **data_style["input"])
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
            spacing=15,
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
            self.update_data()
            self.color_depends(bmi=bmi)

        except ValueError:
            print("Invalid input. Please enter numeric values for weight and height.")

    def color_depends(self, bmi: float):
        if bmi < 18.50:
            self.c = ft.Container(width=100, height=100, bgcolor=ft.colors.RED)
        elif 18.50 < bmi <= 24.90:
            self.c = ft.Container(width=100, height=100, bgcolor=ft.colors.GREEN)
        elif 25.00 < bmi <= 29.90:
            self.c = ft.Container(width=100, height=100, bgcolor=ft.colors.YELLOW)
        elif bmi > 30:
            self.c = ft.Container(width=100, height=100, bgcolor=ft.colors.RED)
        else:
            print("Error: ")

    def update_data(self):
        self.content = ft.Row(
            spacing=1,
            controls=[
                self.peso,
                self.altura,
                self.add_button,
                self.bmi_text,
                self.c
            ]
        )
        self.update()

def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text('Calculadora de índice de masa corporal'),
        center_title=True
    )

    form: ft.Container = ColectingData()
    vertical_column = ft.Column(
        expand=True,
        spacing=0,
        controls=[
            form,
            ft.Text("Otro elemento"),  # Ejemplo de otro elemento
        ],
    )
    page.add(vertical_column)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
