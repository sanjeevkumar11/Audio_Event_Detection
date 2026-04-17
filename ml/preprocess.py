import os
from backend.app.utils.audio_processing import extract_features

file_path = r"D:\audio-event-detection\ml\dataset\test.wav"  

features = extract_features(file_path)

if features is not None:
    print("Feature shape:", features.shape)
else:
    print("Feature extraction failed")