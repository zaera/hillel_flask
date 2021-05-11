from flask import Flask, request, Response
from utils import file_read#, users, average, space

app = Flask('Homework_punishman')

@app.route('/requirements/')
def requirements():
    return Response(file_read('requirements.txt'))
if __name__ == '__main__':
    app.run(port='5000', debug=True)