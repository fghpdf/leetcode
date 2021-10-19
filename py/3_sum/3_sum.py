'''
Author: fghpdf
Date: 2021-10-19 09:35:01
LastEditTime: 2021-10-19 09:49:42
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for left in range(len(nums) - 2):
          if left > 0 and nums[left] == nums[left-1]: # no deduplicate
            continue

          mid = left + 1
          right = len(nums) - 1

          while mid < right:
            curSum = nums[left] + nums[mid] + nums[right]
            if curSum < 0:
              mid += 1
            elif curSum > 0:
              right -= 1
            else:
              res.append([nums[left], nums[mid], nums[right]])
              while mid < right and nums[mid] == nums[mid + 1]:
                mid += 1
              while mid < right and nums[right] == nums[right - 1]:
                right -= 1

              mid += 1
              right -= 1

        return res
            
class TestSolution(unittest.TestCase):
    def testThreeSum(self):
      sol = Solution()
      self.assertEqual(sol.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
      self.assertEqual(sol.threeSum([]), [])
      self.assertEqual(sol.threeSum([0]), [])

if __name__ == '__main__':
    unittest.main()