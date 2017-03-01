#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtGui



class LaVentanita(QtGui.QDialog):
    def __init__( self , parent = None ):
        # creada una ventana QDialog con QT-Designer,
        # exportado con pyuic4 ventananita.ui > ventanita.py
        # o pyuic4 -o ventananita.py ventananita.ui
        # o pyuic4 -x ventananita.ui -o ventananita.py
        # -x para generar código extra para test y ver la clase al ejecutar
        QtGui.QDialog.__init__(self , parent)  # o super(LaVentanita, self).__init__(parent)
        self.ventana = QtGui.QDialog(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self.ventana)
        # self.ventana.setWindowTitle("Esta ventanita")
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.MiBotonAceptar)
        self.ui.pushButton.clicked.connect(self.PulsaPushButton)

    def MiBotonAceptar( self ):
        self.ui.buttonBox.button(QtGui.QDialogButtonBox.Cancel).setText(u"Cancélate")

    def PulsaPushButton( self ):
        pass


if __name__ == '__main__':
    pass