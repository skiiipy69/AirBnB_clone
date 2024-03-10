#!/usr/bin/python3
"""0x00. AirBnB clone __init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
