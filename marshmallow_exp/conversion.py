import dataclasses
import re
from typing import Type, TypeVar, Any, Dict


def snake_to_camel(input: str) -> str:
    camel_cased = "".join(x.capitalize() for x in input.lower().split("_"))
    if camel_cased:
        return camel_cased[0].lower() + camel_cased[1:]
    else:
        return camel_cased


__camel_to_snake_pattern = re.compile(r"(?<!^)(?=[A-Z])")


def camel_to_snake(input: str) -> str:
    return __camel_to_snake_pattern.sub("_", input).lower()


T = TypeVar("T")


class Dataclass:

    def to_json(self, include_null=False) -> dict:
        return dataclasses.asdict(
            self,
            dict_factory=lambda fields: { snake_to_camel(key): value for (key, value) in fields if value is not None or include_null },
        )

    @classmethod
    def from_json(cls: Type[T], json: dict) -> T:
        if not dataclasses.is_dataclass(cls):
            raise ValueError(f"{cls.__name__} must be a dataclass")
        field_names = {field.name for field in dataclasses.fields(cls)}
        kwargs = {
            camel_to_snake(key): value
            for key, value in json.items()
            if camel_to_snake(key) in field_names
        }
        return cls(**kwargs)


@dataclasses.dataclass
class PersonModel(Dataclass):
    age: int = 20
    first_name: str = "Brad"
    last_name: str = "Pitt"


older_brad = PersonModel.from_json({"age": 30, "education": "Bachelor's degree"})
print(older_brad.to_json())  # PersonModel(age=30, first_name='Brad', last_name='Pitt')
