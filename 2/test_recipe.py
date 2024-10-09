import unittest
from recipe import Recipe
from ingredient import Ingredient

class TestRecipeMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_recipe_from_api = {
            'title': 'Гюдон',
            'ingredients': [
                ('Говядина', 400, 350, 540),
                ('Рис', 150, 120, 180),
                ('Лук', 40, 25, 70),
                ('Яйцо', 60, 40, 90)
            ]
        }
        cls.test_recipe = Recipe(test_recipe_from_api['title'], test_recipe_from_api['ingredients'])

    def test_ingredient(self):
        ingredient_variations = (
            ('Лук', 10, 5, 30, None),
            ('Перец', -514, 15, 60, ValueError),
            ('Горох', 10, -321, 39, ValueError),
            ('Что-то', 16, 12, -100, ValueError),
            ('1', 'Строка', 13, 41, TypeError),
            ('2', 15, 'Строка', 100, TypeError),
            ('3', 15, 12, 'Строка', TypeError)
        )

        for name, raw, cooked, cost, expected in ingredient_variations:
            with self.subTest():
                try:
                    Ingredient(name, raw, cooked, cost).name == name
                except expected:
                    ...
                except:
                    self.fail()

    def test_weight(self):
        # ( portions, raw, expected )
        weight_variations = (
            (1, True, 650),
            (2, True, 1300),
            (1, False, 535),
            (2, False, 1070),
            ('Hello', False, TypeError),
            (1, 'False', TypeError),
            (None, False, TypeError),
            (1, None, TypeError),
            (2, 12, TypeError),
            (-3, False, ValueError)
        )

        for portions, raw, expected in weight_variations:
            with self.subTest():
                try:
                    result = self.test_recipe.get_weight(portions, raw)
                    self.assertEqual(result, expected)
                except expected:
                    ...
                except:
                    self.fail()

    def test_cost(self):
        cost_variations = (
            (1, 880),
            (2, 1760),
            (-1, ValueError),
            (None, TypeError),
            ('Hi', TypeError),
            ([1], TypeError)
        )

        for portions, expected in cost_variations:
            with self.subTest():
                try:
                    result = self.test_recipe.get_full_cost(portions)
                    self.assertEqual(result, expected)
                except expected:
                    ...
                except:
                    self.fail()

    @classmethod
    def tearDownClass(cls):
        cls.test_recipe = None