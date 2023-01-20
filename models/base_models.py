#!/usr/bin/python3
""" this is the base class for all models """
import uuid
from datetime import date, datetime, time


class BaseModel():
    """class defining commom attributes
    for other classes"""

    def __init__(self):
        """ instance attributes
        id : string
        created_at: datetime
        updated_at: datetime
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ default string output of class name \
                ,id and dictionary files """
        return '[{}] ({}) <{}>'\
            .format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ update of attribute updated_at with latest time
        updated_at: datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        get the objects of the instance
        returns: dictionary
        """
        temp_dict = self.__dict__
        temp_dict['__class__'] = __class__.__name__
        return temp_dict
