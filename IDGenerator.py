class IDGenerator:

    def __init__(self):
        self.__ingredientID = 0
        self.__recipeID = 0

    def loadLastIngredientID(self, lastID=0):
        self.__ingredientID = lastID

    def getIngredientID(self):
        self.__ingredientID += 1
        return self.__ingredientID

    def loadLastRecipeID(self, lastID=0):
        self.__recipeID = lastID

    def getRecipeID(self):
        self.__recipeID += 1
        return self.__recipeID

    @property
    def lastIngredientID(self):
        return self.__ingredientID


g_IDGenerator = IDGenerator()
