from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_loginWindow(object):
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
        self.kpasswordlineedit = QLineEdit(self.centralwidget)
        self.kpasswordlineedit.setObjectName(u"kpasswordlineedit")
        self.kpasswordlineedit.setEchoMode(QLineEdit.Password)
        self.kpasswordlineedit.setGeometry(QRect(310, 240, 201, 36))
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

        self.retranslateUi(loginWindow)

        QMetaObject.connectSlotsByName(loginWindow)

    # setupUi

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(QCoreApplication.translate("loginWindow", u"Document Registrar", None))
        self.label_2.setText(QCoreApplication.translate("loginWindow", u"Welcome Back!", None))
        self.label.setText(QCoreApplication.translate("loginWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("loginWindow", u"Unlock", None))
    # retranslateUi
