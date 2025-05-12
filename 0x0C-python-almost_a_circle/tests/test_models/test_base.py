#!/usr/bin/python3

""" module unittest """
import unittest

""" import main class Base from models/base.py """
from models.base import Base

"""createa a subclass of the main class unitest"""


class TestBaseClass(unittest.TestCase):
    a = Base(34)
    b = Base()
    b.id = 99

    self.AssertEqual(a.id, 34)
