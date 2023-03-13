# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addProductDialogCksffM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_addProductDialog(object):
    def setupUi(self, addProductDialog):
        if not addProductDialog.objectName():
            addProductDialog.setObjectName(u"addProductDialog")
        addProductDialog.resize(280, 335)
        addProductDialog.setMinimumSize(QSize(280, 335))
        addProductDialog.setMaximumSize(QSize(280, 335))
        addProductDialog.setStyleSheet(u"* {\n"
"	color: #fff;\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #16191d;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(addProductDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(addProductDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_3)
        self.formLayout.setObjectName(u"formLayout")
        self.nameIngredient = QLabel(self.frame_3)
        self.nameIngredient.setObjectName(u"nameIngredient")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameIngredient)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.measureIngredient = QLabel(self.frame_3)
        self.measureIngredient.setObjectName(u"measureIngredient")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.measureIngredient)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_20 = QFrame(self.frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_20)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.labelErrorAddProduct = QLabel(self.frame_20)
        self.labelErrorAddProduct.setObjectName(u"labelErrorAddProduct")
        self.labelErrorAddProduct.setFont(font1)
        self.labelErrorAddProduct.setStyleSheet(u"color: red")
        self.labelErrorAddProduct.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.labelErrorAddProduct)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_32.addItem(self.verticalSpacer)

        self.label_22 = QLabel(self.frame_20)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_32.addWidget(self.label_22)

        self.inputAmount = QLineEdit(self.frame_20)
        self.inputAmount.setObjectName(u"inputAmount")
        self.inputAmount.setMinimumSize(QSize(200, 0))
        self.inputAmount.setMaximumSize(QSize(300, 16777215))
        self.inputAmount.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)
        self.inputAmount.setClearButtonEnabled(True)

        self.verticalLayout_32.addWidget(self.inputAmount)


        self.verticalLayout_2.addWidget(self.frame_20, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.createBtn = QPushButton(self.frame_2)
        self.createBtn.setObjectName(u"createBtn")

        self.horizontalLayout.addWidget(self.createBtn)

        self.buttonBox = QDialogButtonBox(self.frame_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(addProductDialog)
        self.buttonBox.rejected.connect(addProductDialog.reject)
        QMetaObject.connectSlotsByName(addProductDialog)
    # setupUi

    def retranslateUi(self, addProductDialog):
        addProductDialog.setWindowTitle(QCoreApplication.translate("addProductDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("addProductDialog", u"Add product", None))
        self.label_6.setText(QCoreApplication.translate("addProductDialog", u"Selected Ingredient", None))
        self.nameIngredient.setText(QCoreApplication.translate("addProductDialog", u"name", None))
        self.label_2.setText(QCoreApplication.translate("addProductDialog", u"Name:", None))
        self.label_4.setText(QCoreApplication.translate("addProductDialog", u"Measure:", None))
        self.measureIngredient.setText(QCoreApplication.translate("addProductDialog", u"measure", None))
        self.labelErrorAddProduct.setText(QCoreApplication.translate("addProductDialog", u"The number must not be less than zero", None))
        self.label_22.setText(QCoreApplication.translate("addProductDialog", u"Amount", None))
        self.createBtn.setText(QCoreApplication.translate("addProductDialog", u"Create", None))
    # retranslateUi

