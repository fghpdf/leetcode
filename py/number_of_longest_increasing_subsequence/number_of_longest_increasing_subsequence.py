'''
Author: fghpdf
Date: 2021-11-01 09:10:41
LastEditTime: 2021-11-01 09:28:28
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp, longest = [[1,1] for i in range(len(nums))], 1
        for i, num in enumerate(nums):
          curLongest, count = 1, 0
          for j in range(i):
            if nums[j] < num:
                curLongest = max(curLongest, dp[j][0]+1)

          for j in range(i):
            if dp[j][0] == curLongest-1 and nums[j]<num:
              count+=dp[j][1]
          
          dp[i] = [curLongest, max(count, dp[i][1])]
          longest=max(curLongest, longest)
        
        return sum([item[1] for item in dp if item[0] == longest])

class TestSolution(unittest.TestCase):
    def testFindNumberOfLIS(self):
        sol = Solution()
        self.assertEqual(sol.findNumberOfLIS([1,3,5,4,7]), 2)
        self.assertEqual(sol.findNumberOfLIS([2,2,2,2,2]), 5)

if __name__ == '__main__':
    unittest.main()