'''
Author: fghpdf
Date: 2021-12-27 10:41:40
LastEditTime: 2021-12-27 10:55:44
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 0:
            return []

        # the sum of indices on all diagonals are equal
        diagonals = {}
        for i in range(len(mat)):
          for j in range(len(mat[i])):
            if i + j not in diagonals:
                diagonals[i+j] = [mat[i][j]]
            else:
                diagonals[i+j].append(mat[i][j])
        
        ans = []
        for snake in diagonals.items():
            # even should be reversed
            if snake[0] % 2 == 0:
                [ans.append(x) for x in snake[1][::-1]]
            else:
                [ans.append(x) for x in snake[1]]

        return ans


class TestSolution(unittest.TestCase):
    def testFindDiagonalOrder(self):
        sol = Solution()
        self.assertEqual(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])
        self.assertEqual(sol.findDiagonalOrder([[1,2],[3,4]]), [1,2,3,4])
        self.assertEqual(sol.findDiagonalOrder([[2,3]]), [2,3])

if __name__ == '__main__':
    unittest.main()