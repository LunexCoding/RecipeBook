import unittest
from ingredient import Ingredient


class TestIngredient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._ingredient = Ingredient(
            name='ingredientName',
            measure='ingredientMeasure'
        )

    def test_ingredient(self):
        self.assertEqual([self._ingredient.name, self._ingredient.measure], ['ingredientName', 'ingredientMeasure'])  # add assertion here


if __name__ == '__main__':
    unittest.main()
