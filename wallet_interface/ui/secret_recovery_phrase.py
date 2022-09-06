from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateWalletWindow(object):
    def setupUi(self, CreateWalletWindow):
        if not CreateWalletWindow.objectName():
            CreateWalletWindow.setObjectName(u"CreateWalletWindow")
        CreateWalletWindow.resize(800, 600)
        self.centralwidget = QWidget(CreateWalletWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backBT = QPushButton(self.centralwidget)
        self.backBT.setObjectName(u"backBT")
        self.backBT.setGeometry(QRect(20, 20, 103, 36))
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
        self.phraseBrowser = QTextBrowser(self.centralwidget)
        self.phraseBrowser.setObjectName(u"phraseBrowser")
        self.phraseBrowser.setGeometry(QRect(180, 190, 461, 91))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 280, 471, 141))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.okBT = QPushButton(self.centralwidget)
        self.okBT.setObjectName(u"okBT")
        self.okBT.setGeometry(QRect(180, 430, 103, 36))
        CreateWalletWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CreateWalletWindow)
        self.statusbar.setObjectName(u"statusbar")
        CreateWalletWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CreateWalletWindow)

        QMetaObject.connectSlotsByName(CreateWalletWindow)

    # setupUi

    def retranslateUi(self, CreateWalletWindow):
        CreateWalletWindow.setWindowTitle(
            QCoreApplication.translate("CreateWalletWindow", u"Secret Recovery Phrase", None))
        self.backBT.setText(QCoreApplication.translate("CreateWalletWindow", u"back", None))
        self.label_2.setText(QCoreApplication.translate("CreateWalletWindow", u"Secret Recovery Phrase", None))
        self.phraseBrowser.setHtml(QCoreApplication.translate("CreateWalletWindow",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:'Fira Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">potato just sorry excess say fuel atom spawn snap boss aisle shock actress churn tube drip race sweet novel token truth satoshi disease void</span></p></body></html>",
                                                              None))
        self.label_3.setText(QCoreApplication.translate("CreateWalletWindow",
                                                        u"Store this phrase in a password manager like 1Password.\n"
                                                        "\n"
                                                        "Write this phrase on a piece of paper and store in a secure location.\n"
                                                        "\n"
                                                        "WARNING: Never disclose your Secret Recovery Phrase. Anyone with\n"
                                                        "this phrase can take your wallet assets forever.", None))
        self.okBT.setText(QCoreApplication.translate("CreateWalletWindow", u"OK", None))
    # retranslateUi
