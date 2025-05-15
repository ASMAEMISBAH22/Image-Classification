from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  
import shutil
import uuid
import os
from pathlib import Path
from functools import lru_cache  

from app.predict import predict_image

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["POST"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "temp_uploads"
Path(UPLOAD_FOLDER).mkdir(exist_ok=True)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(400, "File must be an image")

    filename = f"{uuid.uuid4().hex}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    try:
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        result = predict_image(file_path)

        return JSONResponse(content=result)
        
    except Exception as e:
        raise HTTPException(500, f"Processing error: {str(e)}")
    finally:
        try:
            os.remove(file_path)
        except:
            pass