from RecipeBook import g_RecipeBook
from IDGenerator import g_IDGenerator
from storage import g_storage
from ingredientsDB import g_ingredientsDB


class App:
    def __init__(self):
       ...

    def _loading(self):
        try:
            g_ingredientsDB.loadIngredients()
            g_storage.loadProducts()
            g_RecipeBook.loadRecipes()
            g_RecipeBook.filtration()
            g_RecipeBook.sorting()
            g_RecipeBook.changeFilter("hasIngridients")
            g_RecipeBook.changeSorting("byName")
            g_RecipeBook.filtration()

        except IndexError:
            g_IDGenerator.loadLastIngredientID()

    def run(self):
        self._loading()

    def close(self):
        ...

    def saveData(self):
        ...


app = App()
app.run()