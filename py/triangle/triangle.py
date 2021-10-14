'''
Author: fghpdf
Date: 2021-10-14 21:42:20
LastEditTime: 2021-10-14 21:56:24
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0 or len(triangle[0]) == 0:
          return 0

        for layer in range(len(triangle) - 2, -1, -1):
          for index in range(0, len(triangle[layer])):
            triangle[layer][index] = min(triangle[layer+1][index], triangle[layer+1][index+1]) + triangle[layer][index]

        return triangle[0][0]

class TestMinimumTotal(unittest.TestCase):
    def test_minimum_total(self):
        sol = Solution()
        self.assertEqual(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]), 11)
        self.assertEqual(sol.minimumTotal([[-10]]), -10)

if __name__ == '__main__':
    unittest.main()