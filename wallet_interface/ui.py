import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from ui import UiMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    theWindow = QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(theWindow)
    theWindow.show()
    sys.exit(app.exec_())
