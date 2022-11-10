from logger import logger


log = logger.getLogger(__name__)


class Recipe:

    def __init__(self, name=None, ingredients=None, cookingSteps=None, description=None):
        self._name = name
        self._ingredients = ingredients if ingredients is not None else []
        self._cookingSteps = cookingSteps
        self._description = description
        log.debug(f'Рецепт {self._name} создан')

    def addIngredient(self, ingredient):
        self._ingredients.append(ingredient)

    @property
    def name(self):
        return self._name

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def cookingSteps(self):
        return self._cookingSteps

    @property
    def description(self):
        return self._description
