from flask import Flask
app = Flask(__name__)


@app.route('/')
def bismillah():
    return "Bismillah Project"


@app.before_request
def before_request():
    print("before_request")
    # return "Access Denied"


def br():
    print("BR")


if __name__ == '__main__':
    app.before_request_funcs.setdefault(None, []).append(br)
    app.run()
