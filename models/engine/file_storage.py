#!/usr/bin/python3
""" python file
    converts to json
    stores and does the reverse
"""
import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """ file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns : dictionary """
        return self.__objects

    def new(self, obj):
        """ set object with key """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ serializes to json file """
        if path.exists(self.__file_path):
            temp = {}
            for key in self.__objects:
                temp[key] = self.__objects[key].to_dict()
            with open(self.__file_path, "w", encoding='utf-8') as out_file:
                json.dump(temp, out_file)

    def reload(self):
        """ deserializes json to file """
        from models.base_model import BaseModel

        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as in_file:
                dataset = json.load(in_file)
                for data in dataset.values():
                    name_of_class = data['__class__']
                    self.new(eval(name_of_class + "(**" + str(data) + ")"))






