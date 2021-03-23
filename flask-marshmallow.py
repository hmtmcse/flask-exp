from flask import Flask, request
from marshmallow import Schema, fields, ValidationError, pprint, validates_schema

app = Flask(__name__)


class NumberSchema(Schema):
    field_a = fields.Integer(required=True, error_messages={"required": "Please enter name."})
    field_b = fields.Integer()

    @validates_schema(skip_on_field_errors=True)
    def conditional_validation(self, data, **kwargs):
        if data["field_a"] != 'mia':
            raise ValidationError("field_a must be greater than field_b")


class UserDTO(Schema):
    name = fields.String(required=True, error_messages={"required": "Please enter name."})
    email = fields.Email(required=True, error_messages={"required": "Please enter email.", "invalid": "Invalid email address."})
    age = fields.Float()

    @validates_schema
    def conditional_validation(self, data, **kwargs):
        if data["name"] != 'mia':
            raise ValidationError("field_a must be greater than field_b")


@app.route("/")
def index():
    return "index"


@app.route("/validation", methods=['POST', 'GET'])
def validation():
    schema = NumberSchema()
    try:
        schema.load({"field_a": 1, "field_b": 2})
        schema.validate({"field_a": 1, "field_b": 2})
    except ValidationError as err:
        print("error")
    return "validation"


@app.route("/user/create", methods=['POST'])
def create_user():
    try:
        user = UserDTO()
        try:
            user.load({"field_a": 1, "field_b": 2})
        except ValidationError as err:
            print("error")
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
