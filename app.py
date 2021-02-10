from flask import Flask, redirect, url_for, request, g
from functools import wraps
app = Flask(__name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        fruits = ["apple", "banana", "cherry"]
        for x in fruits:
            print(x)
        return f(*args, **kwargs)
    return decorated_function


def restricted(access_level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(access_level)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@login_required
@app.route('/')
def bismillah():
    return "Bismillah Project"


@app.route("/login")
def login():
    return "Login"

if __name__ == '__main__':
    app.run()