import joblib
import numpy as np
from app.utils.audio_processing import extract_features

# Load model once (important for performance)
model = joblib.load("app/model/model.pkl")

def predict_audio(file_path):
    features = extract_features(file_path)

    scaler = joblib.load("app/model/scaler.pkl")
    model = joblib.load("app/model/model.pkl")

    features = extract_features(file_path)

    if features is None:
        return {"error": "Feature extraction failed"}

    features = scaler.transform([features])   # ✅ THIS LINE IS CRITICAL

    prediction = model.predict(features)

    return prediction[0]