import os
import joblib
import pandas as pd

def train_model():
    print("🚀 Menjalankan training model...")
    os.system("python src/train_model.py")  # Jalankan script training
    print("✅ Training selesai!")

def predict_weather():
    print("🌤️ Menjalankan prediksi cuaca...")
    
    # Cek apakah model tersedia
    model_path = "models/weather_rf.pkl"  # Sesuaikan dengan nama model yang disimpan
    if not os.path.exists(model_path):
        print("❌ Model belum ada. Jalankan training dulu!")
        return
    
    # Load model
    model = joblib.load(model_path)

    # Input manual
    day = int(input("Masukkan hari (1-31): "))
    month = int(input("Masukkan bulan (1-12): "))
    hour = int(input("Masukkan jam (0-23): "))
    humidity = float(input("Masukkan kelembapan (%): "))
    wind_speed = float(input("Masukkan kecepatan angin (km/h): "))
    cloud_cover = float(input("Masukkan tutupan awan (%): "))

    # Prediksi suhu
    data = pd.DataFrame([[day, month, hour, humidity, wind_speed, cloud_cover]],
                        columns=["day", "month", "hour", "humidity", "wind_speed", "cloud_cover"])
    prediction = model.predict(data)

    print(f"🌡️ Prediksi suhu: {prediction[0]:.2f} °C")

# Menu utama
while True:
    print("\n=== CUACA PREDICTOR ===")
    print("1. Latih Model")
    print("2. Prediksi Cuaca")
    print("3. Keluar")
    pilihan = input("Pilih opsi (1/2/3): ")

    if pilihan == "1":
        train_model()
    elif pilihan == "2":
        predict_weather()
    elif pilihan == "3":
        print("👋 Keluar dari program. Sampai jumpa!")
        break
    else:
        print("❌ Pilihan tidak valid, coba lagi!")
