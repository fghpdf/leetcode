'''
Author: fghpdf
Date: 2021-10-17 18:17:35
LastEditTime: 2021-10-17 19:16:14
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        # find root
        left = 0
        right = len(nums) - 1
        while left <= right:
          mid = (left + right) // 2
          if nums[mid] == target:
            return mid

          if nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
              right = mid - 1
            else:
              left = mid + 1
          else:
            if nums[right] >= target and target > nums[mid]:
              left = mid + 1
            else:
              right = mid - 1 

        return -1


class TestSearch(unittest.TestCase):
    def test_search(self):
        sol = Solution()
        self.assertEqual(sol.search([4,5,6,7,0,1,2], 0), 4)
        self.assertEqual(sol.search([4,5,6,7,0,1,2], 3), -1)
        self.assertEqual(sol.search([1], 0), -1)
        self.assertEqual(sol.search([1,2,3,4,5,6], 4), 3)
        self.assertEqual(sol.search([1,3], 0), -1)
        self.assertEqual(sol.search([1,3], 3), 1)


if __name__ == '__main__':
    unittest.main()