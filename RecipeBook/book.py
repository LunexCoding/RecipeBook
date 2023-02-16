from pathlib import Path
from logger import logger
from jsonTools import JsonTools
from IDGenerator import g_IDGenerator
from RecipeBook import Recipe
from filters import BaseFilter, FilterByName, FilterByFavorite, FilterByRating, HasAllIngredientsFilter


RECIPES_DIRECTORY = Path("data/recipes")
FILE_SUFFIX = ".json"
log = logger.getLogger(__name__)


class _RecipeBook:

    def __init__(self):
        self._recipes = {}
        self._lastLoadedRecipeID = None
        self._filters = {
            'all': BaseFilter,
            'byName': FilterByName,
            'byFavorite': FilterByFavorite,
            'byRating': FilterByRating,
            'hasIngridients': HasAllIngredientsFilter,
        }
        self._activeFilter = self._filters['all']()

    def loadRecipes(self):
        if sorted(RECIPES_DIRECTORY.glob('*.json')):
            for recipeFile in RECIPES_DIRECTORY.iterdir():
                self._lastLoadedRecipeID = int(recipeFile.stem)
                self._readRecipeFile(recipeFile)
            g_IDGenerator.loadLastRecipeID(self._lastLoadedRecipeID)
            self._lastLoadedRecipeID = None

    def _readRecipeFile(self, filename):
        with filename.open(encoding='utf-8') as file:
            data = JsonTools.jsonLoad(file) if filename.stat().st_size != 0 else {}
            if data:
                self.addRecipe(
                    Recipe(
                        name=data['_name'],
                        ingredients=data["_ingredients"],
                        cookingSteps=data['_cookingSteps'],
                        description=data['_description'],
                        isFavorite=data['_isFavorite'],
                        rating=data['_rating']
                    )
                )

    def addRecipe(self, recipe):
        if self._checkRecipeInBook(recipe.name):
            recipeIngredients = {}
            for ingredientID, amount in recipe.ingredients.items():
                recipeIngredients[int(ingredientID)] = amount
            recipe.ingredients = recipeIngredients
            if self._lastLoadedRecipeID is not None:
                self._recipes[int(self._lastLoadedRecipeID)] = recipe
            else:
                self._recipes[g_IDGenerator.getRecipeID()] = recipe
            log.debug(f'Рецепт <{recipe.name}> добавлен в книгу')
        else:
            log.warning(f'Рецепт <{recipe.name}> уже есть в книге')

    def _checkRecipeInBook(self, recipeName):
        return True if recipeName not in [self.getRecipeByID(recipe).name for recipe in self._recipes] else False

    def writeRecipesFiles(self):
        for recipeID in self._recipes:
            self._writeRecipeFile(recipeID)

    def _writeRecipeFile(self, recipeID):
        path = RECIPES_DIRECTORY / str(recipeID)
        with path.with_suffix(FILE_SUFFIX).open('w', encoding='utf-8') as file:
            JsonTools.jsonWrite(self._recipes[recipeID], file)

    def deleteRecipeByID(self, recipeID):
        log.debug(f'Рецепт {self.getRecipeByID(recipeID).name} с ID {recipeID} был удален из книги')
        del self._recipes[recipeID]

    def filtration(self):
        log.debug(f'Начата фильтрация {self._activeFilter.__class__}')
        if isinstance(self._activeFilter, (FilterByName, FilterByRating)):
            self._recipes = self._activeFilter.call(self._recipes)
        else:
            for recipe in self._recipes.values():
                if self._activeFilter.call(recipe):
                    self.showRecipe(recipe)

    def changeFilter(self, filter):
        self._activeFilter = self._filters[filter]()

    def showRecipe(self, recipe):
        # Temporary stub -> GUI
        log.debug(f'Рецерт <{recipe.name}> прошел фильтрацию!')

    def getRecipeByID(self, recipeID):
        return self._recipes[recipeID]

    @property
    def recipes(self):
        return self._recipes


g_RecipeBook = _RecipeBook()
