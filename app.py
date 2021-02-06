from flask import Flask
app = Flask(__name__)


@app.route('/')
def bismillah():
    return "Bismillah Project"


if __name__ == '__main__':
    app.run()