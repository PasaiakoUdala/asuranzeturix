import configparser
import os.path , sys
from os.path import expanduser
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic
from ui.hobespenak import Ui_Dialog

home = expanduser("~")
SETTINGS = home + "/.asuranzeturix/config"




app = QApplication()

window = QDialog()

ui = Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())