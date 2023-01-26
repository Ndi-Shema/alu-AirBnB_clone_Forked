#!/usr/bin/python3
""" python file
    converts to json
    stores and does the reverse
"""
import json


class FileStorage:
    """ file storage class"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ for instance variables """

    def all(self):
        """ returns : dictionary """
        return self.__objects

    def new(self, obj):
        """ set object with key """
        self.__objects[obj['__class__'] + '.' + obj['id']] = obj

    def save(self):
        """ serializes to json file """
        # if path.exists(self.__file_path):
        with open(self.__file_path, "w", encoding='utf-8') as out_file:
            json.dump(self.__objects, out_file)

    def reload(self):
        """ deserializes json to file """
        # if path.exists(self.__file_path):
        with open(self.__file_path, "r", encoding='utf-8') as in_file:
            self.__objects = json.load(in_file)



