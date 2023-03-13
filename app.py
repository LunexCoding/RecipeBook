from book import g_RecipeBook
from recipe import Recipe
from ingredient import Ingredient
from IDGenerator import g_IDGenerator
from storage import g_storage
from ingredientsDB import g_ingredientsDB


class App:
    def __init__(self):
       ...

    def _loading(self):
        g_ingredientsDB.loadIngredients()
        g_RecipeBook.loadRecipes()
        g_ingredientsDB.loadIngredients()

    def run(self):
        self._loading()

    def close(self):
        ...

    def saveData(self):
        ...


app = App()
app.run()
