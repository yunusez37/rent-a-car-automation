# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kiralama.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(516, 371)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 110, 231, 171))
        self.groupBox.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }\n"
"")
        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(20, 110, 181, 22))
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 50, 181, 22))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 121, 21))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 90, 51, 20))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 171, 20))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setBold(True)
        self.label_7.setFont(font)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(260, 110, 231, 171))
        self.groupBox_2.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }\n"
"")
        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(100, 40, 121, 22))
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 90, 121, 21))
        self.dateEdit = QDateEdit(self.groupBox_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(100, 120, 121, 22))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 81, 21))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 90, 61, 21))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 120, 71, 20))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 171, 20))
        self.label_8.setFont(font)
        self.label_toplam = QLabel(self.groupBox_2)
        self.label_toplam.setObjectName(u"label_toplam")
        self.label_toplam.setGeometry(QRect(90, 60, 141, 31))
        self.label_toplam.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_toplam_2 = QLabel(self.groupBox_2)
        self.label_toplam_2.setObjectName(u"label_toplam_2")
        self.label_toplam_2.setGeometry(QRect(10, 60, 81, 31))
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(100, 0, 301, 80))
        self.groupBox_4.setStyleSheet(u"QGroupBox { background-color: #1c6071; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 40, 301, 31))
        font1 = QFont()
        font1.setFamilies([u"MS Gothic"])
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 290, 241, 31))
        self.pushButton.setStyleSheet(u"QPushButton { background-color: #1c6071;  color: white; font-size: 12px; font-weight: bold; padding: 10px 30px; border-radius: 8px; border: none; } QPushButton:hover { background-color: #27ae60; }")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("Form", u"M\u00fc\u015fteri (Ad\u0131 Soyad\u0131)", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Ara\u00e7", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"M\u00dc\u015eTER\u0130 VE ARA\u00c7 SE\u00c7\u0130M\u0130", None))
        self.groupBox_2.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Kiralama S\u00fcresi", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Gidilcek yer", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Ba\u015flang\u0131\u00e7 tarihi", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"K\u0130RALAMA DETAYLARI", None))
        self.label_toplam.setText("")
        self.label_toplam_2.setText(QCoreApplication.translate("Form", u"YAPILAN \u0130ND\u0130R\u0130M:", None))
        self.groupBox_4.setTitle("")
        self.label.setText(QCoreApplication.translate("Form", u"K\u0130RALAMA KAYIT EKRANI", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"K\u0130RALAMA \u0130\u015eLEM\u0130N\u0130 TAMAMLA", None))
    # retranslateUi

