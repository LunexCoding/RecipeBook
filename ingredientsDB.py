from logger import logger
from ingredient import Ingredient
from IDGenerator import g_IDGenerator
from fileSystem import fileSystem


_log = logger.getLogger(__name__)
_DATABASE_FILE = "data/ingredientsDB.json"


class IngredientsDatabase:
    def __init__(self):
        self._ingredients = {}

    def loadIngredients(self):
        try:
            loadedIngredients = fileSystem.readJson(_DATABASE_FILE)
            _log.debug(f"Начинается загрузка ингредиентов")
            for ingredientID, ingredientData in loadedIngredients.items():
                self._addIngredient(
                    ingredientID,
                    Ingredient(
                        ingredientData["_name"],
                        ingredientData["_measure"]
                    )
                )
            _log.debug(f"Загрузка ингредиентов завершена")
        except:
            _log.error("Не удалось загрузить ингредиенты в базу")

    def _addIngredient(self, ingredientID, ingredient):
        if self._checkIngredientInDB(ingredient) is False:
            self._ingredients[ingredientID] = ingredient
            _log.debug(f"Ингредиент <{ingredient.name}> с ID<'{ingredientID}'> загружен в базу")
        else:
            _log.debug(f"Ингредиент <{ingredient.name}> с ID<'{ingredientID}'> уже находится в базе")

    def addIngredientToDB(self, ingredient):
        if self._checkIngredientInDB(ingredient) is False:
            self._ingredients[g_IDGenerator.getID()] = ingredient
            _log.debug(f"Ингредиент <{ingredient.name}> с ID<'{self._getIngredientID(ingredient)}'> добавлен в базу")
        else:
            _log.warning(f"Ингредиент <{ingredient.name}> с ID<'{self._getIngredientID(ingredient)}'> уже находится в базе")

    def _getIngredientID(self, ingredient):
        return "".join([ingredientID for ingredientID, ingredientObj in self._ingredients.items() if ingredientObj.name == ingredient.name])

    def _checkIngredientInDB(self, ingredient):
        return True if ((ingredient.name, ingredient.measure) in [(ingredientDB.name, ingredientDB.measure) for ingredientDB in self._ingredients.values()]) else False

    def writeDBFile(self):
        fileSystem.writeJson(_DATABASE_FILE, self._ingredients)

    def getIngredientByID(self, ingredientID):
        return self._ingredients[ingredientID]

    def deleteIngredientByID(self, ingredientID):
        _log.debug(f"Ингредиент <{self.getIngredientByID(ingredientID).name}> с ID<'{ingredientID}'> удален из базы")
        del self._ingredients[ingredientID]

    @property
    def ingredients(self):
        return self._ingredients


g_ingredientsDB = IngredientsDatabase()
