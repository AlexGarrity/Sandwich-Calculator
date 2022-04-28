import json


class SandwichRecipe:

    name: str
    components: dict[str, int]

    def __init__(self, name: str, components: dict[str, int]):
        self.name = name
        self.components = components


    def __init__(self, json_recipe: json):
        self.name = json_recipe["name"]
        self.components = json_recipe["ingredients"]