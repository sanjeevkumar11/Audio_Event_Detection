import librosa
import numpy as np

def extract_features(file_path):
    try:
        audio, sr = librosa.load(file_path, sr=22050)

        # MFCC + delta + delta2
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
        delta = librosa.feature.delta(mfcc)
        delta2 = librosa.feature.delta(mfcc, order=2)

        # Spectral features
        chroma = librosa.feature.chroma_stft(y=audio, sr=sr)
        contrast = librosa.feature.spectral_contrast(y=audio, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(audio)
        rms = librosa.feature.rms(y=audio)

        # Combine with richer stats
        def stats(x):
            return np.hstack([
                np.mean(x, axis=1),
                np.std(x, axis=1),
                np.max(x, axis=1),
                np.min(x, axis=1)
            ])

        features = np.hstack([
            stats(mfcc),
            stats(delta),
            stats(delta2),
            stats(chroma),
            stats(contrast),
            stats(zcr),
            stats(rms)
        ])

        return features

    except Exception as e:
        print("Error:", e)
        return None