import unittest
from models.base_model import BaseModel
from models.place import Place


class TestCasePlace(unittest.TestCase):

    def test_amenity_ids(self):
        """ testing the amenity ids"""
        place = Place()
        place.amenity_ids = [1, 2, 3, 4]
        self.assertEqual(place.amenity_ids, [1, 2, 3, 4])
        self.assertIsNotNone(place.id)

        if __name__ == '__main__':
            unittest.main()
