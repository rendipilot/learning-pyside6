# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page1.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 800)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 1181, 771))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1181, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.horizontalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.btnChangePage = QPushButton(self.widget_2)
        self.btnChangePage.setObjectName(u"btnChangePage")
        self.btnChangePage.setGeometry(QRect(20, 30, 81, 25))

        self.horizontalLayout_2.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnChangePage.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

