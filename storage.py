from logger import logger
from ingredientsDB import g_ingredientsDB
from fileSystem import fileSystem


_log = logger.getLogger(__name__)
_STORAGE_FILE = "data/storage.json"


class Storage:
    def __init__(self):
        self._products = {}

    def loadProducts(self):
        try:
            loadedProduct = fileSystem.readJson(_STORAGE_FILE)
            _log.debug(f"Начинается заполнение хранилища")
            for productID, amount in loadedProduct.items():
                self.addProduct(productID, amount)
            _log.debug(f"Заполнение хранилища завершено")
        except:
            _log.error("Не удалось загрузить продукты в хранилище")

    def writeStorageFile(self):
        fileSystem.writeJson(_STORAGE_FILE, self._products)

    def addProduct(self, productID, amount):
        if productID in self._products:
            oldAmout = self._products[productID]
            self._products[productID] = oldAmout + amount
            _log.debug(f"Продукт <{g_ingredientsDB.getIngredientByID(productID).name}> с ID<'{productID}'> изменил количество с {oldAmout} на {self._products[productID]}")
        else:
            self._products[productID] = amount
            _log.debug(f"Продукт <{g_ingredientsDB.getIngredientByID(productID).name}> с ID<'{productID}'> добавлен в хранилище")

    def getProductByID(self, productID):
        return g_ingredientsDB.getIngredientByID(productID)

    def getProductAmountByID(self, productID):
        return self._products[productID]

    def deleteProductByID(self, productID):
        del self._products[productID]
        _log.debug(f"Продукт <{self.getProductByID(productID).name}> с ID<'{productID}'> был удален из хранилище")

    @property
    def products(self):
        return self._products

g_storage = Storage()
