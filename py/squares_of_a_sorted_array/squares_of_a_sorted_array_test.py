import unittest

from squares_of_a_sorted_array import Solution

class TestSquaresOfASortedArray(unittest.TestCase):
    def test_squares_of_a_sorted_array(self):
      sol = Solution()
      self.assertEqual(sol.sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
      self.assertEqual(sol.sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])


if __name__ == '__main__':
    unittest.main()