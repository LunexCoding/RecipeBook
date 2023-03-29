# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteIngredientDialogeelQXH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class DeleteIngredientDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(300, 200))
        Dialog.setMaximumSize(QSize(300, 200))
        Dialog.setStyleSheet(u"* {\n"
"	background-color: #1f232a;;\n"
"\n"
"	color: #fff;\n"
"}\n"
"\n"
"#nameIngredient, #measureIngredient {\n"
"	margin-left: 20px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nameIngredient = QLabel(self.frame_2)
        self.nameIngredient.setObjectName(u"nameIngredient")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameIngredient)

        self.label4 = QLabel(self.frame_2)
        self.label4.setObjectName(u"label4")
        self.label4.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label4)

        self.measureIngredient = QLabel(self.frame_2)
        self.measureIngredient.setObjectName(u"measureIngredient")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.measureIngredient)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_2.addWidget(self.buttonBox)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Are you sure you want to remove the following ingredient:", None))
        self.nameIngredient.setText(QCoreApplication.translate("Dialog", u"name", None))
        self.label4.setText(QCoreApplication.translate("Dialog", u"measure:", None))
        self.measureIngredient.setText(QCoreApplication.translate("Dialog", u"measure", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"name:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Once an ingredient is removed, recipes using that ingredient will be invalid.", None))
    # retranslateUi

