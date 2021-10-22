'''
Author: fghpdf
Date: 2021-10-22 08:57:14
LastEditTime: 2021-10-22 09:11:55
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
          return 0

        res = 0
        for row in range(len(grid)):
          for col in range(len(grid[row])):
            if grid[row][col] == "1":
              area = self.backtrack(grid, row, col, 0)
              if area:
                res += 1
        
        return res

    def backtrack(self, grid: List[List[str]], row, col, area) -> int:
      # edge
      if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[row])):
        return area

      # visited or 0
      if grid[row][col] == "0":
        return area

      # island area incr
      if grid[row][col] == "1":
        area += 1
        grid[row][col] = "0"

      area = self.backtrack(grid, row - 1, col, area)
      area = self.backtrack(grid, row + 1, col, area)
      area = self.backtrack(grid, row, col + 1, area)
      area = self.backtrack(grid, row, col - 1, area)

      return area

class TestSolution(unittest.TestCase):
    def testNumIsLands(self):
        sol = Solution()
        self.assertEqual(sol.numIslands(grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]), 1)
        self.assertEqual(sol.numIslands(grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]), 3)

if __name__ == '__main__':
    unittest.main()