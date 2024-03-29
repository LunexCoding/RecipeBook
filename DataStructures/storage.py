from helpers.logger import logger
from DataStructures.ingredientsDB import g_ingredientsDB
from helpers.fileSystem import fileSystem
from event import Event


_log = logger.getLogger(__name__)
_STORAGE_FILE = "../data/storage.json"


class Storage:
    def __init__(self):
        self._products = {}
        self.onProductAdded = Event()
        self.onProductUpdated = Event()
        self.onProductDeleted = Event()

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
            self.onProductUpdated.trigger(productID, oldAmout + amount)
        else:
            self._products[productID] = amount
            _log.debug(f"Продукт <{g_ingredientsDB.getIngredientByID(productID).name}> с ID<'{productID}'> добавлен в хранилище")
            self.onProductAdded.trigger(productID, amount)

    def resetProductAmount(self, productID, amount):
        if productID in self._products:
            self._products[productID] = amount

    def getProductByID(self, productID):
        return g_ingredientsDB.getIngredientByID(productID)

    def getProductAmountByID(self, productID):
        return self._products[productID]

    def deleteProductByID(self, productID):
        if productID in self._products:
            _log.debug(f"Продукт <{self.getProductByID(productID).name}> с ID<'{productID}'> был удален из хранилище")
            del self._products[productID]
            self.onProductDeleted.trigger(productID)

    @property
    def products(self):
        return self._products


g_storage = Storage()
