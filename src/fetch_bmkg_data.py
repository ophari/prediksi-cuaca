import requests
import json
import os

# Ganti dengan kode wilayah tingkat IV yang sesuai
KODE_WILAYAH = "36.03.28.1001"  # Contoh kode wilayah kab tangerang, kel.kelapa dua, kec.kelapa dua

# URL API BMKG
API_URL = f"https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={KODE_WILAYAH}"

# Pastikan folder data ada
os.makedirs("data", exist_ok=True)

def fetch_weather_data():
    """Mengambil data cuaca dari API BMKG"""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        # Simpan data JSON
        with open("data/weather_data.json", "w") as file:
            json.dump(data, file, indent=4)
        
        print("✅ Data cuaca berhasil diambil dan disimpan di weather_data.json!")
        return data

    except requests.exceptions.RequestException as e:
        print(f"❌ Error saat mengambil data: {e}")
        return None

if __name__ == "__main__":
    fetch_weather_data()
