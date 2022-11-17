class MyConfig:
    name: str = "Touhid"
    age: int = 30


setattr(MyConfig, "name", "Mia")
print(MyConfig.name)
