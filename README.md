# Araç Kiralama Otomasyonu

Bu proje, Python ve PySide6 (Qt) kullanılarak geliştirilmiş bir araç kiralama yönetim sistemidir. MySQL veritabanı kullanarak müşteri takibi, araç stoğu ve kiralama işlemlerini yönetir.

## Özellikler

* **Müşteri Yönetimi:** Müşteri ekleme ve listeleme.
* **Araç Yönetimi:** Araç marka, model, yakıt türü ve günlük ücret bilgilerini kaydetme.
* **Kiralama İşlemleri:** Müşteri ve araç seçimi yaparak kiralama kaydı oluşturma.
* **Otomatik Hesaplama:** Elektrikli araçlarda indirim ve gün sayısına göre toplam tutar hesaplama.
* **Raporlama:** Aktif kiralamaları tablo halinde görüntüleme.

## Kurulum

1.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

2.  MySQL veritabanınızın çalıştığından emin olun.

3.  `main.py` dosyasını açın ve veritabanı şifrenizi güncelleyin:
    ```python
    self.db_config = {
        "host": "localhost",
        "user": "root",
        "password": "sifreniz_buraya", # Şifrenizi buraya yazın
        ...
    }
    ```

4.  Uygulamayı başlatın:
    ```bash
    python main.py
    ```

## Kullanılan Teknolojiler
* Python 3
* PySide6
* MySQL
* Qt Designer
