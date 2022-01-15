'''
Author: fghpdf
Date: 2022-01-15 11:19:41
LastEditTime: 2022-01-15 11:25:00
LastEditors: fghpdf
'''
import re
from typing import List
import unittest

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if len(ribbons) == 0:
            return 0

        total = sum(ribbons)
        if k > total:
            return 0

        left = 1
        right = min(total // k, max(ribbons))

        while left < right:
            mid = (left + right + 1) // 2
            if sum(x // mid for x in ribbons) >= k:
              left = mid
            else:
              right = mid - 1

        return left

class TestSolution(unittest.TestCase):
    def testMaxLength(self):
        sol = Solution()
        self.assertEqual(sol.maxLength(ribbons = [9,7,5], k = 3), 5)
        self.assertEqual(sol.maxLength(ribbons = [7,5,9], k = 4), 4)
        self.assertEqual(sol.maxLength(ribbons = [5,7,9], k = 22), 0)

if __name__ == "__main__":
    unittest.main()