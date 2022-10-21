from .recipe import Recipe


class RecipeBook:

    def __init__(self):
        pass

    def _loadRecipes(self):
        pass

    def _readRecipeFile(self):
        pass

    def createRecipe(self, args):
        return Recipe(args)

    def deleteRecipe(self):
        pass

    def getRecipeByRecipeId(self, _id):
        pass

    def viewRecipes(self): # or Recipe._view
        pass


g_RecipeBook = RecipeBook()
