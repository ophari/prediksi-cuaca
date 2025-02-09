import joblib
import numpy as np
import pandas as pd

# Load dataset untuk mendapatkan jumlah fitur
df = pd.read_csv("data/weather.csv")
features = ["day", "month", "hour", "humidity", "wind_speed", "cloud_cover"]

# Load model Random Forest
model = joblib.load("models/weather_rf.pkl")

# Minta input dari user
day = int(input("Masukkan hari (1-31): "))
month = int(input("Masukkan bulan (1-12): "))
hour = int(input("Masukkan jam (0-23): "))
humidity = float(input("Masukkan kelembapan (%): "))
wind_speed = float(input("Masukkan kecepatan angin (km/h): "))
cloud_cover = float(input("Masukkan tutupan awan (%): "))

# Buat input dalam bentuk DataFrame
user_input = pd.DataFrame([[day, month, hour, humidity, wind_speed, cloud_cover]], columns=features)

# Prediksi suhu
prediction = model.predict(user_input)

print(f"🌡️ Prediksi suhu: {prediction[0]:.2f} °C")
