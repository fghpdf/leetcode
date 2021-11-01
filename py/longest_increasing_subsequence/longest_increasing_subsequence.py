'''
Author: fghpdf
Date: 2021-11-01 09:00:34
LastEditTime: 2021-11-01 09:06:03
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [1] * (len(nums)+1)

        maxLen = 0
        for i in range(len(nums)):
          for j in range(i):
              if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)

          maxLen = max(maxLen, dp[i])
        return maxLen


class TestSolution(unittest.TestCase):
    def testLengthOfLIS(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLIS([10,9,2,5,3,7,101,18]), 4)
        self.assertEqual(sol.lengthOfLIS([0,1,0,3,2,3]), 4)
        self.assertEqual(sol.lengthOfLIS([7,7,7,7,7,7,7]), 1)

if __name__ == '__main__':
    unittest.main()