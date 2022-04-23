import math
from typing import List
import unittest

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums) == 0:
          return 0

        left = 1
        right = max(nums)
        while left < right:
          mid = (left + right) // 2
          total = self.getSum(nums, mid)
          if total > threshold:
            left = mid + 1
          else:
            right = mid
        
        return left

    def getSum(self, nums: List[int], divisor: int) -> int:
        if len(nums) == 0:
          return 0

        total = 0
        for num in nums:
          total += math.ceil(num / divisor)

        return total

class TestSolution(unittest.TestCase):
    def testSmallestDivisor(self):
        sol = Solution()
        self.assertEqual(sol.smallestDivisor(nums = [1,2,5,9], threshold = 6), 5)
        self.assertEqual(sol.smallestDivisor(nums = [44,22,33,11,1], threshold = 5), 44)

if __name__ == '__main__':
    unittest.main()