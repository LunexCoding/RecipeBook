from logger import logger


log = logger.getLogger(__name__)


class IngredientsDatabase:

    def __init__(self):
        self._ingredients = []

    def addIngredientToDB(self, ingredient):
        self._ingredients.append(ingredient)
        log.debug(f"Ингредиент {ingredient.name} добавлен в базу")

    def getIngredientByID(self, _id):
        return self._ingredients[_id]

    def deleteIngredientByID(self, _id):
        del self._ingredients[_id]


g_ingredientsDB = IngredientsDatabase()
