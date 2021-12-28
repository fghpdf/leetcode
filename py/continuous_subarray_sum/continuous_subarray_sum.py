'''
Author: fghpdf
Date: 2021-12-28 08:55:30
LastEditTime: 2021-12-28 09:15:02
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False

        track = {0:-1}

        sum = 0
        for i, n in enumerate(nums):
            sum = (sum+n)%k
            if sum not in track:
              track[sum] = i
            else:
              if i - track[sum] >= 2:
                  return True

        return False


class TestSolution(unittest.TestCase):
    def testCheckSubarraySum(self):
        sol = Solution()
        self.assertEqual(sol.checkSubarraySum(nums = [23,2,4,6,7], k = 6), True)
        self.assertEqual(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 6), True)
        self.assertEqual(sol.checkSubarraySum(nums = [23,2,6,4,7], k = 13), False)
        self.assertEqual(sol.checkSubarraySum(nums = [23,2,4,6,6], k = 7), True)

if __name__ == '__main__':
    unittest.main()