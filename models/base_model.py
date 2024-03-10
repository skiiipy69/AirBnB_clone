#!/usr/bin/python3
""" 0x00. AirBnB clone - The console """
from . import storage
from datetime import datetime
import uuid


class BaseModel():
    """Defines all common attributes/methods for `BaseModel` its subclasses.

    Use of kwargs is currently very brittle and assumes no use of *args,
    and either empty **kwargs, or a dictionary that contains a key for every
    instance attrtibute named in `__init__`, and corresponding values of the
    correct type and formatting.

    Attributes:
        id (str): a unique UUID that is assigned when an instance is created
        created_at (datetime.datetime): the current datetime when an instance
            is created
        updated_at (datetime.datetime): the current datetime when an instance
            is created, but updated everytime object is changed

    """
    def __init__(self, *args, **kwargs):
        """`BaseModel` class constructor.

        Project tasks:
            3. BaseModel
            4. Create BaseModel from dictionary

        """
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            ISO_fmt = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(kwargs['created_at'], ISO_fmt)
            self.updated_at = datetime.strptime(kwargs['updated_at'], ISO_fmt)
            for key, value in kwargs.items():
                if key not in ('created_at', 'updated_at', '__class__'):
                    self.__dict__[key] = value

    def __str__(self):
        """Returns the string representation of BaseModel.

        Returns:
             '[<class name>] (<self.id>) <self.__dict__>'

        Project tasks:
            3. BaseModel

        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """Updates updated_at with the current datetime. Saves updates to JSON
        serialization.

        Project tasks:
            3. BaseModel
            5. Store first object

        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance, plus `__class__`, `created-at`, and `updated_at`.

        Project tasks:
            3. BaseModel

        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
