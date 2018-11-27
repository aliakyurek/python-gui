# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\download.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_downloadDialog(object):
    def setupUi(self, downloadDialog):
        downloadDialog.setObjectName("downloadDialog")
        downloadDialog.resize(326, 316)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(downloadDialog.sizePolicy().hasHeightForWidth())
        downloadDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(downloadDialog)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(downloadDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.isAutoConnectCb = QtWidgets.QCheckBox(self.groupBox)
        self.isAutoConnectCb.setObjectName("isAutoConnectCb")
        self.verticalLayout_2.addWidget(self.isAutoConnectCb)
        self.userNameLe = QtWidgets.QLineEdit(self.groupBox)
        self.userNameLe.setObjectName("userNameLe")
        self.verticalLayout_2.addWidget(self.userNameLe)
        self.passwordLe = QtWidgets.QLineEdit(self.groupBox)
        self.passwordLe.setInputMask("")
        self.passwordLe.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLe.setObjectName("passwordLe")
        self.verticalLayout_2.addWidget(self.passwordLe)
        self.httpProxyAddressLe = QtWidgets.QLineEdit(self.groupBox)
        self.httpProxyAddressLe.setObjectName("httpProxyAddressLe")
        self.verticalLayout_2.addWidget(self.httpProxyAddressLe)
        self.httpsProxyAddressLe = QtWidgets.QLineEdit(self.groupBox)
        self.httpsProxyAddressLe.setObjectName("httpsProxyAddressLe")
        self.verticalLayout_2.addWidget(self.httpsProxyAddressLe)
        self.verticalLayout.addWidget(self.groupBox)
        self.urlLe = QtWidgets.QLineEdit(downloadDialog)
        self.urlLe.setObjectName("urlLe")
        self.verticalLayout.addWidget(self.urlLe)
        self.saveLocationLe = QtWidgets.QLineEdit(downloadDialog)
        self.saveLocationLe.setObjectName("saveLocationLe")
        self.verticalLayout.addWidget(self.saveLocationLe)
        self.browseBtn = QtWidgets.QPushButton(downloadDialog)
        self.browseBtn.setObjectName("browseBtn")
        self.verticalLayout.addWidget(self.browseBtn)
        self.transferPb = QtWidgets.QProgressBar(downloadDialog)
        self.transferPb.setProperty("value", 0)
        self.transferPb.setAlignment(QtCore.Qt.AlignCenter)
        self.transferPb.setObjectName("transferPb")
        self.verticalLayout.addWidget(self.transferPb)
        self.downloadBtn = QtWidgets.QPushButton(downloadDialog)
        self.downloadBtn.setObjectName("downloadBtn")
        self.verticalLayout.addWidget(self.downloadBtn)

        self.retranslateUi(downloadDialog)
        QtCore.QMetaObject.connectSlotsByName(downloadDialog)

    def retranslateUi(self, downloadDialog):
        _translate = QtCore.QCoreApplication.translate
        downloadDialog.setWindowTitle(_translate("downloadDialog", "PyDownloader"))
        self.groupBox.setTitle(_translate("downloadDialog", "Connection Settings"))
        self.isAutoConnectCb.setText(_translate("downloadDialog", "Auto"))
        self.userNameLe.setPlaceholderText(_translate("downloadDialog", "username"))
        self.passwordLe.setPlaceholderText(_translate("downloadDialog", "password"))
        self.httpProxyAddressLe.setPlaceholderText(_translate("downloadDialog", "HTTP proxy address"))
        self.httpsProxyAddressLe.setPlaceholderText(_translate("downloadDialog", "HTTP proxy address"))
        self.urlLe.setPlaceholderText(_translate("downloadDialog", "url"))
        self.saveLocationLe.setPlaceholderText(_translate("downloadDialog", "save location"))
        self.browseBtn.setText(_translate("downloadDialog", "Browse"))
        self.downloadBtn.setText(_translate("downloadDialog", "Download"))

