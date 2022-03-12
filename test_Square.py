from Square import Square
import unittest

class TestSquare(unittest.TestCase):

  def test_Square(self):
    self.assertEqual(Square(1), 1)
    self.assertEqual(Square(2), 4)
    self.assertEqual(Square(3), 9)
    self.assertEqual(Square(4), 16)

if __name__ == "__main__":
  unittest.main()
