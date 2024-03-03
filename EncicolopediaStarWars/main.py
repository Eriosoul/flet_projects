from EncicolopediaStarWars.templates.get_data import TheStarWarsAPIData
from EncicolopediaStarWars.templates.lib.star_wars import DataStarWars

if __name__ == '__main__':
    t: TheStarWarsAPIData = TheStarWarsAPIData()
    if t.check_status():
        t.get_data_star_wars(char_name=DataStarWars.name)
    else:
        print("Error del servidor...")