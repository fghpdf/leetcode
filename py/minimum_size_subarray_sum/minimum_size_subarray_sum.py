from typing import List
import unittest

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
          return 0

        window = 0
        left = 0
        right = 0

        res = len(nums) + 1
        while right < len(nums):
          num = nums[right]
          # update window
          window += num

          while window >= target and left <= right:
            res = min(res, right - left + 1)
            window -= nums[left]
            left += 1
    
          # extend
          right += 1

        if res == len(nums) + 1:
          res = 0
        return res


class TestSolution(unittest.TestCase):
    def testMinSubArrayLen(self):
        sol = Solution()
        self.assertEqual(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]), 2)
        self.assertEqual(sol.minSubArrayLen(target = 4, nums = [1,4,4]), 1)
        self.assertEqual(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]), 0)

if __name__ == '__main__':
    unittest.main()