AUDIO EVENT DETECTION SYSTEM - This project classifies environmental sounds such as dog barking, glass breaking, etc.
The system uses machine learning to analyse sound signals and predict the type of sound 

SOLUTION APPROACH:

Audio Input:
User uploads a .wav audio file via the frontend
Feature Extraction:
Audio is processed using MFCC (Mel Frequency Cepstral Coefficients) with Librosa
Model Prediction:
A trained Random Forest Classifier predicts the sound category
Output:
The predicted label is returned via API and displayed on the frontend

TECH STACK :

Frontend:
-React.js
-Axios
Backend:
-FastAPI
-Uvicorn
Machine Learning:
-Scikit-learn
-Librosa
-NumPy
-Joblib
Dataset:
ESC-50 (Environmental Sound Classification Dataset)

DEPENDENCIES:

Backend:
-fastapi
-uvicorn
-librosa
-numpy
-scikit-learn
-joblib
Frontend:
-react
-axios

SETUP INSTRUCTIONS:

1. Clone Repository
git clone <https://github.com/sanjeevkumar11/Audio_Event_Detection.git>
cd audio-event-detection
2. Backend Setup
cd backend
python -m venv venv
Activate virtual environment:
-Windows:venv\Scripts\activate
-Mac/Linux:source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
3. Run Backend Server
uvicorn app.main:app --reload

API runs at:
http://127.0.0.1:8000
Swagger UI:
http://127.0.0.1:8000/docs

4. Frontend Setup
cd frontend
npm install
npm start

Frontend runs at:
http://localhost:3000

USAGE:

Open the frontend in browser
Upload a .wav audio file
Click Upload & Predict
View predicted audio event