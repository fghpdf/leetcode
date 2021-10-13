'''
Author: fghpdf
Date: 2021-10-13 09:11:14
LastEditTime: 2021-10-13 09:50:19
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        track = []
        res = []
        self.backtrack(n, k, 1, track, res)
        return res

    def backtrack(self, n: int, k: int, start: int, track: List[int], res: List[List[int]]):
        # end
        if k == 0:
          res.append(track[:])
          return

        for i in range(start, n+1):
          track.append(i)
          self.backtrack(n, k - 1, i + 1, track, res)
          track.pop(len(track) - 1)


class TestCombine(unittest.TestCase):
    def test_combine(self):
        sol = Solution()
        self.assertEqual(sol.combine(4,2), [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
        self.assertEqual(sol.combine(1,1), [[1]])

if __name__ == '__main__':
    unittest.main()