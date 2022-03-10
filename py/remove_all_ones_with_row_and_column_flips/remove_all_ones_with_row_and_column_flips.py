from typing import List
import unittest

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        if len(grid) == 0:
          return False

        rowOne, rowOneInvert = grid[0], [1-val for val in grid[0]]

        for i in range(1, len(grid)):
          row = grid[i]
          if row != rowOne and row != rowOneInvert:
            return False
        
        return True

class TestSolution(unittest.TestCase):
    def testRemoveOnes(self):
      sol = Solution()
      self.assertEqual(sol.removeOnes([[0,1,0],[1,0,1],[0,1,0]]), True)
      self.assertEqual(sol.removeOnes([[1,1,0],[0,0,0],[0,0,0]]), False)
      self.assertEqual(sol.removeOnes([[0]]), True)

if __name__ == '__main__':
    unittest.main()