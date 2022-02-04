'''
Author: fghpdf
Date: 2022-02-04 09:16:45
LastEditTime: 2022-02-04 09:29:02
LastEditors: fghpdf
'''
import collections
from typing import List
import unittest

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1

        rowLen = len(grid)
        colLen = len(grid[0])
        dirs = [(1,0),(0,-1),(-1,0),(0,1)]

        q = collections.deque()
        # find the start point
        for row in range(rowLen):
          for col in range(colLen):
            if grid[row][col] == "*":
              q.append((row, col, 0))
              break

        # BFS
        while q:
          row, col, step = q.popleft()
          for y, x in dirs:
            newRow = y + row
            newCol = x + col
            # check edge
            if newRow >= 0 and newRow < rowLen and newCol >= 0 and newCol < colLen and grid[newRow][newCol] in ('#', 'O'):
              # found food
              if grid[newRow][newCol] == '#':
                return step+1
              # visited
              grid[newRow][newCol] = '|'
              q.append((newRow, newCol, step+1))
        return -1
              

class TestSolution(unittest.TestCase):
    def testGetFood(self):
        sol = Solution()
        self.assertEqual(sol.getFood([["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]), 3)
        self.assertEqual(sol.getFood([["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]), -1)
        self.assertEqual(sol.getFood([["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]), 6)

if __name__ == '__main__':
    unittest.main()