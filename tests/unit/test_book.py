import unittest
import book
from book import _RecipeBook
from recipe import Recipe
from fileSystem import FileSystem
from filters import _BaseFilter, _FilterByFavorite, _HasAllIngredientsFilter


_FIXTURES_DIRECTORY = "fixtures"
_RECIPES_DIRECTORY = f"{_FIXTURES_DIRECTORY}/recipes"
_FILE_SUFFIX = ".json"


class TestRecipeBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._book = _RecipeBook()
        cls._fileSystem = FileSystem()
        cls._fileSystem.makeDirs(_RECIPES_DIRECTORY)

        cls._recipe1 = Recipe(
                name="Капустница",
                ingredients={
                    2: 300,
                    3: 2
                },
                cookingSteps={
                    "1": "Белокочанную капусту промываем под холодной водой, чистим лук и морковь.",
                    "2": "Капусту нарезаем тонкой соломкой.",
                    "3": "Морковь натираем на крупной терке, лук нарезаем кубиками, чеснок либо мелко-мелко нарезаем, либо пропускаем через чесночницу.",
                    "4": "Все овощи перекладываем в одну посуду.",
                    "5": "Поливаем салат подсолнечным маслом и уксусом, добавляем немножко сахара и соли. Хорошенько перемешиваем."
                },
                description="Едва ли не самый популярный гарнир к котлетам в простых столовых.",
                isFavorite=True,
                rating=12
            )
        cls._recipe2 = Recipe(
            name="Bread",
            ingredients={
                1: 300,
                2: 2
            },
            cookingSteps={
                "1": "Белокочанную капусту промываем под холодной водой, чистим лук и морковь.",
                "2": "Капусту нарезаем тонкой соломкой.",
                "3": "Морковь натираем на крупной терке, лук нарезаем кубиками, чеснок либо мелко-мелко нарезаем, либо пропускаем через чесночницу.",
                "4": "Все овощи перекладываем в одну посуду.",
                "5": "Поливаем салат подсолнечным маслом и уксусом, добавляем немножко сахара и соли. Хорошенько перемешиваем."
            },
            description="Едва ли не самый популярный гарнир к котлетам в простых столовых.",
            isFavorite=True,
            rating=6
        )

    @classmethod
    def tearDownClass(cls):
        cls._fileSystem.removeTree(_FIXTURES_DIRECTORY)

    @classmethod
    def getRecipeIDByRecipe(cls, recipe):
        return "".join([recipeID for recipeID, recipeObj in cls._book.recipes.items() if recipeObj.name == recipe.name])

    def test_addRecipe(self):
        self._book.addRecipe(self._recipe1)
        self._book.addRecipe(self._recipe1)
        self._book.addRecipe(self._recipe2)
        recipe1ID = self.getRecipeIDByRecipe(self._recipe1)
        recipe2ID = self.getRecipeIDByRecipe(self._recipe2)
        self.assertIn(recipe1ID, self._book.recipes)
        self.assertIn(recipe2ID, self._book.recipes)
        self.assertEqual(self._book.recipes[recipe1ID].name, "Капустница")
        self.assertEqual(self._book.recipes[recipe2ID].name, "Bread")

    def test_changeFilter(self):
        self._book.changeFilter("byFavorite")
        self.assertIsInstance(self._book._activeFilter, _FilterByFavorite)
        self._book.changeFilter("hasIngridients")
        self.assertIsInstance(self._book._activeFilter, _HasAllIngredientsFilter)
        self._book.changeFilter("all")
        self.assertIsInstance(self._book._activeFilter, _BaseFilter)

    def test_deleteRecipeByID(self):
        recipeID = self.getRecipeIDByRecipe(self._recipe1)
        self._book.deleteRecipeByID(recipeID)
        self.assertNotIn(recipeID, self._book.recipes)

    def test_writeRecipesFilesAndLoadRecipes(self):
        recipeID = self.getRecipeIDByRecipe(self._recipe2)
        book._RECIPES_DIRECTORY = _RECIPES_DIRECTORY
        self._book.writeRecipesFiles()
        self.assertTrue(self._fileSystem.exists(f"{_RECIPES_DIRECTORY}/{recipeID}{_FILE_SUFFIX}"))
        self._book._recipes = {}
        self._book.loadRecipes()
        self.assertTrue(len(self._book.recipes) != 0)
        self.assertIn(recipeID, self._book.recipes)
        self.assertEqual(self._book.recipes[recipeID].name, "Bread")


if __name__ == "__main__":
    unittest.main()
