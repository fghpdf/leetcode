'''
Author: fghpdf
Date: 2021-10-17 20:53:01
LastEditTime: 2021-10-17 21:26:33
LastEditors: fghpdf
'''
from typing import List
import unittest


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rowLen = len(matrix)
        colLen = len(matrix[0])

        left = 0
        right = rowLen * colLen - 1

        while left <= right:
          mid = (left + right) // 2
          number = matrix[mid // colLen][mid % colLen]

          if number == target:
              return True

          if number < target:
              left = mid + 1
          else:
              right = mid - 1

        return False

class TestSearchMatrix(unittest.TestCase):
    def test_search_matrix(self):
        sol = Solution()
        self.assertEqual(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), True)
        self.assertEqual(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False)
        self.assertEqual(sol.searchMatrix([[1,1]], 2), False)


if __name__ == '__main__':
    unittest.main()