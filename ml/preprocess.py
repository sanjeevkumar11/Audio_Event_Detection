import os
from backend.app.utils.audio_processing import extract_features

# test with one audio file
file_path = r"D:\audio-event-detection\ml\dataset\test.wav"  # put any .wav file here

features = extract_features(file_path)

if features is not None:
    print("Feature shape:", features.shape)
else:
    print("Feature extraction failed")