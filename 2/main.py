from recipe import Recipe


if __name__ == '__main__':
    recipe_from_api = {
        'title': 'Абон',
        'ingredients': [
            ('Мясо', 500, 360, 760),
            ('Курятина', 300, 160, 450),
            ('Рыба', 150, 130, 800),
            ('Кокосовое молоко', 5, 3.5, 290),
            ('Грибы', 30, 16, 130)
        ]
    }

    recipe = Recipe(recipe_from_api['title'], recipe_from_api['ingredients'])

    print(recipe.get_full_cost())