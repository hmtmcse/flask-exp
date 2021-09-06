from flask import Flask
app = Flask(__name__)


@app.route('/')
def bismillah():
    return "Bismillah Project"


@app.before_request
def before_request():
    print("before_request")
    return "Access Denied"


if __name__ == '__main__':
    app.run()
