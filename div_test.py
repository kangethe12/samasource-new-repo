import unittest

from div import divid
class testdivision(unittest.TestCase):
  def test_dividing(self):
    self.assertEqual(divid(10,2),5)
    self.assertEqual(divid(-6,3),-2)
  def test_divide_by_zero(self):
    try:
      divid(12,0)
    except ZeroDivisionError:
      self.fail("can't divide by zero")
  def test_edgecase(self):
    self.assertEqual(divid(1000,-2),-500)
    self.assertEqual(divid(-500,-250),2)


if __name__ == '__main__':
    unittest.main()
