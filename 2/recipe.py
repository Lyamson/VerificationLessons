from ingredient import Ingredient


class Recipe:
    def __init__(self, name : str, ingredients : list[tuple[str, int, int, int]]) -> None:
        self.name = name
        self.ingredients = [
            Ingredient(ing_name, ing_raw_weight, ing_cooked_weight, ing_cost) 
            for ing_name, ing_raw_weight, ing_cooked_weight, ing_cost in ingredients
        ]

    def get_weight(self, portions = 1, raw : bool = False) -> int:
        return sum([ingredient.weight_raw if raw else ingredient.weight_cooked for ingredient in self.ingredients]) * portions

    def get_full_cost(self, portions = 1) -> int:
        return sum([ingredient.cost for ingredient in self.ingredients]) * portions