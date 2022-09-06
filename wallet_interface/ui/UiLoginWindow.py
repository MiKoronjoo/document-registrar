from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiLoginWindow(object):
    def setupUi(self, loginWindow):
        if not loginWindow.objectName():
            loginWindow.setObjectName(u"loginWindow")
        loginWindow.resize(800, 600)
        self.centralwidget = QWidget(loginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 60, 461, 141))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.passEdit = QLineEdit(self.centralwidget)
        self.passEdit.setObjectName(u"passEdit")
        self.passEdit.setEchoMode(QLineEdit.Password)
        self.passEdit.setGeometry(QRect(310, 240, 201, 36))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 210, 91, 19))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 290, 201, 36))
        loginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(loginWindow)
        self.statusbar.setObjectName(u"statusbar")
        loginWindow.setStatusBar(self.statusbar)
        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName("error_label")
        self.error_label.setGeometry(QRect(310, 340, 201, 36))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.error_label.setFont(font1)

        self.pushButton.clicked.connect(lambda: self._unlock(loginWindow))
        self.retranslateUi(loginWindow)

        QMetaObject.connectSlotsByName(loginWindow)

    def _unlock(self, win):
        try:
            win.wallet.unlock(self.passEdit.text())
        except AssertionError:
            msg = 'Incorrect password'
            self.error_label.setText(QCoreApplication.translate("loginWindow",
                                                                f"<html><head/><body><p><span style=\" color:#ff0000;\">{msg}</span></p></body></html>",
                                                                None))
        else:
            from . import UiWalletWindow
            UiWalletWindow().setupUi(win)

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(QCoreApplication.translate("loginWindow", u"Document Registrar", None))
        self.label_2.setText(QCoreApplication.translate("loginWindow", u"Welcome Back!", None))
        self.label.setText(QCoreApplication.translate("loginWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("loginWindow", u"Unlock", None))
