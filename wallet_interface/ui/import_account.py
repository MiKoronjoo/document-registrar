from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ImportAccountWindow(object):
    def setupUi(self, ImportAccountWindow):
        if not ImportAccountWindow.objectName():
            ImportAccountWindow.setObjectName(u"ImportAccountWindow")
        ImportAccountWindow.resize(800, 600)
        self.centralwidget = QWidget(ImportAccountWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 70, 461, 141))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.cancelBT = QPushButton(self.centralwidget)
        self.cancelBT.setObjectName(u"cancelBT")
        self.cancelBT.setGeometry(QRect(20, 20, 103, 36))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 220, 271, 19))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.accountNameEdit = QLineEdit(self.centralwidget)
        self.accountNameEdit.setObjectName(u"accountNameEdit")
        self.accountNameEdit.setGeometry(QRect(240, 340, 241, 36))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 310, 271, 19))
        self.label_3.setFont(font1)
        self.importBT = QPushButton(self.centralwidget)
        self.importBT.setObjectName(u"importBT")
        self.importBT.setGeometry(QRect(240, 410, 103, 36))
        self.privateKeyEdit = QLineEdit(self.centralwidget)
        # self.privateKeyEdit.setEchoMode(QLineEdit.Password)
        self.privateKeyEdit.setObjectName(u"privateKeyEdit")
        self.privateKeyEdit.setGeometry(QRect(240, 250, 351, 36))
        ImportAccountWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ImportAccountWindow)
        self.statusbar.setObjectName(u"statusbar")
        ImportAccountWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImportAccountWindow)

        QMetaObject.connectSlotsByName(ImportAccountWindow)

    # setupUi

    def retranslateUi(self, ImportAccountWindow):
        ImportAccountWindow.setWindowTitle(QCoreApplication.translate("ImportAccountWindow", u"Import Account", None))
        self.label_2.setText(QCoreApplication.translate("ImportAccountWindow", u"Import Account", None))
        self.cancelBT.setText(QCoreApplication.translate("ImportAccountWindow", u"cancel", None))
        self.label.setText(
            QCoreApplication.translate("ImportAccountWindow", u"Enter your private key string here:", None))
        self.accountNameEdit.setText(QCoreApplication.translate("ImportAccountWindow", u"Main", None))
        self.label_3.setText(QCoreApplication.translate("ImportAccountWindow", u"Account Name", None))
        self.importBT.setText(QCoreApplication.translate("ImportAccountWindow", u"Import", None))
    # retranslateUi
