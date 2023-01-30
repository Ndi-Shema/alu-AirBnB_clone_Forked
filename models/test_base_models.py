#!/usr/bin/python3

import unittest
from datetime import datetime
from base_models import BaseModel
from __init__ import storage

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()
        self.test_dict = {"id": self.model.id, "created_at": self.model.created_at.isoformat(), "updated_at": self.model.updated_at.isoformat()}

    def test_init(self):
        """Test if id, created_at and updated_at are correctly set"""
        self.assertEqual(self.model.id, self.test_dict["id"])
        self.assertEqual(self.model.created_at.isoformat(), self.test_dict["created_at"])
        self.assertEqual(self.model.updated_at.isoformat(), self.test_dict["updated_at"])

    def test_save(self):
        """Test if the updated_at attribute is correctly updated"""
        previous_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(previous_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test if the to_dict method returns the correct dictionary"""
        self.assertEqual(self.model.to_dict(), self.test_dict)

    def test_str(self):
        """Test if the __str__ method returns the correct string representation of the object."""
        self.assertEqual(str(self.model), "[BaseModel] ({}) <{'id': '{}', 'created_at': datetime.datetime({}, {}, {}, {}, {}), 'updated_at': datetime.datetime({}, {}, {}, {}, {})}>".format(self.model.id, self.model.id, self.model.created_at.year, self.model.created_at.month, self.model.created_at.day, self.model.created_at.hour, self.model.created_at.minute, self.model.updated_at.year, self.model.updated_at.month, self.model.updated_at.day, self.model.updated_at.hour, self.model.updated_at.minute))

if __name__ == '__main__':
    unittest.main()
