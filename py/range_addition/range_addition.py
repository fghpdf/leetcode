'''
Author: fghpdf
Date: 2022-01-17 09:14:37
LastEditTime: 2022-01-17 09:26:37
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0]*length
        for start, end, incr in updates:
          res[start] += incr
          end += 1
          if end < len(res):
              res[end] -= incr

        for i in range(1, length):
          res[i] += res[i-1]

        return res

class TestSolution(unittest.TestCase):
    def testGetModifiedArray(self):
        sol = Solution()
        self.assertEqual(sol.getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]), [-2,0,3,5,3])
        self.assertEqual(sol.getModifiedArray(length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]), [0,-4,2,2,2,4,4,-4,-4,-4])

if __name__ == '__main__':
    unittest.main()