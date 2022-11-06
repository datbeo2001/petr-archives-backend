from pydantic import BaseModel
class Sticker(BaseModel):

    name: str = ""
    image_link: str = ""
    time_stamp: str = ""
    location: str = ""
    instagram: str = ""


