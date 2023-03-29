import unittest
from DataStructures import ingredientsDB
from DataStructures.ingredientsDB import _IngredientsDatabase
from entities.ingredient import Ingredient
from helpers.fileSystem import FileSystem


_FIXTURES_DIRECTORY = "fixtures"
_DATABASE_FILE = f"{_FIXTURES_DIRECTORY}/ingredientsDB.json"


class TestIngredientsDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._ingredientsDB = _IngredientsDatabase()
        cls._fileSystem = FileSystem()
        cls._fileSystem.makeDir(_FIXTURES_DIRECTORY)

        cls._ingredient1 = Ingredient(
            name="Tea",
            measure="kg"
        )
        cls._ingredient2 = Ingredient(
            name="Tea",
            measure="l"
        )
        cls._ingredient3 = Ingredient(
            name="Salt",
            measure="kg"
        )

    @classmethod
    def tearDownClass(cls):
        cls._fileSystem.removeTree(_FIXTURES_DIRECTORY)

    @classmethod
    def getIngredientIDByIngredient(cls, ingredient):
        return ''.join([ingredientID for ingredientID, ingredientObj in cls._ingredientsDB.ingredients.items() if (ingredientObj.name == ingredient.name and ingredientObj.measure == ingredient.measure)])

    def test_addIngredientToDB(self):
        self._ingredientsDB.addIngredientToDB(self._ingredient1)
        self._ingredientsDB.addIngredientToDB(self._ingredient1)
        self._ingredientsDB.addIngredientToDB(self._ingredient2)
        self._ingredientsDB.addIngredientToDB(self._ingredient3)
        ingredient1ID = self.getIngredientIDByIngredient(self._ingredient1)
        ingredient2ID = self.getIngredientIDByIngredient(self._ingredient2)
        ingredient3ID = self.getIngredientIDByIngredient(self._ingredient3)
        self.assertIn(ingredient1ID, self._ingredientsDB.ingredients)
        self.assertIn(ingredient2ID, self._ingredientsDB.ingredients)
        self.assertIn(ingredient3ID, self._ingredientsDB.ingredients)
        self.assertEqual([self._ingredientsDB.ingredients[ingredient1ID].name, self._ingredientsDB.ingredients[ingredient1ID].measure], ["Tea", "kg"])
        self.assertEqual([self._ingredientsDB.ingredients[ingredient2ID].name, self._ingredientsDB.ingredients[ingredient2ID].measure], ["Tea", "l"])
        self.assertEqual([self._ingredientsDB.ingredients[ingredient3ID].name, self._ingredientsDB.ingredients[ingredient3ID].measure], ["Salt", "kg"])

    def test_deleteIngredientByID(self):
        ingredientID = self.getIngredientIDByIngredient(self._ingredient1)
        self._ingredientsDB.deleteIngredientByID(ingredientID)
        self.assertNotIn(ingredientID, self._ingredientsDB.ingredients)

    def test_writeDBFileAndLoadIngredients(self):
        ingredientsDB._DATABASE_FILE = _DATABASE_FILE
        self._ingredientsDB.writeDBFile()
        self.assertTrue(self._fileSystem.exists(_DATABASE_FILE))
        self._ingredientsDB._ingredients = {}
        self._ingredientsDB.loadIngredients()
        ingredient2ID = self.getIngredientIDByIngredient(self._ingredient2)
        ingredient3ID = self.getIngredientIDByIngredient(self._ingredient3)
        self.assertIn(ingredient2ID, self._ingredientsDB.ingredients)
        self.assertIn(ingredient3ID, self._ingredientsDB.ingredients)


if __name__ == "__main__":
    unittest.main()
