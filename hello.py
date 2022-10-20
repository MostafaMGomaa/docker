from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world!"


@app.route('/hamo')
def index():
    return "Hello hamo!"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
