from flask import Flask, redirect, url_for, request
from functools import wraps
app = Flask(__name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function

@login_required
@app.route('/')
def bismillah():
    return "Bismillah Project"


if __name__ == '__main__':
    app.run()