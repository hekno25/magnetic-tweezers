# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainFMbpte.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QScrollArea, QSizePolicy, QSlider, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(773, 603)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cameraPlaceholder = QLabel(self.centralwidget)
        self.cameraPlaceholder.setObjectName(u"cameraPlaceholder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cameraPlaceholder.sizePolicy().hasHeightForWidth())
        self.cameraPlaceholder.setSizePolicy(sizePolicy1)
        self.cameraPlaceholder.setMaximumSize(QSize(1280, 1024))

        self.verticalLayout.addWidget(self.cameraPlaceholder)

        self.connectionStatus = QLabel(self.centralwidget)
        self.connectionStatus.setObjectName(u"connectionStatus")
        self.connectionStatus.setMaximumSize(QSize(1280, 1024))

        self.verticalLayout.addWidget(self.connectionStatus)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 631, 539))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.coilSlider2 = QSlider(self.groupBox_2)
        self.coilSlider2.setObjectName(u"coilSlider2")
        self.coilSlider2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.coilSlider2, 0, 0, 1, 1)

        self.coilSpinBox2 = QDoubleSpinBox(self.groupBox_2)
        self.coilSpinBox2.setObjectName(u"coilSpinBox2")

        self.gridLayout_4.addWidget(self.coilSpinBox2, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.coilSlider1 = QSlider(self.groupBox)
        self.coilSlider1.setObjectName(u"coilSlider1")
        self.coilSlider1.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.coilSlider1, 0, 0, 1, 1)

        self.coilSpinBox1 = QDoubleSpinBox(self.groupBox)
        self.coilSpinBox1.setObjectName(u"coilSpinBox1")

        self.gridLayout_2.addWidget(self.coilSpinBox1, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.coilSlider3 = QSlider(self.groupBox_3)
        self.coilSlider3.setObjectName(u"coilSlider3")
        self.coilSlider3.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.coilSlider3, 0, 0, 1, 1)

        self.coilSpinBox3 = QDoubleSpinBox(self.groupBox_3)
        self.coilSpinBox3.setObjectName(u"coilSpinBox3")

        self.gridLayout_5.addWidget(self.coilSpinBox3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 773, 22))
        self.menuSerial = QMenu(self.menuBar)
        self.menuSerial.setObjectName(u"menuSerial")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuSerial.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cameraPlaceholder.setText(QCoreApplication.translate("MainWindow", u"Camera Placeholder", None))
        self.connectionStatus.setText(QCoreApplication.translate("MainWindow", u"Connection Status", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Y-Axis", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"X-Axis", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Z-Axis", None))
        self.menuSerial.setTitle(QCoreApplication.translate("MainWindow", u"Serial", None))
    # retranslateUi

