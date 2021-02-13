from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, request
from marshmallow import Schema, fields, ValidationError, pprint

app = Flask(__name__)

# Create an APISpec
spec = APISpec(
    title="Swagger Petstore",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()],
)

jwt_scheme = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
spec.components.security_scheme("jwt", jwt_scheme)


class UserDTO(Schema):
    name = fields.String(required=True, error_messages={"required": "Please enter name."})
    email = fields.Email(required=True, error_messages={
        "required": "Please enter email.", "invalid": "Invalid email address."})
    age = fields.Float()


class MessageDTO(Schema):
    message = fields.String()
    code = fields.Integer()


spec.components.schema("User", schema=UserDTO)
spec.components.schema("Message", schema=MessageDTO)

# Create
spec.path(
    path="/user/create",
    operations=dict(
        post=dict(
            requestBody={"required": True, "content": {"application/json": {"schema": "User"}}},
            responses={"200": {"content": {"application/json": {"schema": {
                "anyOf": [{"$ref": "#/components/schemas/User"}, {"$ref": "#/components/schemas/Message"}]}}},
                "description": "Description"}}
        )
    )
)

# Update
spec.path(
    path="/user/update/{id}",
    operations=dict(
        post=dict(
            requestBody={"required": True, "content": {"application/json": {"schema": "User"}}},
            responses={"200": {"content": {"application/json": {"schema": {
                "anyOf": [{"$ref": "#/components/schemas/User"}, {"$ref": "#/components/schemas/Message"}]}}},
                "description": "Description"}}
        )
    ),
    parameters=[
        {
            "name": "id",
            "in": "path",
            "schema": {
                "type": "integer"
            }
        }
    ]
)

# List with pagination
spec.path(
    path="/user/list",
    operations=dict(
        get=dict(
            responses={"200": {"content": {"application/json": {"schema": {
                "type": "array",
                "items": "User",
            }}},
                "description": "Description"}}
        )
    ),
    parameters=[
        {
            "name": "offset",
            "in": "query",
            "schema": {
                "type": "integer"
            }
        },
        {
            "name": "max",
            "in": "query",
            "schema": {
                "type": "integer"
            }
        },
        {
            "name": "order-by",
            "in": "query",
            "schema": {
                "type": "string"
            }
        },
        {
            "name": "order-field",
            "in": "query",
            "schema": {
                "type": "string"
            }
        }
    ]
)

# Details by Id
spec.path(
    path="/user/details/{id}",
    operations=dict(
        get=dict(
            responses={"200": {"content": {"application/json": {"schema": "User"}}, "description": "Details"}}
        )
    ),
    parameters=[
        {
            "name": "id",
            "in": "path",
            "schema": {
                "type": "integer"
            }
        }
    ]
)
# Delete
spec.path(
    path="/user/delete/{id}",
    operations=dict(
        delete=dict(
            responses={"200": {"content": {"application/json": {"schema": "Message"}}, "description": "Details"}}
        )
    ),
    parameters=[
        {
            "name": "id",
            "in": "path",
            "schema": {
                "type": "integer"
            }
        }
    ]
)


@app.route("/")
def swagger():
    return spec.to_dict()


if __name__ == '__main__':
    app.run()
