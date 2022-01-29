'''
Author: fghpdf
Date: 2022-01-29 10:58:08
LastEditTime: 2022-01-29 11:10:57
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        res = 0
        count = 0
        left, right = 0, 0

        while right < len(nums):
          rightNum = nums[right]
          right += 1
          # update window
          if rightNum % 2 == 1:
            k -= 1
            count = 0
          
          # shrink
          while k == 0:
            k += nums[left] % 2
            left += 1
            count += 1
          res += count
        return res
          

class TestSolution(unittest.TestCase):
    def testNumberOfSubarrays(self):
        sol = Solution()
        self.assertEqual(sol.numberOfSubarrays(nums = [1,1,2,1,1], k = 3), 2)
        self.assertEqual(sol.numberOfSubarrays(nums = [2,4,6], k = 1), 0)
        self.assertEqual(sol.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2), 16)

if __name__ == '__main__':
    unittest.main()