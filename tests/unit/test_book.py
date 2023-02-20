import unittest
from pathlib import Path
from RecipeBook import Recipe, book
from RecipeBook.book import _RecipeBook
from fileSystem import FileSystem
from logger import logger
from filters import BaseFilter, FilterByFavorite, HasAllIngredientsFilter


log = logger.getLogger(__name__)


class TestRecipeBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._book = _RecipeBook()
        cls._fileSystem = FileSystem()
        cls._fileSystem.initTree([Path("fixtures/recipes")])

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
        cls._fileSystem.removeTree("fixtures/recipes")

    def test_addRecipe(self):
        self._book.addRecipe(self._recipe1)
        self._book.addRecipe(self._recipe1)
        self._book.addRecipe(self._recipe2)
        self.assertEqual(self._book.recipes[1].name, 'Капустница')
        self.assertEqual(self._book.recipes[2].name, 'Bread')

    def test_changeFilter(self):
        self._book.changeFilter("byFavorite")
        self.assertIsInstance(self._book._activeFilter, FilterByFavorite)
        self._book.changeFilter("hasIngridients")
        self.assertIsInstance(self._book._activeFilter, HasAllIngredientsFilter)
        self._book.changeFilter("all")
        self.assertIsInstance(self._book._activeFilter, BaseFilter)

    def test_deleteRecipeByID(self):
        self._book.deleteRecipeByID(1)
        log.debug(self._book.recipes)
        self.assertNotIn(1, self._book.recipes)
        self._book.addRecipe(self._recipe1)

    def test_writeRecipesFiles(self):
        book.RECIPES_DIRECTORY = Path("fixtures/recipes")
        self._book.writeRecipesFiles()
        log.debug(self._fileSystem.getFileNameWithSuffix(self._fileSystem.listDir(book.RECIPES_DIRECTORY)))
        self.assertTrue(set(["2.json", "3.json"]).issubset(self._fileSystem.getFileNameWithSuffix(self._fileSystem.listDir(book.RECIPES_DIRECTORY))))

    def test_loadRecipes(self):
        self._book.loadRecipes()

if __name__ == '__main__':
    unittest.main()
