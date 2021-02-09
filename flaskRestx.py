from flask import Flask
from flask_restx import Api

app = Flask(__name__)

api = Api(app, version='1.0', title='RestX Example',
    description='RestX Example Description',
)

@app.route('/')
def bismillah():
    return "Bismillah Project"


if __name__ == '__main__':
    app.run()