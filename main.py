from Custom_Widgets.Widgets import *

from forms.ui_interface import Ui_MainWindow
from widgets.elementIngredient import ElementIngredient
from widgets.elementProduct import ElementProduct
from widgets.flowLayout import FlowLayout
from forms.ui_deleteIngredientDialog import DeleteIngredientDialog
from widgets.addProductDialog import AddProductDialog

from logger import logger
from ingredient import Ingredient
from ingredientsDB import g_ingredientsDB
from storage import g_storage


_log = logger.getLogger(__name__)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.show()

        # events
        g_ingredientsDB.onIngredientAdded.register(self.__ingredientAdded)
        g_ingredientsDB.onIngredientDeleted.register(self.__ingredientDeleted)
        g_storage.onProductAdded.register(self.__addProductToPage)
        g_storage.onProductUpdated.register(self.__updateProduct)
        g_storage.onProductDeleted.register(self.__deleteProduct)

        # show / hide some elements
        self.ui.labelErrorAddIngredient.hide()

        # init custom Layouts
        self.flowIngredientLayout = FlowLayout()
        self.ui.ingredientLayout.addLayout(self.flowIngredientLayout)
        self.flowProductLayout = FlowLayout()
        self.ui.productLayout.addLayout(self.flowProductLayout)

        # открыть виджет центрального меню
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        # закрыть виджета центрального меню
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # открыть виджет правого меню
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        # закрыть виджет правого меню
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        # закрыть виджет меню уведомления
        self.ui.closeNotifacationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        # connect buttons
        self.ui.saveIngredientBtn.clicked.connect(lambda: self.createIngredient())

    def showErrorLabelAddIngredient(self, message):
        self.ui.labelErrorAddIngredient.setText(message)
        self.ui.labelErrorAddIngredient.show()

    def showFillingErrorAddIngredient(self, message):
        self.ui.labelErrorAddIngredient.setText()
        self.ui.labelErrorAddIngredient.show()

    # ingredient
    def createIngredient(self):
        nameIngredient = self.ui.inputNameIngredient.text()
        measureIngredient = self.ui.inputMeasureIngredient.text()
        if all([len(nameIngredient), (measureIngredient)]):
            ingredientID = g_ingredientsDB.addIngredientToDB(
                Ingredient(
                    name=nameIngredient,
                    measure=measureIngredient
                )
            )
            self.ui.labelErrorAddIngredient.hide()
            if ingredientID is None:
                self.showErrorLabelAddIngredient("Ingredient already exists")
        else:
            self.showErrorLabelAddIngredient("All fields must be filled!")

    def __ingredientAdded(self, widgetID, ingredient):
        itemIngredient = ElementIngredient(widgetID, ingredient.name, ingredient.measure)
        self.flowIngredientLayout.addWidget(itemIngredient)
        itemIngredient._delete.connect(self._ingredientDelete)
        itemIngredient._addToStorage.connect(self.addIngredientToStorage)

    def _ingredientDelete(self, ingredientID):
        dialog = QtWidgets.QDialog()
        ui = DeleteIngredientDialog()
        ui.setupUi(dialog)
        
        ingredient = g_ingredientsDB.getIngredientByID(ingredientID)
        ui.nameIngredient.setText(ingredient.name)
        ui.measureIngredient.setText(ingredient.measure)
        
        dialog.show()
        responce = dialog.exec_()
        if responce == QtWidgets.QDialog.Accepted:
            g_ingredientsDB.deleteIngredientByID(ingredientID)

    def __ingredientDeleted(self):
        widget = self.sender()
        self.flowIngredientLayout.removeWidget(widget)
        widget.deleteLater()

    # product
    def addIngredientToStorage(self, ingredientID):
        widget = self.sender()
        ingredient = g_ingredientsDB.getIngredientByID(ingredientID)
        dialog = AddProductDialog(ingredient)
        responce = dialog.exec_()
        while not dialog.validate():
            dialog.show()
            if responce == QtWidgets.QDialog.Rejected:
                break
        else:
            amount = dialog.amount
            g_storage.addProduct(ingredientID, amount)

    def __addProductToPage(self, productID, amount):
        ingredient = g_ingredientsDB.getIngredientByID(productID)
        itemProduct = ElementProduct(productID, ingredient, amount)
        self.flowProductLayout.addWidget(itemProduct)
        itemProduct._delete.connect(self._deleteProduct)
        itemProduct._edit.connect(self.editProductAmount)
        itemProduct._save.connect(self.editProductAmount)
        itemProduct._update.connect(self.__updateProduct)

    def _deleteProduct(self, productID):
        g_storage.deleteProductByID(productID)

    def __deleteProduct(self, widgetID):
        widget = self.sender()
        self.flowProductLayout.removeWidget(widget)
        widget.deleteLater()

    def __updateProduct(self, productID, amount):
        widget = self.sender()
        g_storage.resetProductAmount(productID, amount)

    def editProductAmount(self, widgetID, amount):
        widget = self.sender()
        widget.show()
        g_storage.resetProductAmount(widgetID, amount)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
