class Fridge:

    def __init__(self):
        self._productsList = None

    def addProduct(self, args):
        # Продукт, это одно и то же что и ингредиент? Или необязательно указывать сколько в граммах колбасы или
        # литров молока в наличии?
        pass

    def deleteProduct(self, args):
        pass

    @property
    def productList(self):
        return self._productsList
