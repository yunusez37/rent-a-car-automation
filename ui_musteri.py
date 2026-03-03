# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'musteri.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(523, 497)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 30, 521, 51))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.line_2.setFont(font)
        self.line_2.setFrameShadow(QFrame.Shadow.Raised)
        self.line_2.setLineWidth(20)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 0, 521, 41))
        self.line_3.setLineWidth(20)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.baslik2 = QLabel(Form)
        self.baslik2.setObjectName(u"baslik2")
        self.baslik2.setGeometry(QRect(100, 20, 331, 41))
        font1 = QFont()
        font1.setFamilies([u"MS Gothic"])
        font1.setPointSize(25)
        self.baslik2.setFont(font1)
        self.baslik2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.kaydet = QPushButton(Form)
        self.kaydet.setObjectName(u"kaydet")
        self.kaydet.setGeometry(QRect(170, 430, 181, 31))
        font2 = QFont()
        font2.setBold(True)
        self.kaydet.setFont(font2)
        self.kaydet.setStyleSheet(u"QPushButton { background-color: #1c6071;  color: white; font-size: 10px; font-weight: bold; padding: 10px 30px; border-radius: 8px; border: none; } QPushButton:hover { background-color: #27ae60; }")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 80, 441, 181))
        self.groupBox.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }\n"
"")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(110, 30, 241, 151))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label1 = QLabel(self.widget)
        self.label1.setObjectName(u"label1")
        self.label1.setFrameShape(QFrame.Shape.NoFrame)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.label2 = QLabel(self.widget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label2)

        self.lineEdit1 = QLineEdit(self.widget)
        self.lineEdit1.setObjectName(u"lineEdit1")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit1)

        self.label3 = QLabel(self.widget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label3)

        self.lineEdit2 = QLineEdit(self.widget)
        self.lineEdit2.setObjectName(u"lineEdit2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit2)

        self.label4 = QLabel(self.widget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label4)

        self.lineEdit3 = QLineEdit(self.widget)
        self.lineEdit3.setObjectName(u"lineEdit3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.lineEdit3)

        self.baslik3 = QLabel(self.widget)
        self.baslik3.setObjectName(u"baslik3")
        font3 = QFont()
        font3.setFamilies([u"MS Gothic"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.baslik3.setFont(font3)
        self.baslik3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.baslik3)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 250, 211, 171))
        self.groupBox_2.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }\n"
"")
        self.widget1 = QWidget(self.groupBox_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(9, 40, 171, 64))
        self.formLayout_3 = QFormLayout(self.widget1)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label5 = QLabel(self.widget1)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label5)

        self.lineEdit4 = QLineEdit(self.widget1)
        self.lineEdit4.setObjectName(u"lineEdit4")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit4)

        self.label6 = QLabel(self.widget1)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label6)

        self.lineEdit5 = QLineEdit(self.widget1)
        self.lineEdit5.setObjectName(u"lineEdit5")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lineEdit5)

        self.baslik4 = QLabel(self.widget1)
        self.baslik4.setObjectName(u"baslik4")
        self.baslik4.setFont(font3)
        self.baslik4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.baslik4)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(260, 250, 211, 171))
        self.groupBox_3.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }\n"
