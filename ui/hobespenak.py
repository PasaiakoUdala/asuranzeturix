# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/hobespenak.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 396)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 441, 181))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 40, 81, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 81, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 120, 81, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(0, 160, 81, 18))
        self.label_4.setObjectName("label_4")
        self.txtZerbitzaria = QtWidgets.QLineEdit(self.groupBox)
        self.txtZerbitzaria.setGeometry(QtCore.QRect(90, 30, 291, 30))
        self.txtZerbitzaria.setObjectName("txtZerbitzaria")
        self.txtPortua = QtWidgets.QLineEdit(self.groupBox)
        self.txtPortua.setGeometry(QtCore.QRect(90, 70, 291, 30))
        self.txtPortua.setObjectName("txtPortua")
        self.txtUsername = QtWidgets.QLineEdit(self.groupBox)
        self.txtUsername.setGeometry(QtCore.QRect(90, 110, 291, 30))
        self.txtUsername.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(self.groupBox)
        self.txtPassword.setGeometry(QtCore.QRect(90, 150, 291, 30))
        self.txtPassword.setObjectName("txtPassword")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 230, 421, 80))
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.txtEmaila = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtEmaila.setGeometry(QtCore.QRect(90, 40, 291, 30))
        self.txtEmaila.setObjectName("txtEmaila")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(0, 50, 81, 18))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "AMI Server"))
        self.label.setText(_translate("Dialog", "Zerbitzaria:"))
        self.label_2.setText(_translate("Dialog", "Portua:"))
        self.label_3.setText(_translate("Dialog", "Erabiltzailea:"))
        self.label_4.setText(_translate("Dialog", "Pasahitza:"))
        self.groupBox_2.setTitle(_translate("Dialog", "Erabiltzailea"))
        self.label_5.setText(_translate("Dialog", "Emaila"))

