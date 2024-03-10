#!/usr/bin/python3
""" 0x00. AirBnB clone - The console """
from .base_model import BaseModel


class Review(BaseModel):
    """Defines attributes for `Review`.

    Attributes:
        place_id (str)
        user_id (str)
        text (str)
    """

    place_id = ""
    user_id = ""
    text = ""
