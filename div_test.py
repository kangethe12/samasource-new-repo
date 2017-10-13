import unittest

from div import divid
"""testing my div.py"""
class testdivision(unittest.TestCase):
    """testing normal and small numbers"""
    def test_dividing(self):
        self.assertEqual(divid(10,2),5)
        self.assertEqual(divid(-6,3),-2)
    """testing the division by zero"""
    def test_divide_by_zero(self):
        try:
          divid(12,0)
        except ZeroDivisionError:
            self.fail("can't divide by zero")
    """testing the division by extreme numbers"""
    def test_edgecase(self):
        self.assertEqual(divid(1000,-2),-500)
        self.assertEqual(divid(-500,-250),2)


if __name__ == '__main__':
    unittest.main()
