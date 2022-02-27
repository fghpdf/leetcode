from typing import List
import unittest

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
          return 0

        rows = len(matrix)
        cols = len(matrix[0])

        res = 0

        for r in range(rows):
          for c in range(cols):
            if matrix[r][c] == 1:
              if r == 0 or c == 0:
                # first row or col should be excluded
                res += 1
              else:
                cellVal = min(matrix[r-1][c-1], matrix[r][c-1], matrix[r-1][c]) + matrix[r][c]
                res += cellVal
                matrix[r][c] = cellVal

        return res

class TestSolution(unittest.TestCase):
    def testCountSquares(self):
        sol = Solution()
        self.assertEqual(sol.countSquares( matrix =[[0,1,1,1],[1,1,1,1],[0,1,1,1]]), 15)
        self.assertEqual(sol.countSquares([[1,0,1],[1,1,0],[1,1,0]]), 7)

if __name__ == '__main__':
    unittest.main()