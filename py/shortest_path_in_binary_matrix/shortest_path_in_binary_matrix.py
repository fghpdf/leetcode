'''
Author: fghpdf
Date: 2021-10-24 09:33:43
LastEditTime: 2021-10-24 10:20:11
LastEditors: fghpdf
'''
from typing import List
import unittest
import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1

        if grid[0][0] == 1:
            return -1
        
        dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]
        seen = set()
        queue = collections.deque([(0,0,1)])
        seen.add((0, 0))
        while queue:
          i, j, dist = queue.popleft()
          if i == len(grid) - 1 and j == len(grid) -1:
            return dist

          for d1, d2 in dirs:
            x, y = i + d1, j + d2
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid):
              if (x,y) not in seen and grid[x][y] == 0:
                seen.add((x, y))
                queue.append((x, y, dist + 1))

        return -1



class TestSolution(unittest.TestCase):
    def testShorttestPathBinaryMatrix(self):
        sol = Solution()
        self.assertEqual(sol.shortestPathBinaryMatrix(grid = [[0,1],[1,0]]),2)
        self.assertEqual(sol.shortestPathBinaryMatrix( grid = [[0,0,0],[1,1,0],[1,1,0]]), 4)
        self.assertEqual(sol.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]), -1)

if __name__ == '__main__':
    unittest.main()