import sys


from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles 
import shutil
import uuid
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from pathlib import Path
from functools import lru_cache
from app.predict import predict_image

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # adapte le port de ton frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "temp_uploads"
Path(UPLOAD_FOLDER).mkdir(exist_ok=True)  # to save uploads

# Serve static files (index.html, JS, CSS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")  # <-- Serve static content

@app.get("/")
def root():
    return {"message": "Welcome to the image classifier API"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(400, "File must be an image")

    filename = f"{uuid.uuid4().hex}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    try:
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)  # saves it on disk
        
        result = predict_image(file_path)

        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(500, f"Processing error: {str(e)}")
    finally:
        try:
            os.remove(file_path)
        except:
            pass

@app.get("/predict")
def predict_get():
    return {"message": "Use POST for predictions"}
