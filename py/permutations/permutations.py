'''
Author: fghpdf
Date: 2021-10-13 10:01:56
LastEditTime: 2021-10-13 10:11:59
LastEditors: fghpdf
'''
from logging import exception
from typing import List
import unittest

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        res = []
        self.backtrack(nums, track, res)
        return res

    def backtrack(self, nums: List[int], track: List[int], res: List[List[int]]):
      # end
      if len(nums) == len(track):
          res.append(track[:])
          return

      for n in nums:
          # exclude visited
          try: 
            track.index(n)
            continue
          except ValueError:
            track.append(n)
            self.backtrack(nums, track, res)
            track.pop()

class TestPermute(unittest.TestCase):
    def test_permute(self):
        sol = Solution()
        self.assertEqual(sol.permute([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
        self.assertEqual(sol.permute([0,1]), [[0,1],[1,0]])
        self.assertEqual(sol.permute([1]), [[1]])

if __name__ == '__main__':
    unittest.main()
