'''
Author: fghpdf
Date: 2022-01-21 09:20:40
LastEditTime: 2022-01-21 09:39:41
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        arrLength = len(arr)
        mod = 10**9+7

        left, right = [0]*arrLength,[0]*arrLength
        s1, s2 = [], []

        for i in range(arrLength):
          count = 1
          while s1 and s1[-1][0] > arr[i]:
            count += s1.pop()[1]
          left[i] = count
          s1.append([arr[i], count])
        for i in range(arrLength)[::-1]:
          count = 1
          while s2 and s2[-1][0] >= arr[i]:
            count += s2.pop()[1]
          right[i] = count
          s2.append([arr[i], count])
        return sum(a * l * r for a, l, r in zip(arr, left, right)) % mod

class TestSolution(unittest.TestCase):
    def testSumSubarrayMins(self):
        sol = Solution()
        self.assertEqual(sol.sumSubarrayMins([71,55,82,55]), 593)
        self.assertEqual(sol.sumSubarrayMins(arr = [3,1,2,4]), 17)
        self.assertEqual(sol.sumSubarrayMins(arr = [11,81,94,43,3]), 444)


if __name__ == "__main__":
    unittest.main()