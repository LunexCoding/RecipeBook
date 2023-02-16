from pathlib import Path
from logger import logger
from jsonTools import JsonTools
from ingredient import Ingredient
from IDGenerator import g_IDGenerator


log = logger.getLogger(__name__)
DATABASE_FILE = Path('data/ingredientsDB.json')


class IngredientsDatabase:

    def __init__(self):
        self._ingredients = {}
        self._lastLoadedIngredientID = None

    def loadIngredients(self):
        with DATABASE_FILE.open(encoding='utf-8') as file:
            loadedIngredients = JsonTools.jsonLoad(file) if DATABASE_FILE.stat().st_size != 0 else []
            if loadedIngredients:
                log.debug(f"Начинается загрузка ингредиентов")
                for ingredient in loadedIngredients:
                    self._lastLoadedIngredientID = ingredient
                    ingredientData = loadedIngredients[self._lastLoadedIngredientID]
                    self.addIngredientToDB(
                        Ingredient(
                            ingredientData['_name'],
                            ingredientData['_measure']
                        )
                    )
                g_IDGenerator.loadLastIngredientID(int(self._lastLoadedIngredientID))
                self._lastLoadedIngredientID = None
                log.debug(f"Загрузка ингредиентов завершена")

    def addIngredientToDB(self, ingredient):
        if self._lastLoadedIngredientID is not None:
            self._ingredients[int(self._lastLoadedIngredientID)] = ingredient
        else:
            if self._checkIngredientInDB(ingredient):
                self._ingredients[g_IDGenerator.getIngredientID()] = ingredient
                log.debug(f"Ингредиент <{ingredient.name}> добавлен в базу")

    def _checkIngredientInDB(self, ingredient):
        return False if (ingredient.name in [ingredientDB.name for ingredientDB in self._ingredients.values()]) else True

    def updateFile(self):
        with DATABASE_FILE.open('w', encoding='utf-8') as file:
            JsonTools.jsonWrite(self._ingredients, file)

    def getIngredientByID(self, ingredientID):
        return self._ingredients[ingredientID]

    def deleteIngredientByID(self, ingredientID):
        log.debug(f"Ингредиент <{self.getIngredientByID(ingredientID).name}> с ID<{ingredientID}> удален из базы")
        del self._ingredients[ingredientID]

    @property
    def ingredients(self):
        return self._ingredients


g_ingredientsDB = IngredientsDatabase()
