from storage import g_storage
from logger import logger


log = logger.getLogger(__name__)


class BaseFilter:
    def call(self, recipe):
        return True


class FilterByFavorite(BaseFilter):
    def call(self, recipe):
        return True if recipe.isFavorite is True else False


class HasAllIngredientsFilter(BaseFilter):
    def call(self, recipe):
        listBool = []
        for ingredientID, ingredientAmount in recipe.ingredients.items():
            if ingredientID in g_storage.products:
                if ingredientAmount <= g_storage.products[ingredientID]:
                    listBool.append(True)
                else:
                    listBool.append(False)
        return True if all(listBool) else False
