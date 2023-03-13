from logger import logger
from IDGenerator import g_IDGenerator
from recipe import Recipe
from filters import baseFilter, filterByFavorite, filterHasAllIngredients
from sortings import baseSorting, sortingByName, sortingByRating
from fileSystem import fileSystem
from customException import TypeException


_RECIPES_DIRECTORY = "data/recipes"
_FILE_SUFFIX = ".json"
_log = logger.getLogger(__name__)


class _RecipeBook:
    def __init__(self):
        self._recipes = {}
        self._filters = {
            "all": baseFilter,
            "byFavorite": filterByFavorite,
            "hasIngridients": filterHasAllIngredients,
        }
        self._sortings = {
            "all": baseSorting,
            "byName": sortingByName,
            "byRating": sortingByRating,
        }
        self._activeFilter = self._filters["all"]
        self._activeSorting = self._sortings["all"]

    def loadRecipes(self):
        _log.debug("Загрузка рецептов начата")
        for recipeFile in fileSystem.getSortedDir(_RECIPES_DIRECTORY):
            self._readRecipeFile(recipeFile)
        _log.debug("Загрузка рецептов закончена")

    def _readRecipeFile(self, filename):
        with filename.open(encoding="utf-8") as file:
            try:
                data = fileSystem.readJson(filename)
                self._addRecipe(
                    fileSystem.getFilename(filename),
                    Recipe(
                        name=data["_name"],
                        ingredients=data["_ingredients"],
                        cookingSteps=data["_cookingSteps"],
                        description=data["_description"],
                        isFavorite=data["_isFavorite"],
                        rating=data["_rating"]
                    )
                )
            except:
                data = {}

    def _addRecipe(self, recipeID, recipe):
        if self._checkRecipeInBook(recipe.name) is False:
            recipeIngredients = {}
            print(recipeID, recipe.ingredients)
            for ingredientID, amount in recipe.ingredients.items():
                recipeIngredients[ingredientID] = amount
            recipe.ingredients = recipeIngredients
            self._recipes[recipeID] = recipe
            _log.debug(f"Рецепт <{recipe.name}> с ID<{recipeID}> загружен в книгу")
        else:
            _log.warning(f"Рецепт <{recipe.name}> с ID<{recipeID}> уже есть в книге")

    def addRecipe(self, recipe):
        if self._checkRecipeInBook(recipe.name) is False:
            self._recipes[g_IDGenerator.getID()] = recipe
            _log.debug(f"Рецепт <{recipe.name}> с ID<{self._getRecipeID(recipe)}> добавлен в книгу")
        else:
            _log.warning(f"Рецепт <{recipe.name}> с ID<{self._getRecipeID(recipe)}>  уже есть в книге")

    def _getRecipeID(self, recipe):
        return "".join([recipeID for recipeID, recipeObj in self._recipes.items() if recipeObj.name == recipe.name])

    def _checkRecipeInBook(self, recipeName):
        return True if recipeName in [recipe.name for recipe in self._recipes.values()] else False

    def writeRecipesFiles(self):
        for recipeID in self._recipes:
            try:
                self._writeRecipeFile(recipeID)
            except TypeException as e:
                _log.error(e)

    def _writeRecipeFile(self, recipeID):
        path = f"{_RECIPES_DIRECTORY}/{recipeID + _FILE_SUFFIX}"
        if not isinstance(self._recipes[recipeID], Recipe):
            raise TypeException(self._recipes[recipeID], type(self._recipes[recipeID]), Recipe.__name__)
        fileSystem.writeJson(path, self._recipes[recipeID])

    def deleteRecipeByID(self, recipeID):
        _log.debug(f"Рецепт {self.getRecipeByID(recipeID).name} с ID{recipeID} был удален из книги")
        del self._recipes[recipeID]

    def filtration(self):
        _log.debug(f"Начата фильтрация {self._activeFilter.__class__}")
        for recipe in self._recipes.values():
            if self._activeFilter.call(recipe):
                self.showRecipe(recipe)
        _log.debug(f"Закончена фильтрация {self._activeFilter.__class__}")

    def changeFilter(self, filter):
        self._activeFilter = self._filters[filter]

    def sorting(self):
        _log.debug(f"Сортировка {self._activeSorting.__class__}")
        self._recipes = self._activeSorting.call(self._recipes)

    def changeSorting(self, sorting):
        self._activeSorting = self._sortings[sorting]()

    def showRecipe(self, recipe):
        # Temporary stub -> GUI
        _log.debug(f"Рецерт <{recipe.name}> c ID<{self._getRecipeID(recipe)}> прошел фильтрацию!")

    def getRecipeByID(self, recipeID):
        return self._recipes[recipeID]

    @property
    def recipes(self):
        return self._recipes


g_RecipeBook = _RecipeBook()
