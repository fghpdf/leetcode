'''
Author: fghpdf
Date: 2021-10-17 10:46:18
LastEditTime: 2021-10-17 11:28:52
LastEditors: fghpdf
'''
from typing import List
import unittest


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 0:
            return [-1, -1]

        if len(nums) == 2 and nums[0] == nums[1] == target:
            return [0,1]
        
        # find the target
        left = 0
        right = len(nums) - 1

        foundIndex = -1
        while left <= right:
          mid = (left + right) // 2

          if nums[mid] == target:
            foundIndex = mid
            break

          if nums[mid] < target:
            left = mid + 1
          else:
            right = mid - 1

        if foundIndex == -1:
          return [-1, -1]

        # find the first target
        left = 0
        right = foundIndex

        firstIndex = -1
        while left <= right:
          mid = (left + right) // 2

          if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
            firstIndex = mid
            break

          if nums[mid] < target:
            left = mid + 1
          else:
            right = mid - 1

        # find the right target
        left = foundIndex
        right = len(nums) - 1

        lastIndex = -1
        while left <= right:
          mid = (left + right) // 2

          if nums[mid] == target and (mid == len(nums) -1 or nums[mid + 1] != target):
            lastIndex = mid
            break

          if nums[mid] <= target:
            left = mid + 1
          else:
            right = mid - 1

        return [firstIndex, lastIndex]


class TestSearchRange(unittest.TestCase):
    def test_search_range(self):
        sol = Solution()
        self.assertEqual(sol.searchRange([5,7,7,8,8,10], 8), [3,4])
        self.assertEqual(sol.searchRange([5,7,7,8,8,10], 6), [-1,-1])
        self.assertEqual(sol.searchRange([5,7,8,8,8,8,8,9,10], 8), [2, 6])
        self.assertEqual(sol.searchRange([], 8), [-1, -1])
        self.assertEqual(sol.searchRange([2,2], 2), [0, 1])
        self.assertEqual(sol.searchRange([2,2], 1), [-1, -1])
        self.assertEqual(sol.searchRange([1,2,2], 2), [1,2])

if __name__ == '__main__':
    unittest.main()