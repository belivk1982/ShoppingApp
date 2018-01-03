from PyQt5 import QtWidgets

import sys
import  ui_login

class Main():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        prijava =  ui_login.Ui_Prijava()
        prijava.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main = Main()