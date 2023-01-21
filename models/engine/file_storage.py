#!/usr/bin/python3
""" python file
    converts to json
    stores and does the reverse
"""
import json
import os.path
from os import path


class FileStorage():
    """ file storage class"""

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """ for instance variables """

    def all(self):
        """ returns : dictionary """
        return self.__objects

    def new(self, obj):
        """ set object with key """
        self.__objects[__class__.__name__ + '.' + obj['id']] = obj

    def save(self):
        """ serializes to json file """
        if path.exists(self.__file_path):
            with open(self.__file_path, "w") as file:
                json.dump(self.__objects, file)

    def reload(self):
        """ deserializes json to file """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.loads(file)
