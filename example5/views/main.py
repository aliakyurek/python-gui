from PyQt5.QtWidgets import QDialog,QFileDialog,QMessageBox
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt,QDir
from ui.download import Ui_downloadDialog

class Download(QDialog):
    def __init__(self):
        super(Download, self).__init__()
        self.ui = Ui_downloadDialog()
        self.ui.setupUi(self)

        self.setFocus()

###### event handlers #######
        self.ui.browseBtn.clicked.connect(self.browseClickedHandler)

    def setProgress(self, percent):
        self.ui.transferPb.setValue(percent)
        if (percent == 100):
            QMessageBox.information(self, 'Information', 'The download is complete!')

    def changeConnectionSettingsVisibility(self, state):
        palette = QPalette()
        palette.setColor(QPalette.Base, Qt.gray if(state) else Qt.white)
        palette.setColor(QPalette.Text, Qt.darkGray if(state) else Qt.black)

        self.ui.userNameLe.setPalette(palette)
        self.ui.passwordLe.setPalette(palette)
        self.ui.httpProxyAddressLe.setPalette(palette)
        self.ui.httpsProxyAddressLe.setPalette(palette)

        self.ui.userNameLe.setReadOnly(state)
        self.ui.passwordLe.setReadOnly(state)
        self.ui.httpProxyAddressLe.setReadOnly(state)
        self.ui.httpsProxyAddressLe.setReadOnly(state)

    def browseClickedHandler(self):
        save_file = QFileDialog.getSaveFileName(self, caption='Save file as', directory='D:\\', filter='All Files (*.*)')
        self.ui.saveLocationLe.setText(QDir.toNativeSeparators(save_file))
