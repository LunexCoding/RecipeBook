from storage import g_storage


class _BaseFilter:
    def call(self, recipe):
        return True


class _FilterByFavorite(_BaseFilter):
    def call(self, recipe):
        return True if recipe.isFavorite is True else False


class _HasAllIngredientsFilter(_BaseFilter):
    def call(self, recipe):
        listBool = []
        for ingredientID, ingredientAmount in recipe.ingredients.items():
            if ingredientID in g_storage.products:
                if ingredientAmount <= g_storage.products[ingredientID]:
                    listBool.append(True)
                else:
                    listBool.append(False)
        return True if all(listBool) else False


baseFilter = _BaseFilter()
filterByFavorite = _FilterByFavorite()
filterHasAllIngredients = _HasAllIngredientsFilter()
