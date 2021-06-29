from enum import Flag, auto

class Side(Flag):
    GUACAMOLE = auto()
    TORTILLA = auto()
    FRIES = auto()
    BEER = auto()
    POTATO_SALAD = auto()

mexican_sides = Side.GUACAMOLE | Side.BEER | Side.TORTILLA
bavarian_sides = Side.BEER | Side.POTATO_SALAD
common_sides = mexican_sides & bavarian_sides

print(Side.GUACAMOLE in mexican_sides)
print(Side.TORTILLA in bavarian_sides)
print(common_sides)