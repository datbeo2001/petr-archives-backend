# import cloudinary
# import cloudinary.uploader
import cloudinary
from pydantic import BaseSettings
from PIL import Image
import io

class Settings(BaseSettings):

    cloud_name = "CLOUD_NAME"
    api_key = "API_KEY"
    api_sec = "API_SECRET"

    class Config:
        env_file = ".env"

settings = Settings()


import cloudinary.uploader
import cloudinary.api

def cloudinaryUpload(img: bytes | str, contentType: str):
    if type(img) is bytes:
        file = Image.open(io.BytesIO(img))
        file.save("something.jpeg")
    res = cloudinary.uploader.upload(r"something.jpeg")
    url = res["url"]
    return url