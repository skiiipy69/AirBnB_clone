#!/usr/bin/python3
""" 0x00. AirBnB clone - The console """
from .base_model import BaseModel


class City(BaseModel):
    """Defines attributes for `City`.

    Attributes:
        state_id (str)
        name (str)
    """

    state_id = ""
    name = ""
