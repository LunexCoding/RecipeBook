from RecipeBook import Ingredient


class Storage:

    def __init__(self):
        self._productsList = []

    def addProduct(self, args):
        pass

    def deleteProduct(self, args):
        pass

    @property
    def productList(self):
        return self._productsList


g_storage = Storage()
