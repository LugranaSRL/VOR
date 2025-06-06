from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Backend attivo"}

@app.post("/upload")
async def upload_file(frame: UploadFile = File(...)):
    with open("received_frame.png", "wb") as f:
        shutil.copyfileobj(frame.file, f)
    return {"status": "ricevuto", "filename": frame.filename}
