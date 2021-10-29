import unittest
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        return math.comb(m + n - 2, n - 1)

class TestSolution(unittest.TestCase):
    def testUniquePaths(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(m = 3, n = 7), 28)
        self.assertEqual(sol.uniquePaths(m = 3, n = 2), 3)
        self.assertEqual(sol.uniquePaths(m = 7, n = 3), 28)
        self.assertEqual(sol.uniquePaths(m = 3, n = 3), 6)

if __name__ == '__main__':
    unittest.main()