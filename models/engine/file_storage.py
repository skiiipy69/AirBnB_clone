#!/usr/bin/python3
""" 0x00. AirBnB clone - The console """
import json
from os import path


class FileStorage():
    """Class meant to manage JSON file storage for `BaseModel` and its child
    classes.

    Attributes:
        __file_path (str): default path to save JSON serializations to file
        __objects (dict): dict of items with `BaseModel` and its child classes
            as values, and '<object class name>.<object.id>' as keys

    Project tasks:
        5. Store first object

    """
    __file_path = 'HBnB_objects.json'
    __objects = dict()

    def __init__(self):
        pass

    def all(self):
        """Returns the dictionary __objects.

        Returns:
            __objects (dict): dict of items with `BaseModel` and its child
                classes as values, and '<object class name>.<object.id>' as
                keys

        Project tasks:
            5. Store first object

        """
        return self.__objects

    def new(self, obj):
        """Sets a new object as value in __objects with key
        '<object class name>.<object.id>'

        Args:
            obj (BaseModel or child): BaseModel-derived object to be added to
               __objects

        Project tasks:
            5. Store first object

        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)

        Project tasks:
           5. Store first object

        """
        json_dict = dict()
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_dict))

    def reload(self):
        """Deserializes the JSON file at __file_path into  __objects, if it
        exists; otherwise, no exception is raised.

        Project tasks:
            5. Store first object

        """
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        class_dict = dict()
        for c in classes:
            class_dict[c.__name__] = c

        if path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if content is not None and content != '':
                    json_dict = json.loads(content)
                    for key, value in json_dict.items():
                        obj_class = class_dict[value['__class__']]
                        self.__objects[key] = obj_class(**value)
        else:
            pass
