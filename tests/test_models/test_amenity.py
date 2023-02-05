#!/usr/bin/python3
""" testing amenity model """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def test_amenity_creation(self):
        """ Test if Amenity instance is created correctly. """
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_subclass(self):
        """ checking if subclass """
        a = Amenity()
        self.assertTrue(issubclass(type(a), BaseModel))

    def test_amenity_name(self):
        """ Test if amenity name is set correctly. """
        a = Amenity()
        a.name = "Wifi"
        self.assertEqual(a.name, "Wifi")
        self.assertIsNotNone(a.id)

    if __name__ == '__main__':
        unittest.main()

