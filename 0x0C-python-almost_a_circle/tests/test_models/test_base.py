#!/usr/bin/python3
""" import the unittest module """
import unittest
from models import base
from models.base import Base

"""createa a subclass of the main class unitest"""


class TestBaseClass(unittest.TestCase):
    model_one = Base()
    model_two = Base()

    self.AssertNotEqual(model_one.id, model_two.id)


if __name__ == "__main__":
    unittest.main()
