'''
Author: fghpdf
Date: 2021-10-26 09:45:15
LastEditTime: 2021-10-26 09:54:36
LastEditors: fghpdf
'''
from typing import List
import unittest

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        candidates.sort()
        res = []
        track = []
        self.backtrack(candidates, track, target, res, 0)
        return res

    def backtrack(self, candidates: List[int], track: List[int],remain: int, res: List[List[int]], start):
        if remain < 0:
            return

        if remain == 0:
            res.append(track[:])
            return
        
        for i in range(start, len(candidates)):
            track.append(candidates[i])
            self.backtrack(candidates, track, remain-candidates[i], res, i)
            track.pop()


class TestSolution(unittest.TestCase):
    def testCombinationSum(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum(candidates = [2,3,6,7], target = 7), [[2,2,3],[7]])
        self.assertEqual(sol.combinationSum(candidates = [2,3,5], target = 8), [[2,2,2,2],[2,3,3],[3,5]])
        self.assertEqual(sol.combinationSum(candidates = [2], target = 1), [])
        self.assertEqual(sol.combinationSum(candidates = [1], target = 1), [[1]])
        self.assertEqual(sol.combinationSum(candidates = [1], target = 2), [[1,1]])

if __name__ == '__main__':
    unittest.main()