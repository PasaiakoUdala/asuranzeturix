import configparser
import os.path
import sys
from os.path import expanduser
from pathlib import Path

from PyQt5.QtWidgets import QDialog , QApplication

from ui.hobespenak import Ui_Dialog

home = expanduser("~")
SETTINGS_DIR = os.path.join(home , '.asuranzeturix/')
SETTINGS_FILE = os.path.join(home , '.asuranzeturix/config')
SETTINGS = {}


class MainWindow(QDialog , Ui_Dialog):
    def __init__( self , parent = None ):
        super(MainWindow , self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.gorde)

    def gorde( self ):
        print("gorde")
        if not os.path.isfile(SETTINGS_FILE):
            os.makedirs(SETTINGS_DIR)
            Path(SETTINGS_FILE).touch()
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


def read_config( ):
    parser = configparser.ConfigParser()
    parser.read(SETTINGS_FILE)
    confdict = {section: dict(parser.items(section)) for section in parser.sections()}
    return confdict


def main( ):
    print("Yaml irakurtzen")
    SETTINGS = read_config()



if __name__ == '__main__':
    if not os.path.isfile(SETTINGS_FILE):
        print("Ez da existitzen")
        app = QApplication(sys.argv)
        form = MainWindow()
        form.show()
        sys.exit(app.exec_())

    main()
