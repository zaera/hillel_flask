from flask import Flask, request, Response
from utils import space

app = Flask('Homework_punishman')

@app.route('/space/')
def orbital():
    return space('http://api.open-notify.org/astros.json')

if __name__ == '__main__':
    app.run(port='5000', debug=True)