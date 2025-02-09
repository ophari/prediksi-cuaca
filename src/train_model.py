import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Pastikan folder models ada
os.makedirs("models", exist_ok=True)

# Load dataset
try:
    df = pd.read_csv("data/weather.csv")
except FileNotFoundError:
    print("❌ File weather.csv tidak ditemukan. Jalankan preprocess.py dulu!")
    exit()

# Konversi datetime menjadi fitur numerik
df["local_datetime"] = pd.to_datetime(df["local_datetime"])
df["day"] = df["local_datetime"].dt.day
df["month"] = df["local_datetime"].dt.month
df["hour"] = df["local_datetime"].dt.hour

# Pilih fitur & target
features = ["day", "month", "hour", "humidity", "wind_speed", "cloud_cover"]
target = "temperature"

# Bagi dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Inisialisasi model Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluasi Model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"✅ Model selesai dilatih! MAE: {mae:.4f}")

# Simpan model
joblib.dump(model, "models/weather_rf.pkl")
print("✅ Model Random Forest berhasil disimpan!")
