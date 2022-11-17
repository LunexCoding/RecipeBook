from pathlib import Path
from logger import logger
from jsonTools import JsonTools
from RecipeBook.ingredient import Ingredient


log = logger.getLogger(__name__)
DATABASE_FILE = Path('data/ingredientsDB.json')


class IngredientsDatabase:

    def __init__(self):
        self._ingredients = []

    def loadIngredients(self):
        with DATABASE_FILE.open(encoding='utf-8') as file:
            loadedIngredients = JsonTools.jsonLoad(file) if DATABASE_FILE.stat().st_size != 0 else []
            if loadedIngredients:
                log.debug(f"Начинается загрузка ингредиентов")
                for ingredient in loadedIngredients:
                    self.addIngredientToDB(
                        Ingredient(
                            ingredient['_name'],
                            ingredient['_measure']
                        )
                    )
                log.debug(f"Загрузка ингредиентов завершена")

    def updateFile(self):
        with DATABASE_FILE.open('w', encoding='utf-8') as file:
            JsonTools.jsonWrite(self._ingredients, file)

    def addIngredientToDB(self, ingredient):
        self._ingredients.append(ingredient)
        log.debug(f"Ингредиент <{ingredient.name}> добавлен в базу")

    def getIngredientByID(self, _id):
        return self._ingredients[_id]

    def deleteIngredientByID(self, _id):
        log.debug(f"Ингредиент <{self.getIngredientByID(_id).name}> с ID<{_id}> удален из базы")
        del self._ingredients[_id]



g_ingredientsDB = IngredientsDatabase()
