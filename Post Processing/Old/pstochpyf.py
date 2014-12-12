from PyQt4 import QtCore, QtGui
from pstochpyf1 import *
import sys


if __name__ == "__main__":
     import sys
     from PyQt4.QtGui import QApplication, QDialog
     from pstochpyf1 import Ui_Dialog
     app = QApplication(sys.argv)
     window = QDialog()
     ui = Ui_Dialog()
     ui.setupUi(window)
     window.show()
     sys.exit(app.exec_())
