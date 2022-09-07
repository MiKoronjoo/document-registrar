from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.importWalletBT = QPushButton(self.centralwidget)
        self.importWalletBT.setObjectName("importWalletBT")
        self.importWalletBT.setGeometry(QRect(150, 390, 131, 36))
        self.createWalletBT = QPushButton(self.centralwidget)
        self.createWalletBT.setObjectName("createWalletBT")
        self.createWalletBT.setGeometry(QRect(520, 390, 131, 36))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(100, 290, 231, 111))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(180, 70, 461, 141))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(470, 290, 231, 111))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(80, 230, 281, 91))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(450, 230, 281, 91))
        self.label_5.setFont(font1)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        from . import UiImportWalletWindow, UiCreatePasswordWindow
        self.importWalletBT.clicked.connect(lambda: UiImportWalletWindow().setupUi(MainWindow))
        self.createWalletBT.clicked.connect(lambda: UiCreatePasswordWindow().setupUi(MainWindow))

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Document Registrar", None))
        self.importWalletBT.setText(QCoreApplication.translate("MainWindow", "Import Wallet", None))
        self.createWalletBT.setText(QCoreApplication.translate("MainWindow", "Create a Wallet", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Import your existing wallet using\n"
                                                                    "a Secret Recovery Phrase", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Do you have a Recovery Phrase?", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "This will create a new wallet and\n"
                                                                      "Secret Recovery Phrase", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Yes, I already have a Recovery\n"
                                                                      "Phrase", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "No, let's get set up!", None))
