import sys
from PyQt5 import QtWidgets

from utility.qt.qt_excute import QtMainWindow
from utility.ui.main_window import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

