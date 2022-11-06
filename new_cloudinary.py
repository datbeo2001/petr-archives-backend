import cloudinary
import cloudinary.uploader
import cloudinary
import cloudinary.uploader
from pydantic import BaseSettings

class Settings(BaseSettings):

    cloud_name = "CLOUD_NAME"
    api_key = "API_KEY"
    api_sec = "API_SECRET"

    class Config:
        env_file = ".env"

settings = Settings()

cloudinary.config(
    cloud_name = settings.cloud_name,
    api_key = settings.api_key,
    api_secret = settings.api_sec
)


def cloudinaryUpload(img: bytes | str):
    res = cloudinary.uploader.upload(img)
    url = res["url"]
    return url
