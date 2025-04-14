#!/usr/bin/python3

""" module unittest """
import unittest

""" import main class Base from models/base.py """
from models.base import Base

"""createa a subclass of the main class unitest"""


class TestBaseClass(unittest.TesstCase):

    b1 = Base()
    self.asseretEqual(b1.id, 1)
