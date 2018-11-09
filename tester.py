import unittest
import rect
class TestRect(unittest.TestCase):
    """ this tests for normal function (integers), normal function (floats) and
    for a negative number where it raises an error. there is no reason to test for
    the error raised by a string because it is impossible to input a string into
    the function. """

    def test_normal(self):
        self.assertEqual(rect.rectarea(4, 2), 8.0)

    def test_float(self):
        self.assertEqual(rect.rectarea(4.0, 2.0), 8.0)

    @unittest.expectedFailure
    def test_negative(self):
        self.assertRaises(rect.rectarea(-2, 4), ValueError)

if __name__ == 'main':
    unittest.main()