'''
Author: fghpdf
Date: 2021-10-18 09:43:42
LastEditTime: 2021-10-18 09:50:03
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        right = len(nums) - 1

        while left < right:
          mid = (left + right) // 2

          if nums[mid] > nums[mid+1]:
            right = mid
          else:
            left = mid + 1

        return right

class TestSolution(unittest.TestCase):
    def testFindPeakElement(self):
        sol = Solution()
        self.assertEqual(sol.findPeakElement([1,2,3,1]), 2)
        self.assertEqual(sol.findPeakElement([1,2,1,3,5,6,4]), 5)

if __name__ == '__main__':
    unittest.main()