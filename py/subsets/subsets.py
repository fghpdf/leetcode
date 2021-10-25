'''
Author: fghpdf
Date: 2021-10-25 08:45:51
LastEditTime: 2021-10-25 08:56:25
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
          return []

        res = []
        self.backtrack(nums, res, [], 0)
        return res

    def backtrack(self, nums: List[int], res: List[List[int]], track: List[int], start: int):
        res.append(track[:])
        for i in range(start, len(nums)):
          track.append(nums[i])
          self.backtrack(nums, res, track, i + 1)
          track.pop()


class TestSolution(unittest.TestCase):
    def testSubsets(self):
        sol = Solution()
        self.assertEqual(sol.subsets([1,2,3]),[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
        self.assertEqual(sol.subsets([0]), [[], [0]])


if __name__ == '__main__':
    unittest.main()