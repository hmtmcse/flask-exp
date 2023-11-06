class ClsProps:
    name: str = "Touhid"

    def __init__(self, name=None):
        if name:
            self.name = name

    def update_name(self):
        self.name = "Mia"


cls = ClsProps()
print(cls.name)

cls.update_name()
print(cls.name)

cls = ClsProps(name="name")
print(cls.name)
print(ClsProps.name)
