#!/usr/bin/python3
"""
this is a class with attributes/methods for other classes
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    this is a class called BaseModel
    """
    def __init__(self):
        """
        this is the constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """str method
        Returns:
            class name, id and __dict__ representation
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates time when object changes
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            }
