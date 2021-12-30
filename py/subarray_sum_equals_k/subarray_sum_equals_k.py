'''
Author: fghpdf
Date: 2021-12-30 09:03:13
LastEditTime: 2021-12-30 09:24:49
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0

        summ = 0
        res = 0

        # can get sum[i,j] from sum[0,i] and sum[0,j]
        preSum = {}
        preSum[0] = 1

        for i in range(len(nums)):
          summ += nums[i]
          if (summ - k) in preSum:
            res += preSum[summ-k]
          preSum[summ] = preSum.get(summ, 0) + 1

        return res


class TestSolution(unittest.TestCase):
    def testSubarraySum(self):
        sol = Solution()
        self.assertEqual(sol.subarraySum(nums = [1,1,1], k = 2), 2)
        self.assertEqual(sol.subarraySum(nums = [1,2,3], k = 3), 2)


if __name__ == '__main__':
    unittest.main()