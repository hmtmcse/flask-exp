from dataclasses import dataclass
from marshmallow_exp.dto_base import DTOBase, PropsModType


@dataclass(kw_only=True)
class StudentBase(DTOBase):
    roll: str = None


@dataclass(kw_only=True)
class Student(DTOBase):
    name: str
    email: str
    password: str
    age: int
    companyName: str = None
    base: StudentBase = None

    def set_serialize_conf(self):
        self.props_mod_type = PropsModType.CAMEL_TO_SNAKE


student = Student(name="Touhid", email="email@bfei.net", password="123456", age=33)
print(student)
print(student.to_dict())

print("\n")
print("----- Load -----")
student = Student.load_dict({"name": "Touhid", "email": "email@bfei.net", "password": "123456", "age": 33, "base":StudentBase(roll="Rool"), "companyName": "BM"})
print(student)
print(student.to_dict())

