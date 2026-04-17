from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.model.predict import predict_audio

router = APIRouter()

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Predict
    result = predict_audio(file_path)

    # Remove file after prediction
    os.remove(file_path)

    return {"prediction": result}