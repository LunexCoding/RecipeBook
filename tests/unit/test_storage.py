import unittest
from unittest.mock import patch, PropertyMock, Mock
import storage
from storage import Storage
from ingredient import Ingredient
from fileSystem import FileSystem
from IDGenerator import g_IDGenerator
import ingredientsDB


_FIXTURES_DIRECTORY = "fixtures"
_STORAGE_FILE = f"{_FIXTURES_DIRECTORY}/storage.json"


class TestStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._fileSystem = FileSystem()
        cls._fileSystem.makeDir(_FIXTURES_DIRECTORY)

        cls._storage = Storage()

        cls._ingredient1 = Ingredient(
            name="Tea",
            measure="kg"
        )
        cls._ingredient2 = Ingredient(
            name="Meat",
            measure="kg"
        )
        cls._ingredient3 = Ingredient(
            name="Salt",
            measure="kg"
        )
        cls._amount1 = 5
        cls._amount2 = 7
        cls._amount3 = 2
        cls._amount1AfterDuplicate = cls._amount1 * 2
        cls._amount2AfterDuplicate = cls._amount2 * 2
        cls._amount3AfterDuplicate = cls._amount3 * 2

        dataDB = {
            g_IDGenerator.getID(): cls._ingredient1,
            g_IDGenerator.getID(): cls._ingredient2,
            g_IDGenerator.getID(): cls._ingredient3,
        }

        cls._ingredientsDB = Mock()
        cls._ingredientsDB._ingredients = dataDB
        type(cls._ingredientsDB).ingredients = PropertyMock(return_value=cls._ingredientsDB._ingredients)

        cls._ingredient1ID = cls.getIngredientIDByIngredient(cls._ingredient1)
        cls._ingredient2ID = cls.getIngredientIDByIngredient(cls._ingredient2)
        cls._ingredient3ID = cls.getIngredientIDByIngredient(cls._ingredient3)

    @classmethod
    def tearDownClass(cls):
        cls._fileSystem.removeTree(_FIXTURES_DIRECTORY)

    @classmethod
    def getIngredientIDByIngredient(cls, ingredient):
        return "".join([ingredientID for ingredientID, ingredientObj in cls._ingredientsDB.ingredients.items() if (ingredientObj.name == ingredient.name and ingredientObj.measure == ingredient.measure)])

    @patch.object(ingredientsDB._IngredientsDatabase, "getIngredientByID")
    def test_addProduct(self, mockGetIngredientByID):
        mockGetIngredientByID.return_value = self._ingredient1
        self._storage.addProduct(self._ingredient1ID, self._amount1)
        mockGetIngredientByID.return_value = self._ingredient2
        self._storage.addProduct(self._ingredient2ID, self._amount2)
        mockGetIngredientByID.return_value = self._ingredient3
        self._storage.addProduct(self._ingredient3ID, self._amount3)
        self.assertIn(self._ingredient1ID, self._storage.products)
        self.assertIn(self._ingredient2ID, self._storage.products)
        self.assertIn(self._ingredient3ID, self._storage.products)
        self.assertEqual(self._storage.getProductAmountByID(self._ingredient1ID), self._amount1)
        self.assertEqual(self._storage.getProductAmountByID(self._ingredient2ID), self._amount2)
        self.assertEqual(self._storage.getProductAmountByID(self._ingredient3ID), self._amount3)
        # duplicates
        mockGetIngredientByID.return_value = self._ingredient1
        self._storage.addProduct(self._ingredient1ID, self._amount1)
        mockGetIngredientByID.return_value = self._ingredient2
        self._storage.addProduct(self._ingredient2ID, self._amount2)
        mockGetIngredientByID.return_value = self._ingredient3
        self._storage.addProduct(self._ingredient3ID, self._amount3)
        self.assertEqual(self._storage.getProductAmountByID(self._ingredient1ID), self._amount1AfterDuplicate)
        self.assertEqual(self._storage.getProductAmountByID(self._ingredient2ID), self._amount2AfterDuplicate)
        self.assertEqual(self._storage.getProductAmountByID(self._ingredient3ID), self._amount3AfterDuplicate)

    @patch.object(ingredientsDB._IngredientsDatabase, "getIngredientByID")
    def test_deleteProductByID(self, mockGetIngredientByID):
        mockGetIngredientByID.return_value = self._ingredient1
        self._storage.deleteProductByID(self._ingredient1ID)
        self.assertNotIn(self._ingredient1ID, self._storage.products)

    @patch.object(ingredientsDB._IngredientsDatabase, "getIngredientByID")
    def test_writeAndLoadStorageFile(self, mockGetIngredientByID):
        storage._STORAGE_FILE = _STORAGE_FILE
        self._storage.writeStorageFile()
        self.assertTrue(self._fileSystem.exists(_STORAGE_FILE))
        self._storage._products = {}
        self._storage.loadProducts()  # проблема с логом (test/unit/logs/log.md) вместо имени ингредиента
        # MagicMock name='getIngredientByID().name' id='2720856815824'>, чтобы хоть как-то противодействовать этому
        # нужно перед загрузкой добавить mockGetIngredientByID.return_value = self._ingredient2, но это не совсем решает
        # проблему. В лог пишутся все продукты с именем self._ingredient2 и с разными ID. Есть ли способ исправить это?
        mockGetIngredientByID.return_value = self._ingredient2
        self.assertIn(self._ingredient2ID, self._storage.products)
        mockGetIngredientByID.return_value = self._ingredient3
        self.assertIn(self._ingredient3ID, self._storage.products)
        self.assertEqual(self._storage.getProductAmountByID(self._ingredient2ID), self._amount2AfterDuplicate)
        self.assertEqual(self._storage.getProductAmountByID(self._ingredient3ID), self._amount3AfterDuplicate)


if __name__ == "__main__":
    unittest.main()
