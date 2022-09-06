from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiImportWalletWindow(object):
    def setupUi(self, ImportWalletWindow):
        if not ImportWalletWindow.objectName():
            ImportWalletWindow.setObjectName("ImportWalletWindow")
        ImportWalletWindow.resize(800, 600)
        self.centralwidget = QWidget(ImportWalletWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(190, 50, 461, 141))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.seedPhraseEdit = QPlainTextEdit(self.centralwidget)
        self.seedPhraseEdit.setObjectName("seedPhraseEdit")
        self.seedPhraseEdit.setGeometry(QRect(190, 170, 471, 81))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(190, 310, 281, 19))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(190, 390, 131, 19))
        self.importBT = QPushButton(self.centralwidget)
        self.importBT.setObjectName("importBT")
        self.importBT.setGeometry(QRect(190, 480, 103, 36))
        self.backBT = QPushButton(self.centralwidget)
        self.backBT.setObjectName("backBT")
        self.backBT.setGeometry(QRect(20, 20, 103, 36))
        self.passEdit = QLineEdit(self.centralwidget)
        self.passEdit.setEchoMode(QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        self.passEdit.setGeometry(QRect(190, 340, 291, 36))
        self.pass2Edit = QLineEdit(self.centralwidget)
        self.pass2Edit.setObjectName("pass2Edit")
        self.pass2Edit.setEchoMode(QLineEdit.Password)
        self.pass2Edit.setGeometry(QRect(190, 420, 291, 36))
        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName("error_label")
        self.error_label.setGeometry(QRect(190, 260, 471, 21))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.error_label.setFont(font1)
        ImportWalletWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ImportWalletWindow)
        self.statusbar.setObjectName(u"statusbar")
        ImportWalletWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImportWalletWindow)
        from . import UiMainWindow

        self.backBT.clicked.connect(lambda: UiMainWindow().setupUi(ImportWalletWindow))
        self.importBT.clicked.connect(lambda: self.import_seed_phrase(ImportWalletWindow))
        QMetaObject.connectSlotsByName(ImportWalletWindow)

    def check_password(self):
        msg = ''
        if self.passEdit.text() != self.pass2Edit.text():
            msg = 'passwords does not match'
        elif len(self.passEdit.text()) < 8 or len(self.passEdit.text()) > 32:
            msg = 'password length should between 8-32 characters'
        else:
            return True
        self.error_label.setText(QCoreApplication.translate("ImportWalletWindow",
                                                            f"<html><head/><body><p><span style=\" color:#ff0000;\">{msg}</span></p></body></html>",
                                                            None))
        return False

    def import_seed_phrase(self, win):
        sp = self.seedPhraseEdit.toPlainText()
        lsp = sp.strip().split()
        if self.check_password():
            if len(lsp) in (12, 15, 18, 21, 24):
                win.wallet.set_password(self.passEdit.text())
                win.wallet.import_wallet(' '.join(lsp))
                from . import UiWalletWindow
                UiWalletWindow().setupUi(win)
            else:
                msg = 'Invalid Secret Recovery Phrase'
                self.error_label.setText(QCoreApplication.translate("ImportWalletWindow",
                                                                    f"<html><head/><body><p><span style=\" color:#ff0000;\">{msg}</span></p></body></html>",
                                                                    None))

    def retranslateUi(self, ImportWalletWindow):
        ImportWalletWindow.setWindowTitle(QCoreApplication.translate("ImportWalletWindow", u"Import Wallet", None))
        self.label_2.setText(
            QCoreApplication.translate("ImportWalletWindow", u"Enter your Secret Recovery Phrase:", None))
        self.seedPhraseEdit.setPlainText(QCoreApplication.translate("ImportWalletWindow",
                                                                    u"potato just sorry excess say fuel atom spawn snap boss aisle shock actress churn tube drip race sweet novel token truth satoshi disease void",
                                                                    None))
        self.label.setText(QCoreApplication.translate("ImportWalletWindow", u"New Password (8 Characters min)", None))
        self.label_3.setText(QCoreApplication.translate("ImportWalletWindow", u"Confirm Password", None))
        self.importBT.setText(QCoreApplication.translate("ImportWalletWindow", u"Import", None))
        self.backBT.setText(QCoreApplication.translate("ImportWalletWindow", u"back", None))
