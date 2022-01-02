'''
Author: fghpdf
Date: 2022-01-02 10:41:38
LastEditTime: 2022-01-02 10:51:50
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # row
        for i in range(len(matrix[0])):
          # diagonals
          row, col = 0, i
          if not self.isDiagonalsSame(matrix, row, col):
                return False
        
        # col
        for i in range(len(matrix)):
            # diagonals
            row, col = i, 0
            if not self.isDiagonalsSame(matrix, row, col):
                return False

        return True

    def isDiagonalsSame(self, matrix: List[List[int]], row: int, col: int) -> bool:
        startElement = matrix[row][col]
        while row < len(matrix) and col < len(matrix[row]):
            if matrix[row][col] != startElement:
                return False
            row += 1
            col += 1

        return True

class TestSolution(unittest.TestCase):
    def testIsToeplitzMatrix(self):
        sol = Solution()
        self.assertEqual(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]), True)
        self.assertEqual(sol.isToeplitzMatrix([[1,2],[2,2]]), False)

if __name__ == '__main__':
    unittest.main()