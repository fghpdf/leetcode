from typing import List
import unittest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
          return 0

        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
          j, k = i+1, len(nums) - 1
          while j < k:
            sum = nums[i]+nums[j]+nums[k]
            if sum == target:
              return sum

            if abs(sum - target) < abs(result - target):
              result = sum

            if sum < target:
                j += 1
            elif sum > target:
                k -= 1
        
        return result

class TestSolution(unittest.TestCase):
  def testThreeSumCloset(self):
    sol = Solution()
    self.assertEqual(sol.threeSumClosest(nums = [0,1,2], target = 3), 3)
    self.assertEqual(sol.threeSumClosest(nums = [-1,2,1,-4], target = 1), 2)
    self.assertEqual(sol.threeSumClosest(nums = [0,0,0], target = 1), 0)
   

if __name__ == '__main__':
  unittest.main()