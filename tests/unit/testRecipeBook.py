import unittest
from pathlib import Path
from logger import logger
from RecipeBook import book, Recipe, g_RecipeBook
from ingredient import Ingredient
from ingredientsDB import g_ingredientsDB


log = logger.getLogger(__name__)


class TestRecipeBook(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        g_ingredientsDB.addIngredientToDB(
            Ingredient(
                name="Slime",
                measure="Thing"
            )
        )

        g_ingredientsDB.addIngredientToDB(
            Ingredient(
                name="Salt",
                measure="Gr"
            )
        )

        g_ingredientsDB.addIngredientToDB(
            Ingredient(
                name="Apple",
                measure="Thing"
            )
        )

        g_RecipeBook.addRecipe(
            Recipe(
                name="Салат",
                ingredients={
                    1: 3,
                    2: 500
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
                rating=10
            )
        )
        g_RecipeBook.addRecipe(
            Recipe(
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
        )


    def test_1_ingredient(self):
        ingredient1 = g_ingredientsDB.getIngredientByID(1)
        ingredient2 = g_ingredientsDB.getIngredientByID(2)
        ingredient3 = g_ingredientsDB.getIngredientByID(3)
        self.assertEqual([ingredient1.name, ingredient1.measure], ["Slime", "Thing"], "Ингредиент <Slime> в измерении <Thing> добавлен в базу")
        self.assertEqual([ingredient2.name, ingredient2.measure], ["Salt", "Gr"], "Ингредиент <Salt> в измерении <Gr> добавлен в базу")
        self.assertEqual([ingredient3.name, ingredient3.measure], ["Apple", "Thing"], "Ингредиент <Apple> в измерении <Thing> добавлен в базу")

    def test_2_recipe(self):
        recipe = g_RecipeBook.getRecipeByID(2)
        self.assertEqual([recipe.name, [g_ingredientsDB.getIngredientByID(ingredient).name for ingredient in recipe.ingredients]], ["Капустница", ['Salt', 'Apple']], "Рецепт <Капустница> из <['Salt', 'Apple']> добавлен в базу")

    def test_3_recipe_addIngredient(self):
        recipe = g_RecipeBook.getRecipeByID(1)
        ingredient = 3
        recipe.addIngredient(ingredient, 500)
        self.assertEqual([recipe.name, [g_ingredientsDB.getIngredientByID(ingredient).name for ingredient in recipe.ingredients]], ["Салат", ['Slime', 'Salt', 'Apple']], "В рецепт <Салат> добавлен ингредиент <Apple>")

    def test_4_book_addRecipe(self):
        recipe = g_RecipeBook.getRecipeByID(1)
        g_RecipeBook.addRecipe(recipe)
        self.assertIn(recipe, g_RecipeBook.recipes.values(), "Рецепт <Капустница> добавлен в книгу")
        g_RecipeBook.addRecipe(recipe)  # duplicate
        self.assertNotIn(recipe, g_RecipeBook.recipes, "Рецепт <Капустница> уже был добавлен в книгу")

    def test_5_book_deleteRecipe(self):
        recipe = g_RecipeBook.getRecipeByID(2)
        g_RecipeBook.deleteRecipeByID(2)
        self.assertNotIn(recipe, g_RecipeBook.recipes, "Рецепт <Капустница> удален из книги")

    def test_6_book_writeRecipesFiles(self):
        book.RECIPES_DIRECTORY = Path("fixtures/recipes")
        g_RecipeBook.writeRecipesFiles()

    def test_7_filters_FilterByName(self):
        recipeListBeforeFiltration = [recipe.name for recipe in g_RecipeBook.recipes.values()]
        g_RecipeBook.changeFilter('byName')
        g_RecipeBook.filtration()
        log.debug(f"{recipeListBeforeFiltration} | {[recipe.name for recipe in g_RecipeBook.recipes.values()]}")
        self.assertEqual(recipeListBeforeFiltration, [recipe.name for recipe in g_RecipeBook.recipes.values()])

    def test_8_filters_FilterByRating(self):
        ...

    def test_9_filters_FilterByFavorite(self):
        ...

    def test_10_filters_HasAllIngredientsFilter(self):
        ...


if __name__ == '__main__':
    unittest.main()
