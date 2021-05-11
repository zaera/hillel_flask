from flask import Flask, request, Response
from utils import average

app = Flask('Homework_punishman')

@app.route('/mean/')
def mean():
    return average('hw.csv')

if __name__ == '__main__':
    app.run(port='5000', debug=True)