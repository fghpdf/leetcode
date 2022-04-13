from typing import List
import unittest

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
          return []

        res, low = [[n*n]], n*n
        while low > 1:
          low, high = low - len(res), low
          res = [[i for i in range(low, high)]] + [list(j) for j in zip(*res[::-1])]
        return res


class TestSolution(unittest.TestCase):
    def testGenerateMatrix(self):
        sol = Solution()
        self.assertEqual(sol.generateMatrix(3), [[1,2,3],[8,9,4],[7,6,5]])
        self.assertEqual(sol.generateMatrix(1), [[1]])

if __name__ == '__main__':
    unittest.main()