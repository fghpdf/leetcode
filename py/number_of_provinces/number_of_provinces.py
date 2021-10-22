'''
Author: fghpdf
Date: 2021-10-22 09:26:49
LastEditTime: 2021-10-22 10:03:33
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) == 0:
          return 0

        res = 0
        visited = set()
        for i in range(len(isConnected)):
            if i in visited :
              continue
            self.backtrack(isConnected, i, visited)
            res += 1

        return res

    def backtrack(self, isConnected: List[List[int]], i, visited: set) -> int:
      for j in range(len(isConnected)):
        # edge
        if i < 0 or i >= len(isConnected) or  j < 0 or j >= len(isConnected):
            return

        # connected
        if isConnected[i][j] == 1 and j in visited:
            visited.add(j)
            self.backtrack(isConnected, j, visited)

class TestSolution(unittest.TestCase):
    def testFindCircleNum(self):
       sol = Solution()
       self.assertEqual(sol.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]), 2)
       self.assertEqual(sol.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]), 3)

if __name__ == '__main__':
    unittest.main()