# Proyek Prediksi Cuaca

## 📌 Ringkasan

Proyek ini memprediksi suhu cuaca berdasarkan berbagai fitur seperti tanggal, kelembapan, kecepatan angin, dan tutupan awan. Model yang digunakan adalah **Random Forest Regressor** untuk prediksi yang akurat dan efisien.

Proyek ini mengambil data cuaca dari **API BMKG** untuk mendapatkan informasi prakiraan cuaca secara real-time.

## 🚀 Persyaratan

Sebelum menjalankan proyek, pastikan Anda telah menginstal:

- Python 3.8 atau lebih baru
- Pustaka yang diperlukan (instal melalui `requirements.txt`)

### 🔹 Instalasi Dependensi

Jalankan perintah berikut untuk menginstal pustaka yang diperlukan:

```bash
pip install -r requirements.txt
```

## 🌐 Penggunaan API BMKG

Proyek ini mengambil data cuaca dari **API BMKG**. Format URL API yang digunakan adalah:

```
https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={kode_wilayah}
```

**Parameter utama API:**

- `utc_datetime` → Waktu dalam UTC (YYYY-MM-DD HH:mm:ss)
- `local_datetime` → Waktu lokal (YYYY-MM-DD HH:mm:ss)
- `t` → Suhu udara (°C)
- `hu` → Kelembapan udara (%)
- `weather_desc` → Deskripsi cuaca
- `ws` → Kecepatan angin (km/jam)
- `tcc` → Tutupan awan (%)

## 🏗️ Struktur Proyek

```
weather_forecast_project/
│── data/                    # Folder untuk dataset
│── models/                  # Menyimpan model yang telah dilatih
│── src/
│   ├── preprocess.py        # Skrip untuk pra-pemrosesan data
│   ├── train_model.py       # Melatih model Random Forest
│   ├── predict.py           # Memprediksi suhu menggunakan model
│   ├── fetch_bmkg_data.py   # Mengambil data dari API BMKG
│── main.py                  # Skrip utama dengan menu interaktif
│── requirements.txt         # Daftar pustaka yang dibutuhkan
│── README.md                # Dokumentasi proyek
```

## 🎯 Cara Menggunakan

### 1️⃣ Jalankan Program Utama

Eksekusi perintah berikut untuk memulai menu interaktif:

```bash
python main.py
```

Anda akan melihat tampilan seperti ini:

```
=== PREDIKSI CUACA ===
1. Latih Model
2. Prediksi Cuaca
3. Keluar
```

### 2️⃣ Latih Model

Jika model belum dilatih, pilih opsi **1** untuk melatih model:

```bash
1
```

✅ Model yang telah dilatih akan disimpan di `models/weather_rf.pkl`.

### 3️⃣ Prediksi Cuaca

Setelah model dilatih, pilih opsi **2** untuk melakukan prediksi cuaca.
Anda akan diminta memasukkan data seperti tanggal, kelembapan, kecepatan angin, dan tutupan awan.
Contoh:

```
Masukkan hari (1-31): 5
Masukkan bulan (1-12): 2
Masukkan jam (0-23): 14
Masukkan kelembapan (%): 80
Masukkan kecepatan angin (km/h): 15
Masukkan tutupan awan (%): 60
```

🌡️ **Suhu yang diprediksi akan ditampilkan!**

## 🛠️ Catatan Tambahan

- Jika terjadi error, pastikan Anda telah menginstal pustaka menggunakan `pip install -r requirements.txt`.
- Jika model tidak ditemukan, latih ulang menggunakan opsi **1** di `main.py`.
- Dataset harus ditempatkan di folder `data/` dengan nama `weather.csv`.

## 🤝 Kontribusi

Silakan fork proyek ini, berikan saran perbaikan, atau tambahkan fitur baru!

---

📌 **Pembuat:** Muhamad Yusuf
📅 **Terakhir Diperbarui:** 2025-02-09

<!--//////////////////////////////////////////////////////////////////////////////////////////////////////////// -->

# Prediksi Cuaca dengan Flask

## 📌 Deskripsi Proyek

Aplikasi prediksi cuaca berbasis **Flask** yang menggunakan model **Random Forest** untuk memprediksi kondisi cuaca berdasarkan input pengguna.

## 🛠 Teknologi yang Digunakan

- **Python** (Flask, Pandas, Joblib)
- **HTML, CSS, JavaScript** (Frontend dengan efek blur dan responsif)
- **Model Machine Learning** (Random Forest)

## 📂 Struktur Folder

```
project-root/
│── models/
│   └── weather_rf.pkl   # Model Machine Learning
│── static/
│   ├── bg-cuaca.jpg     # Background Image
│   ├── style.css        # Styling Frontend
│   └── script.js        # JavaScript Interaksi
│── templates/
│   └── index.html       # Halaman utama
│── app.py               # Backend Flask
│── README.md            # Dokumentasi
```

## 🚀 Cara Menjalankan Aplikasi

1. **Pastikan Python terinstal**, lalu install dependensi:
   ```bash
   pip install flask pandas joblib
   ```
2. **Jalankan aplikasi Flask:**
   ```bash
   python app.py
   ```
3. **Buka browser dan akses:**
   ```
   http://127.0.0.1:5000/
   ```

## 🎨 Tampilan Aplikasi

- **Responsif** untuk desktop, tablet, dan mobile.
- **Efek blur & hover** untuk tampilan modern.
- **Prediksi cuaca ditampilkan secara dinamis.**

## 💡 Kontribusi

Jika ingin berkontribusi, silakan fork repository ini dan buat pull request! 🚀

---

📌 **Pembuat backend:** Muhamad Yusuf
📌 **Pembuat frontend:** Wisnu Septa Harianto Putra
📅 **Terakhir Diperbarui:** 2025-02-28

semua sayang yusuf
