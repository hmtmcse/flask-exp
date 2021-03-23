from marshmallow import Schema, fields, validates_schema, ValidationError


class NumberSchema(Schema):
    field_a = fields.Integer()
    field_b = fields.Integer()

    @validates_schema
    def validate_numbers(self, data, **kwargs):
        if data["field_b"] >= data["field_a"]:
            raise ValidationError("field_a must be greater than field_b")


if __name__ == '__main__':
    schema = NumberSchema()
    try:
        schema.load({"field_a": 1, "field_b": 2})
    except ValidationError as err:
        print("error")
