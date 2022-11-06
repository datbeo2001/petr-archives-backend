import cloudinary
from pydantic import BaseSettings
from PIL import Image
import io
from dotenv import load_dotenv, find_dotenv

# class Settings(BaseSettings):
#
#     cloud_name = "CLOUD_NAME"
#     api_key = "API_KEY"
#     api_secret = "API_SECRET"
#
#     class Config:
#         env_file = ".env"
#
#
# settings = Settings()

import cloudinary.uploader
import cloudinary.api

load_dotenv(find_dotenv())


def cloudinaryUpload(img: bytes | str, contentType: str):
    file_name = f"something.{contentType.split('/')[1]}"
    if type(img) is bytes:
        file = Image.open(io.BytesIO(img))
        file.save(file_name)
    res = cloudinary.uploader.upload(file_name)
    url = res["url"]
    return url
