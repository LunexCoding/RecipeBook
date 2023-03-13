import PySide2
from PySide2.QtCore import QSize, QRect, QPoint, Qt
from PySide2.QtWidgets import QLayout


class FlowLayout(QLayout):
    def __init__(self, margin=0, spacing=0, parent=None):
        super(FlowLayout, self).__init__()
        if parent is None:
            self.setMargin(margin)
        self.setSpacing(spacing)
        self._itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, arg__1: PySide2.QtWidgets.QLayoutItem) -> None:
        self._itemList.append(arg__1)

    def count(self) -> int:
        return len(self._itemList)

    def itemAt(self, index: int) -> PySide2.QtWidgets.QLayoutItem:
        if 0 <= index < len(self._itemList):
            return self._itemList[index]

    def takeAt(self, index: int) -> PySide2.QtWidgets.QLayoutItem:
        if 0 <= index < len(self._itemList):
            return self._itemList.pop(index)

    def expandingDirections(self) -> PySide2.QtCore.Qt.Orientations:
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self) -> bool:
        return True

    def heightForWidth(self, arg__1: int) -> int:
        return self.processing(QRect(0, 0, arg__1, 0))

    def setGeometry(self, arg__1: PySide2.QtCore.QRect) -> None:
        super(FlowLayout, self).setGeometry(arg__1)
        self.processing(arg__1)

    def sizeHint(self) -> PySide2.QtCore.QSize:
        return self.minimumSize()

    def minimumSize(self) -> PySide2.QtCore.QSize:
        size = QSize()
        for item in self._itemList:
            size = size.expandedTo(item.minimumSize())

        size += QSize(
            2 * self.contentsMargins().top(),
            2 * self.contentsMargins().top()
        )
        return size

    def processing(self, rect):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self._itemList:
            spaceX = self.spacing()
            spaceY = self.spacing()
            nextX = x + item.sizeHint().width() + spaceX
            if (nextX - spaceX > rect.right()) and (lineHeight > 0):
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight + rect.y()
