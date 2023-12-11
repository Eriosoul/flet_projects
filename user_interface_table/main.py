import flet as ft # pip install flet or pip3 install flet
import os
import csv

# DAta Table styling directory
data_table_style: dict = {
    "main": {
        "expand": 3,
        "bgcolor": "#fdfdfe",
    },
    "data_table": {
        "heading_row_color": "#e3e4ea",
        "expand": True,
        "heading_row_height": 35,
        "data_row_max_height": 40,
    },
}


# Data table
class DataTable(ft.Container):
    def __init__(self):
        super().__init__(**data_table_style["main"])

        self.table = ft.DataTable(**data_table_style["data_table"],)
        headers: list = ["Full Name", "Email Address", "Role",]

        self.table.columns = [
            ft.DataColumn(
                ft.Text(title, weight="w600", size=12)) for title in headers
        ]

        self.content = ft.Column(
            scroll="hidden",
            controls=[ft.Row(controls=[self.table])]
        )


# form class styling
form_style: dict = {
    "main": {
        "expand": 2,
        "bgcolor": "#fdfdfe",
        "padding": ft.padding.only(left=35, right=35),
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
    },
}
# From class
class Form(ft.Container):
    def __init__(self, table: ft.DataTable):
        super().__init__(**form_style["main"])
        self.table = table

#     input files
        self.name = ft.TextField(**form_style["input"])
        self.email = ft.TextField(**form_style["input"])
        self.role = ft.TextField(**form_style["input"])
        data: list = ["Full Name", "Email Address", "Role"]
        files: list = [self.name, self.email, self.role]

        items: list = [
            ft.Column(
                expand=True,
                controls=[
                    ft.Text(title, size=12, weight="w500"), files[index]
                ]
            )
            for index, title in enumerate(data)
        ]

        # save buttont to push the data in the table and a CSV file
        self.add = ft.ElevatedButton(
            text="Save",
            color="white",
            bgcolor="blue600",
            height=40,
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=5)}),
            on_click=self.save_data,
        )
        self.content = ft.Column(
            controls=[
                ft.Divider(height=10, color="transparent"),
                ft.Text("Records System", size=28, weight="w900"),
                ft.Divider(height=30, color="transparent"),
                ft.Row(spacing=20, expand=True, controls=items),
                ft.Divider(height=10, color="transparent"),
                ft.Row(alignment="end", controls=[self.add], expand=True),
            ]
        )

    #  creating the data to show
    def create_data_row(self, values: list):
        data = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(values[0], size=12, weight="w600")),
                ft.DataCell(ft.Text(values[1], size=12, weight="w600")),
                ft.DataCell(ft.Text(values[2], size=12, weight="w600")),
            ]
        )
        return data

    def update_data_table(self,data:ft.DataRow):
        self.table.rows.append(data)
        self.table.update()
    def save_data(self, event):
        values: list = [self.name.value, self.email.value, self.role.value]
        if all(values):
            data = self.create_data_row(values)
            # update data table
            self.update_data_table(data)
            # update and write to a csv
            self.check_if_csv_exists()

    def write_data_to_csv(self):
        csv_rows: list =[]
        for row in self.table.rows[:]:
            temp_list: list = []
            for control in row.cells[:]:
                temp_list.append(control.content.value)
            csv_rows.append(temp_list)
        with open("data.csv", "w") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["Full Name", "Email Address", "Role"])
            csvwriter.writerows(csv_rows)
    def check_if_csv_exists(self):
        if "data.csv" not in os.listdir("."):
            with open("data.csv", "a"):
                pass
        #  if file aready there, just push data to it
        else:
            self.write_data_to_csv()
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    dataTable: ft.Container = DataTable()
    form: ft.Container = Form(table=dataTable.table)
    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Column(
                    expand=5,
                    controls=[form, dataTable],
                )
            ],
        )
    )
    page.update()

if __name__ == '__main__':
    ft.app(target=main)

