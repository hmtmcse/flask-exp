from flask import Flask
from flask_bismillah import Bismillah

app = Flask(__name__)

bismillah = Bismillah(app)

@app.route('/')
def bismillah():
    bismillah.print()
    return "Bismillah Project"


if __name__ == '__main__':
    app.run()