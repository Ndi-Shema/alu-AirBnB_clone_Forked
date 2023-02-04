import unittest
from models.base_model import BaseModel
from models.place import Place


class TestCasePlace(unittest.TestCase):
    def setUp(self):
        self.p = Place()

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsInstance(self.p, Place)

    def test_is_class(self):
        self.assertEqual(str(type(self.p)), "<class 'models.place.Place'>")

    def test_is_subclass(self):
        self.assertTrue(issubclass(type(self.p), BaseModel))

    def test_city_id(self):
        self.p.city_id = "SF"
        self.assertEqual(self.p.city_id, "SF")

    def test_user_id(self):
        self.p.user_id = "123"
        self.assertEqual(self.p.user_id, "123")

    def test_name(self):
        self.p.name = "Place 1"
        self.assertEqual(self.p.name, "Place 1")

    def test_description(self):
        self.p.description = "A place to stay in SF"
        self.assertEqual(self.p.description, "A place to stay in SF")

    def test_number_rooms(self):
        self.p.number_rooms = 2
        self.assertEqual(self.p.number_rooms, 2)

    def test_number_bathrooms(self):
        self.p.number_bathrooms = 2
        self.assertEqual(self.p.number_bathrooms, 2)

    def test_max_guest(self):
        self.p.max_guest = 4
        self.assertEqual(self.p.max_guest, 4)

    def test_price_by_night(self):
        self.p.price_by_night = 100
        self.assertEqual(self.p.price_by_night, 100)

    def test_latitude(self):
        self.p.latitude = 37.7749
        self.assertEqual(self.p.latitude, 37.7749)

    def test_longitude(self):
        self.p.longitude = -122.4194
        self.assertEqual(self.p.longitude, -122.4194)

    def test_amenity_ids(self):
        self.p.amenity_ids = [1, 2, 3, 4]
        self.assertEqual(self.p.amenity_ids, [1, 2, 3, 4])

        if __name__ == '__main__':
            unittest.main()
