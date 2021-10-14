'''
Author: fghpdf
Date: 2021-10-14 09:44:58
LastEditTime: 2021-10-14 09:54:42
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
          return 0

        dp = [0, nums[0]]
        for i in range(1, len(nums)):
          dp.append(max(dp[i], dp[i-1] + nums[i]))

        return dp[len(nums)]


class TestRob(unittest.TestCase):
    def test_rob(self):
      sol = Solution()
      self.assertEqual(sol.rob([1,2,3,1]), 4)
      self.assertEqual(sol.rob([2,7,9,3,1]), 12)

if __name__ == '__main__':
    unittest.main()