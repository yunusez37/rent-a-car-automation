# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'giris.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_anaPencere(object):
    def setupUi(self, anaPencere):
        if not anaPencere.objectName():
            anaPencere.setObjectName(u"anaPencere")
        anaPencere.resize(496, 365)
        anaPencere.setMouseTracking(False)
        anaPencere.setStyleSheet(u"QWidget#centralwidget, QDialog {\n"
"    background-color: #EAEDED; /* \"Platinum\" Gri */\n"
"}")
        self.groupBox = QGroupBox(anaPencere)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 100, 441, 241))
        self.groupBox.setStyleSheet(u"QGroupBox { background-color: #FFFFF0; border: 1px solid #DDDDDD; border-radius: 12px; margin-top: 25px; padding-top: 10px; } QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 0 5px; font-size: 16px; font-weight: bold; color: #555555; }\n"
"")
        self.musteri_bilgileri = QPushButton(self.groupBox)
        self.musteri_bilgileri.setObjectName(u"musteri_bilgileri")
        self.musteri_bilgileri.setGeometry(QRect(20, 70, 181, 41))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.musteri_bilgileri.setFont(font)
        self.musteri_bilgileri.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.musteri_bilgileri.setStyleSheet(u"QPushButton { background-color: #1c6071;  color: white; font-size: 10px; font-weight: bold; padding: 10px 30px; border-radius: 8px; border: none; } QPushButton:hover { background-color: #27ae60; }")
        self.arac_bilgileri = QPushButton(self.groupBox)
        self.arac_bilgileri.setObjectName(u"arac_bilgileri")
        self.arac_bilgileri.setGeometry(QRect(240, 70, 181, 41))
        font1 = QFont()
        font1.setBold(True)
        self.arac_bilgileri.setFont(font1)
        self.arac_bilgileri.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.arac_bilgileri.setStyleSheet(u"QPushButton { background-color: #1c6071;  color: white; font-size: 10px; font-weight: bold; padding: 10px 30px; border-radius: 8px; border: none; } QPushButton:hover { background-color: #27ae60; }")
        self.kirlama_islem = QPushButton(self.groupBox)
        self.kirlama_islem.setObjectName(u"kirlama_islem")
        self.kirlama_islem.setGeometry(QRect(20, 140, 181, 41))
        self.kirlama_islem.setFont(font1)
        self.kirlama_islem.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.kirlama_islem.setStyleSheet(u"QPushButton { background-color: #1c6071;  color: white; font-size: 10px; font-weight: bold; padding: 10px 30px; border-radius: 8px; border: none; } QPushButton:hover { background-color: #27ae60; }")
        self.aktif_kiralama = QPushButton(self.groupBox)
        self.aktif_kiralama.setObjectName(u"aktif_kiralama")
        self.aktif_kiralama.setGeometry(QRect(240, 140, 181, 41))
        self.aktif_kiralama.setFont(font1)
        self.aktif_kiralama.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.aktif_kiralama.setStyleSheet(u"QPushButton { background-color: #1c6071;  color: white; font-size: 10px; font-weight: bold; padding: 10px 30px; border-radius: 8px; border: none; } QPushButton:hover { background-color: #27ae60; }")
        self.baslik_kutu = QPushButton(anaPencere)
        self.baslik_kutu.setObjectName(u"baslik_kutu")
        self.baslik_kutu.setGeometry(QRect(30, 30, 441, 51))
        self.baslik_kutu.setFont(font)
        self.baslik_kutu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.baslik_kutu.setStyleSheet(u"QPushButton { background-color: #1c6071;  color: white; font-size: 8px; font-weight: bold; padding: 10px 30px; border-radius: 8px; border: none; }")
        self.baslik = QLabel(anaPencere)
        self.baslik.setObjectName(u"baslik")
        self.baslik.setGeometry(QRect(30, 40, 441, 31))
        font2 = QFont()
        font2.setFamilies([u"Marlett"])
        font2.setPointSize(19)
        font2.setBold(True)
        font2.setItalic(False)
        self.baslik.setFont(font2)
        self.baslik.setStyleSheet(u"# ffffff")
        self.baslik.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(anaPencere)

        QMetaObject.connectSlotsByName(anaPencere)
    # setupUi

    def retranslateUi(self, anaPencere):
        anaPencere.setWindowTitle(QCoreApplication.translate("anaPencere", u"anaPencere", None))
        self.groupBox.setTitle("")
        self.musteri_bilgileri.setText(QCoreApplication.translate("anaPencere", u"M\u00dc\u015eTER\u0130 B\u0130LG\u0130LER\u0130", None))
        self.arac_bilgileri.setText(QCoreApplication.translate("anaPencere", u"ARA\u00c7 B\u0130LG\u0130LER\u0130", None))
        self.kirlama_islem.setText(QCoreApplication.translate("anaPencere", u"K\u0130RALAMA \u0130\u015eLEMLER\u0130", None))
        self.aktif_kiralama.setText(QCoreApplication.translate("anaPencere", u"AKT\u0130F K\u0130RALAMA TAK\u0130B\u0130", None))
        self.baslik_kutu.setText("")
        self.baslik.setText(QCoreApplication.translate("anaPencere", u"ARA\u00c7 K\u0130RALAMA OTOMASYONU", None))
    # retranslateUi

