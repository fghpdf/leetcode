'''
Author: fghpdf
Date: 2021-10-18 09:03:03
LastEditTime: 2021-10-18 09:31:30
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left < right:
          mid = (left + right) // 2

          if nums[mid] > nums[right]:
            left = mid + 1
          else:
            right = mid

        return nums[left]
          

          

class TestSolution(unittest.TestCase):
    def testFindMin(self):
        sol = Solution()
        self.assertEqual(sol.findMin([3,1,2]), 1)
        self.assertEqual(sol.findMin([3,4,5,1,2]), 1)
        self.assertEqual(sol.findMin([4,5,6,7,0,1,2]), 0)
        self.assertEqual(sol.findMin([11,13,15,17]), 11)
        

if __name__ == '__main__':
    unittest.main()