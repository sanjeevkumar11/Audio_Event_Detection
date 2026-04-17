import numpy as np
import soundfile as sf

sr = 22050
t = np.linspace(0, 1, sr)
audio = 0.5 * np.sin(2 * np.pi * 220 * t)

sf.write("test.wav", audio, sr)