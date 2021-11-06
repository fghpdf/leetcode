'''
Author: fghpdf
Date: 2021-11-06 18:07:28
LastEditTime: 2021-11-06 18:36:19
LastEditors: fghpdf
'''
from typing import List
import unittest
import math
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False

        memo = set()
        while n not in memo:
            memo.add(n)
            n = sum(int(i)**2 for i in str(n))
        return 1 in memo


          

class TestSolution(unittest.TestCase):
    def testIsHappy(self):
        sol = Solution()
        self.assertEqual(sol.isHappy(19), True)
        self.assertEqual(sol.isHappy(2), False)


if __name__ == '__main__':
    unittest.main()