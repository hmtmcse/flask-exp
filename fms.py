import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError, pprint, fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy.orm import session

db = SQLAlchemy()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(BASE_DIR, 'fms.sqlite3')

# Register ORM
db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    age = db.Column(db.Float())


with app.app_context():
    db.create_all()


class UserDTO(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    name = auto_field()
    email = fields.Email(required=True, error_messages={"required": "Please enter email.", "invalid": "Invalid email address."})
    age = auto_field()


@app.route("/user/create", methods=['POST'])
def create_user():
    try:
        user = UserDTO().load(request.json, session=session)
        db.session.add(user)
        db.session.commit()
        return {"data": {"status": "success", "message": "Validation Success"}}
    except ValidationError as err:
        errors = {}
        if err and err.messages:
            for message in err.messages:
                error_text = ""
                for text in err.messages[message]:
                    error_text += text
                errors[message] = error_text
        pprint(err.messages)
    return {"data": {"status": "error", "errors": errors}}


@app.route("/user/list")
def list_user():
    user_list = User.query.all()
    return UserDTO(many=True).dumps(user_list)


@app.route('/')
def bismillah():
    return "FMS Project"


if __name__ == '__main__':
    app.run()
