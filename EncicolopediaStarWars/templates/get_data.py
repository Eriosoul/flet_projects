import os
import requests
from dotenv import load_dotenv
from requests import Response
from lib.star_wars import AllResults, DataStarWars


class TheStarWarsAPIData:
    def __init__(self):
        self.url = None
        load_dotenv()
        self.env_data: str = os.getenv("APILINK")
        self.count: int = 1
        self.all_url: list = []

    def check_status(self) -> AllResults:
        try:
            while True:
                self.url: str = f"{self.env_data}?page={self.count}"  # actualizar la url
                print("URL:", self.url)
                self.all_url.append(self.url)  # Agregar la URL actual a la lista
                r: Response = requests.get(self.url)
                if r.status_code != 200:
                    print("Error, status code:", r.status_code)
                    return AllResults(count=0, next="", previous="", results=[])
                data: dict = r.json()
                next_data: str = data.get("next")
                if next_data is not None:
                    self.count += 1
                else:
                    print("No more pages.")
                    break
            return AllResults(
                count=data.get("count"), next=data.get("next"),
                previous=data.get("previous"), results=data.get("results")
            )
        except requests.exceptions.RequestException as e:
            print("Error al obtener los datos:", e)
            return AllResults(count=0, next="", previous="", results=[])

    def get_data_star_wars(self) -> DataStarWars:
        char_name: str = "Darth Maul"
        try:
            character_found: bool = False
            for item in self.all_url:
                next_url = item
                while next_url and not character_found:
                    r: Response = requests.get(next_url)
                    if r.status_code != 200:
                        print(f'Error al obtener datos de {next_url}')
                        break
                    data: dict = r.json()
                    for person_data in data["results"]:
                        name: str = person_data.get("name")
                        if char_name == name:
                            height: str = person_data.get("height")
                            hair_color: str = person_data.get("hair_color")
                            skin_color: str = person_data.get("skin_color")
                            eye_color: str = person_data.get("eye_color")
                            birth_year: str = person_data.get("birth_year")
                            gender: str = person_data.get("gender")
                            character_found = True  # Si personaje encontrado devolvemos true y cerramos bucle
                            print(DataStarWars(
                                name=name, height=height, hair_color=hair_color, skin_color=skin_color,
                                eye_color=eye_color, birth_year=birth_year, gender=gender
                            ))
                    next_url = data.get("next")
        except requests.exceptions.RequestException as e:
            print("Error al obtener los datos:", e)
            return DataStarWars(
                name="", height="", hair_color="", skin_color="", eye_color="", birth_year="", gender=""
            )


if __name__ == '__main__':
    t: TheStarWarsAPIData = TheStarWarsAPIData()
    t.check_status()
    t.get_data_star_wars()
