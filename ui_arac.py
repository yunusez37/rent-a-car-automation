# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arac.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(626, 467)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 120, 191, 241))
        self.groupBox.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }\n"
"")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 30, 101, 211))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300;  }")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300;  }")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; }")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; /* Odaklan\u0131nca sar\u0131 */ }")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; /* Odaklan\u0131nca sar\u0131 */ }")
        self.spinBox.setMinimum(1990)
        self.spinBox.setMaximum(2025)

        self.verticalLayout.addWidget(self.spinBox)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 161, 31))
        self.label.setStyleSheet(u"QLabel { font-size: 18px; font-weight: bold; color: #555555; padding: 5px;  }")
        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 32, 52, 211))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(210, 130, 191, 331))
        self.groupBox_2.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }")
        self.layoutWidget2 = QWidget(self.groupBox_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(100, 20, 91, 261))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.layoutWidget2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; }")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.lineEdit_menzil = QLineEdit(self.layoutWidget2)
        self.lineEdit_menzil.setObjectName(u"lineEdit_menzil")
        self.lineEdit_menzil.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300;  }")

        self.verticalLayout_2.addWidget(self.lineEdit_menzil)

        self.comboBox_5 = QComboBox(self.layoutWidget2)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; }\n"
"")

        self.verticalLayout_2.addWidget(self.comboBox_5)

        self.lineEdit_4 = QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300;  }")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.comboBox_3 = QComboBox(self.layoutWidget2)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; }")

        self.verticalLayout_2.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.layoutWidget2)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; }")

        self.verticalLayout_2.addWidget(self.comboBox_4)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 161, 31))
        self.label_2.setStyleSheet(u"QLabel { font-size: 18px; font-weight: bold; color: #555555; padding: 5px; \n"
" }")
        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 30, 81, 251))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_6.addWidget(self.label_10)

        self.label_menzil = QLabel(self.layoutWidget_2)
        self.label_menzil.setObjectName(u"label_menzil")

        self.verticalLayout_6.addWidget(self.label_menzil)

        self.label_12 = QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_6.addWidget(self.label_12)

        self.label_13 = QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_6.addWidget(self.label_13)

        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_6.addWidget(self.label_14)

        self.label_18 = QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_6.addWidget(self.label_18)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(410, 120, 191, 241))
        self.groupBox_3.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }")
        self.layoutWidget3 = QWidget(self.groupBox_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(100, 30, 91, 211))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.doubleSpinBox = QDoubleSpinBox(self.layoutWidget3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; }")

        self.verticalLayout_3.addWidget(self.doubleSpinBox)

        self.lineEdit_5 = QLineEdit(self.layoutWidget3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300;  }")

        self.verticalLayout_3.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.layoutWidget3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; }")

        self.verticalLayout_3.addWidget(self.lineEdit_6)

        self.checkBox = QCheckBox(self.layoutWidget3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; /* Odaklan\u0131nca sar\u0131 */ }")

        self.verticalLayout_3.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.layoutWidget3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"QLineEdit, QComboBox, QSpinBox, QTextEdit { background-color: #FFFFFF; color: #333333; border: 1px solid #CCCCCC; border-radius: 6px; padding: 6px; } QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QTextEdit:focus { border: 2px solid #FFC300; /* Odaklan\u0131nca sar\u0131 */ }")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 141, 31))
        self.label_3.setStyleSheet(u"QLabel { font-size: 18px; font-weight: bold; color: #555555; padding: 5px; \n"
" }")
        self.layoutWidget_3 = QWidget(self.groupBox_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 30, 85, 131))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget_3)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_7.addWidget(self.label_15)

        self.label_16 = QLabel(self.layoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_7.addWidget(self.label_16)

        self.label_17 = QLabel(self.layoutWidget_3)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_7.addWidget(self.label_17)

        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(160, 10, 301, 80))
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
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(410, 370, 201, 41))
        self.pushButton.setStyleSheet(u"QPushButton { background-color: #1c6071;  color: white; font-size: 18px; font-weight: bold; padding: 10px 30px; border-radius: 8px; border: none; } QPushButton:hover { background-color: #27ae60; }")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Otomobil", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Arazi / SUV", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"Ticari", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"Motosiklet", None))

        self.label.setText(QCoreApplication.translate("Form", u"TEMEL B\u0130LG\u0130LER", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"ARA\u00c7 T\u00dcR\u00dc:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"MARKA:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"MODEL:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"RENK:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u00dcRET\u0130M YILI:", None))
        self.groupBox_2.setTitle("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Benzin", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Dizel", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"LPG", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Elektrik", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"Hibrit", None))

        self.comboBox_5.setItemText(0, QCoreApplication.translate("Form", u"Sedan", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("Form", u"Hatchback", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("Form", u"Station Wagon", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("Form", u"Cabrio", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("Form", u"Coupe", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"\u00d6nden \u00c7eki\u015f", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"Arkadan \u0130ti\u015f", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"AWD", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("Form", u"Manuel", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Form", u"Otomatik", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Form", u"Yar\u0131 Otomatik", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"TEKN\u0130K B\u0130LG\u0130LER", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"YAKIT T\u00dcR\u00dc:", None))
        self.label_menzil.setText(QCoreApplication.translate("Form", u"MENZ\u0130L:", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"KASA T\u0130P\u0130:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"MOTOR G\u00dcC\u00dc:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u00c7EK\u0130\u015e:", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"V\u0130TES:", None))
        self.groupBox_3.setTitle("")
        self.checkBox.setText(QCoreApplication.translate("Form", u"Kirada M\u0131?", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"Kullan\u0131m D\u0131\u015f\u0131 M\u0131?", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ARA\u00c7 DURUM", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"G\u00dcNL\u00dcK K\u0130RALAMA:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u015eAS\u0130 NO:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"MOTOR NO:", None))
        self.groupBox_4.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Form", u"ARA\u00c7 B\u0130LG\u0130LER\u0130 G\u0130R\u0130\u015e", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"ARACI KAYDET", None))
    # retranslateUi

