'''
Author: fghpdf
Date: 2021-10-26 09:08:18
LastEditTime: 2021-10-26 09:36:21
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums.sort()
        res = []
        track = []
        self.trackback(nums, track, res)
        return res

    def trackback(self, nums: List[int], track: List[int], res: List[List[int]]):
        if not nums:
          res.append(track[:])
          return
        
        for i in range(len(nums)):
          if (i+1 < len(nums) and nums[i] != nums[i+1]) or i+1 == len(nums):
            self.trackback(nums[:i]+nums[i+1:], track+[nums[i]], res)



class TestSolution(unittest.TestCase):
    def testPermuteUnique(self):
        sol = Solution()
        self.assertEqual(sol.permuteUnique(nums = [1,1,2]), [[1,1,2],[1,2,1],[2,1,1]])
        self.assertEqual(sol.permuteUnique(nums = [1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

if __name__ == '__main__':
    unittest.main()
