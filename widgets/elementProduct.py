from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal

from forms.ui_elementProduct import Ui_elementProduct
from storage import g_storage


class ElementProduct(QWidget):
    _delete = Signal(str)
    _edit = Signal(str)
    _save = Signal(str, float)
    _update = Signal(str, float)

    def __init__(self, widgetID, ingredient, amount, parent=None):
        super(ElementProduct, self).__init__(parent)
        g_storage.onProductUpdated.register(self._onProductAdded)
        self.ui = Ui_elementProduct()
        self.ui.setupUi(self)
        self._widgetID = widgetID
        self._name = ingredient.name
        self._measure = ingredient.measure
        self._amount = amount
        self.ui.nameIngredient.setText(self._name)
        self.ui.measureIngredient.setText(self._measure)
        self.ui.amount.setText(str(amount))

        self.ui.deleteProductBtn.clicked.connect(self.delete)
        self.ui.editProductBtn.clicked.connect(self._showEdit)
        self.ui.saveBtn.clicked.connect(self.saveChanges)
        self.ui.cancelBtn.clicked.connect(self._closeEdit)
        self._closeEdit()

    def validate(self):
        amount = self.ui.inputAmount.text()
        if not amount:
            self.ui.inputAmount.setFocus()
        try:
            self._amount = float(amount)
            self.close()
            return True
        except:
            self.ui.inputAmount.selectAll()
            self.ui.inputAmount.setFocus()

    def delete(self):
        self._delete.emit(self._widgetID)

    def _onProductAdded(self, productID, amount):
        print("product added", productID)
        print(amount)
        if productID == self._widgetID:
            self.ui.amount.setText(str(amount))

    def saveChanges(self):
        if self.validate():
            self._closeEdit()
            self.ui.amount.setText(str(self._amount))
            self._save.emit(self._widgetID, self._amount)

    def _showEdit(self):
        self.ui.inputAmount.show()
        self.ui.buttonBox.show()

    def _closeEdit(self):
        self.ui.inputAmount.hide()
        self.ui.buttonBox.hide()
