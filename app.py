from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("hahah1")
    #test123
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
