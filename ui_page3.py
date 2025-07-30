# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page3.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        if not SecondWindow.objectName():
            SecondWindow.setObjectName(u"SecondWindow")
        SecondWindow.resize(802, 559)
        self.centralwidget = QWidget(SecondWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 801, 511))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 781, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.horizontalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background: #FCF8DD;")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 241, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(570, 10, 101, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #78C841;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(680, 10, 91, 31))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFD700;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")

        self.horizontalLayout.addWidget(self.widget_2)

        self.verticalLayoutWidget_2 = QWidget(self.widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 90, 781, 391))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.verticalLayoutWidget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background: #FCF8DD;\n"
"border: 1px solid black;")

        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SecondWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 22))
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SecondWindow)
        self.statusbar.setObjectName(u"statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)

        QMetaObject.connectSlotsByName(SecondWindow)
    # setupUi

    def retranslateUi(self, SecondWindow):
        SecondWindow.setWindowTitle(QCoreApplication.translate("SecondWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SecondWindow", u"Managemen Data Murid", None))
        self.pushButton.setText(QCoreApplication.translate("SecondWindow", u"Tambah Murid", None))
        self.pushButton_2.setText(QCoreApplication.translate("SecondWindow", u"Kembali", None))
    # retranslateUi

