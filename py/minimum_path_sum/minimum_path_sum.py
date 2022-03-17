from typing import List
import unittest

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
          return 0

        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
          grid[0][i] += grid[0][i-1]
        for i in range(1, m):
          grid[i][0] += grid[i-1][0]
        
        for i in range(1, m):
          for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]

class TestSolution(unittest.TestCase):
  def testMinPathSum(self):
    sol = Solution()
    self.assertEqual(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]), 7)
    self.assertEqual(sol.minPathSum([[1,2,3],[4,5,6]]), 12)


if __name__ == "__main__":
  unittest.main()