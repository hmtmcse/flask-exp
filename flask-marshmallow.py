from flask import Flask, request
from marshmallow import Schema, fields, ValidationError, pprint

app = Flask(__name__)


class UserDTO(Schema):
    name = fields.String(required=True, error_messages={"required": "Please enter name."})
    email = fields.Email(required=True, error_messages={"required": "Please enter email.", "invalid": "Invalid email address."})
    age = fields.Float()

@app.route("/")
def index():
    return "index"


@app.route("/user/create", methods=['POST'])
def create_user():
    try:
        user = UserDTO().load(request.json)
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
