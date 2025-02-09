import os
import joblib
import pandas as pd

# Load model
model_path = "models/weather_rf.pkl"

def train_model():
    print("\n🚀 Menjalankan training model...")
    os.system("python src/train_model.py")
    print("✅ Training selesai!")

def predict_weather():
    if not os.path.exists(model_path):
        print("❌ Model belum ada. Jalankan training dulu!")
        return

    model = joblib.load(model_path)

    print("\n🌤️ Masukkan data cuaca untuk prediksi:")
    try:
        day = int(input("Hari (1-31): "))
        month = int(input("Bulan (1-12): "))
        hour = int(input("Jam (0-23): "))
        humidity = float(input("Kelembapan (%): "))
        wind_speed = float(input("Kecepatan angin (km/h): "))
        cloud_cover = float(input("Tutupan awan (%): "))

        user_input = pd.DataFrame([[day, month, hour, humidity, wind_speed, cloud_cover]],
                                  columns=["day", "month", "hour", "humidity", "wind_speed", "cloud_cover"])

        prediction = model.predict(user_input)[0]
        print(f"\n🌡️ Prediksi suhu: {prediction:.2f} °C\n")

    except ValueError:
        print("❌ Masukkan angka yang valid!")

# Menu utama CLI
while True:
    print("\n=== 🌤️ PREDIKSI CUACA CLI ===")
    print("1. Latih Model")
    print("2. Prediksi Cuaca")
    print("3. Keluar")
    
    pilihan = input("Pilih opsi (1/2/3): ").strip()

    match pilihan:
        case "1":
            train_model()
        case "2":
            predict_weather()
        case "3":
            print("👋 Keluar dari program. Sampai jumpa!")
            break
        case _:
            print("❌ Pilihan tidak valid, coba lagi!")
