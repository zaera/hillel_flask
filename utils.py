from faker import Faker
import csv
import requests

def space(link: str) -> str:
    try:
        nasa = requests.get(link).json()
        data = 'There are <font size="+4">' + str(len(nasa['people'])) + "</font> astronauts in space right now. They are: <br>"
        for name in nasa['people']:
            data = data + name['name'] + '<br>'
        return data
    except Exception:
        return 'Something wrong with the Nasa link! Sorry.'