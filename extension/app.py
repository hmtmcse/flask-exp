from flask import Flask
from flask_bismillah import Bismillah

app = Flask(__name__)

b = Bismillah()
b.init_app(app)

@app.route('/')
def bismillah():
    return "Bismillah Project " + b.print_me()


if __name__ == '__main__':
    app.run()