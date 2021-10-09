'''
Author: fghpdf
Date: 2021-10-09 12:21:19
LastEditTime: 2021-10-09 12:41:38
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      if (len(grid) == 0 or len(grid[0]) == 0):
        return 0    

      maxArea = 0
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          if grid[i][j] == 1:
            area = self.backtrack(grid, i, j, 0)
            maxArea = max(maxArea, area)

      return maxArea
      
    def backtrack(self, grid, row, col, area) -> int:
      # edge is end
      if (row < 0 or row >= len(grid) or (col < 0 or col >= len(grid[row]))): 
        return area

      # sea 0 is end
      if grid[row][col] == 0:
        return area

      # island area +1
      if grid[row][col] == 1:
        area += 1
        grid[row][col] = 0 # visited
      
      # left
      area = self.backtrack(grid, row, col-1, area)
      # up
      area = self.backtrack(grid, row-1, col, area)
      # right
      area = self.backtrack(grid, row, col+1, area)
      # down
      area = self.backtrack(grid, row+1, col, area)

      return area
      


class TestMaxAreaOfIsland(unittest.TestCase):
  def test_max_area_of_island(self):
    sol = Solution()
    self.assertEqual(sol.maxAreaOfIsland([
      [0,0,1,0,0,0,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,1,1,0,1,0,0,0,0,0,0,0,0],
      [0,1,0,0,1,1,0,0,1,0,1,0,0],
      [0,1,0,0,1,1,0,0,1,1,1,0,0],
      [0,0,0,0,0,0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,0,0,0,0,0,0,1,1,0,0,0,0]]), 6)
    self.assertEqual(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]), 0)

if __name__ == '__main__':
  unittest.main()