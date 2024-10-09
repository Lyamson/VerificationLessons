from recipe import Recipe


if __name__ == '__main__':
    recipe_from_api = {
        'title': 'Абон',
        'ingredients': [
            ('Мясо', 500, 360, 760),
            ('Курятина', 300, 160, 450),
            ('Рыба', 150, 130, 800),
            ('Кокосовое молоко', 5, 3, 290),
            ('Грибы', 30, 16, 130)
        ]
    }

    recipe = Recipe(recipe_from_api['title'], recipe_from_api['ingredients'])
    assert recipe.get_full_cost() == 2430, 'Invalid full cost for 1 portion'
    assert recipe.get_weight(2, raw = True) == 1970, 'Invalid raw weight for 2 portions'
    
    recipe_from_api = {
        'title': 'Воппер',
        'ingredients': [
            ('Булочка с кунжутом', 100, 80, 60),
            ('Котлета', 300, 160, 120),
            ('Огурец', 20, 15, 40),
            ('Помидор', 30, 25, 35),
            ('Кетчуп', 10, 7, 30)
        ]
    }

    recipe = Recipe(recipe_from_api['title'], recipe_from_api['ingredients'])
    assert recipe.get_full_cost(2) == 570, 'Invalid full cost for 2 portions'
    assert recipe.get_weight() == 287, 'Invalid cooked weight for 1 portion'

'''
Name             Stmts   Miss  Cover
------------------------------------
ingredient.py       41      0   100%
recipe.py           14      0   100%
test_recipe.py      43      6    86%
------------------------------------
TOTAL               98      6    94%
'''