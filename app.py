from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model yang sudah dilatih
MODEL_PATH = "models/weather_rf.pkl"
model = joblib.load(MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        user_input = pd.DataFrame([[
            data['day'], data['month'], data['hour'],
            data['humidity'], data['wind_speed'], data['cloud_cover']
        ]], columns=["day", "month", "hour", "humidity", "wind_speed", "cloud_cover"])

        prediction = model.predict(user_input)[0]  # Prediksi hasil cuaca
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

# Pastikan struktur folder yang benar
# templates/index.html -> Untuk tampilan HTML
# static/style.css -> Untuk tampilan CSS
# static/script.js -> Untuk interaksi JavaScript
