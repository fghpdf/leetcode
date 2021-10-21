from typing import List
import unittest
import math

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        
        window = 1

        left = 0
        right  = 0

        res = 0
        while right < len(nums):
          num = nums[right]
         
          # judge and update window
          window *= num

          while window >= k and left <= right:
            window /= nums[left]
            left += 1
          
          res += (right - left + 1)

           # extend
          right += 1

        return res

class TestSolution(unittest.TestCase):
    def testNumSubarrayProductLessThanK(self):
        sol = Solution()
        self.assertEqual(sol.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100), 8)
        self.assertEqual(sol.numSubarrayProductLessThanK(nums = [1,2,3], k = 0), 0)

if __name__ == '__main__':
    unittest.main()