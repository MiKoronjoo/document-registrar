from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiRegistrarWindow(object):
    def setupUi(self, RegistrarWindow):
        if not RegistrarWindow.objectName():
            RegistrarWindow.setObjectName(u"RegistrarWindow")
        RegistrarWindow.resize(800, 600)
        self.centralwidget = QWidget(RegistrarWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.browseBT = QPushButton(self.centralwidget)
        self.browseBT.setObjectName(u"browseBT")
        self.browseBT.setGeometry(QRect(20, 161, 103, 36))
        self.filePathLabel = QLabel(self.centralwidget)
        self.filePathLabel.setObjectName(u"filePathLabel")
        self.filePathLabel.setGeometry(QRect(20, 130, 761, 31))
        self.txHashLabel = QLabel(self.centralwidget)
        self.txHashLabel.setObjectName(u"txHashLabel")
        self.txHashLabel.setGeometry(QRect(20, 455, 761, 36))
        self.openExplorerBT = QPushButton(self.centralwidget)
        self.openExplorerBT.setObjectName(u"openExplorerBT")
        self.openExplorerBT.setGeometry(QRect(20, 455, 41, 36))
        self.openExplorerBT.setText('Open')
        self.fileHashText = QTextBrowser(self.centralwidget)
        self.fileHashText.setObjectName(u"fileHashText")
        self.fileHashText.setGeometry(QRect(200, 161, 591, 36))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 161, 70, 36))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 101, 121, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.registerBT = QPushButton(self.centralwidget)
        self.registerBT.setObjectName(u"registerBT")
        self.registerBT.setEnabled(False)
        self.registerBT.setGeometry(QRect(20, 365, 161, 36))
        self.registerWsBT = QPushButton(self.centralwidget)
        self.registerWsBT.setObjectName(u"registerWsBT")
        self.registerWsBT.setGeometry(QRect(20, 405, 161, 36))
        self.serverDownLabel = QLabel(self.centralwidget)
        self.serverDownLabel.setObjectName(u"serverDownLabel")
        self.serverDownLabel.setEnabled(True)
        self.serverDownLabel.setGeometry(QRect(190, 375, 101, 19))
        self.infoLabel = QLabel(self.centralwidget)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setEnabled(True)
        self.infoLabel.setGeometry(QRect(24, 290, 701, 121))
        self.copyBT = QPushButton(self.centralwidget)
        self.copyBT.setObjectName(u"copyBT")
        self.copyBT.setGeometry(QRect(747, 164, 41, 30))
        self.titleEdit = QLineEdit(self.centralwidget)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setGeometry(QRect(20, 325, 161, 36))
        self.r1RM = QLabel(self.centralwidget)
        self.r1RM.setObjectName(u"r1RM")
        self.r1RM.setGeometry(QRect(20, 290, 41, 31))
        self.r2RM = QLabel(self.centralwidget)
        self.r2RM.setObjectName(u"r2RM")
        self.r2RM.setGeometry(QRect(20, 250, 121, 40))
        self.r2RM.setFont(font)
        self.I1RM = QLabel(self.centralwidget)
        self.I1RM.setObjectName(u"I1RM")
        self.I1RM.setGeometry(QRect(24, 250, 161, 40))
        self.I1RM.setFont(font)
        self.titleMayEdit = QLineEdit(self.centralwidget)
        self.titleMayEdit.setObjectName(u"titleMayEdit")
        self.titleMayEdit.setEnabled(False)
        self.titleMayEdit.setGeometry(QRect(70, 300, 201, 30))
        self.backBT = QPushButton(self.centralwidget)
        self.backBT.setObjectName(u"backBT")
        self.backBT.setGeometry(QRect(20, 20, 103, 36))
        self.editCancelBT = QPushButton(self.centralwidget)
        self.editCancelBT.setObjectName(u"editCancelBT")
        self.editCancelBT.setGeometry(QRect(276, 300, 61, 30))
        self.submitBT = QPushButton(self.centralwidget)
        self.submitBT.setObjectName(u"submitBT")
        self.submitBT.setGeometry(QRect(340, 300, 61, 30))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 20, 171, 41))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_4.setFont(font1)
        self.donateBT = QPushButton(self.centralwidget)
        self.donateBT.setObjectName(u"donateBT")
        self.donateBT.setGeometry(QRect(532, 330, 61, 36))
        self.donateEdit = QLineEdit(self.centralwidget)
        self.donateEdit.setObjectName(u"donateEdit")
        self.donateEdit.setValidator(QDoubleValidator(0, 1000000, 12))
        self.donateEdit.setGeometry(QRect(596, 330, 71, 36))
        self.donateEdit.setInputMethodHints(Qt.ImhNone)
        self.donateEdit.setDragEnabled(False)
        self.donateEdit.setReadOnly(False)
        self.ethLabel = QLabel(self.centralwidget)
        self.ethLabel.setObjectName(u"ethLabel")
        self.ethLabel.setGeometry(QRect(670, 335, 66, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.ethLabel.setFont(font)
        self.gasCheckBox = QCheckBox(self.centralwidget)
        self.gasCheckBox.setObjectName(u"gasCheckBox")
        self.gasCheckBox.setGeometry(QRect(190, 410, 171, 25))
        self.gasCheckBox.setChecked(False)
        self.gasCheckBox.setTristate(False)
        self.gweiEdit = QLineEdit(self.centralwidget)
        self.gweiEdit.setObjectName(u"gweiEdit")
        self.gweiEdit.setValidator(QDoubleValidator(0, 1000000, 8))
        self.gweiEdit.setGeometry(QRect(340, 408, 81, 30))
        self.gweiLabel = QLabel(self.centralwidget)
        self.gweiLabel.setObjectName(u"gweiLabel")
        self.gweiLabel.setGeometry(QRect(426, 410, 70, 31))
        self.gweiLabel.setFont(font)
        RegistrarWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(RegistrarWindow)
        self.statusbar.setObjectName(u"statusbar")
        RegistrarWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegistrarWindow)

        QMetaObject.connectSlotsByName(RegistrarWindow)
        self.hide_register_elements()
        self.hide_info_elements()
        from . import UiWalletWindow
        self.backBT.clicked.connect(lambda: UiWalletWindow().setupUi(RegistrarWindow))
        self.editCancelBT.clicked.connect(self.edit_cancel)
        self.browseBT.clicked.connect(lambda: self.browse_file(RegistrarWindow))
        self.registerWsBT.clicked.connect(lambda: self.register_file(RegistrarWindow))
        self.copyBT.clicked.connect(lambda: self._copy(RegistrarWindow))
        self.submitBT.clicked.connect(lambda: self.submit(RegistrarWindow))
        self.donateBT.clicked.connect(lambda: self.donate(RegistrarWindow))
        self.openExplorerBT.clicked.connect(self.open_url)
        self.gasCheckBox.toggled.connect(self.custom_gas_toggled)
        self.donateEdit.textEdited.connect(lambda: self.donateBT.setEnabled(True))
        self.openExplorerBT.hide()

    def open_url(self):
        tx_hash = self.txHashLabel.text().split()[-1]
        QDesktopServices().openUrl(f'https://rinkeby.etherscan.io/tx/{tx_hash}')

    def _copy(self, win):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.fileHashText.toPlainText(), mode=cb.Clipboard)

    def donate(self, win):
        self.donateBT.setEnabled(False)
        to = self.temp_author
        value = round(float(self.donateEdit.text()) * 10 ** 18)
        tx_hash = win.registrar.send_ether(to, value, win.wallet.selected.private_key)
        self.txHashLabel.setText(f'            Txn Hash: {tx_hash}')
        self.openExplorerBT.show()

    def register_file(self, win):
        self.registerWsBT.setEnabled(False)
        file_hash = self.fileHashText.toPlainText()
        title = self.titleEdit.text().strip() or 'Document'
        private_key = win.wallet.selected.private_key
        gas_price = self.gweiEdit.text() if self.gasCheckBox.isChecked() else None
        tx_hash = win.registrar.register_without_sign(file_hash, title, private_key, gas_price)
        self.txHashLabel.setText(f'            Txn Hash: {tx_hash}')
        self.openExplorerBT.show()

    def submit(self, win):
        self.titleMayEdit.setEnabled(False)
        self.editCancelBT.setText('edit')
        self.submitBT.hide()
        file_hash = self.fileHashText.toPlainText()
        title = self.titleMayEdit.text()
        if not title.strip() or title == self.temp_title:
            self.titleMayEdit.setText(self.temp_title)
            return
        private_key = win.wallet.selected.private_key
        tx_hash = win.registrar.update_title(file_hash, title, private_key)
        self.txHashLabel.setText(f'            Txn Hash: {tx_hash}')
        self.openExplorerBT.show()

    def browse_file(self, win):
        file_path = QFileDialog.getOpenFileName(win, 'Open file')[0]
        if file_path:
            from utils import hash_file
            file_hash = hash_file(file_path)
            self.fileHashText.setText(file_hash)
            if len(file_path) > 100:
                file_path = '...' + file_path[-97:]
            self.filePathLabel.setText(file_path)
            if not win.registrar.file_timestamp(file_hash):
                self.show_register_elements()
            else:
                title, author, timestamp = win.registrar.get_info(file_hash)
                self.temp_author = author
                self.infoLabel.setText(
                    f"<html><head/><body><p><span style=\" font-size:14pt;\">Title:</span></p><p><span style=\" font-size:14pt;\">Author: {author}</span></p><p><span style=\" font-size:14pt;\">Time: {timestamp}</span></p></body></html>")
                self.titleMayEdit.setText(title)
                self.titleMayEdit.setEnabled(False)
                self.show_info_elements()
                if win.wallet.selected.address != author:
                    self.editCancelBT.hide()
                else:
                    self.donateBT.hide()
                    self.donateEdit.hide()
                    self.ethLabel.hide()

    def custom_gas_toggled(self):
        is_checked = self.gasCheckBox.isChecked()
        self.gweiEdit.setEnabled(is_checked)
        self.gweiLabel.setEnabled(is_checked)

    def hide_register_elements(self):
        elements = [self.r1RM, self.r2RM, self.titleEdit, self.registerBT, self.registerWsBT, self.serverDownLabel,
                    self.gasCheckBox, self.gweiEdit, self.gweiLabel]
        for elm in elements:
            elm.hide()

    def show_register_elements(self):
        self.hide_info_elements()
        self.registerWsBT.setEnabled(True)
        self.gasCheckBox.setChecked(False)
        self.gweiEdit.setEnabled(False)
        self.gweiLabel.setEnabled(False)
        elements = [self.r1RM, self.r2RM, self.titleEdit, self.registerBT, self.registerWsBT, self.serverDownLabel,
                    self.gasCheckBox, self.gweiEdit, self.gweiLabel]
        for elm in elements:
            elm.show()

    def hide_info_elements(self):
        elements = [self.I1RM, self.titleMayEdit, self.infoLabel, self.editCancelBT, self.submitBT,
                    self.donateBT, self.donateEdit, self.ethLabel]
        for elm in elements:
            elm.hide()

    def show_info_elements(self):
        self.hide_register_elements()
        self.donateBT.setEnabled(True)
        elements = [self.I1RM, self.titleMayEdit, self.infoLabel, self.editCancelBT,
                    self.donateBT, self.donateEdit, self.ethLabel]
        for elm in elements:
            elm.show()

    def edit_cancel(self):
        if self.titleMayEdit.isEnabled():
            self.titleMayEdit.setEnabled(False)
            self.editCancelBT.setText('edit')
            self.submitBT.hide()
            self.titleMayEdit.setText(self.temp_title)
        else:
            self.titleMayEdit.setEnabled(True)
            self.editCancelBT.setText('cancel')
            self.submitBT.show()
            self.temp_title = self.titleMayEdit.text()

    def retranslateUi(self, RegistrarWindow):
        RegistrarWindow.setWindowTitle(QCoreApplication.translate("RegistrarWindow", u"Register", None))
        self.browseBT.setText(QCoreApplication.translate("RegistrarWindow", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("RegistrarWindow", u"File hash:", None))
        self.label_3.setText(QCoreApplication.translate("RegistrarWindow", u"Open file", None))
        self.registerBT.setText(QCoreApplication.translate("RegistrarWindow", u"Register this file", None))
        self.registerWsBT.setText(QCoreApplication.translate("RegistrarWindow", u"Register without sign", None))
        self.serverDownLabel.setText(QCoreApplication.translate("RegistrarWindow",
                                                                u"<html><head/><body><p><span style=\" color:#ff0000;\">server is down</span></p></body></html>",
                                                                None))
        self.infoLabel.setText(QCoreApplication.translate("RegistrarWindow",
                                                          u"<html><head/><body><p><span style=\" font-size:14pt;\">Title:</span></p><p><span style=\" font-size:14pt;\">Author: 0xbcB26b9fc4496379bB81dB4acA1E4Bb07c538Bcc</span></p><p><span style=\" font-size:14pt;\">Time: 2022 May 08, 14:32:17</span></p></body></html>",
                                                          None))
        self.copyBT.setText(QCoreApplication.translate("RegistrarWindow", u"copy", None))
        self.r1RM.setText(QCoreApplication.translate("RegistrarWindow", u"Title:", None))
        self.r2RM.setText(QCoreApplication.translate("RegistrarWindow", u"Register", None))
        self.I1RM.setText(QCoreApplication.translate("RegistrarWindow", u"Information", None))
        self.titleMayEdit.setText(QCoreApplication.translate("RegistrarWindow", u"title of this document", None))
        self.backBT.setText(QCoreApplication.translate("RegistrarWindow", u"back", None))
        self.editCancelBT.setText(QCoreApplication.translate("RegistrarWindow", u"edit", None))
        self.submitBT.setText(QCoreApplication.translate("RegistrarWindow", u"submit", None))
        self.label_4.setText(QCoreApplication.translate("RegistrarWindow", u"Register File", None))
        self.donateBT.setText(QCoreApplication.translate("RegistrarWindow", u"Donate", None))
        self.donateEdit.setText(QCoreApplication.translate("RegistrarWindow", u"0.001", None))
        self.ethLabel.setText(QCoreApplication.translate("RegistrarWindow", u"ETH", None))
        self.gasCheckBox.setText(QCoreApplication.translate("RegistrarWindow", u"custom gas price", None))
        self.gweiEdit.setText(QCoreApplication.translate("RegistrarWindow", u"1.1", None))
        self.gweiLabel.setText(QCoreApplication.translate("RegistrarWindow", u"GWei", None))
