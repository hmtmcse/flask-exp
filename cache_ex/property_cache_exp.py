from functools import cached_property


class Address:
    myname: str = "Touhid Mia"

    @property
    def name(self):
        return self.myname

    @name.setter
    def name(self, value):
        self.myname = value


print(Address.name)
