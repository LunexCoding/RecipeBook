from pathlib import Path
from logger import logger
from jsonTools import JsonTools
from ingredientsDB import g_ingredientsDB


log = logger.getLogger(__name__)
STORAGE_FILE = Path('data/storage.json')


class Storage:

    def __init__(self):
        self._products = {}

    def loadProducts(self):
        with STORAGE_FILE.open(encoding='utf-8') as file:
            loadedProduct = JsonTools.jsonLoad(file) if STORAGE_FILE.stat().st_size != 0 else {}
            if loadedProduct:
                log.debug(f"Начинается заполнение хранилища")
                for _id, amount in loadedProduct.items():
                    self.addProduct(int(_id), amount)
                log.debug(f"Заполнение хранилища завершено")

    def updateFile(self):
        with STORAGE_FILE.open('w', encoding='utf-8') as file:
            JsonTools.jsonWrite(self._products, file)

    def addProduct(self, productID, amount):
        if productID in self._products:
            oldAmout = self._products[productID]
            self._products[productID] = oldAmout + amount
            log.debug(f'Продукт <{g_ingredientsDB.getIngredientByID(productID).name}> с ID<{productID}> изменил количество с {oldAmout} на {self._products[productID]}')
        else:
            self._products[productID] = amount
            log.debug(f'Продукт <{g_ingredientsDB.getIngredientByID(productID).name}> с ID<{productID}> добавлен в хранилище')

    def getProductIDByID(self, productID):
        return g_ingredientsDB.getIngredientByID(productID)

    def deleteProductByID(self, productID):
        del self._products[productID]
        log.debug(f'Продукт <{self.getProductIDByID(productID).name}> с ID<{productID}> был удален из хранилище')

    @property
    def products(self):
        return self._products

g_storage = Storage()
