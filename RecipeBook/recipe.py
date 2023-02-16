from logger import logger


log = logger.getLogger(__name__)


class Recipe:

    def __init__(self, name=None, ingredients=None, cookingSteps=None, description=None, isFavorite=False, rating=0):
        self._name = name
        self._ingredients = ingredients if ingredients is not None else {}
        self._cookingSteps = cookingSteps
        self._description = description
        self._isFavorite = isFavorite
        self._rating = rating
        log.debug(f"Рецепт <{self._name}> создан")

    def addIngredient(self, ingredientID, amount):
        self._ingredients[ingredientID] = amount

    @property
    def name(self):
        return self._name

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredientDict):
        self._ingredients = ingredientDict

    @property
    def cookingSteps(self):
        return self._cookingSteps

    @property
    def description(self):
        return self._description

    @property
    def isFavorite(self):
        return self._isFavorite

    @property
    def rating(self):
        return self._rating
