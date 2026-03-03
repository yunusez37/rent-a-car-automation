import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MusteriPenceresi(QWidget):
    def __init__(self):
        super().__init__()

        # 1. UI Dosyasını Yükle
        loader = QUiLoader()
        ui_file = QFile("musteri.ui")

        if not ui_file.open(QFile.ReadOnly):
            print(f"HATA: {ui_file.fileName()} dosyası bulunamadı!")
            return

        # UI'ı yükle ve sınıfa bağla
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print("HATA: UI yüklenirken bir sorun oluştu.")
            return

        # Pencereyi göster
        self.ui.show()

        # 2. Buton Kontrolü ve Bağlantısı
        # Object Name'in "kaydet" olduğundan emin olduğumuz için doğrudan bağlıyoruz
        if hasattr(self.ui, 'kaydet'):
            self.ui.kaydet.clicked.connect(self.veriyi_isle)
            print("Sistem: 'kaydet' butonu bulundu ve bağlantı kuruldu.")
        else:
            print("HATA: UI içinde 'kaydet' isminde bir buton bulunamadı! Lütfen Qt Designer'da objectName'i kontrol edin.")

    def veriyi_isle(self):
        print("Sistem: Kaydet butonuna basıldı, işlemler başlıyor...")

        # Verileri Topla
        try:
            # Görseldeki lineEdit isimlerine göre
            ad = self.ui.lineEdit.text()
            tc = self.ui.lineEdit1.text()
            tel = self.ui.lineEdit2.text()
            mail = self.ui.lineEdit3.text()
            adres = self.ui.lineEdit4.text()
            d_tarih = self.ui.lineEdit5.text()
            ehliyet_no = self.ui.lineEdit6.text()
            notlar = self.ui.lineEdit7.text()

            e_sinifi = self.ui.ehliyet_sinifi.currentText()

            cinsiyet = ""
            if self.ui.radioButton.isChecked():
                cinsiyet = self.ui.radioButton.text()
            elif self.ui.radioButton_2.isChecked():
                cinsiyet = self.ui.radioButton_2.text()

            # Veritabanına Gönder
            self.mysql_kaydet(ad, tc, tel, mail, adres, d_tarih, ehliyet_no, e_sinifi, notlar, cinsiyet)

        except Exception as e:
            print(f"Veri toplama hatası: {e}")
            QMessageBox.critical(self.ui, "Hata", f"Veriler alınırken hata oluştu: {e}")

    def mysql_kaydet(self, ad, tc, tel, mail, adres, d_tarih, ehliyet_no, e_sinifi, notlar, cinsiyet):
        try:
            print("Sistem: MySQL'e bağlanılıyor...")
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db90240000230", # <--- BURAYA KENDİ OKUL NUMARANI YAZ
                port=3306
            )
            cursor = db.cursor()

            # Sorgu (Tablo adının 'musteriler' olduğunu varsayıyorum)
            sql = """INSERT INTO musteriler
                    (ad_soyad, tc_no, telefon, e_posta, adres, dogum_tarihi, ehliyet_no, ehliyet_sinifi, notlar, cinsiyet)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            values = (ad, tc, tel, mail, adres, d_tarih, ehliyet_no, e_sinifi, notlar, cinsiyet)

            cursor.execute(sql, values)
            db.commit()

            print("Sistem: Kayıt başarıyla tamamlandı.")
            QMessageBox.information(self.ui, "Başarılı", "Müşteri veritabanına kaydedildi.")

        except mysql.connector.Error as err:
            print(f"MySQL Hatası: {err}")
            QMessageBox.critical(self.ui, "Veritabanı Hatası", f"MySQL hatası: {err}")
        finally:
            if 'db' in locals() and db.is_connected():
                db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = MusteriPenceresi()
    sys.exit(app.exec())
