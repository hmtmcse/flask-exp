import yaml


class Hero(yaml.YAMLObject):
    yaml_tag = " "

    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp
        self.sp = sp


print(yaml.dump(Hero("Galain Ysseleg", hp=-3, sp=2)))
