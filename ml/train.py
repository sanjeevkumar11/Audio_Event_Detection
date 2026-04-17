import os
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC

from backend.app.utils.audio_processing import extract_features


# ==============================
# PATHS
# ==============================
DATA_PATH = r"D:\audio-event-detection\ml\dataset\ESC-50\audio"
CSV_PATH = r"D:\audio-event-detection\ml\dataset\ESC-50\meta\esc50.csv"


# ==============================
# LOAD DATA
# ==============================
print("Loading dataset...")
df = pd.read_csv(CSV_PATH)

features = []
labels = []


# ==============================
# FEATURE EXTRACTION
# ==============================
print("Extracting features... (this may take time)")

for index, row in df.iterrows():
    file_path = os.path.join(DATA_PATH, row["filename"])
    label = row["category"]

    data = extract_features(file_path)

    if data is not None:
        features.append(data)
        labels.append(label)

print("Feature extraction complete")


# ==============================
# CONVERT TO NUMPY
# ==============================
X = np.array(features)
y = np.array(labels)

print("Feature shape:", X.shape)


# ==============================
# TRAIN-TEST SPLIT
# ==============================
print("Splitting data...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)


# ==============================
# SCALING (IMPORTANT)
# ==============================
print("Scaling features...")

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# ==============================
# HYPERPARAMETER TUNING (SVM)
# ==============================
print("Tuning model (GridSearch)...")

param_grid = {
    "C": [1, 10, 50],
    "gamma": ["scale", 0.01, 0.001],
    "kernel": ["rbf"]
}

grid = GridSearchCV(
    SVC(),
    param_grid,
    cv=3,
    n_jobs=-1,
    verbose=1
)

grid.fit(X_train, y_train)

model = grid.best_estimator_

print("Best Parameters:", grid.best_params_)


# ==============================
# CROSS VALIDATION SCORE
# ==============================
print("Running cross-validation...")

cv_scores = cross_val_score(model, X_train, y_train, cv=5)

print("CV Accuracy:", cv_scores.mean())


# ==============================
# FINAL EVALUATION
# ==============================
print("Evaluating on test set...")

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# ==============================
# SAVE MODEL + SCALER
# ==============================
print("Saving model...")

os.makedirs("backend/app/model", exist_ok=True)

joblib.dump(model, "backend/app/model/model.pkl")
joblib.dump(scaler, "backend/app/model/scaler.pkl")

print("Model and scaler saved successfully!")