from flask import Flask, request
import datetime
now = datetime.datetime.now()

app = Flask(__name__)
@app.route('/hello')

def hello_func():
    name = request.args.get('name')
    return f'hello {name}!'

@app.route('/time')

def current_time():
#    name = request.args.get('name')
    return {'time': datetime.datetime.now()}



if __name__ == '__main__':

    app.run('localhost', 5000)