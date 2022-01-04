from functools import wraps

from flask import Flask, request

app = Flask(__name__)


def check_auth(username, password):
    if username == "admin" and password == "password":
        return True
    return False


def login_required(f):
    @wraps(f)
    def wrapped_view(**kwargs):
        auth = request.authorization
        if not (auth and check_auth(auth.username, auth.password)):
            return ('You are not authorize to access the URL.', 401, {
                'WWW-Authenticate': 'Basic realm="Login Required"'
            })
        return f(**kwargs)
    return wrapped_view


@app.route('/')
def bismillah():
    return "Bismillah Project"


@app.route('/login')
@login_required
def need_login():
    return "Login Success"


@app.route('/other')
@login_required
def other():
    return "Other URL"


if __name__ == '__main__':
    app.run()
