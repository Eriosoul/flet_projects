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

        # save buttont to calculata masa
        self.add = ft.ElevatedButton(
            text="Save",
            color="white",
            bgcolor="blue600",
            height=40,
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=5)}),
            on_click=self.save_data,
        )

        # Data to calculate
        self.peso = ft.TextField(hint_text="Peso...", **data_style["input"])
        self.altura = ft.TextField(hint_text="Altura...", **data_style["input"])

        # Label to display BMI
        self.bmi_text = ft.Text("BMI: ", size=16, weight="w500", color="black")

        self.content = ft.Row(
            spacing=20,
            controls=[
                self.peso,
                self.altura,
                self.add,
                self.bmi_text,
                # Add the TextField for data input
            ],
        )
    def save_data(self, e):
        try:
            # Get weight and height as float values
            weight = float(self.peso.value)
            height = float(self.altura.value)

            # Calculate BMI
            bmi = weight / (height ** 2)

            # Update the label text
            print(bmi)
            self.bmi_text.text = f"BMI: {bmi:.2f}"
        except ValueError:
            print("Invalid input. Please enter numeric values for weight and height.")



def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text('Calculadora de índice de masa corporal'),
        center_title=True
    )

    form = ColectingData()  # Remove the extra comma
    page.add(
        ft.Row(
            expand=True,
            spacing=9,
            controls=[
                ft.Column(
                    expand=5,
                    controls=[form],
                )
            ],
        )
    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main)


