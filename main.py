# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import joblib
# import numpy as np
# import os
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware

# # Inisialisasi aplikasi FastAPI
# app = FastAPI()

# # Middleware CORS untuk mendukung frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Ganti jika Anda hanya ingin mengizinkan domain tertentu
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Path model
# BASE_DIR = os.path.dirname(__file__)
# XGBOOST_MODEL_PATH = os.path.join(BASE_DIR, "models", "xgboost_model.pkl")
# LABEL_ENCODER_PATH = os.path.join(BASE_DIR, "models", "label_encoder.pkl")
# YEAR_PREDICTION_MODEL_PATH = os.path.join(BASE_DIR, "models", "yearsprediction.pkl")

# # Load models
# try:
#     xgboost_model = joblib.load(XGBOOST_MODEL_PATH)
#     label_encoder = joblib.load(LABEL_ENCODER_PATH)
#     year_prediction_model = joblib.load(YEAR_PREDICTION_MODEL_PATH)
# except Exception as e:
#     raise RuntimeError(f"Error loading model: {e}")

# # Mount static files
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Request schemas
# class MentalHealthRequest(BaseModel):
#     symptoms: list

# class YearPredictionRequest(BaseModel):
#     features: list

# # Routes
# @app.get("/", response_class=HTMLResponse)
# def read_root():
#     """Serve the mentalhealth.html as the default page."""
#     try:
#         html_path = os.path.join(BASE_DIR, "static", "mentalheatlh.html")
#         with open(html_path, "r") as file:
#             return HTMLResponse(content=file.read())
#     except FileNotFoundError:
#         raise HTTPException(status_code=404, detail="mentalheatlh.html not found")

# @app.post("/api/predict")
# def predict_mental_health(request: MentalHealthRequest):
#     try:
#         symptoms_array = np.array(request.symptoms)

#         # Validasi jumlah fitur
#         if symptoms_array.shape[0] != 24:
#             raise ValueError(f"Feature shape mismatch: expected 24, got {symptoms_array.shape[0]}")

#         # Prediksi dengan model
#         prediction = xgboost_model.predict([symptoms_array])
#         return {"prediction": int(prediction[0])}
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=f"Input error: {e}")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Server error: {e}")




# @app.post("/api/jawabarat")
# def predict_year(request: YearPredictionRequest):
#     """
#     Endpoint untuk memprediksi berdasarkan tahun.
#     Input: List tahun dari pengguna.
#     Output: Prediksi hasil tahun.
#     """
#     try:
#         year_feature = np.array(request.features).reshape(1, -1)
#         prediction = year_prediction_model.predict(year_feature)
#         return {"prediction": int(prediction[0])}
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=f"Input error: {e}")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Server error: {e}")


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Middleware CORS untuk mendukung frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti jika hanya ingin mengizinkan domain tertentu
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path model
BASE_DIR = os.path.dirname(__file__)
XGBOOST_MODEL_PATH = os.path.join(BASE_DIR, "models", "xgboost_model.pkl")
LABEL_ENCODER_PATH = os.path.join(BASE_DIR, "models", "label_encoder.pkl")
YEAR_PREDICTION_MODEL_PATH = os.path.join(BASE_DIR, "models", "yearsprediction.pkl")

# Load models
try:
    xgboost_model = joblib.load(XGBOOST_MODEL_PATH)
    label_encoder = joblib.load(LABEL_ENCODER_PATH)  # Jika tidak dipakai, bisa dihapus
    year_prediction_model = joblib.load(YEAR_PREDICTION_MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Request schemas
class MentalHealthRequest(BaseModel):
    symptoms: list

class YearPredictionRequest(BaseModel):
    features: list

# Routes
@app.get("/", response_class=HTMLResponse)
def read_root():
    """Serve the mentalhealth.html as the default page."""
    try:
        html_path = os.path.join(BASE_DIR, "static", "mentalhealth.html")
        with open(html_path, "r") as file:
            return HTMLResponse(content=file.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="mentalhealth.html not found")

@app.post("/api/predict")
def predict_mental_health(request: MentalHealthRequest):
    """
    Endpoint untuk memprediksi kesehatan mental.
    Input: List gejala (symptoms) dari pengguna.
    Output: Prediksi dari model XGBoost.
    """
    try:
        symptoms_array = np.array(request.symptoms)

        # Validasi jumlah fitur
        if symptoms_array.shape[0] != 24:
            raise ValueError(f"Feature shape mismatch: expected 24, got {symptoms_array.shape[0]}")

        # Prediksi dengan model
        prediction = xgboost_model.predict([symptoms_array])
        return {"prediction": int(prediction[0])}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Input error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@app.post("/api/jawabarat")
def predict_year(request: YearPredictionRequest):
    """
    Endpoint untuk memprediksi berdasarkan tahun.
    Input: List tahun dari pengguna.
    Output: Prediksi hasil tahun.
    """
    try:
        year_feature = np.array(request.features).reshape(1, -1)
        prediction = year_prediction_model.predict(year_feature)
        return {"prediction": int(prediction[0])}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Input error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")
