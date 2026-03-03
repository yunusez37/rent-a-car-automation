import sys
import mysql.connector
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class AraçKiralamaSistemi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()
        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "deneme",
            "database": "db90240000230",
            "port": 3306
        }
        self.veritabanini_hazirla()
        self.ana_pencereyi_yukle()

    def veritabanini_hazirla(self):
        db = mysql.connector.connect(host=self.db_config["host"], user=self.db_config["user"], password=self.db_config["password"])
        cursor = db.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_config['database']}")
        cursor.execute(f"USE {self.db_config['database']}")

        cursor.execute("""CREATE TABLE IF NOT EXISTS musteriler (id INT AUTO_INCREMENT PRIMARY KEY, ad_soyad VARCHAR(255), tc_no VARCHAR(11), telefon VARCHAR(20))""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS araclar (id INT AUTO_INCREMENT PRIMARY KEY, marka VARCHAR(100), model VARCHAR(100), yakit_turu VARCHAR(50), gunluk_ucret DECIMAL(10, 2))""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS kiralamalar (id INT AUTO_INCREMENT PRIMARY KEY, musteri_id INT, arac_id INT, kiralama_suresi INT, gidilecek_yer VARCHAR(255), baslangic_tarihi DATE)""")

        cursor.execute("SHOW COLUMNS FROM araclar LIKE 'menzil'")
        if not cursor.fetchone(): cursor.execute("ALTER TABLE araclar ADD COLUMN menzil VARCHAR(50)")
        cursor.execute("SHOW COLUMNS FROM kiralamalar LIKE 'toplam_ucret'")
        if not cursor.fetchone(): cursor.execute("ALTER TABLE kiralamalar ADD COLUMN toplam_ucret DECIMAL(10,2)")

        cursor.execute("SELECT count(*) FROM musteriler")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO musteriler (ad_soyad, tc_no, telefon) VALUES ('Ahmet Yılmaz', '111', '555'), ('Elif Kaya', '222', '444'), ('Can Demir', '333', '222')")

        cursor.execute("SELECT count(*) FROM araclar")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO araclar (marka, model, yakit_turu, gunluk_ucret, menzil) VALUES ('Honda', 'Civic', 'Dizel', 1200, ''), ('Ford', 'Focus', 'Benzin', 1000, ''), ('Togg', 'T10X', 'Elektrik', 2000, '523 KM')")

        db.commit()
        db.close()

    def ana_pencereyi_yukle(self):
        ui_file = QFile("giris.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = self.loader.load(ui_file, self)
        ui_file.close()
        self.setCentralWidget(self.ui)
        self.ui.musteri_bilgileri.clicked.connect(self.musteri_sayfasi_ac)
        self.ui.arac_bilgileri.clicked.connect(self.arac_sayfasi_ac)
        self.ui.kirlama_islem.clicked.connect(self.kiralama_sayfasi_ac)
        self.ui.aktif_kiralama.clicked.connect(self.aktif_kira_sayfasi_ac)

    def musteri_sayfasi_ac(self):
        ui_file = QFile("musteri.ui")
        ui_file.open(QFile.ReadOnly)
        self.m_ui = self.loader.load(ui_file)
        ui_file.close()
        self.m_ui.kaydet.clicked.connect(self.musteri_kaydet)
        self.m_ui.show()

    def musteri_kaydet(self):
        db = mysql.connector.connect(**self.db_config)
        cursor = db.cursor()
        sql = "INSERT INTO musteriler (ad_soyad, tc_no, telefon) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.m_ui.lineEdit.text(), self.m_ui.lineEdit1.text(), self.m_ui.lineEdit2.text()))
        db.commit()
        db.close()
        QMessageBox.information(None, "Bilgi", "Müşteri kaydedildi.")

    def arac_sayfasi_ac(self):
        ui_file = QFile("arac.ui")
        ui_file.open(QFile.ReadOnly)
        self.arac_ui = self.loader.load(ui_file)
        ui_file.close()
        if self.arac_ui.comboBox.findText("Elektrik") == -1: self.arac_ui.comboBox.addItem("Elektrik")
        self.arac_ui.label_menzil.setVisible(False)
        self.arac_ui.lineEdit_menzil.setVisible(False)
        self.arac_ui.comboBox.currentTextChanged.connect(self.yakit_kontrol)
        self.arac_ui.pushButton.clicked.connect(self.arac_kaydet)
        self.arac_ui.show()

    def yakit_kontrol(self, metin):
        durum = (metin.lower() == "elektrik")
        self.arac_ui.label_menzil.setVisible(durum)
        self.arac_ui.lineEdit_menzil.setVisible(durum)

    def arac_kaydet(self):
        db = mysql.connector.connect(**self.db_config)
        cursor = db.cursor()
        sql = "INSERT INTO araclar (marka, model, yakit_turu, gunluk_ucret, menzil) VALUES (%s, %s, %s, %s, %s)"
        val = (self.arac_ui.lineEdit.text(), self.arac_ui.lineEdit_2.text(), self.arac_ui.comboBox.currentText(), self.arac_ui.doubleSpinBox.value(), self.arac_ui.lineEdit_menzil.text())
        cursor.execute(sql, val)
        db.commit()
        db.close()
        QMessageBox.information(None, "Bilgi", "Araç kaydedildi.")

    def kiralama_sayfasi_ac(self):
        ui_file = QFile("kiralama.ui")
        ui_file.open(QFile.ReadOnly)
        self.k_ui = self.loader.load(ui_file)
        ui_file.close()
        self.kira_verileri_yukle()
        self.k_ui.spinBox.valueChanged.connect(self.ucret_hesapla)
        self.k_ui.comboBox_3.currentIndexChanged.connect(self.ucret_hesapla)
        self.k_ui.pushButton.clicked.connect(self.kiralama_kaydet)
        self.ucret_hesapla()
        self.k_ui.show()

    def ucret_hesapla(self):
        a_id = self.k_ui.comboBox_3.currentData()
        if a_id is None: return 0
        db = mysql.connector.connect(**self.db_config)
        cursor = db.cursor()
        cursor.execute("SELECT gunluk_ucret, yakit_turu FROM araclar WHERE id = %s", (a_id,))
        res = cursor.fetchone()
        db.close()
        if res:
            total = float(res[0]) * self.k_ui.spinBox.value()
            if "elektrik" in str(res[1]).lower(): total *= 0.5
            if hasattr(self.k_ui, 'label_toplam'): self.k_ui.label_toplam.setText(f"Toplam Ücret: {total} TL")
            return total
        return 0

    def kiralama_kaydet(self):
        toplam = self.ucret_hesapla()
        db = mysql.connector.connect(**self.db_config)
        cursor = db.cursor()
        sql = "INSERT INTO kiralamalar (musteri_id, arac_id, kiralama_suresi, toplam_ucret, baslangic_tarihi, gidilecek_yer) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.k_ui.comboBox_2.currentData(), self.k_ui.comboBox_3.currentData(), self.k_ui.spinBox.value(), toplam, self.k_ui.dateEdit.date().toString("yyyy-MM-dd"), self.k_ui.lineEdit.text())
        cursor.execute(sql, val)
        db.commit()
        db.close()
        QMessageBox.information(None, "Bilgi", f"Kiralama yapıldı. Ücret: {toplam} TL")

    def kira_verileri_yukle(self):
        db = mysql.connector.connect(**self.db_config)
        cursor = db.cursor()
        cursor.execute("SELECT id, ad_soyad FROM musteriler")
        for (i, a) in cursor: self.k_ui.comboBox_2.addItem(a, i)
        cursor.execute("SELECT id, marka, model FROM araclar")
        for (i, m, mo) in cursor: self.k_ui.comboBox_3.addItem(f"{m} {mo}", i)
        db.close()

    def aktif_kira_sayfasi_ac(self):
        ui_file = QFile("aktif_kira.ui")
        ui_file.open(QFile.ReadOnly)
        self.l_ui = self.loader.load(ui_file)
        ui_file.close()
        self.tabloyu_guncelle()
        self.l_ui.show()

    def tabloyu_guncelle(self):
        db = mysql.connector.connect(**self.db_config)
        cursor = db.cursor()
        cursor.execute("""SELECT m.ad_soyad, a.marka, a.model, k.kiralama_suresi, k.toplam_ucret
                          FROM kiralamalar k
                          INNER JOIN musteriler m ON k.musteri_id = m.id
                          INNER JOIN araclar a ON k.arac_id = a.id""")
        res = cursor.fetchall()
        self.l_ui.tableWidget.setRowCount(len(res))
        self.l_ui.tableWidget.setColumnCount(5)
        self.l_ui.tableWidget.setHorizontalHeaderLabels(["Müşteri", "Marka", "Model", "Süre", "Ücret"])
        for r_no, row in enumerate(res):
            for c_no, val in enumerate(row): self.l_ui.tableWidget.setItem(r_no, c_no, QTableWidgetItem(str(val)))
        db.close()

if __name__ == "__main__":
    program_klasoru = os.path.dirname(os.path.abspath(__file__))
    os.chdir(program_klasoru)
    app = QApplication(sys.argv)
    window = AraçKiralamaSistemi()
    window.show()
    sys.exit(app.exec())
