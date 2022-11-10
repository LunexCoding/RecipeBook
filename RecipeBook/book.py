from .recipe import Recipe
from logger import logger


log = logger.getLogger(__name__)


class RecipeBook:

    def __init__(self):
        self._recipes = []

    def loadRecipes(self):
        self._readRecipeFile()

    def _readRecipeFile(self):
        pass

    def addRecipe(self, recipe):
        self._recipes.append(recipe)
        log.debug(f'Рецепт {recipe.name} добавлен в книгу')

    def deleteRecipeByID(self, _id):
        del self._recipes[_id]

    def getRecipeByID(self, _id):
        return self._recipes[_id]

    # для тестов
    def viewRecipesInfo(self):
        for recipe in self._recipes:
            print(recipe.name, '\t' + 'ingredients:', sep='\n')
            for ingredient in recipe.ingredients:
                print('\t' * 2 + ingredient.name)


g_RecipeBook = RecipeBook()
