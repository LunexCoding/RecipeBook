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

    def addProduct(self, product, amount):
        self._products[product] = amount
        log.debug(f'Продукт <{g_ingredientsDB.getIngredientByID(product).name}> был добавлен в хранилище')

    def getProductByID(self, _id):
        return g_ingredientsDB.getIngredientByID(_id)

    def deleteProductByID(self, _id):
        del self._products[_id]
        log.debug(f'Продукт <{self.getProductByID(_id).name}> с ID<{_id}> был удален из хранилище')


g_storage = Storage()
