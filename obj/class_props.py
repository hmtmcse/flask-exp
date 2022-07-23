import inspect


class Something:
    name: str


class ClassProps:
    name: str
    age: int
    something: Something

    def __init__(self):
        self.ex1 = "xyz"

    def get_members(self):
        res = inspect.getmembers(self)
        for i in inspect.getmembers(self.__class__):
            if not i[0].startswith('_'):
                # print(i)
                pass


ClassProps().get_members()

# print(vars(ClassProps()))
# print(dir(ClassProps()))

# print(inspect.getmembers(ClassProps))

# print(ClassProps.__dict__)

for i in inspect.getmembers(ClassProps):
    if len(i) == 2 and i[0] == "__annotations__":
        for field_name in i[1]:
            # print(field_name)
            # print(i[1][field_name])
            print(i[1][field_name].__name__)
        break
    print("--->>")