"")
        self.widget2 = QWidget(self.groupBox_3)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(3, 30, 201, 121))
        self.gridLayout = QGridLayout(self.widget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.baslik5 = QLabel(self.widget2)
        self.baslik5.setObjectName(u"baslik5")
        self.baslik5.setFont(font3)
        self.baslik5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.baslik5, 0, 0, 3, 3)

        self.ehliyet_sinifi = QComboBox(self.widget2)
        self.ehliyet_sinifi.addItem("")
        self.ehliyet_sinifi.addItem("")
        self.ehliyet_sinifi.addItem("")
        self.ehliyet_sinifi.addItem("")
        self.ehliyet_sinifi.addItem("")
        self.ehliyet_sinifi.addItem("")
        self.ehliyet_sinifi.addItem("")
        self.ehliyet_sinifi.setObjectName(u"ehliyet_sinifi")

        self.gridLayout.addWidget(self.ehliyet_sinifi, 4, 1, 1, 2)

        self.lineEdit7 = QLineEdit(self.widget2)
        self.lineEdit7.setObjectName(u"lineEdit7")

        self.gridLayout.addWidget(self.lineEdit7, 6, 1, 1, 2)

        self.radioButton_2 = QRadioButton(self.widget2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 5, 2, 1, 1)

        self.radioButton = QRadioButton(self.widget2)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 5, 1, 1, 1)

        self.label7 = QLabel(self.widget2)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label7, 3, 0, 1, 1)

        self.label9 = QLabel(self.widget2)
        self.label9.setObjectName(u"label9")
        self.label9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label9, 5, 0, 1, 1)

        self.label10 = QLabel(self.widget2)
        self.label10.setObjectName(u"label10")
        self.label10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label10, 6, 0, 1, 1)

        self.label8 = QLabel(self.widget2)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label8, 4, 0, 1, 1)

        self.lineEdit6 = QLineEdit(self.widget2)
        self.lineEdit6.setObjectName(u"lineEdit6")

        self.gridLayout.addWidget(self.lineEdit6, 3, 1, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.baslik2.setText(QCoreApplication.translate("Form", u"M\u00dc\u015eTER\u0130 B\u0130LG\u0130 G\u0130R\u0130\u015e\u0130", None))
        self.kaydet.setText(QCoreApplication.translate("Form", u"M\u00dc\u015eTER\u0130Y\u0130 KAYDET", None))
        self.groupBox.setTitle("")
        self.label1.setText(QCoreApplication.translate("Form", u"AD:", None))
        self.label2.setText(QCoreApplication.translate("Form", u"SOYAD:", None))
        self.label3.setText(QCoreApplication.translate("Form", u"TC K\u0130ML\u0130K:", None))
        self.label4.setText(QCoreApplication.translate("Form", u"DO\u011eUM TAR\u0130H\u0130:", None))
        self.baslik3.setText(QCoreApplication.translate("Form", u"K\u0130\u015e\u0130SEL B\u0130LG\u0130LER", None))
        self.groupBox_2.setTitle("")
        self.label5.setText(QCoreApplication.translate("Form", u"CEP TELEFONU:", None))
        self.label6.setText(QCoreApplication.translate("Form", u"ADRES:", None))
        self.baslik4.setText(QCoreApplication.translate("Form", u"\u0130LET\u0130\u015e\u0130M B\u0130LG\u0130LER\u0130", None))
        self.groupBox_3.setTitle("")
        self.baslik5.setText(QCoreApplication.translate("Form", u"MESLEK VE DURUM B\u0130LG\u0130LER\u0130", None))
        self.ehliyet_sinifi.setItemText(0, QCoreApplication.translate("Form", u"M", None))
        self.ehliyet_sinifi.setItemText(1, QCoreApplication.translate("Form", u"A1", None))
        self.ehliyet_sinifi.setItemText(2, QCoreApplication.translate("Form", u"A2", None))
        self.ehliyet_sinifi.setItemText(3, QCoreApplication.translate("Form", u"B", None))
        self.ehliyet_sinifi.setItemText(4, QCoreApplication.translate("Form", u"C", None))
        self.ehliyet_sinifi.setItemText(5, QCoreApplication.translate("Form", u"C1", None))
        self.ehliyet_sinifi.setItemText(6, QCoreApplication.translate("Form", u"D1", None))

        self.radioButton_2.setText(QCoreApplication.translate("Form", u"BEKAR", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"EVL\u0130", None))
        self.label7.setText(QCoreApplication.translate("Form", u"MESLEK:", None))
        self.label9.setText(QCoreApplication.translate("Form", u"MEDEN\u0130 HAL\u0130:", None))
        self.label10.setText(QCoreApplication.translate("Form", u"E\u011e\u0130T\u0130M DURUMU:", None))
        self.label8.setText(QCoreApplication.translate("Form", u"EHL\u0130YET SINIFI:", None))
    # retranslateUi

