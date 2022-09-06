from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiWalletWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.accountNameLabel = QLabel(self.centralwidget)
        self.accountNameLabel.setObjectName(u"accountNameLabel")
        self.accountNameLabel.setGeometry(QRect(300, 50, 211, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.accountNameLabel.setFont(font)
        self.accountNameLabel.setScaledContents(False)
        self.accountNameLabel.setAlignment(Qt.AlignCenter)
        self.addressLabel = QLabel(self.centralwidget)
        self.addressLabel.setObjectName(u"addressLabel")
        self.addressLabel.setGeometry(QRect(300, 90, 211, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.addressLabel.setFont(font1)
        self.addressLabel.setScaledContents(False)
        self.addressLabel.setAlignment(Qt.AlignCenter)
        self.balanceLabel = QLabel(self.centralwidget)
        self.balanceLabel.setObjectName(u"balanceLabel")
        self.balanceLabel.setGeometry(QRect(220, 130, 371, 81))
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setWeight(75)
        self.balanceLabel.setFont(font2)
        self.balanceLabel.setScaledContents(False)
        self.balanceLabel.setAlignment(Qt.AlignCenter)
        self.copyBT = QPushButton(self.centralwidget)
        self.copyBT.setObjectName(u"copyBT")
        self.copyBT.setGeometry(QRect(478, 86, 41, 36))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(610, 46, 171, 37))
        self.importBT = QPushButton(self.centralwidget)
        self.importBT.setObjectName(u"importBT")
        self.importBT.setGeometry(QRect(660, 130, 121, 36))
        self.createBT = QPushButton(self.centralwidget)
        self.createBT.setObjectName(u"createBT")
        self.createBT.setGeometry(QRect(660, 90, 121, 36))
        self.lockBT = QPushButton(self.centralwidget)
        self.lockBT.setObjectName(u"lockBT")
        self.lockBT.setGeometry(QRect(10, 47, 103, 36))
        self.showRegistersBT = QPushButton(self.centralwidget)
        self.showRegistersBT.setObjectName(u"showRegistersBT")
        self.showRegistersBT.setGeometry(QRect(340, 300, 121, 36))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(340, 350, 121, 36))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        from . import UiImportAccountWindow, UiCreateAccountWindow
        self.lockBT.clicked.connect(lambda: self._lock(MainWindow))
        self.copyBT.clicked.connect(lambda: self._copy(MainWindow))
        self.importBT.clicked.connect(lambda: UiImportAccountWindow().setupUi(MainWindow))
        self.createBT.clicked.connect(lambda: UiCreateAccountWindow().setupUi(MainWindow))

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.comboBox.currentIndexChanged.connect(lambda: self._select_account(MainWindow))

    def _select_account(self, win):
        index = self.comboBox.currentIndex()
        win.wallet.selected_index = index
        account = win.wallet.selected
        self.accountNameLabel.setText(account.name)
        self.addressLabel.setText(self.str_addr(account.address))
        self.balanceLabel.setText("1 ETH")

    def _lock(self, win):
        from . import UiLoginWindow
        win.wallet.lock()
        UiLoginWindow().setupUi(win)

    def _copy(self, win):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)

        cb.setText(win.wallet.selected.address, mode=cb.Clipboard)

    def str_addr(self, address: str):
        return address[:5] + '...' + address[-4:]

    def retranslateUi(self, MainWindow):
        account = MainWindow.wallet.selected
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Document Registrar", None))
        self.accountNameLabel.setText(QCoreApplication.translate("MainWindow", account.name, None))
        self.addressLabel.setText(QCoreApplication.translate("MainWindow", self.str_addr(account.address), None))
        self.balanceLabel.setText(QCoreApplication.translate("MainWindow", u"73.0132 ETH", None))
        self.copyBT.setText(QCoreApplication.translate("MainWindow", u"copy", None))
        for i, acc in enumerate(MainWindow.wallet.accounts):
            self.comboBox.addItem("")
            label = acc.name
            if acc.is_imported:
                label += ' | imported'
            self.comboBox.setItemText(i, QCoreApplication.translate("MainWindow", label, None))

        self.comboBox.setCurrentIndex(MainWindow.wallet.selected_index)

        self.importBT.setText(QCoreApplication.translate("MainWindow", u"Import Account", None))
        self.createBT.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.lockBT.setText(QCoreApplication.translate("MainWindow", u"Lock", None))
        self.showRegistersBT.setText(QCoreApplication.translate("MainWindow", u"register a file", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"show registers", None))
