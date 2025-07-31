# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page2.ui'
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
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 549)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 791, 551))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.horizontalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 160, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.navmenu = QWidget(self.verticalLayoutWidget)
        self.navmenu.setObjectName(u"navmenu")
        self.navmenu.setStyleSheet(u"#navmenu{\n"
"	background-color: #FCF8DD;\n"
"	border: 1px solid black; 	\n"
"}\n"
"")
        self.btnMenu1 = QPushButton(self.navmenu)
        self.btnMenu1.setObjectName(u"btnMenu1")
        self.btnMenu1.setEnabled(True)
        self.btnMenu1.setGeometry(QRect(10, 60, 141, 37))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMenu1.sizePolicy().hasHeightForWidth())
        self.btnMenu1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.btnMenu1.setFont(font)
        self.btnMenu1.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")
        self.btnMenu2 = QPushButton(self.navmenu)
        self.btnMenu2.setObjectName(u"btnMenu2")
        self.btnMenu2.setGeometry(QRect(10, 110, 141, 37))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnMenu2.sizePolicy().hasHeightForWidth())
        self.btnMenu2.setSizePolicy(sizePolicy1)
        self.btnMenu2.setFont(font)
        self.btnMenu2.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")
        self.label_3 = QLabel(self.navmenu)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 131, 17))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.btnMenu3 = QPushButton(self.navmenu)
        self.btnMenu3.setObjectName(u"btnMenu3")
        self.btnMenu3.setEnabled(True)
        self.btnMenu3.setGeometry(QRect(10, 160, 141, 37))
        sizePolicy.setHeightForWidth(self.btnMenu3.sizePolicy().hasHeightForWidth())
        self.btnMenu3.setSizePolicy(sizePolicy)
        self.btnMenu3.setFont(font)
        self.btnMenu3.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")
        self.btnMagMurid = QPushButton(self.navmenu)
        self.btnMagMurid.setObjectName(u"btnMagMurid")
        self.btnMagMurid.setGeometry(QRect(10, 210, 141, 41))
        self.btnMagMurid.setFont(font)
        self.btnMagMurid.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")

        self.verticalLayout.addWidget(self.navmenu)

        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(190, 30, 561, 451))
        self.stackedWidget.setStyleSheet(u"background-color: #FCF8DD;\n"
"")
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.label = QLabel(self.stackedWidgetPage1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 54, 17))
        self.label_4 = QLabel(self.stackedWidgetPage1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 190, 301, 71))
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setLineWidth(2)
        self.label_4.setMidLineWidth(-2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.label_2 = QLabel(self.stackedWidgetPage2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 54, 17))
        self.txtIndo = QTextEdit(self.stackedWidgetPage2)
        self.txtIndo.setObjectName(u"txtIndo")
        self.txtIndo.setGeometry(QRect(20, 70, 521, 101))
        self.txtIndo.setStyleSheet(u"background: #ffffff\n"
"")
        self.txtEng = QTextEdit(self.stackedWidgetPage2)
        self.txtEng.setObjectName(u"txtEng")
        self.txtEng.setGeometry(QRect(20, 220, 521, 101))
        self.txtEng.setStyleSheet(u"background: #f0f0f0\n"
"")
        self.txtEng.setReadOnly(True)
        self.label_5 = QLabel(self.stackedWidgetPage2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 50, 101, 17))
        self.label_6 = QLabel(self.stackedWidgetPage2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 200, 91, 17))
        self.btnTranslate = QPushButton(self.stackedWidgetPage2)
        self.btnTranslate.setObjectName(u"btnTranslate")
        self.btnTranslate.setGeometry(QRect(460, 340, 81, 41))
        self.btnTranslate.setFont(font)
        self.btnTranslate.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QWidget()
        self.stackedWidgetPage3.setObjectName(u"stackedWidgetPage3")
        self.label_7 = QLabel(self.stackedWidgetPage3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 54, 17))
        self.btnSend = QPushButton(self.stackedWidgetPage3)
        self.btnSend.setObjectName(u"btnSend")
        self.btnSend.setGeometry(QRect(450, 410, 91, 31))
        self.btnSend.setFont(font)
        self.btnSend.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")
        self.scrollArea = QScrollArea(self.stackedWidgetPage3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 39, 521, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 519, 279))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.chatLayout = QVBoxLayout()
        self.chatLayout.setObjectName(u"chatLayout")

        self.verticalLayout_2.addLayout(self.chatLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.txtAi = QTextEdit(self.stackedWidgetPage3)
        self.txtAi.setObjectName(u"txtAi")
        self.txtAi.setGeometry(QRect(20, 330, 521, 70))
        self.txtAi.setStyleSheet(u"background: #ffffff;\n"
"border-radius: 12;")
        self.stackedWidget.addWidget(self.stackedWidgetPage3)

        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnMenu1.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btnMenu2.setText(QCoreApplication.translate("MainWindow", u"Translator", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Aplikasi Sekolah", None))
        self.btnMenu3.setText(QCoreApplication.translate("MainWindow", u"AI ", None))
<<<<<<< HEAD
=======
        self.btnMagMurid.setText(QCoreApplication.translate("MainWindow", u"Data Murid", None))
>>>>>>> 8fd90da (add button in main page)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Menu 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Welcome To Aplikasi \n"
"SDIT NurHikmah", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Menu 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bahasa Indonesia", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bahasa Inggris", None))
        self.btnTranslate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Menu 3", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

