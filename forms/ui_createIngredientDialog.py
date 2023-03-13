# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createIngredientDialogteodyf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class DialogCreateIngredient(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(200, 200)
        Dialog.setMinimumSize(QSize(200, 200))
        Dialog.setMaximumSize(QSize(200, 200))
        font = QFont()
        font.setPointSize(13)
        Dialog.setFont(font)
        Dialog.setContextMenuPolicy(Qt.NoContextMenu)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet(u"* {\n"
"	background: transparent;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#widget {\n"
"	background-color: #343b47;\n"
"}\n"
"")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setFont(font)
        self.widget.setAutoFillBackground(False)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        self.label_4.setFont(font1)
        self.label_4.setVisible(False)

        self.verticalLayout_2.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.centralContainer = QFrame(self.widget)
        self.centralContainer.setObjectName(u"centralContainer")
        self.centralContainer.setMaximumSize(QSize(300, 300))
        self.centralContainer.setFrameShape(QFrame.StyledPanel)
        self.centralContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.centralContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralContainer)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(8)
        self.label.setFont(font2)

        self.verticalLayout.addWidget(self.label)

        self.nameIngredient = QLineEdit(self.centralContainer)
        self.nameIngredient.setObjectName(u"nameIngredient")
        self.nameIngredient.setMaxLength(25)
        self.nameIngredient.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.nameIngredient)

        self.label_2 = QLabel(self.centralContainer)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.measureIngredient = QLineEdit(self.centralContainer)
        self.measureIngredient.setObjectName(u"measureIngredient")
        self.measureIngredient.setAutoFillBackground(False)
        self.measureIngredient.setStyleSheet(u"")
        self.measureIngredient.setMaxLength(25)
        self.measureIngredient.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.measureIngredient)

        self.buttonBox = QDialogButtonBox(self.centralContainer)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font2)
        self.buttonBox.setTabletTracking(False)
        self.buttonBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.buttonBox.setAcceptDrops(False)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.centralContainer)


        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def showErrorLabel(self):
        if not self.label_4.isVisible():
            self.label_4.setVisible(True)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Create Indredient", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u043d\u0433\u0440\u0435\u0434\u0438\u0435\u043d\u0442\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"All fields must be filled!", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0438\u043d\u0433\u0440\u0435\u0434\u0438\u0435\u043d\u0442\u0430", None))
        self.nameIngredient.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.measureIngredient.setText("")
    # retranslateUi

