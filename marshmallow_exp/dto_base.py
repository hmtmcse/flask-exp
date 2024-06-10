import dataclasses
from enum import Enum
import re


class PropsModType(Enum):
    CAMEL_TO_SNAKE = "CAMEL_TO_SNAKE"
    SNAKE_TO_CAMEL = "SNAKE_TO_CAMEL"


class DTOBase(object):
    exclude_props_mod: dict = {}
    props_mod_type: PropsModType = None
    camel_to_snake_regex = re.compile(r"(?<!^)(?=[A-Z])")
    include_null: bool = False

    def convert_snake_to_camel_case(self, text: str) -> str:
        camel_cased = "".join(x.capitalize() for x in text.lower().split("_"))
        if camel_cased:
            return camel_cased[0].lower() + camel_cased[1:]
        else:
            return camel_cased

    def convert_camel_to_snake_case(self, text: str) -> str:
        return self.camel_to_snake_regex.sub("_", text).lower()

    def _get_property_modifier(self):
        if not self.props_mod_type:
            return None
        elif self.props_mod_type == PropsModType.CAMEL_TO_SNAKE:
            return self.convert_camel_to_snake_case
        elif self.props_mod_type == PropsModType.SNAKE_TO_CAMEL:
            return self.convert_snake_to_camel_case
        return None

    def _load_nested_data_class(cls, data: dict):
        kwargs = cls._get_load_kwargs(cls, data=data)
        return cls(**kwargs)

    def _get_load_kwargs(cls, data: dict):
        property_modifier = cls._get_property_modifier(cls)
        field_name_type = {field.name: field.type for field in dataclasses.fields(cls)}
        kwargs = {}
        for key, value in data.items():
            if property_modifier and (not cls.exclude_props_mod or key not in cls.exclude_props_mod):
                key = property_modifier(cls, text=key)
            if key in field_name_type:
                field_type = field_name_type[key]
                if issubclass(field_type, DTOBase) and isinstance(value, dict):
                    kwargs[key] = cls._load_nested_data_class(field_type, data=value)
                else:
                    kwargs[key] = value
        return kwargs

    @classmethod
    def load_dict(cls, data: dict):
        if not dataclasses.is_dataclass(cls):
            raise ValueError(f"{cls.__name__} must be a dataclass")
        kwargs = cls._get_load_kwargs(cls, data=data)
        return cls(**kwargs)

    def _dict_factory(self, fields):
        dict_field = {}
        property_modifier = self._get_property_modifier()
        for (key, value) in fields:
            if property_modifier and (not self.exclude_props_mod or key not in self.exclude_props_mod):
                key = property_modifier(text=key)
            if value is not None or self.include_null:
                dict_field[key] = value
        return dict_field

    def to_dict(self, include_null=False):
        self.include_null = include_null
        self.set_serialize_conf()
        return dataclasses.asdict(self, dict_factory=self._dict_factory)

    def set_serialize_conf(self):
        pass

    def set_deserialize_conf(self):
        pass
