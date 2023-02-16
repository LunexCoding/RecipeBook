import unittest
from pathlib import Path
import ingredientsDB
from ingredientsDB import IngredientsDatabase
from ingredient import Ingredient
from fileSystem import FileSystem


class TestIngredientsDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._ingredientsDB = IngredientsDatabase()
        cls._fileSystem = FileSystem()


    def test_addIngredientToDB(self):
        self._ingredientsDB.addIngredientToDB(
            Ingredient(
                name='Tea',
                measure='kg'
            )
        )
        ingredientID = [ingredientID for ingredientID, ingredient in self._ingredientsDB.ingredients.items() if ingredient.name == 'Tea']
        self.assertIn('Tea', [ingredient.name for ingredient in self._ingredientsDB.ingredients.values()])
        self._ingredientsDB.deleteIngredientByID(*ingredientID)
        self.assertNotIn(*ingredientID, self._ingredientsDB.ingredients)

    def test_addDuplicateIngredientToDB(self):
        self._ingredientsDB.addIngredientToDB(
            Ingredient(
                name='Meat',
                measure='kg'
            )
        )
        self._ingredientsDB.addIngredientToDB(
            Ingredient(
                name='Meat',
                measure='kg'
            )
        )
        self.assertEqual(self._ingredientsDB.ingredients[1].name, 'Meat')
        self.assertNotIn(2, self._ingredientsDB.ingredients)
        self._ingredientsDB.deleteIngredientByID(1)
        self.assertNotIn(1, self._ingredientsDB.ingredients)

    def test_fileOperations(self):
        ingredientsDB.DATABASE_FILE = Path('fixtures/ingredientsDB.json')
        self._ingredientsDB.addIngredientToDB(
            Ingredient(
                name='Salt',
                measure='kg'
            )
        )
        self._ingredientsDB.addIngredientToDB(
            Ingredient(
                name='Apple',
                measure='thin'
            )
        )
        self._ingredientsDB.updateFile()
        self._ingredientsDB.loadIngredients()
        self.assertIn(3, self._ingredientsDB.ingredients)
        self.assertIn(4, self._ingredientsDB.ingredients)
        self._fileSystem.removeFile('fixtures/ingredientsDB.json')


if __name__ == '__main__':
    unittest.main()
