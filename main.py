from flask import Flask, request, Response

app = Flask('Homework_punishman')

if __name__ == '__main__':
    app.run(port='5000', debug=True)