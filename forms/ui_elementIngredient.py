# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'elementIngredientxkTyPA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_elementIngredient(object):
    def setupUi(self, elementIngredient):
        if not elementIngredient.objectName():
            elementIngredient.setObjectName(u"elementIngredient")
        elementIngredient.resize(343, 133)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elementIngredient.sizePolicy().hasHeightForWidth())
        elementIngredient.setSizePolicy(sizePolicy)
        elementIngredient.setStyleSheet(u"* {\n"
"	border: None;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	color: #fff;\n"
"	background-color: #1f232a;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(elementIngredient)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(elementIngredient)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(350, 100))
        self.groupBox.setStyleSheet(u"")
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


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.deleteIngredientBtn = QPushButton(self.frame)
        self.deleteIngredientBtn.setObjectName(u"deleteIngredientBtn")
        icon = QIcon()
        icon.addFile(u":/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteIngredientBtn.setIcon(icon)
        self.deleteIngredientBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.deleteIngredientBtn)

        self.addIngredientToStorageBtn = QPushButton(self.frame)
        self.addIngredientToStorageBtn.setObjectName(u"addIngredientToStorageBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/truck.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addIngredientToStorageBtn.setIcon(icon1)
        self.addIngredientToStorageBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.addIngredientToStorageBtn)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(elementIngredient)

        QMetaObject.connectSlotsByName(elementIngredient)
    # setupUi

    def retranslateUi(self, elementIngredient):
        elementIngredient.setWindowTitle(QCoreApplication.translate("elementIngredient", u"Form", None))
        self.groupBox.setTitle("")
        self.nameIngredient.setText(QCoreApplication.translate("elementIngredient", u"name", None))
        self.measureIngredient.setText(QCoreApplication.translate("elementIngredient", u"measure", None))
        self.deleteIngredientBtn.setText("")
        self.addIngredientToStorageBtn.setText("")
    # retranslateUi

