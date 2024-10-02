import unittest
import main

class TestBackwardNumberMethod(unittest.TestCase):
    def test_none(self):
        self.assertEquals(main.algo_func(None), -1)

    def test_list(self):
        list_variations = (
            ([None], -1),
            ([123], -1),
            ([-1], -1),
            ([1.323], -1)
        )

        for param, expected in list_variations:
            with self.subTest():
                result = main.algo_func(param)
                self.assertEquals(result, expected)

    def test_dict(self):
        dict_variations = (
            ({'a': 1, 'b': 2}, -1),
            ({'a': 1}, -1),
            ({1: 2}, -1)
        )

        for param, expected in dict_variations:
            with self.subTest():
                result = main.algo_func(param)
                self.assertEquals(result, expected)

    def test_str(self):
        list_variations = (
            ('', -1),
            ('123', 5),
            ('-12', 44),
            ('Hello there', -1)
        )

        for param, expected in list_variations:
            with self.subTest():
                result = main.algo_func(param)
                self.assertEquals(result, expected)