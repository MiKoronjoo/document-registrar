import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from wallet import Wallet, create_database_if_not_exists
from ui import UiMainWindow, UiLoginWindow, UiRegistrarWindow
from utils import Registrar
from config import CONTRACT_ADDRESS, RPC_URL

create_database_if_not_exists()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    theWindow = QMainWindow()
    theWindow.wallet = Wallet()
    theWindow.registrar = Registrar(CONTRACT_ADDRESS, RPC_URL)
    if theWindow.wallet.check_database():
        ui = UiLoginWindow()
    else:
        ui = UiMainWindow()
    ui.setupUi(theWindow)
    theWindow.show()
    sys.exit(app.exec_())
