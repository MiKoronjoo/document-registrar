from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiCreateAccountWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.accountNameEdit = QLineEdit(self.centralwidget)
        self.accountNameEdit.setObjectName(u"accountNameEdit")
        self.accountNameEdit.setGeometry(QRect(290, 250, 241, 36))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 220, 271, 19))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.cancelBT = QPushButton(self.centralwidget)
        self.cancelBT.setObjectName(u"cancelBT")
        self.cancelBT.setGeometry(QRect(20, 20, 103, 36))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 70, 461, 141))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.createBT = QPushButton(self.centralwidget)
        self.createBT.setObjectName(u"createBT")
        self.createBT.setGeometry(QRect(290, 320, 103, 36))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        from . import UiWalletWindow
        self.createBT.clicked.connect(lambda: self._create(MainWindow))
        self.cancelBT.clicked.connect(lambda: UiWalletWindow().setupUi(MainWindow))

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def _create(self, win):
        name = self.accountNameEdit.text().strip()
        if not name:
            ac = len(win.wallet.accounts) + 1
            name = f'Account {ac}'
        win.wallet.create_account(name)
        from . import UiWalletWindow
        UiWalletWindow().setupUi(win)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Create Account", None))
        # self.accountNameEdit.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.cancelBT.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.createBT.setText(QCoreApplication.translate("MainWindow", u"Create", None))
