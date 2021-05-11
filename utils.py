from faker import Faker
import csv
import requests

def file_read(file: str) -> dict():
    try:
        with open(file, 'r') as f:
            file_contents = f.readlines()
        f.close()
        file_contents = map(lambda line: line.replace('\n', '<br>'), file_contents)
        res_dct = []
        for file_content in file_contents:
            res_dct.append(file_content)

        return res_dct
    except Exception:

        return 'OOOOps!! Check filename!'

def users(number: int = 100) -> str:
    fake = Faker()
    user_list=''
    for _ in range(number):
        user_list = user_list + fake.first_name() + ' ' + fake.free_email() + '<br>'

    return user_list

def average(file: str) -> str:
    try:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            heights = []
            weights = []
            for row in reader:
                heights.append(float(row[reader.fieldnames[1]]))
                weights.append(float(row[reader.fieldnames[2]]))
        avg_height = sum(heights) / len(heights)
        print(avg_height)
        avg_weights = sum(weights) / len(weights)
        print(avg_weights)

        return 'Average height~: ' + str(round(avg_height*2.54, 2)) + ' cm' + '<br>' + 'Average weight~: ' + str(round(avg_weights/2.2046)) + ' kg' + '<br>' + 'Collected: ' + str(len(heights)) + ' items'
    except Exception:

        return 'OOOOps!! Check filename!'

def space(link: str) -> str:
    try:
        nasa = requests.get(link).json()
        data = 'There are <font size="+4">' + str(len(nasa['people'])) + "</font> astronauts in space right now. They are: <br>"
        for name in nasa['people']:
            data = data + name['name'] + '<br>'
        return data
    except Exception:
        return 'Something wrong with the Nasa link! Sorry.'