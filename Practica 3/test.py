from functions import quadrant
import unittest

class test_quadrant (unittest.TestCase):

    def test_quadrant(self):
        self.assertEqual(quadrant(10,-5), "Fourth Quadrant")