import json
import pandas as pd
import os

# Pastikan folder data ada
os.makedirs("data", exist_ok=True)

# Load data JSON
try:
    with open("data/weather_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print("❌ File weather_data.json tidak ditemukan. Jalankan fetch_bmkg_data.py dulu!")
    exit()
except json.JSONDecodeError as e:
    print(f"❌ Error membaca JSON: {e}")
    exit()

# Debug: Periksa struktur JSON
print("📌 Tipe data JSON:", type(data))

# Ambil data cuaca
try:
    # Ambil data cuaca dari list pertama
    cuaca_data = data["data"][0]["cuaca"]
except (KeyError, IndexError) as e:
    print(f"❌ Struktur JSON tidak sesuai! Error: {e}")
    exit()

# Simpan data yang relevan dalam format tabel
weather_data = []

for waktu_prakiraan in cuaca_data:  # List dalam list
    for entry in waktu_prakiraan:  # Ambil setiap prakiraan dalam waktu tertentu
        weather_data.append({
            "local_datetime": entry.get("local_datetime", "N/A"),
            "temperature": entry.get("t", None),
            "humidity": entry.get("hu", None),
            "weather_desc": entry.get("weather_desc", "N/A"),
            "wind_speed": entry.get("ws", None),
            "cloud_cover": entry.get("tcc", None),
            "visibility": entry.get("vs_text", "N/A")
        })

# Konversi ke DataFrame
df = pd.DataFrame(weather_data)

# Simpan ke CSV
csv_path = "data/weather.csv"
df.to_csv(csv_path, index=False)

print(f"✅ Data cuaca berhasil diproses dan disimpan ke {csv_path}!")
