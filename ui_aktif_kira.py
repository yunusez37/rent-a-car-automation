# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aktif_kira.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(583, 526)
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(140, 20, 301, 80))
        self.groupBox_4.setStyleSheet(u"QGroupBox { background-color: #1c6071; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 40, 301, 31))
        font = QFont()
        font.setFamilies([u"MS Gothic"])
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QLabel { font-size: 18px; font-weight: bold; color: #FFFFFF; padding: 5px;  }")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 80, 561, 401))
        self.groupBox.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }")
        self.tableWidget = QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 40, 541, 351))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_4.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Form", u"K\u0130RADAK\u0130 ARA\u00c7 L\u0130STES\u0130", None))
        self.groupBox.setTitle("")
    # retranslateUi

