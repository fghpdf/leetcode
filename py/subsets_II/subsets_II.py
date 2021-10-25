'''
Author: fghpdf
Date: 2021-10-25 09:02:35
LastEditTime: 2021-10-25 09:21:41
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums.sort()

        res = []
        self.backtrack(nums, res, [], 0)
        return res

    def backtrack(self, nums: List[int], res: List[List[int]], track: List[int], start: int):
        res.append(track[:])
        for i in range(start, len(nums)):
          if i == start or nums[i] != nums[i-1]:
            track.append(nums[i])
            self.backtrack(nums, res, track, i + 1)
            track.pop()

class TestSolution(unittest.TestCase):
    def testSubsetsWithDup(self):
        sol = Solution()
        self.assertEqual(sol.subsetsWithDup([1,2,2]), [[],[1],[1,2],[1,2,2],[2],[2,2]])
        self.assertEqual(sol.subsetsWithDup([0]), [[],[0]])

if __name__ == '__main__':
    unittest.main()