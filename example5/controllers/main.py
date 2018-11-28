import models.main
import views.main
from PyQt5 import QtCore

class Download:
    def __init__(self):
        ###### Model Creation #####
        self.model = models.main.Download()

        ###### Binding the model events to controller handlers #####
        self.model.bind('downloadProgressChanged', self.downloadProgressChangedHandler)
        self.model.bind('autoConnectChanged', self.autoConnectChangedHandler)

        ###### View creation #####
        self.view = views.main.Download()
        self.view.show()

        ###### View initialization ####
        # must be before to prevent unnecessary triggering handlers here
        self.view.ui.isAutoConnectCb.setChecked(self.model.autoConnect)
        self.view.ui.userNameLe.setText(self.model.username)
        self.view.ui.passwordLe.setText(self.model.password)
        self.view.ui.urlLe.setText(self.model.url)
        self.view.ui.saveLocationLe.setText(self.model.saveLocation)
        self.view.ui.httpProxyAddressLe.setText(self.model.proxyAddress['http'])
        self.view.ui.httpsProxyAddressLe.setText(self.model.proxyAddress['https'])

        self.autoConnectChangedHandler(self.model.autoConnect)
        ###### Binding the view events to the controller handler #####
        self.view.ui.userNameLe.textChanged.connect(self.userNameChangedHandler)
        self.view.ui.passwordLe.textChanged.connect(self.passwordChangedHandler)
        self.view.ui.saveLocationLe.textChanged.connect(self.saveLocationLeChangedHandler)
        self.view.ui.urlLe.textChanged.connect(self.urlLeChangedHandler)
        self.view.ui.downloadBtn.clicked.connect(self.downloadBtnTriggeredHandler)
        self.view.ui.isAutoConnectCb.stateChanged.connect(self.isAutoConnectCbChangedHandler)

    ###### Model event handlers #####
    def downloadProgressChangedHandler(self, percent):
        self.view.setProgress(percent)

    def autoConnectChangedHandler(self, state):
        self.view.changeConnectionSettingsVisibility(state)

    ###### View event handlers #####
    def userNameChangedHandler(self, text):
        self.model.username = text

    def passwordChangedHandler(self, text):
        self.model.password = text

    def saveLocationLeChangedHandler(self, text):
        self.model.saveLocation = text

    def urlLeChangedHandler(self, text):
        self.model.url = text

    def downloadBtnTriggeredHandler(self):
        self.model.startDownload()

    def isAutoConnectCbChangedHandler(self, state):
        self.model.autoConnect = True if(state == QtCore.Qt.Checked) else False

