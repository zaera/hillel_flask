from flask import Flask, request, Response
from utils import file_read, users, average, space

app = Flask('Homework_punishman')

@app.route('/requirements/')
def requirements():
    return Response(file_read('requirements.txt'))

@app.route('/generate-users/')
def generate_users():
    query_params = request.args
    number = query_params.get('number') or ''
    default_users_number = 100
    minimum_users_number = 1
    maximum_users_number = 100

    if number.isdigit():
        number = int(number)
        if number > maximum_users_number or number < minimum_users_number:
            number = default_users_number
    else:
        number = default_users_number

    return users(number)

@app.route('/mean/')
def mean():
    return average('hw.csv')

@app.route('/space/')
def orbital():
    return space('http://api.open-notify.org/astros.json')

if __name__ == '__main__':
    app.run(port='5000', debug=True)