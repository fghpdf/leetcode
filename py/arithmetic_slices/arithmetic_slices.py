'''
Author: fghpdf
Date: 2021-10-30 16:37:11
LastEditTime: 2021-10-30 17:02:50
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        n = len(nums)
        dp = [0] * n
        ans = 0

        for i in range(2, n):
          if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
              dp[i] = dp[i-1]+1
          ans += dp[i]

        return ans

class TestSolution(unittest.TestCase):
    def testNumberOfArithmeticSlices(self):
        sol = Solution()
        self.assertEqual(sol.numberOfArithmeticSlices([1,2,3,4]), 3)
        self.assertEqual(sol.numberOfArithmeticSlices([1]), 0)

if __name__ == '__main__':
      unittest.main()