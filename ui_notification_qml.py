from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlProperty, QQmlEngine
from PyQt5.QtCore import QUrl, QObject, QVariant
from PyQt5.QtWidgets import QApplication, QWidget

from bicimageprovider import BicImageProvider

import os 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Notification(object):
    twidth  = 800
    theight = 0

    def setupUi(self, Notification):

        msgv = QQuickView()
        
        msgv.setSource(QUrl('message.qml'))
        rootObj = msgv.rootObject();
        total_width = int(QQmlProperty.read(rootObj, "width"))
        total_height = int(QQmlProperty.read(rootObj, "height"))

        self.twidth = total_width
        self.theight = total_height

        qmlengine = msgv.engine()
        qmlengine.addImageProvider("bicimage", BicImageProvider())

        rootObj.findChild(QObject, "img").setProperty("source","image://bicimage/"+Notification.mssg["icon"])
        rootObj.findChild(QObject, "textprocess").setProperty("text",Notification.mssg["process"])
        rootObj.findChild(QObject, "filename").setProperty("text",Notification.mssg["file"])
        rootObj.findChild(QObject, "textaction").setProperty("text",Notification.mssg["action"])
        rootObj.findChild(QObject, "textaction").setProperty("color",Notification.mssg["color"])
        rootObj.findChild(QObject, "timestr").setProperty("text",Notification.mssg["time"])

        Notification.setObjectName(_fromUtf8("Notification"))
        Notification.setMinimumSize(QtCore.QSize(total_width, total_height))
        Notification.setMaximumSize(QtCore.QSize(total_width, total_height))
        
        # Notification.setWindowOpacity(1.0)
        # Notification.setAutoFillBackground(False)
        # Notification.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)

        centralwidget = QWidget.createWindowContainer(msgv)
        centralwidget.setObjectName(_fromUtf8("centralwidget"))
                
        Notification.setCentralWidget(centralwidget)

        # self.retranslateUi(Notification)
        # QtCore.QMetaObject.connectSlotsByName(Notification)

    def retranslateUi(self, Notification):
        Notification.setWindowTitle(QtWidgets.QApplication.translate("Notification", "MainWindow", None))
        # self.lbl_mssg.setText(QtWidgets.QApplication.translate("Notification", "TextLabel", None))

