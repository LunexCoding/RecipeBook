# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementProductlgphFh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_elementProduct(object):
    def setupUi(self, elementProduct):
        if not elementProduct.objectName():
            elementProduct.setObjectName(u"elementProduct")
        elementProduct.resize(194, 185)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementProduct.sizePolicy().hasHeightForWidth())
        elementProduct.setSizePolicy(sizePolicy)
        elementProduct.setMinimumSize(QSize(0, 0))
        elementProduct.setMaximumSize(QSize(350, 190))
        elementProduct.setStyleSheet(u"* {\n"
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
        self.verticalLayout_2 = QVBoxLayout(elementProduct)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(elementProduct)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setStyleSheet(u"border: none")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 15, 0, 0)
        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nameIngredient = QLabel(self.frame_2)
        self.nameIngredient.setObjectName(u"nameIngredient")

        self.verticalLayout.addWidget(self.nameIngredient)

        self.measureIngredient = QLabel(self.frame_2)
        self.measureIngredient.setObjectName(u"measureIngredient")

        self.verticalLayout.addWidget(self.measureIngredient)

        self.amount = QLabel(self.frame_2)
        self.amount.setObjectName(u"amount")
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.amount.setFont(font)
        self.amount.setMouseTracking(False)

        self.verticalLayout.addWidget(self.amount)

        self.inputAmount = QLineEdit(self.frame_2)
        self.inputAmount.setObjectName(u"inputAmount")
        self.inputAmount.setMaximumSize(QSize(120, 16777215))
        self.inputAmount.setAutoFillBackground(False)
        self.inputAmount.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.inputAmount.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.inputAmount)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.deleteProductBtn = QPushButton(self.frame)
        self.deleteProductBtn.setObjectName(u"deleteProductBtn")
        icon = QIcon()
        icon.addFile(u":/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteProductBtn.setIcon(icon)
        self.deleteProductBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.deleteProductBtn)

        self.editProductBtn = QPushButton(self.frame)
        self.editProductBtn.setObjectName(u"editProductBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.editProductBtn.setIcon(icon1)
        self.editProductBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.editProductBtn)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.buttonBox = QFrame(elementProduct)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFrameShape(QFrame.StyledPanel)
        self.buttonBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttonBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.saveBtn = QPushButton(self.buttonBox)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout_2.addWidget(self.saveBtn)

        self.cancelBtn = QPushButton(self.buttonBox)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_2.addWidget(self.cancelBtn)


        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(elementProduct)

        QMetaObject.connectSlotsByName(elementProduct)
    # setupUi

    def retranslateUi(self, elementProduct):
        elementProduct.setWindowTitle(QCoreApplication.translate("elementProduct", u"Form", None))
        self.groupBox.setTitle("")
        self.nameIngredient.setText(QCoreApplication.translate("elementProduct", u"name", None))
        self.measureIngredient.setText(QCoreApplication.translate("elementProduct", u"measure", None))
        self.amount.setText(QCoreApplication.translate("elementProduct", u"amount", None))
        self.deleteProductBtn.setText("")
        self.editProductBtn.setText("")
        self.saveBtn.setText(QCoreApplication.translate("elementProduct", u"Save", None))
        self.cancelBtn.setText(QCoreApplication.translate("elementProduct", u"Cancel", None))
    # retranslateUi

