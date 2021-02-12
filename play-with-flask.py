from functools import wraps

from flask import Flask


app = Flask(__name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        fruits = ["apple", "banana", "cherry"]
        for x in fruits:
            print(x)
        return "La LA LA"
        # return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@login_required
def bismillah():
    return "Bismillah Project"


@app.route("/login", methods=["POST"])
def login():
    return "Return Login Params"


@app.route("/with-url/<name>")
def with_name(name):
    return "With URL " + name


def get_decorators(function):
  if not function.func_closure:
    return [function]
  decorators = []
  for closure in function.func_closure:
    decorators.extend(get_decorators(closure.cell_contents))
  return [function] + decorators


@app.route("/swagger")
def swagger():
    ignore_verbs = {"HEAD", "OPTIONS"}
    for rule in app.url_map.iter_rules():
        endpoint = app.view_functions[rule.endpoint]
        # get_decorators(endpoint)
        for verb in rule.methods.difference(ignore_verbs):
            print(rule.rule + " " + verb)
    return "Swagger"


if __name__ == '__main__':
    app.run()
