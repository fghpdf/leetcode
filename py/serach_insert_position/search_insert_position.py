from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target > nums[right]:
          return right + 1
        
        if target < nums[left]:
          return left

        # loop [left, right]
        # return target when nums[mid] is target
        # return mid when nums[mid] > target and nums[mid - 1] < target
        while (left <= right):
          mid = (left + right) // 2

          if nums[mid] == target:
            return mid
          elif nums[mid] > target:
            if mid >= 1 and nums[mid - 1] < target:
              return mid
            
            right = mid - 1
          else:
            left = mid + 1

        # target is beyond list
        return len(nums)