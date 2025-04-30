#!/usr/bin/python3
""" import the unittest module """
import unittest
from models import base
from models.base import Base

""" subclass of the testing class """
class MyUnitTesting(unittest.TestCase):
	cl_1 = Base(1)
	self.assertEqual(cl_1.id, 1)
