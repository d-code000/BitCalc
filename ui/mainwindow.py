# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(375, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(375, 360))
        MainWindow.setMaximumSize(QSize(375, 360))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 351, 51))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 60, 371, 54))
        self.ClearlLayout = QHBoxLayout(self.layoutWidget)
        self.ClearlLayout.setObjectName(u"ClearlLayout")
        self.ClearlLayout.setContentsMargins(5, 5, 5, 5)
        self.clearAllButton = QPushButton(self.layoutWidget)
        self.clearAllButton.setObjectName(u"clearAllButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.clearAllButton.sizePolicy().hasHeightForWidth())
        self.clearAllButton.setSizePolicy(sizePolicy2)

        self.ClearlLayout.addWidget(self.clearAllButton)

        self.clearButton = QPushButton(self.layoutWidget)
        self.clearButton.setObjectName(u"clearButton")
        sizePolicy2.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy2)

        self.ClearlLayout.addWidget(self.clearButton)

        self.backspaseButton = QPushButton(self.layoutWidget)
        self.backspaseButton.setObjectName(u"backspaseButton")
        sizePolicy2.setHeightForWidth(self.backspaseButton.sizePolicy().hasHeightForWidth())
        self.backspaseButton.setSizePolicy(sizePolicy2)

        self.ClearlLayout.addWidget(self.backspaseButton)

        self.ClearlLayout.setStretch(0, 1)
        self.ClearlLayout.setStretch(1, 1)
        self.ClearlLayout.setStretch(2, 1)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 110, 371, 251))
        self.MainKeyboardLayout = QGridLayout(self.layoutWidget1)
        self.MainKeyboardLayout.setSpacing(5)
        self.MainKeyboardLayout.setObjectName(u"MainKeyboardLayout")
        self.MainKeyboardLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.MainKeyboardLayout.setContentsMargins(5, 5, 5, 5)
        self.valButton_8 = QPushButton(self.layoutWidget1)
        self.valButton_8.setObjectName(u"valButton_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.valButton_8.sizePolicy().hasHeightForWidth())
        self.valButton_8.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(15)
        self.valButton_8.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_8, 0, 2, 1, 1)

        self.dotButton = QPushButton(self.layoutWidget1)
        self.dotButton.setObjectName(u"dotButton")
        sizePolicy3.setHeightForWidth(self.dotButton.sizePolicy().hasHeightForWidth())
        self.dotButton.setSizePolicy(sizePolicy3)
        self.dotButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.dotButton, 3, 2, 1, 1)

        self.valButton_6 = QPushButton(self.layoutWidget1)
        self.valButton_6.setObjectName(u"valButton_6")
        sizePolicy3.setHeightForWidth(self.valButton_6.sizePolicy().hasHeightForWidth())
        self.valButton_6.setSizePolicy(sizePolicy3)
        self.valButton_6.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_6, 1, 3, 1, 1)

        self.valButton_2 = QPushButton(self.layoutWidget1)
        self.valButton_2.setObjectName(u"valButton_2")
        sizePolicy3.setHeightForWidth(self.valButton_2.sizePolicy().hasHeightForWidth())
        self.valButton_2.setSizePolicy(sizePolicy3)
        self.valButton_2.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_2, 2, 2, 1, 1)

        self.valButton_9 = QPushButton(self.layoutWidget1)
        self.valButton_9.setObjectName(u"valButton_9")
        sizePolicy3.setHeightForWidth(self.valButton_9.sizePolicy().hasHeightForWidth())
        self.valButton_9.setSizePolicy(sizePolicy3)
        self.valButton_9.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_9, 0, 3, 1, 1)

        self.valButton_0 = QPushButton(self.layoutWidget1)
        self.valButton_0.setObjectName(u"valButton_0")
        sizePolicy3.setHeightForWidth(self.valButton_0.sizePolicy().hasHeightForWidth())
        self.valButton_0.setSizePolicy(sizePolicy3)
        self.valButton_0.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_0, 3, 1, 1, 1)

        self.msButton = QPushButton(self.layoutWidget1)
        self.msButton.setObjectName(u"msButton")
        sizePolicy3.setHeightForWidth(self.msButton.sizePolicy().hasHeightForWidth())
        self.msButton.setSizePolicy(sizePolicy3)
        self.msButton.setFont(font1)
        self.msButton.setMouseTracking(False)
        self.msButton.setAutoFillBackground(False)

        self.MainKeyboardLayout.addWidget(self.msButton, 0, 0, 1, 1)

        self.valButton_7 = QPushButton(self.layoutWidget1)
        self.valButton_7.setObjectName(u"valButton_7")
        sizePolicy3.setHeightForWidth(self.valButton_7.sizePolicy().hasHeightForWidth())
        self.valButton_7.setSizePolicy(sizePolicy3)
        self.valButton_7.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_7, 0, 1, 1, 1)

        self.valButton_4 = QPushButton(self.layoutWidget1)
        self.valButton_4.setObjectName(u"valButton_4")
        sizePolicy3.setHeightForWidth(self.valButton_4.sizePolicy().hasHeightForWidth())
        self.valButton_4.setSizePolicy(sizePolicy3)
        self.valButton_4.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_4, 1, 1, 1, 1)

        self.valButton_1 = QPushButton(self.layoutWidget1)
        self.valButton_1.setObjectName(u"valButton_1")
        sizePolicy3.setHeightForWidth(self.valButton_1.sizePolicy().hasHeightForWidth())
        self.valButton_1.setSizePolicy(sizePolicy3)
        self.valButton_1.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_1, 2, 1, 1, 1)

        self.plusMinusButton = QPushButton(self.layoutWidget1)
        self.plusMinusButton.setObjectName(u"plusMinusButton")
        sizePolicy3.setHeightForWidth(self.plusMinusButton.sizePolicy().hasHeightForWidth())
        self.plusMinusButton.setSizePolicy(sizePolicy3)
        self.plusMinusButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.plusMinusButton, 3, 3, 1, 1)

        self.mrButton = QPushButton(self.layoutWidget1)
        self.mrButton.setObjectName(u"mrButton")
        sizePolicy3.setHeightForWidth(self.mrButton.sizePolicy().hasHeightForWidth())
        self.mrButton.setSizePolicy(sizePolicy3)
        self.mrButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.mrButton, 1, 0, 1, 1)

        self.valButton_3 = QPushButton(self.layoutWidget1)
        self.valButton_3.setObjectName(u"valButton_3")
        sizePolicy3.setHeightForWidth(self.valButton_3.sizePolicy().hasHeightForWidth())
        self.valButton_3.setSizePolicy(sizePolicy3)
        self.valButton_3.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_3, 2, 3, 1, 1)

        self.valButton_5 = QPushButton(self.layoutWidget1)
        self.valButton_5.setObjectName(u"valButton_5")
        sizePolicy3.setHeightForWidth(self.valButton_5.sizePolicy().hasHeightForWidth())
        self.valButton_5.setSizePolicy(sizePolicy3)
        self.valButton_5.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.valButton_5, 1, 2, 1, 1)

        self.mPlusButton = QPushButton(self.layoutWidget1)
        self.mPlusButton.setObjectName(u"mPlusButton")
        sizePolicy3.setHeightForWidth(self.mPlusButton.sizePolicy().hasHeightForWidth())
        self.mPlusButton.setSizePolicy(sizePolicy3)
        self.mPlusButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.mPlusButton, 2, 0, 1, 1)

        self.mMinusButton = QPushButton(self.layoutWidget1)
        self.mMinusButton.setObjectName(u"mMinusButton")
        sizePolicy3.setHeightForWidth(self.mMinusButton.sizePolicy().hasHeightForWidth())
        self.mMinusButton.setSizePolicy(sizePolicy3)
        self.mMinusButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.mMinusButton, 3, 0, 1, 1)

        self.multButton = QPushButton(self.layoutWidget1)
        self.multButton.setObjectName(u"multButton")
        sizePolicy3.setHeightForWidth(self.multButton.sizePolicy().hasHeightForWidth())
        self.multButton.setSizePolicy(sizePolicy3)
        self.multButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.multButton, 0, 4, 1, 1)

        self.divButton = QPushButton(self.layoutWidget1)
        self.divButton.setObjectName(u"divButton")
        sizePolicy3.setHeightForWidth(self.divButton.sizePolicy().hasHeightForWidth())
        self.divButton.setSizePolicy(sizePolicy3)
        self.divButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.divButton, 1, 4, 1, 1)

        self.plusButton = QPushButton(self.layoutWidget1)
        self.plusButton.setObjectName(u"plusButton")
        sizePolicy3.setHeightForWidth(self.plusButton.sizePolicy().hasHeightForWidth())
        self.plusButton.setSizePolicy(sizePolicy3)
        self.plusButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.plusButton, 2, 4, 1, 1)

        self.minusButton = QPushButton(self.layoutWidget1)
        self.minusButton.setObjectName(u"minusButton")
        sizePolicy3.setHeightForWidth(self.minusButton.sizePolicy().hasHeightForWidth())
        self.minusButton.setSizePolicy(sizePolicy3)
        self.minusButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.minusButton, 3, 4, 1, 1)

        self.equalButton = QPushButton(self.layoutWidget1)
        self.equalButton.setObjectName(u"equalButton")
        sizePolicy3.setHeightForWidth(self.equalButton.sizePolicy().hasHeightForWidth())
        self.equalButton.setSizePolicy(sizePolicy3)
        self.equalButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.equalButton, 3, 5, 1, 1)

        self.expButton = QPushButton(self.layoutWidget1)
        self.expButton.setObjectName(u"expButton")
        sizePolicy3.setHeightForWidth(self.expButton.sizePolicy().hasHeightForWidth())
        self.expButton.setSizePolicy(sizePolicy3)
        self.expButton.setFont(font1)

        self.MainKeyboardLayout.addWidget(self.expButton, 1, 5, 1, 1)

        self.MainKeyboardLayout.setRowStretch(0, 1)
        self.MainKeyboardLayout.setRowStretch(1, 1)
        self.MainKeyboardLayout.setRowStretch(2, 1)
        self.MainKeyboardLayout.setRowStretch(3, 1)
        self.MainKeyboardLayout.setColumnStretch(0, 1)
        self.MainKeyboardLayout.setColumnStretch(1, 1)
        self.MainKeyboardLayout.setColumnStretch(2, 1)
        self.MainKeyboardLayout.setColumnStretch(3, 1)
        self.MainKeyboardLayout.setColumnStretch(4, 1)
        self.MainKeyboardLayout.setColumnStretch(5, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText("")
        self.clearAllButton.setText(QCoreApplication.translate("MainWindow", u"Clear all", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.backspaseButton.setText(QCoreApplication.translate("MainWindow", u"Backspace", None))
        self.valButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.dotButton.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.valButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.valButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.valButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.valButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.msButton.setText(QCoreApplication.translate("MainWindow", u"MS", None))
        self.valButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.valButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.valButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.plusMinusButton.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.mrButton.setText(QCoreApplication.translate("MainWindow", u"MR", None))
        self.valButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.valButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.mPlusButton.setText(QCoreApplication.translate("MainWindow", u"M+", None))
        self.mMinusButton.setText(QCoreApplication.translate("MainWindow", u"M-", None))
        self.multButton.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.divButton.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.plusButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.minusButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.equalButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.expButton.setText(QCoreApplication.translate("MainWindow", u"x^y", None))
    # retranslateUi

