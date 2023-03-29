from Custom_Widgets.Widgets import QDialog
from forms.ui_addProductDialog import Ui_addProductDialog


class AddProductDialog(QDialog):
    def __init__(self, ingredient, parent=None):
        super(AddProductDialog, self).__init__(parent)
        self.ui = Ui_addProductDialog()
        self.ui.setupUi(self)
        self._name = ingredient.name
        self._measure = ingredient.measure
        self.ui.nameIngredient.setText(self._name)
        self.ui.measureIngredient.setText(self._measure)
        self.ui.labelErrorAddProduct.hide()
        self.ui.createBtn.clicked.connect(self.validate)

    def validate(self):
        self._amount = self.ui.inputAmount.text()
        if not self._amount:
            self.showFillingErrorAddIProduct()
            self.ui.inputAmount.setFocus()
        try:
            self._amount = float(self._amount)
            self.close()
            return True
        except:
            self.showFillingErrorAddIProduct()
            self.ui.inputAmount.selectAll()
            self.ui.inputAmount.setFocus()

    def showFillingErrorAddIProduct(self):
        if len(self.ui.inputAmount.text()) == 0:
            self.ui.labelErrorAddProduct.setText("Fields must be filled")
        else:
            self.ui.labelErrorAddProduct.setText("The number must not be less than zero")
        self.ui.labelErrorAddProduct.show()

    @property
    def amount(self):
        return self._amount

