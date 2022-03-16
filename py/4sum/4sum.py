from operator import le
from typing import List
import unittest

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0:
          return []

        res = []
        nums.sort()
        for i in range(len(nums)-3):
          if i == 0 or nums[i] != nums[i-1]:
            threeResult = self.threeSum(nums[i+1:], target-nums[i])
            for item in threeResult:
              res.append([nums[i]] + item)
        return res
        

    def threeSum(self, nums: List[int], target: int):
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
          left = i + 1
          right = len(nums) - 1
          t = target - nums[i]

          if i == 0 or nums[i] != nums[i-1]:
            while left < right:
              s = nums[left] + nums[right]
              if s == t:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                  left += 1
                while left < right and nums[right] == nums[right-1]:
                  right -= 1
                
                left += 1
                right -= 1
              elif s < t:
                left += 1
              else:
                right -= 1

        return res

class TestSolution(unittest.TestCase):
    def testFourSum(self):
        sol = Solution()
        self.assertEqual(sol.fourSum(nums = [1,0,-1,0,-2,2], target = 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
        self.assertEqual(sol.fourSum(nums = [2,2,2,2,2], target = 8), [[2,2,2,2]])

if __name__ == '__main__':
  unittest.main()