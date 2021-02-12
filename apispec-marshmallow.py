from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask
from marshmallow import Schema, fields


# Create an APISpec
spec = APISpec(
    title="Swagger Petstore",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


class CategorySchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)


class PetSchema(Schema):
    category = fields.List(fields.Nested(CategorySchema))
    name = fields.Str()


# Optional security scheme support
api_key_scheme = {"type": "apiKey", "in": "header", "name": "X-API-Key"}
spec.components.security_scheme("ApiKeyAuth", api_key_scheme)


# Optional Flask support
app = Flask(__name__)


@app.route("/random")
def random_pet():
    """A cute furry animal endpoint.
    ---
    get:
      description: Get a random pet
      security:
        - ApiKeyAuth: []
      responses:
        200:
          content:
            application/json:
              schema: PetSchema
    """
    pet = {}
    return PetSchema().dump(pet)


@app.route("/")
def swagger():
    return spec.to_dict()


with app.test_request_context():
    spec.path(view=random_pet)

if __name__ == '__main__':
    app.run()
