from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal

from forms.ui_elementIngredient import Ui_elementIngredient


class ElementIngredient(QWidget):
    _delete = Signal(str)
    _addToStorage = Signal(str)

    def __init__(self, widgetID, name="Name", measure="Measure", parent=None):
        super(ElementIngredient, self).__init__(parent)
        self.ui = Ui_elementIngredient()
        self.ui.setupUi(self)
        self._widgetID = widgetID
        self._name = name
        self._measure = measure
        self.ui.nameIngredient.setText(self._name)
        self.ui.measureIngredient.setText(self._measure)

        self.ui.deleteIngredientBtn.clicked.connect(self.delete)
        self.ui.addIngredientToStorageBtn.clicked.connect(self.addToStorage)

    def addToStorage(self):
        self._addToStorage.emit(self._widgetID)

    def delete(self):
        self._delete.emit(self._widgetID)
