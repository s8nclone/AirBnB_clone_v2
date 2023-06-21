#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest
from unittest.mock import patch
from models.__init__ import storage
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand


class HBNBCommandTestCase(unittest.TestCase):
    """ Class to test the HBNBCommand """

    def setUp(self):
        """ Test setup """
        self.console = HBNBCommand()
        self.place = Place()
        self.city = City()
        self.user = User()
        self.state = State()
        self.review = Review
        self.amenity = Amenity()

    def tearDown(self):
        """ Test tearDown """
        self.console = None

    def test_create_command(self):
        """ Method to test the create command """
        # Test create command with valid arguments
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            # Verify that a valid UUID is printed
            self.assertEqual(len(output), 36)

        # Test create command with missing class name
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        # Test create command with non-existent class name
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create InvalidClass')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        # Test create command with additional arguments
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd('create Place city_id="0001" \
                user_id="0001" name="My_little_house" number_rooms=4 \
                    number_bathrooms=2 max_guest=10 price_by_night=300 \
                        latitude=37.773972 longitude=-122.431297')
            output = fake_out.getvalue().strip()
            self.assertEqual(len(output), 36)

            # Verify that the additional attributes are set correctly
            obj = storage.get(Place, output)
            self.assertEqual(obj.name, "John Doe")
            self.assertEqual(obj.age, 25)


if __name__ == '__main__':
    unittest.main()
