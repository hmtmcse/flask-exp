from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, request
from marshmallow import Schema, fields, ValidationError, pprint

app = Flask(__name__)

# Create an APISpec
spec = APISpec(
    title="Swagger Petstore",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[ MarshmallowPlugin()],
)

jwt_scheme = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
spec.components.security_scheme("jwt", jwt_scheme)


class UserDTO(Schema):
    name = fields.String(required=True, error_messages={"required": "Please enter name."})
    email = fields.Email(required=True, error_messages={"required": "Please enter email.", "invalid": "Invalid email address."})
    age = fields.Float()


spec.components.schema("User", schema=UserDTO)
spec.path(
    path="/gist/{gist_id}",
    operations=dict(
        get=dict(
            responses={"200": {"content": {"application/json": {"schema": "User"}}, "description": "kisu akta"}}
        )
    ),
    parameters=[
        {
            "name": "gist_id",
            "in": "path"
        }
    ]
)


@app.route("/")
def swagger():
    return spec.to_dict()


if __name__ == '__main__':
    app.run()
