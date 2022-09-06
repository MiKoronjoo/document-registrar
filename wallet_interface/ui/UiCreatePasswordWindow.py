import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiCreatePasswordWindow(object):
    def setupUi(self, createPasswordWindow):
        if not createPasswordWindow.objectName():
            createPasswordWindow.setObjectName(u"createPasswordWindow")
        createPasswordWindow.resize(800, 600)
        self.centralwidget = QWidget(createPasswordWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 270, 131, 19))
        self.backBT = QPushButton(self.centralwidget)
        self.backBT.setObjectName(u"backBT")
        self.backBT.setGeometry(QRect(20, 20, 103, 36))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 50, 461, 141))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.importBT = QPushButton(self.centralwidget)
        self.importBT.setObjectName(u"importBT")
        self.importBT.setGeometry(QRect(270, 370, 103, 36))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 190, 281, 19))
        self.errorMsgLabel = QLabel(self.centralwidget)
        self.errorMsgLabel.setObjectName(u"errorMsgLabel")
        self.errorMsgLabel.setGeometry(QRect(270, 340, 291, 21))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.errorMsgLabel.setFont(font1)
        self.passEdit = QLineEdit(self.centralwidget)
        self.passEdit.setObjectName(u"passEdit")
        self.passEdit.setEchoMode(QLineEdit.Password)
        self.passEdit.setGeometry(QRect(270, 220, 291, 36))
        self.pass2Edit = QLineEdit(self.centralwidget)
        self.pass2Edit.setEchoMode(QLineEdit.Password)
        self.pass2Edit.setObjectName(u"pass2Edit")
        self.pass2Edit.setGeometry(QRect(270, 300, 291, 36))
        createPasswordWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(createPasswordWindow)
        self.statusbar.setObjectName(u"statusbar")
        createPasswordWindow.setStatusBar(self.statusbar)

        self.retranslateUi(createPasswordWindow)

        from . import UiMainWindow
        self.backBT.clicked.connect(lambda: UiMainWindow().setupUi(createPasswordWindow))
        self.importBT.clicked.connect(lambda: self.create_wallet(createPasswordWindow))
        QMetaObject.connectSlotsByName(createPasswordWindow)

    def check_password(self):
        msg = ''
        if self.passEdit.text() != self.pass2Edit.text():
            msg = 'passwords does not match'
        elif len(self.passEdit.text()) < 8 or len(self.passEdit.text()) > 32:
            msg = 'password length should between 8-32 characters'
        else:
            return True
        self.errorMsgLabel.setText(QCoreApplication.translate("ImportWalletWindow",
                                                              f"<html><head/><body><p><span style=\" color:#ff0000;\">{msg}</span></p></body></html>",
                                                              None))
        return False

    def create_wallet(self, win):
        if self.check_password():
            win.wallet.set_password(self.passEdit.text())
            win.wallet.create_wallet(12)
            from . import UiCreateWalletWindow
            UiCreateWalletWindow().setupUi(win)

    def retranslateUi(self, createPasswordWindow):
        createPasswordWindow.setWindowTitle(
            QCoreApplication.translate("createPasswordWindow", u"Create Password", None))
        self.label_3.setText(QCoreApplication.translate("createPasswordWindow", u"Confirm Password", None))
        self.backBT.setText(QCoreApplication.translate("createPasswordWindow", u"back", None))
        self.label_2.setText(QCoreApplication.translate("createPasswordWindow", u"Create Password", None))
        self.importBT.setText(QCoreApplication.translate("createPasswordWindow", u"Create", None))
        self.label.setText(QCoreApplication.translate("createPasswordWindow", u"New Password (8 Characters min)", None))
