from pathlib import Path
from logger import logger
from .recipe import Recipe
from jsonTools import JsonTools


log = logger.getLogger(__name__)


class RecipeBook:

    def __init__(self):
        self._recipes = []

    def loadRecipes(self):
        self._readRecipeFile()

    def _readRecipeFile(self):
        pass

    def writeRecipeFile(self, _id):
        with Path(f"./data/recipes/{_id}.json").open('w', encoding='utf-8') as file:
            JsonTools.jsonWrite(self._recipes[_id], file)

    def addRecipe(self, recipe):
        self._recipes.append(recipe)
        log.debug(f'Рецепт <{recipe.name}> добавлен в книгу')

    def deleteRecipeByID(self, _id):
        del self._recipes[_id]
        log.debug(f'Рецепт {self._recipes[_id].name} с ID {_id} был удален из книги')

    def getRecipeByID(self, _id):
        return self._recipes[_id]


g_RecipeBook = RecipeBook()
