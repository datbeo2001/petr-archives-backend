import json
from fastapi import FastAPI, UploadFile, Body, Form, HTTPException, File
import uvicorn
from posts import Sticker
from uploadCloudinary import settings, cloudinaryUpload
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {}

@app.get("/get-data")
def data():
    file = open('data.json')
    JSONdata = json.load(file)
    file.close()
    return JSONdata

def write_json(new_data, filename='data.json'):
    with open('data.json', 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

@app.post("/create-sticker")
def create_new_sticker(file: UploadFile = File(...), name: str = Form(""), timestamp: str = Form(""), 
     location: str = Form(""), instagram: str = Form("")):
    try:
        contentType = file.content_type
        contents = file.file.read()
        url = cloudinaryUpload(contents, contentType)
        stickerDict = {"name": name.title(), "image_link": url, "timestamp": timestamp, "location": location.title(), "instagram": f"http://www.instagram.com/{instagram}"}
        write_json(stickerDict)
        return {"status": "OK"}
    except Exception as E: 
        raise E





if __name__ == '__main__':
    uvicorn.run('api:app', reload=True)

