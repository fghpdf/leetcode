'''
Author: fghpdf
Date: 2021-11-03 09:09:13
LastEditTime: 2021-11-03 09:17:09
LastEditors: fghpdf
'''
import unittest

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 2:
            return 1
        if n == 3:
            return 2
        product = 1
        while n>4:
            product*=3
            n-=3
        product*=n
        return product

class TestSolution(unittest.TestCase):
    def testIntegerBreak(self):
        sol = Solution()
        self.assertEqual(sol.integerBreak(2), 1)
        self.assertEqual(sol.integerBreak(10), 36)

if __name__ == '__main__':
    unittest.main()