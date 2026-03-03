import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import mysql.connector # MySQL bağlantısı için gerekli kütüphane

class MusteriKayit(QWidget):
    def __init__(self):
        super().__init__()

        # 1. UI Yükleme
        loader = QUiLoader()
        ui_file = QFile("musteri.ui")
        if not ui_file.open(QFile.ReadOnly):
            print("UI dosyası açılamadı!")
            return
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # 2. Kaydet Butonuna Fonksiyon Bağlama
        self.ui.kaydet.clicked.connect(self.veriyi_kaydet)

    def veriyi_kaydet(self):
        # 3. Widgetlardan Bilgileri Alma
        # Object name'lerine göre verileri çekiyoruz
        ad_soyad = self.ui.lineEdit.text()
        tc_no = self.ui.lineEdit1.text()
        telefon = self.ui.lineEdit2.text()
        e_posta = self.ui.lineEdit3.text()
        adres = self.ui.lineEdit4.text()
        dogum_tarihi = self.ui.lineEdit5.text()
        ehliyet_no = self.ui.lineEdit6.text()
        notlar = self.ui.lineEdit7.text()

        ehliyet_sinifi = self.ui.ehliyet_sinifi.currentText() # ComboBox verisi

        # RadioButton kontrolü (Örn: Cinsiyet veya Uyruk)
        secenek = ""
        if self.ui.radioButton.isChecked():
            secenek = self.ui.radioButton.text()
        elif self.ui.radioButton_2.isChecked():
            secenek = self.ui.radioButton_2.text()

        # Boş alan kontrolü (Basit bir örnek)
        if not ad_soyad or not tc_no:
            QMessageBox.warning(self, "Hata", "Lütfen zorunlu alanları doldurun!")
            return

        # 4. Veritabanı Bağlantısı ve Kayıt
        try:
            # Buradaki bilgileri birazdan senin vereceğin bilgilerle güncelleyeceğiz
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sifreniz_buraya",
                database="arac_kiralama_db"
            )
            cursor = db.cursor()

            sql = """INSERT INTO musteriler
                     (ad_soyad, tc_no, telefon, e_posta, adres, dogum_tarihi, ehliyet_no, ehliyet_sinifi, notlar, secenek)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            val = (ad_soyad, tc_no, telefon, e_posta, adres, dogum_tarihi, ehliyet_no, ehliyet_sinifi, notlar, secenek)

            cursor.execute(sql, val)
            db.commit() # Değişiklikleri kaydet

            QMessageBox.information(self, "Başarılı", f"{ad_soyad} başarıyla kaydedildi!")

            # Kayıttan sonra kutucukları temizle
            self.formu_temizle()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Veritabanı Hatası", f"Hata oluştu: {err}")
        finally:
            if 'db' in locals() and db.is_connected():
                db.close()

    def formu_temizle(self):
        """Kayıt işleminden sonra inputları boşaltır."""
        for i in range(8): # lineEdit'ten lineEdit7'ye kadar
            obj_name = f"lineEdit{i if i > 0 else ''}"
            getattr(self.ui, obj_name).clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = MusteriKayit()
    pencere.ui.show()
    sys.exit(app.exec())
