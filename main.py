import configparser
import os.path
import sys
from os.path import expanduser
from pathlib import Path

from PyQt5.QtWidgets import QDialog , QApplication

from ui.hobespenak import Ui_Dialog

home = expanduser("~")
SETTINGS_DIR = os.path.join(home , '.asuranzeturix/')
SETTINGS = os.path.join(home , '.asuranzeturix/config')


class MainWindow(QDialog , Ui_Dialog):
    def __init__( self , parent = None ):
        super(MainWindow , self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.gorde)

    def gorde( self ):
        print("gorde")
        if not os.path.isfile(SETTINGS):
            os.makedirs(SETTINGS_DIR)
            Path(SETTINGS).touch()
        server = self.txtZerbitzaria.text()
        portua = self.txtPortua.text()
        user = self.txtUsername.text()
        passwd = self.txtPassword.text()
        email = self.txtEmaila.text()

        config = configparser.ConfigParser()
        config['AMI'] = {
            'zerbitzaria'  : server ,
            'portua'       : portua ,
            'erabiltzailea': user ,
            'pasahitza'    : passwd
        }
        config['USER'] = {
            'email': email
        }

        with open(SETTINGS , 'w') as configfile:
            config.write(configfile)


def main( ):
    print("Yaml irakurtzen")


if __name__ == '__main__':
    if not os.path.isfile(SETTINGS):
        print("Ez da existitzen")
        app = QApplication(sys.argv)
        form = MainWindow()
        form.show()
        sys.exit(app.exec_())

    main()
